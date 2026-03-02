# ACOSUS KNN Model Implementation Guide

**A Complete Walkthrough of the Student Success Prediction Pipeline**

**Author:** Deep Mandloi
**Institution:** Northeastern Illinois University (NEIU)
**Advisor:** Dr. Xiwei Wang
**Grant:** NSF IIS-2219623
**Date:** March 2026

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [The Two-Survey Architecture](#2-the-two-survey-architecture)
3. [Data Assembly](#3-data-assembly)
4. [Feature Encoding](#4-feature-encoding)
5. [Feature Scaling](#5-feature-scaling)
6. [Neighbor Selection](#6-neighbor-selection)
7. [KNN Regressor Training](#7-knn-regressor-training)
8. [Five-Fold Cross-Validation](#8-five-fold-cross-validation)
9. [Understanding the Metrics](#9-understanding-the-metrics)
10. [The Complete Training Pipeline](#10-the-complete-training-pipeline)
11. [The Complete Prediction Pipeline](#11-the-complete-prediction-pipeline)
12. [Training Artifacts](#12-training-artifacts)
13. [Design Decision Rationale](#13-design-decision-rationale)
14. [Backend Data Storage](#14-backend-data-storage)
15. [Future Improvements for Model Predictions](#15-future-improvements-for-model-predictions)
16. [Additional Admin Configuration Options](#16-additional-admin-configuration-options)
17. [Glossary](#17-glossary)

---

## 1. Executive Summary

ACOSUS (Academic Course Outcome Success System) predicts transfer student academic success using a K-Nearest Neighbors (KNN) regressor. The system is designed for academic advisors at NEIU to identify at-risk transfer students early in their academic journey and provide data-driven guidance.

The model takes 11 survey questions about a student's academic background, socioeconomic factors, and career goals as input. These 11 questions are encoded into 17 numeric features. The model outputs a predicted success rate on a 0 to 100 scale, along with a confidence score, a confidence interval, and a ranked list of which features were most influential in that particular prediction.

KNN was chosen as the initial algorithm because it works reliably with as few as 10 students, requires no complex optimization or parameter tuning, and provides transparent, interpretable predictions. When a student asks "why did I get this score?", the system can point to the specific similar students that informed the prediction and explain which features drove the similarity.

The system is currently operational with trained models stored on the model server, and the backend stores complete audit trails of every training run and every prediction made.

---

## 2. The Two-Survey Architecture

The prediction system is built on a pair of surveys that students complete at different points in their academic journey.

### The Target Survey (The Label)

The target survey measures a student's actual academic readiness or outcome. It serves as the "ground truth" that the model learns to predict. When a student completes a target survey with multiple questions, the system computes a single readiness score using the Priority-Weighted Response Scoring (PWRS) formula.

The PWRS formula works in four steps:

1. **Response Normalization**: For each question, the system divides the weightage of the student's selected answer by the maximum possible weightage for that question. This produces a score between 0 and 1 for each question.

2. **Priority Weighting**: Each question has an administrator-assigned priority score reflecting how important that question is for predicting success. The normalized score is multiplied by this priority score.

3. **Base Score Calculation**: All weighted scores are summed and divided by the sum of all priority scores. This produces a single base score between 0 and 1 that represents the weighted average of all the student's responses.

4. **Calibration**: The base score is passed through a logistic calibration curve with a steepness of 6. This S-shaped curve maps the base score to a final success rate between approximately 2 and 98 percent. The logistic curve prevents extreme predictions -- it is very difficult for a student to receive a 0 percent or 100 percent readiness score, which reflects the inherent uncertainty in predicting human outcomes.

The system also supports alternative calibration curves (linear, bounded, and sigmoid), but logistic is the default because it most accurately represents the diminishing returns of additional positive factors.

### The Factor Survey (The Features)

The factor survey collects the predictive variables -- the information the model uses to make predictions. The current factor survey for the background demographics quiz contains 11 questions covering:

- Academic performance indicators (GPA range, SAT score range)
- Academic progress (credits completed, courses currently enrolled)
- Socioeconomic factors (scholarship status, income status, work situation)
- Logistics (commute distance to campus)
- Career orientation (career goals, interest level in the field)
- Prior experience (research or academic experience level)

### Why Two Separate Surveys

Traditional approaches collect features and outcomes in a single survey. ACOSUS separates them for a specific reason: the model learns the mapping from factor survey answers to target survey outcomes. Once trained, it can predict the target outcome for any future student who has only completed the factor survey. This means a new transfer student can receive a predicted success rate immediately after answering the 11 factor questions, without waiting for their actual academic outcome.

---

## 3. Data Assembly

Before the model can be trained, the backend must assemble a dataset of students who have completed both surveys. This is the data assembly step.

### Finding Eligible Students

The backend queries the database for students who have completed both the factor survey and its linked target survey. A student qualifies for the training dataset only if:

- They have at least one completed attempt on the factor survey
- They have at least one completed attempt on the linked target survey
- Their target survey attempt has a valid success rate (either calculated via PWRS or self-reported)

If a student has taken either survey multiple times, the system uses the most recent completed attempt for each.

### Building the Feature Schema

For every question in the factor survey, the system records the question's identifier (slug), its data type (ordinal, cardinal, or date), its priority score, and all available answer options with their assigned weightages. If the administrator has configured additional profile-scoped questions to be included in training, those are merged into the feature schema as well.

This feature schema is critical because it tells the model server exactly how to convert raw survey answers into numbers. The same schema is used during both training and prediction to ensure consistency.

### Creating Student Records

For each matched student, the system pairs their factor survey answers (the raw text values they selected) with their target survey success rate (the numeric label). This creates one training record per student, containing the student identifier, a dictionary of their factor answers keyed by question slug, and the numeric success rate label.

### Extracting Hyperparameters

The quiz's model configuration, which the administrator sets through the admin interface, provides the KNN hyperparameters: the neighbor count (or "auto"), the weight strategy ("distance" or "uniform"), the distance metric ("euclidean", "manhattan", or "minkowski"), and the K-selection strategy ("sqrt", "log", or "fixed"). If no configuration exists, sensible defaults are used: auto neighbors with the square root strategy, distance weighting, and euclidean metric.

### Sending the Payload

Everything is bundled into a training payload with a timestamped model name (for example, "knn_2026-03-02T16-13-14_background-demographics") and sent as an HTTP request to the Python model server's training endpoint.

---

## 4. Feature Encoding

Machine learning models only understand numbers. Survey answers like "Between 3.0 and 3.5" or "Academia / Research" must be converted to numeric values before the model can use them. This conversion is called feature encoding.

### Ordinal Encoding (8 Features)

Ordinal questions are those where the answer options have a natural order -- a higher value is meaningfully "more" than a lower value. For these questions, each answer option has a pre-assigned weightage that reflects its relative value.

The encoder looks up the weightage for the student's selected answer and uses that number directly. For example:

- **GPA**: If a student selects "Between 3.0 and 3.5", the corresponding option weightage is 8. So the encoded value for GPA is 8.0. If they had selected "Below 2.0", the encoded value would be 2.0.
- **SAT Score**: "Below 500" encodes to 2.0, "Between 500 to 800" encodes to 4.0, "Between 800 to 1200" encodes to 6.0, and "More than 1200" encodes to 9.0.
- **Credits Completed**: Ranges from 7.0 for "0-30 credits" up to 9.0 for "91-120 credits" and "Above 120 credits".
- **Courses Currently Enrolled**: Ranges from 6.0 for "1 Course" to 9.0 for "3 Courses" and "4 Courses".
- **Distance to Campus**: 9.0 for "Less than 5 miles" down to 6.0 for "Over 31 miles" (shorter commute is scored higher).
- **Work Situation**: "Full-time" is 9.0, "Part-time" is 7.0, "Not employed" is 6.0.
- **Interest Level**: Ranges from 9.0 for "Extremely Interested" down to 4.0 for "Not at all Interested".
- **Prior Experience**: Ranges from 9.0 for "Extensive experience" down to 5.0 for "No prior experience".

The rationale for ordinal encoding is that these weightages preserve the ordering and relative magnitude of responses, which is essential for distance-based algorithms like KNN.

### Cardinal (One-Hot) Encoding (2 Questions Producing 7 Binary Columns)

Cardinal questions are those where the answer categories have no inherent order. For these, the encoder creates one binary column per possible answer option. Exactly one column is set to 1.0 (the selected answer) and all others are set to 0.0.

- **Scholarship Status**: Two options (Yes/No) produce two binary columns: "scholarship_yes" and "scholarship_no". If the student receives a scholarship, scholarship_yes = 1.0 and scholarship_no = 0.0.
- **Income Status**: Same structure -- "income_yes" and "income_no".
- **Career Goals**: Five options produce five binary columns: "career_academia_research", "career_entrepreneurship_start_up", "career_industry_corporate", "career_public_sector_government", and "career_other". Only the selected career goal column is set to 1.0.

One-hot encoding is used instead of ordinal encoding for these questions because assigning numeric values (like 1, 2, 3, 4, 5) to career goals would imply a false ordering -- "Industry/Corporate" is not inherently "greater than" "Academia/Research". One-hot encoding treats each option as an independent yes/no signal.

Note that for career goals, all five options have the same weightage of 9, meaning the system does not favor one career path over another. The value lies in which career a student has chosen, not in a ranking of careers.

### Date Pair Encoding

When two questions form a date pair (for example, "When did you start your program?" and "When do you expect to graduate?"), the encoder calculates the duration in months between the two dates and creates a single feature representing that duration. This collapses two raw date values into one meaningful numeric feature.

### Numeric Encoding

For questions that already produce numeric values, the encoder simply converts the answer to a floating-point number. If the answer cannot be parsed as a number, it defaults to 0.0.

### The Complete Feature List

After encoding, the current trained model uses 17 features (listed alphabetically as stored in the model artifacts):

1. career_academia_research (binary)
2. career_entrepreneurship_start_up (binary)
3. career_industry_corporate (binary)
4. career_other (binary)
5. career_public_sector_government (binary)
6. courses (ordinal weightage)
7. credits (ordinal weightage)
8. distance (ordinal weightage)
9. experience (ordinal weightage)
10. gpa (ordinal weightage)
11. income_no (binary)
12. income_yes (binary)
13. interested (ordinal weightage)
14. sat (ordinal weightage)
15. scholarship_no (binary)
16. scholarship_yes (binary)
17. work (ordinal weightage)

### Handling Missing Data

If a student did not answer a particular question, the encoded value for that feature (or its one-hot columns) is set to 0.0. This is a conservative default that prevents the system from crashing on incomplete data, though it means the model treats a missing answer the same as the lowest possible value. As the dataset grows, more sophisticated imputation strategies could be explored.

---

## 5. Feature Scaling

### The Problem

Without scaling, features with larger numeric ranges would dominate the distance calculations that KNN relies on. Consider two features: GPA (values ranging from 2 to 9) and scholarship status (values of 0 or 1). A one-unit change in GPA (say, from 8 to 9) represents a modest improvement, while a one-unit change in scholarship status (from 0 to 1) represents having a scholarship versus not having one -- a potentially significant factor. But in raw numbers, the GPA difference could be up to 7 units while scholarship can only differ by 1 unit. KNN would effectively ignore scholarship and base its decisions primarily on GPA, simply because GPA has a larger numeric range.

### The Solution: Standard Scaling

The system uses standard scaling (also called z-score normalization). For each of the 17 features, the scaler computes two numbers from the training data: the mean (average value across all training students) and the standard deviation (how spread out the values are).

Each feature value is then transformed by subtracting the mean and dividing by the standard deviation. After this transformation, every feature has a mean of 0 and a standard deviation of 1, regardless of its original range.

This means a one-standard-deviation change in GPA is treated as equally important as a one-standard-deviation change in scholarship status. The distance calculation becomes fair across all features.

### Why Standard Scaling for KNN

KNN computes distances between students across all features. Standard scaling ensures that no single feature dominates the distance calculation just because of its numeric range. Every feature contributes proportionally to the overall distance, and therefore proportionally to which neighbors are selected.

### Saving the Scaler

The fitted scaler (containing the learned means and standard deviations for each feature) is saved as one of the model artifacts. When predicting for a new student, the exact same scaler is applied to the new student's features. This is essential -- if the new student's features were scaled differently than the training data, the distance calculations would be meaningless.

---

## 6. Neighbor Selection

### What K Means

K is the number of "nearest neighbors" the model consults when making a prediction. If K equals 3, the model finds the 3 most similar students in the training data (based on scaled feature distance) and bases its prediction on their known success rates.

Think of it as asking: "Which 3 past students had the most similar background to this new student, and how did they do?"

### The Auto Strategy (Square Root)

By default, K is set automatically using the square root of the number of training samples:

- With 10 students: K = square root of 10, rounded down = 3
- With 25 students: K = square root of 25 = 5
- With 100 students: K = square root of 100 = 10

### Bounds

K is bounded between 3 at the minimum (to ensure meaningful averaging -- with fewer than 3 neighbors, a single unusual student could dominate the prediction) and the smaller of (number of samples minus 1) or 50 at the maximum. K can never equal the total number of training students because that would mean every prediction is just the average of all students, losing all personalization.

### Why Square Root

The square root heuristic balances two competing concerns:

- **Too few neighbors** (K too small): The model becomes overly sensitive to individual students. If K equals 1, the prediction is entirely determined by the single closest student, who might be an outlier. This leads to overfitting -- the model memorizes individual cases rather than learning general patterns.
- **Too many neighbors** (K too large): The model becomes too smooth. It averages over so many students that it loses the ability to distinguish between different types of students. Everyone gets a prediction close to the overall average. This leads to underfitting.

The square root of the sample size is a well-established default in the machine learning literature that grows slowly enough to avoid underfitting while being large enough to avoid overfitting.

### Alternative Strategies

The system also supports:

- **Logarithmic**: K equals the base-2 logarithm of the sample count. This grows even more slowly than square root and is more conservative -- useful when the dataset has many outliers.
- **Fixed**: K is always 5 regardless of sample size. Simple but does not adapt to the dataset.

Both alternatives are selectable by the administrator through the quiz configuration.

### Current Configuration

With the current dataset, the model uses K equals 3 with the square root auto strategy, distance weighting, and the euclidean distance metric.

---

## 7. KNN Regressor Training

### What "Training" Means for KNN

Unlike neural networks or gradient-boosted trees that learn internal parameters through iterative optimization, KNN "training" simply means storing the training data in memory. The model memorizes every training student's scaled feature values and their known success rate. This is called instance-based learning or lazy learning -- the model does no computation during training and defers all work to prediction time.

This is actually a significant advantage for small datasets. There is no risk of the training process failing to converge, no chance of the optimizer getting stuck in a poor solution, and no need to tune learning rates or training epochs. The model stores the data exactly as given.

### The scikit-learn KNeighborsRegressor

The system creates a KNeighborsRegressor from scikit-learn with the configured K value, weight strategy, and distance metric. When the model is fitted on the training data, it builds an efficient internal data structure (either a ball tree or KD-tree depending on the data characteristics) that enables fast neighbor lookup during prediction.

### Distance Weights

When the weight strategy is set to "distance" (the default), closer neighbors have more influence on the prediction than farther ones. The weight of each neighbor is proportional to the inverse of its distance -- a neighbor at distance 0.1 has ten times the influence of a neighbor at distance 1.0.

This is preferable to "uniform" weighting (where all K neighbors contribute equally) because it prevents a distant, less-similar student from having the same influence as a very close, highly-similar student. If three neighbors have distances of 0.1, 0.5, and 2.0, distance weighting ensures the closest neighbor dominates the prediction, which is usually the most reliable approach.

### Euclidean Metric

The distance between two students is computed as the straight-line distance across all 17 scaled feature dimensions. Euclidean distance is the natural and most common choice for continuous features that have been standardized via scaling.

### Why Regression, Not Classification

Student success rate is a continuous variable ranging from 0 to 100. Using regression preserves this granularity -- the model can predict 72.3 percent versus 68.7 percent, capturing meaningful differences. A classification approach would force students into categories like "high risk", "medium risk", and "low risk", losing the nuance that distinguishes a student at 45 percent from one at 55 percent. Regression also allows the system to compute confidence intervals around the prediction, which would not be possible with categorical output.

---

## 8. Five-Fold Cross-Validation

### The Problem of Self-Evaluation

If the model is tested on the same students it memorized during training, it will appear to perform far better than it actually will on new students. For KNN with K equals 1, it would predict every training student's own success rate exactly, achieving perfect accuracy -- which is meaningless for evaluating real-world performance. This is called overfitting to the training data.

### How Five-Fold Cross-Validation Works

Cross-validation provides an honest estimate of how well the model will perform on students it has never seen. The training data is split into 5 equal parts called "folds." The process runs 5 rounds:

- **Round 1**: Folds 2 through 5 are used for training, fold 1 is used for testing
- **Round 2**: Folds 1, 3, 4, and 5 are used for training, fold 2 is used for testing
- **Round 3**: Folds 1, 2, 4, and 5 are used for training, fold 3 is used for testing
- **Round 4**: Folds 1, 2, 3, and 5 are used for training, fold 4 is used for testing
- **Round 5**: Folds 1 through 4 are used for training, fold 5 is used for testing

Every student is tested exactly once, and the test always uses a model that did not see that student during training. This simulates the real-world scenario of predicting for a new, unseen student.

### Why Five Folds

With 10 students (the minimum for training), each fold contains 2 students. Five folds is the standard choice because it balances two needs: having enough training data per fold (80 percent of the total) and getting enough test evaluations (every student tested once). Fewer folds (like 3) would leave each fold with too few test samples. More folds (like 10, which is leave-one-out) would cause training sets to overlap so heavily that the variance of the estimates increases.

### Adaptive Fold Count

If there are fewer than 5 students in the training set (which should not happen given the minimum threshold of 3, but the system handles it defensively), the fold count is automatically reduced to match the number of available students.

### What Metrics Are Computed Per Fold

Each fold produces two metrics: Mean Absolute Error (MAE) and R-squared. Both are computed by comparing the model's predictions to the actual success rates for the test students in that fold. The final reported cross-validation scores include the per-fold values and the mean across all folds.

---

## 9. Understanding the Metrics

### Mean Absolute Error (MAE)

**What it measures**: The average of the absolute differences between the model's predicted success rates and the students' actual success rates, across all test students. MAE is measured in the same units as the success rate -- percentage points.

**Interpretation in context**: If MAE is 12, the model's predictions are typically about 12 percentage points away from the true success rate. A student with an actual success rate of 75 percent might be predicted anywhere from about 63 to 87 percent.

**Good versus bad MAE values for student success prediction**:

| MAE Range | Quality | Meaning |
|-----------|---------|---------|
| Below 7 | Excellent | Predictions are highly reliable for advising decisions |
| 7 to 12 | Good | Predictions are useful and actionable |
| 12 to 18 | Fair | Predictions give directional guidance but have significant uncertainty |
| Above 18 | Poor | Model needs more data or different features |

**Why MAE is the primary metric**: MAE is robust to outliers -- a single wildly wrong prediction does not disproportionately inflate the score. It is also directly interpretable: an MAE of 8 means "predictions are off by about 8 points on average."

### R-Squared (Coefficient of Determination)

**What it measures**: R-squared measures how much of the variation in actual success rates the model explains, compared to simply predicting the average success rate for everyone. It asks the question: "Is the model better than just guessing the average?"

**Scale**: R-squared of 1.0 means the model's predictions perfectly match the actual outcomes. R-squared of 0.0 means the model is no better than predicting the average for everyone. R-squared can be negative, which means the model's predictions are actively worse than just predicting the average.

**Interpretation in context**: An R-squared of 0.5 means "the model captures 50 percent of the variation in student success rates." The remaining 50 percent is due to factors not captured by the 11 survey questions -- personal circumstances, instructor quality, unexpected life events, motivation changes, and countless other variables.

**Good versus bad R-squared values for student success prediction**:

| R-squared Range | Quality | Meaning |
|-----------------|---------|---------|
| Above 0.7 | Excellent | Model captures most of the variation in outcomes |
| 0.4 to 0.7 | Good | Model is meaningfully predictive |
| 0.1 to 0.4 | Fair | Model captures some signal but significant uncertainty remains |
| 0.0 to 0.1 | Poor | Model provides minimal predictive value |
| Negative | Very Poor | Model is worse than guessing the average |

**Important nuance for small datasets**: In educational prediction with limited features (11 questions) and limited data (10 to 50 students), R-squared of 0.3 to 0.5 is typical and acceptable. Achieving R-squared above 0.8 with so few features and samples would actually be suspicious and might indicate overfitting or data leakage.

### Why R-Squared Varies Across Folds

It is completely normal for R-squared to fluctuate significantly from fold to fold, especially with small datasets. Here is why:

- **Small sample sizes**: With only 2 students per fold, a single unusual student can dramatically affect the fold's R-squared. One fold might have R-squared of 0.7 while another has negative 0.3.
- **Non-representative splits**: If one fold happens to contain two students with very similar success rates (say, both around 70 percent), there is very little variance to explain. R-squared becomes mathematically unstable when the denominator (total variance) is small.
- **Random composition**: The students in each fold are selected randomly. Some folds will, by chance, contain easier-to-predict students while others contain harder cases.

This variation is expected behavior, not a bug or a problem with the model. The mean R-squared across all 5 folds is the more reliable number. As the training set grows to 25, 50, or 100 students, fold-to-fold variation decreases and R-squared stabilizes because each fold contains more students and is more representative of the overall population.

### MSE and RMSE

- **MSE (Mean Squared Error)**: Like MAE but squares the differences before averaging. This means large errors are penalized much more heavily than small ones. A prediction that is off by 20 points contributes 400 to the MSE, while two predictions each off by 10 points contribute only 200 combined. MSE is useful for detecting whether the model has occasional wildly wrong predictions.

- **RMSE (Root Mean Squared Error)**: The square root of MSE, which brings the units back to percentage points. RMSE is always greater than or equal to MAE. The larger the gap between RMSE and MAE, the more uneven the model's errors are -- meaning some predictions are much worse than others.

### Cross-Validation Scores Versus Training Scores

The system reports both training metrics (computed on the same data the model was trained on) and cross-validation metrics (computed on held-out data). The cross-validation scores are always the honest estimate. Training scores will always look better because the model has already seen those students.

If training R-squared is 0.95 but cross-validation R-squared is 0.3, the model is severely overfitting -- it has memorized the training students rather than learning generalizable patterns. This gap typically narrows as the dataset grows.

---

## 10. The Complete Training Pipeline

Here is the end-to-end flow from the moment an administrator triggers model training to the point where a new model is active and ready for predictions:

1. **Admin triggers training** through the admin interface, or the automatic training trigger fires when the student count reaches the configured threshold (default: 10 students for initial training, every 10 new students for retraining).

2. **Backend creates an audit entry**. A TrainingTriggerLog record is created to permanently track this training attempt, including who triggered it, why, and when.

3. **Backend assembles training data**. The system queries the database for all students who have completed both the factor and target surveys, builds the feature schema from question metadata, extracts hyperparameters from the quiz configuration, and packages everything into a training payload.

4. **Backend creates a model metadata record**. A ModelMetaData record is created with status "training/started" to track this model's lifecycle.

5. **Backend sends the training request** to the Python model server as an HTTP POST to the training endpoint. The backend returns immediately with an HTTP 202 (accepted) -- training runs asynchronously.

6. **Model server encodes features**. Raw survey answers are converted to numeric values using ordinal and cardinal encoding rules based on the feature schema.

7. **Model server fits the scaler**. A StandardScaler is fitted on the encoded features, transforming all 17 features to have mean 0 and standard deviation 1.

8. **Model server determines K**. The auto strategy computes K as the square root of the number of training samples, bounded between 3 and the smaller of (n minus 1) or 50.

9. **Model server trains the KNN model**. A KNeighborsRegressor is created with the determined K, distance weighting, and euclidean metric, then fitted on the scaled features and success rate labels.

10. **Model server runs five-fold cross-validation**. The trained model configuration is evaluated using 5-fold CV, computing MAE and R-squared for each fold and reporting the means.

11. **Model server computes training metrics**. MAE, MSE, RMSE, and R-squared are computed on the full training data (these are the optimistic estimates, not the honest cross-validation estimates).

12. **Model server saves five artifacts to disk**. The serialized model, fitted scaler, feature names list, feature schema, and hyperparameter configuration are all persisted to a timestamped directory.

13. **Model server reports progress**. At each pipeline step, the model server sends real-time progress updates back to the backend, including step name, status, duration, and any output or errors.

14. **Model server returns results**. The complete response includes all metrics (training and cross-validation), the configuration used, the feature names, total samples and features, K value used, training duration, and the path where artifacts were saved.

15. **Backend finalizes the model record**. The ModelMetaData record is updated with all metrics, the artifact path, training data summary, and pipeline step details. The new model is marked as the current active model, and any previous model for the same quiz is demoted.

---

## 11. The Complete Prediction Pipeline

Here is the end-to-end flow from the moment a new student completes the factor survey to the prediction being displayed:

1. **Student completes the factor survey**. The backend receives the student's raw answers for all 11 questions.

2. **Backend identifies the current model**. The system queries the ModelMetaData collection to find the active (isCurrent = true) KNN model for this quiz.

3. **Backend sends the prediction request** to the Python model server. The request includes the student's raw answers, the feature schema, the list of trained feature names, and the path to the model artifacts on disk.

4. **Model server loads the model artifacts** from disk, or uses a cached version if this model was recently loaded. Loading includes the KNN model, the fitted scaler, the feature names, the feature schema, and the configuration.

5. **Model server encodes the student's answers** using the exact same encoding logic as training -- ordinal features are mapped to their weightages, cardinal features are one-hot encoded.

6. **Model server aligns features to the training order**. This is a critical step. The new student's encoded features must be in the exact same order as the features the model was trained on. Features that exist in the training set but are missing from the new student are padded with 0.0 (with a warning). Features present in the new student's data but not in the training set are dropped (with a warning).

7. **Model server scales the features** using the saved StandardScaler, applying the same means and standard deviations that were computed during training. This ensures the new student's features are on the same scale as the training data.

8. **Model server makes the prediction**. The KNN model's predict function computes the distance-weighted average of the K nearest neighbors' success rates. The raw prediction is clipped to the 0 to 100 range.

9. **Model server finds the nearest neighbors**. The model's kneighbors function returns the distances and indices of the K closest training students. The system retrieves their known success rate labels. This information is valuable for transparency -- the advisor and student can see which historical students were most similar and what their outcomes were.

10. **Model server computes a confidence score**. Confidence is calculated as a 50/50 blend of two components:
    - **Distance confidence**: How close the nearest neighbors are. If the nearest neighbors are very close (low distance), the model is more confident because it has highly similar reference points. If neighbors are far away, the new student is in a region of the feature space with little training data, and confidence drops.
    - **Label agreement confidence**: How consistent the neighbors' success rates are. If all 3 neighbors had success rates around 72 to 78 percent, the model is confident because the similar students had consistent outcomes. If the neighbors' rates were 40, 70, and 95 percent, the model is less confident because similar students had very different outcomes.

11. **Model server computes a 95 percent confidence interval**. Using the mean and standard deviation of the neighbor labels, the system calculates a range within which the true success rate is expected to fall with 95 percent probability. This gives the advisor a sense of the prediction's uncertainty range.

12. **Model server computes feature importance**. For each of the 17 features, the system measures how similar the K nearest neighbors are on that particular feature (by computing the standard deviation of that feature's values among the neighbors). If all neighbors have nearly identical GPA values, GPA has high importance -- it was a key factor in finding those neighbors. If neighbors have widely varying scholarship status, scholarship has low importance for this particular prediction. The top 10 most important features are returned.

13. **Model server returns the complete response** including the predicted success rate, confidence score, confidence interval, nearest neighbors with their distances and labels, feature importance rankings, any dimension warnings, and performance timing.

14. **Backend stores the prediction**. A PredictionReq record is created with the full prediction details, including the student identifier, the model version used, all prediction outputs, and performance metrics (how long the model took to load, how long inference took).

15. **Backend links the prediction to the attempt**. The student's factor survey attempt record is updated with the predicted success rate, the model version that made the prediction, and a reference to the PredictionReq record.

16. **Prediction is displayed to the student** along with contextual information and, optionally, AI-generated personalized academic advice based on the prediction and the student's specific profile.

---

## 12. Training Artifacts

When a model is trained, five files are saved to a dedicated directory on the model server. Each artifact serves a distinct purpose and is essential for the model to function during prediction.

### The Model File (knn_model.joblib)

This is the serialized KNN model object, saved using the joblib library for efficient binary storage. It contains the internal data structure (ball tree or KD-tree) that enables fast neighbor lookup, as well as a reference to the training data itself (the scaled feature matrix and the success rate labels). Without this file, no predictions can be made.

Joblib is used instead of Python's built-in pickle because it handles large numpy arrays more efficiently, producing smaller files and faster load times.

### The Scaler File (scaler.joblib)

This is the fitted StandardScaler object containing the mean and standard deviation for each of the 17 features, computed from the training data. It ensures that new students are scaled identically to how the training data was scaled. If this artifact were lost or mismatched, predictions would be mathematically invalid because the new student's features would be on a different scale than the training data.

### The Feature Names File (feature_names.json)

This is an ordered list of the 17 feature names, stored as a JSON array. The order of features in this list corresponds exactly to the order in which the model expects to receive them. During prediction, the system uses this list to align the new student's encoded features in the correct order. If features were presented in a different order, the model would interpret the wrong values for each feature.

### The Feature Schema File (feature_schema.json)

This is the complete question metadata used during training, stored as a JSON object keyed by question slug. It includes each question's priority score, data type, and all available options with their weightages. This schema is used during prediction to encode the new student's raw answers using the exact same rules that were applied during training.

### The Configuration File (config.json)

This stores the hyperparameters used for this particular training run: the K value, weight strategy, distance metric, and K-selection strategy. It serves two purposes: reproducibility (anyone can see exactly how this model was configured) and audit (comparing configurations across model versions to understand what changed).

---

## 13. Design Decision Rationale

| Decision | Choice Made | Rationale |
|----------|-------------|-----------|
| **Algorithm** | KNN over Linear Regression | KNN captures non-linear relationships between features and success rates. Linear regression assumes a straight-line relationship, which rarely holds in educational data where multiple factors interact in complex ways. |
| **Algorithm** | KNN over Random Forest | KNN is more interpretable (can show the exact neighbor students and their outcomes), works reliably with as few as 10 samples, and has effectively no tuning parameters when using distance weights. Random forests need at least 50 to 100 samples to avoid overfitting and provide less transparent explanations. |
| **Weight Strategy** | Distance over Uniform | Distance weighting prevents a single outlier neighbor from having the same influence as a very close, reliable neighbor. If one of the three nearest neighbors is much farther away, its contribution is proportionally reduced. |
| **Distance Metric** | Euclidean over Manhattan | Euclidean distance is the natural choice for continuous, standardized features. Manhattan distance (sum of absolute differences) would be preferred if features were sparse or predominantly categorical, but after standard scaling, all features are continuous. |
| **Scaler** | StandardScaler over MinMaxScaler | StandardScaler is less sensitive to outliers. If one student has an extremely unusual GPA value, MinMaxScaler would compress all other students' GPA values into a narrow range. StandardScaler preserves the relative spread of the majority of students. |
| **K Strategy** | Square root with bounds | The square root heuristic automatically adapts as the dataset grows, starting at K equals 3 for 10 students and reaching K equals 10 for 100 students. The lower bound of 3 prevents overfitting to individual students, and the upper bound of 50 prevents the model from averaging over too many neighbors. |
| **Task Type** | Regression over Classification | Success rate is a continuous variable on a 0 to 100 scale. Regression preserves this granularity rather than forcing students into coarse categories like "high risk" or "low risk." Regression also enables confidence intervals, which would not be meaningful for categorical predictions. |
| **PWRS Calibration** | Logistic over Linear | The logistic S-curve prevents extreme predictions (nearly 0 percent or 100 percent), which reflects the inherent uncertainty in predicting human outcomes. A linear calibration would allow predictions at the extremes, implying certainty that is not justified by 11 survey questions. |
| **Feature Encoding Location** | Model Server (not Backend) | Keeping all encoding logic on the model server ensures consistency between training and prediction. If the backend handled encoding, any discrepancy between how training data and prediction data were encoded would silently corrupt predictions. Centralized encoding eliminates this risk. |
| **Model Persistence** | Joblib plus JSON | Binary serialization (joblib) for scikit-learn objects provides fast save and load times with small file sizes. Human-readable JSON for metadata enables easy inspection and debugging without loading the model into Python. |

---

## 14. Backend Data Storage

The backend maintains four primary database collections that together provide a complete audit trail of model training, predictions, and student interactions.

### ModelMetaData

This collection stores one record per trained model version. Each record contains:

- **Model Identity**: A unique name, unique identifier, model type (KNN), version string, and the file path to the model artifacts on disk.
- **Training Metrics**: MAE, MSE, RMSE, R-squared, and the complete cross-validation scores (per-fold values and means for both MAE and R-squared).
- **Training Data Summary**: How many students were used, how many were real versus synthetic, the total number of features, and the ordered list of feature names.
- **Configuration Snapshot**: The exact hyperparameters used -- K value, weights, metric, and K-selection strategy. This allows comparing configurations across model versions.
- **Training Context**: When the model was trained, how long training took in milliseconds, who triggered the training, and what type of trigger it was (manual, initial, retrain).
- **Pipeline Steps**: An array recording each step of the training pipeline (feature encoding, scaling, K selection, model training, cross-validation, metrics computation, persistence) with its status, duration, start time, and any output or errors. This provides fine-grained visibility into the training process.
- **Versioning**: Links to the previous model version and the model that superseded this one, creating a complete version history.
- **Status Flags**: Whether this is the currently active model and whether it has been archived.

### TrainingTriggerLog

This collection serves as a permanent, immutable audit trail of every training attempt. Each record captures:

- **Trigger Details**: What type of trigger fired (initial KNN, retrain, manual), why it fired, and what conditions were met (student count, feedback rating, threshold values).
- **Timeline**: Precise timestamps for when training was triggered, when it was queued, when it started, when it completed (or failed), and the total duration.
- **Results**: Whether training succeeded or failed, how many students were used, and the key metrics (MAE and R-squared) of the resulting model.
- **Error Information**: If training failed, the error message, error code, stack trace, and whether the error is retryable.
- **Retry Tracking**: How many times this training was retried and the outcome of each retry.

### PredictionReq

This collection stores every prediction the system makes. Each record includes:

- **Context**: The student identifier, quiz identifier, and attempt identifier that triggered the prediction.
- **Model Used**: Which model version made the prediction, including the model identifier and version string.
- **Prediction Results**: The predicted success rate, confidence score, confidence interval (lower and upper bounds), and the ranked list of feature importances.
- **Nearest Neighbors**: The distances and labels of the K nearest training students.
- **Performance**: How long the model took to load, how long inference took, and the total prediction time.
- **Timestamps**: When the prediction was requested and when it completed.
- **Actual Outcome**: When eventually available, the student's actual success rate for comparison against the prediction.

### Attempt

The Attempt collection links student survey attempts to predictions and feedback. Relevant fields include:

- **Prediction Information**: The predicted success rate that was shown to the student, the model version that generated it, and a reference to the PredictionReq record.
- **Feedback**: The student's 1-to-5 rating of the prediction's accuracy. Low ratings below the configured threshold trigger a target survey retake to collect updated ground truth.
- **Success Rate Sources**: The calculated success rate (from PWRS), the final success rate used for training, and the source of that rate (calculated, self-reported, feedback-corrected, or pseudo-labeled).

---

## 15. Future Improvements for Model Predictions

### Near-Term Improvements

**Ensemble Methods**: Combine KNN predictions with a lightweight decision tree or ridge regression model. Average or stack the predictions from both models for more stable results. This reduces the model's sensitivity to any single neighbor being unusual. Ensemble methods typically reduce MAE by 5 to 15 percent compared to a single model, with minimal additional complexity.

**Feature Selection and Importance Analysis**: After training with sufficient data, analyze which of the 17 features actually contribute to prediction accuracy and which add noise without improving predictions. If certain features (for example, career goals) show no correlation with success rate, removing those columns reduces dimensionality. Fewer dimensions means KNN's distance calculations are more meaningful, because distance in fewer dimensions is more reliable than distance in many dimensions (the "curse of dimensionality").

**Weighted Feature Distances**: Instead of treating all 17 features equally in the distance calculation (after scaling), weight features by their priority scores or by their learned importance. This would make GPA (priority 9) matter more in determining which neighbors are "nearest" than commute distance (priority 6), reflecting the domain expertise encoded in the priority scores.

**Enhanced Prediction Explanations**: Beyond listing feature importance scores, generate natural language explanations that a student can understand. For example: "Your predicted success rate is 78 percent. Students most similar to you tend to succeed because of their strong academic background (GPA and SAT scores similar to yours). Your part-time work schedule is the factor that most distinguishes you from the highest-performing similar students."

### Medium-Term Improvements (With 50 to 100 Students)

**GAN-Based Data Augmentation**: As designed in the progressive learning strategy, train a Generative Adversarial Network to create synthetic student profiles that are statistically similar to real students. Expanding the dataset from 100 real students to 500 combined (real plus synthetic) enables training more complex models while maintaining realistic data distributions.

**Neural Network Transition**: With sufficient data (augmented via GAN), replace or supplement KNN with a feedforward neural network. Neural networks can learn more complex, non-linear relationships between features and success rates. Based on the performance expectations documented in the progressive learning strategy, this is expected to reduce MAE by approximately 15 to 20 percent compared to KNN alone.

**Time-Series Features**: Track students over multiple semesters rather than using a single snapshot. Instead of a one-time GPA range, the model could use GPA trajectory (improving, stable, declining) to predict future success. This requires longitudinal data collection but significantly enriches the feature space.

**Transfer Learning from Partner Institutions**: Use pre-trained models from partner universities within the NSF grant (which involves 5 institutions) as a starting point, then fine-tune on NEIU-specific data. This effectively increases the training set size by leveraging knowledge from similar institutions.

### Long-Term Improvements (Research Extensions)

**Causal Inference**: Move beyond correlation-based prediction to understanding which factors actually cause academic success versus merely correlating with it. Techniques like propensity score matching could estimate the causal effect of interventions (tutoring, scholarship, reduced work hours), enabling the system to recommend specific actions rather than just predicting outcomes.

**Dynamic Prediction Updates**: Instead of making a single prediction when the student takes the factor survey, update the prediction at multiple points during the semester as new information becomes available -- midterm grades, attendance records, advising session outcomes, and library usage data.

**Fairness and Bias Auditing**: Systematically test whether the model predicts equally well across demographic groups. If the model systematically under-predicts success for a particular group, bias correction techniques can be applied to ensure equitable predictions.

**Bayesian Uncertainty Quantification**: Replace the current heuristic confidence score (based on neighbor distance and label agreement) with a proper Bayesian approach (such as conformal prediction) that provides statistically calibrated prediction intervals. This would allow statements like "there is a 95 percent probability that this student's actual success rate falls between 62 and 84 percent" with mathematical rigor.

---

## 16. Additional Admin Configuration Options

### Currently Available

The admin interface currently supports the following configuration options:

- **KNN Hyperparameters**: Number of neighbors (or "auto"), weight strategy (distance or uniform), distance metric (euclidean, manhattan, or minkowski), and K-selection strategy (sqrt, log, or fixed).
- **Training Triggers**: Initial training threshold (how many students before first model training), retrain interval (how many new students between retraining cycles), feedback rating threshold (rating below which triggers a target survey retake), and a toggle to enable or disable automatic training.
- **PWRS Calibration**: Calibration curve type (logistic, linear, bounded, or sigmoid) and steepness parameter.
- **Profile Question Inclusion**: Per-quiz selection of which profile-scoped questions should be included as additional training features.

### Proposed Additional Configuration Options

**Feature Inclusion/Exclusion Toggle**: Allow admins to enable or disable specific features from the model without removing the survey question itself. For example, if analysis shows that "distance to campus" adds noise but no predictive value, the admin could exclude it from the next training run without altering the student-facing survey. This is a low-effort way to experiment with feature subsets.

**Cross-Validation Fold Count**: Allow admins to select the number of cross-validation folds (3, 5, or 10). With 50 or more students, 10-fold CV provides more reliable metric estimates. With fewer students, 3-fold CV avoids having too few test samples per fold.

**Model Quality Gate**: Set a minimum acceptable R-squared and a maximum acceptable MAE. If a newly trained model fails to meet these thresholds, the system keeps the previous model active and alerts the admin. This prevents a bad training run (due to noisy or insufficient data) from replacing a working model.

**Prediction Confidence Threshold**: A minimum confidence score below which the system flags a prediction as "low confidence." Optionally, low-confidence predictions could be withheld from the student entirely, with a message directing them to speak with an advisor instead. This prevents students from acting on unreliable predictions.

**Model Comparison Dashboard**: After retraining, show a side-by-side comparison of the old model's metrics versus the new model's metrics. Include MAE, R-squared, per-fold cross-validation details, and the number of training samples. This empowers the admin to make an informed decision about whether the new model is genuinely better.

**Feature Weight Overrides**: Allow admins to manually adjust the influence of specific features in the distance calculation. For example, the admin could configure GPA to count twice as much as other features, or reduce the influence of commute distance. This provides a way to incorporate domain expertise beyond what the raw data suggests.

**Outlier Detection Sensitivity**: A configurable distance threshold that flags predictions where the new student is far from all training data points. These "extrapolation zone" predictions are inherently less reliable because the model is being asked to predict for a type of student it has not seen before.

**Time-Based Retraining Schedule**: In addition to count-based triggers (retrain every N new students), support time-based triggers (retrain every 30 days) and degradation-based triggers (retrain if the average confidence of recent predictions drops below a threshold). Multiple trigger types can coexist, and training fires whenever any trigger condition is met.

**A/B Model Testing**: When a new model is trained, optionally serve predictions from both the old and new models to different students (randomly assigned). After collecting enough feedback ratings from both groups, compare which model actually performs better in practice. This data-driven approach to model selection avoids relying solely on offline metrics.

---

## 17. Glossary

**Artifact**: A file saved during model training that is needed for making predictions later. The KNN model saves five artifacts.

**Calibration Curve**: A mathematical function that maps a raw score (0 to 1) to a final percentage (0 to 100). The logistic calibration curve produces an S-shape that avoids extreme values.

**Cardinal Feature**: A feature where the possible values represent categories with no natural ordering. Career goals are a cardinal feature because "Academia" is not inherently "more" or "less" than "Industry."

**Confidence Interval**: A range around the predicted value within which the true value is expected to fall with a stated probability (usually 95 percent).

**Confidence Score**: A number between 0 and 1 indicating how certain the model is about its prediction. Higher values mean more certainty.

**Cross-Validation**: A technique for estimating how well a model will perform on unseen data by repeatedly splitting the training data into training and testing subsets.

**Encoding**: The process of converting non-numeric data (survey answers like "Between 3.0 and 3.5") into numeric values that a machine learning model can process.

**Euclidean Distance**: The straight-line distance between two points in multi-dimensional space. This is how the KNN model measures similarity between students.

**Feature**: A single measurable characteristic of a student used as input to the model. For example, GPA range is one feature. The current model uses 17 features.

**Feature Importance**: A measure of how influential a specific feature was in determining a particular prediction. High importance means the feature was a key factor in finding the nearest neighbors.

**Fold**: One of the subsets that the training data is divided into during cross-validation. In five-fold CV, the data is split into 5 equal parts.

**GAN (Generative Adversarial Network)**: A type of neural network that learns to generate new synthetic data that statistically resembles real data. Planned for Phase 3 of the progressive learning strategy.

**Hyperparameter**: A configuration setting for the model that is set before training, not learned from the data. K (number of neighbors) is a hyperparameter.

**Instance-Based Learning**: A type of machine learning where the model stores all training data and makes predictions by comparing new data to stored instances. KNN is an instance-based learner.

**K (Neighbors)**: The number of nearest neighbors the KNN model consults when making a prediction. With K equals 3, the model finds the 3 most similar training students.

**KNN (K-Nearest Neighbors)**: A machine learning algorithm that predicts a value by finding the K most similar data points in the training set and combining their known values.

**Label**: The known outcome for a training student. In this system, the label is the student's success rate (0 to 100) computed from the target survey.

**MAE (Mean Absolute Error)**: The average of the absolute differences between predicted and actual values. Lower is better.

**MSE (Mean Squared Error)**: The average of the squared differences between predicted and actual values. Penalizes large errors more heavily than MAE.

**Neural Network**: A machine learning model inspired by the human brain, consisting of layers of interconnected nodes. Planned for Phase 4 of the progressive learning strategy.

**One-Hot Encoding**: A technique for converting categorical variables into binary columns, where exactly one column is 1 and all others are 0.

**Ordinal Feature**: A feature where the possible values have a natural ordering. GPA range is ordinal because "More than 3.5" is meaningfully higher than "Below 2.0."

**Overfitting**: When a model performs well on training data but poorly on new, unseen data. It has memorized specific training examples rather than learning general patterns.

**Priority Score**: An administrator-assigned number (typically 1 to 10) reflecting how important a question is for predicting student success. Higher priority questions carry more weight in the PWRS calculation.

**Pseudo-Label**: A success rate generated by the model itself (rather than measured from a survey) and used as a provisional label for students who have not yet completed the target survey.

**PWRS (Priority-Weighted Response Scoring)**: The formula used to compute a readiness score from multi-question target survey responses. It normalizes each answer, weights by question priority, averages, and applies a calibration curve.

**R-Squared (Coefficient of Determination)**: A metric measuring how much of the variation in actual outcomes the model explains. Ranges from negative infinity to 1, where 1 is perfect and 0 means no better than guessing the average.

**Regressor**: A model that predicts a continuous numeric value (as opposed to a classifier, which predicts a category).

**RMSE (Root Mean Squared Error)**: The square root of MSE, in the same units as the predicted value.

**Scaling**: The process of transforming features to have comparable numeric ranges, preventing features with large values from dominating distance calculations.

**Serialization**: The process of converting an in-memory object (like a trained model) into a format that can be saved to disk and loaded back later.

**StandardScaler**: A scaling technique that transforms each feature to have a mean of 0 and a standard deviation of 1 by subtracting the mean and dividing by the standard deviation.

**Underfitting**: When a model is too simple to capture patterns in the data. It performs poorly on both training data and new data.

**Weightage**: A numeric value assigned to a survey answer option, reflecting its relative importance or magnitude. Higher weightages indicate stronger or more favorable responses.

**Z-Score Normalization**: Another name for standard scaling. Each value is expressed as the number of standard deviations from the mean.
