# Progressive Learning Strategy

## Slide 9: Four-Phase Progressive Model Evolution (4 minutes)

### Phase Progression Overview

```
Student Count →  0────10────20────50────100────200────1000+
                 │     │          │     │
Model Stage →    None  KNN        KNN   GAN+NN  NN (continuous)
                       ↑          ↑     ↑
Training Events:  Bootstrap  Retrain  Transform  Optimize
```

---

## Phase 1: Bootstrap (Students 1-10)

**Duration**: 2-4 weeks (depending on enrollment rate)

**Goal**: Collect initial training data

**Model**: None (data collection only)

**Action**: All students complete Target + Factor surveys

**Student Journey**:
```
Student #1-10:
  1. Enroll in program
  2. Complete demographic profile
  3. Complete TARGET survey → Get success rate label
  4. Complete FACTOR survey → Provide features
  5. NO prediction shown (insufficient data)
  6. Wait for more students...
```

**Backend Actions**:
```javascript
// After each student completes surveys
const studentCount = await Student.countDocuments({ quizCompleted: true });

if (studentCount < 10) {
  console.log(`Waiting for more students: ${studentCount}/10`);
  // No training, no predictions
} else if (studentCount === 10) {
  // Trigger KNN training!
  await triggerModelTraining('knn');
}
```

**Why 10 Students?**
- **Statistical minimum**: k-fold cross-validation requires minimum (k × 2) samples
- **5-fold CV**: 5 folds × 2 samples = 10 minimum
- **KNN requirement**: For k=3 neighbors, need at least 9 samples (we use 10 for safety)
- **Practical balance**: Can collect in 2-4 weeks vs waiting years

---

## Phase 2: KNN Deployment (Students 10-99)

**Goal**: Make predictions with minimal data

**Model**: K-Nearest Neighbors (KNN)

**Training Trigger**: When student #10 completes surveys

### KNN Algorithm Details

**Why KNN for Small Data?**

| Advantage | Explanation |
|-----------|-------------|
| **No training phase** | Instance-based learning, no parameters to fit |
| **Works with small data** | Effective with 10-100 samples |
| **Non-parametric** | No assumptions about data distribution |
| **Interpretable** | "You're similar to students #3, #7, #12" |
| **Fast deployment** | <1 second to "train" (just stores data) |

**Disadvantages**:
- ❌ Slow inference (O(n) distance calculations)
- ❌ Memory intensive (stores all training samples)
- ❌ Curse of dimensionality (degrades with >20 features)
- ❌ Sensitive to outliers

---

### KNN Configuration (Admin-Tunable)

```typescript
modelConfig: {
  knn: {
    n_neighbors: "auto",        // sqrt(n_students), capped 3-10
    weights: "distance",        // Closer neighbors weighted higher
    metric: "euclidean",        // L2 distance
    auto_k_strategy: "sqrt"     // k = sqrt(n_students)
  }
}
```

**Parameter Details**:

**1. `n_neighbors` (k value)**
```python
# Auto strategy
def calculate_k(n_students):
    k = int(math.sqrt(n_students))
    return min(10, max(3, k))  # Cap between 3-10

# Examples:
10 students → k = 3
25 students → k = 5
100 students → k = 10 (capped)
```

**2. `weights`**: "distance"
```python
# Distance-weighted prediction
weights = 1 / (distances + epsilon)
prediction = sum(neighbor.success_rate * weights) / sum(weights)

# Example:
# Neighbor #1: distance=0.12, weight=1/0.12=8.33, success=82
# Neighbor #2: distance=0.18, weight=1/0.18=5.56, success=74
# Neighbor #3: distance=0.21, weight=1/0.21=4.76, success=78
# Prediction = (82*8.33 + 74*5.56 + 78*4.76) / (8.33+5.56+4.76) = 78.5%
```

**3. `metric`**: "euclidean"
```python
# Euclidean distance (L2 norm)
distance = sqrt(sum((x_new[i] - x_train[i])^2))

# Example (4 features, all normalized 0-10):
# New student: [10.0, 7.08, 10.0, 10.0]  (GPA, SAT, Support, Duration)
# Neighbor #3:  [8.0, 6.5, 2.0, 9.5]

distance = sqrt(
  (10.0-8.0)^2 +     # GPA difference: 4.0
  (7.08-6.5)^2 +     # SAT difference: 0.34
  (10.0-2.0)^2 +     # Support difference: 64.0
  (10.0-9.5)^2       # Duration difference: 0.25
) = sqrt(68.59) = 8.28
```

---

### KNN Training Process

```python
# Step 1: Normalize all features to 0-10 scale
normalized_features = {
    "gpa": 10.0,        # "More than 3.5" → 10/10
    "sat": 7.08,        # 1250 / 1600 → normalized
    "family_support": 10.0,  # "Yes" → 10/10
    "duration": 10.0    # 3.75 years → ideal range
}

# Step 2: Build feature matrix X and label vector y
X = np.array([
    [10.0, 7.5, 10.0, 10.0],  # Student 1
    [2.0, 3.0, 2.0, 5.0],      # Student 2
    [10.0, 8.0, 10.0, 10.0],   # Student 3
    # ... 7 more students
])

y = np.array([85, 38, 91, ...])  # Success rates

# Step 3: Train KNN (just stores data)
from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(
    n_neighbors=3,
    weights='distance',
    metric='euclidean'
)

knn.fit(X, y)  # <1 second

# Step 4: 5-Fold Cross-Validation
from sklearn.model_selection import cross_val_score

mae_scores = cross_val_score(
    knn, X, y,
    cv=5,  # 5 folds (2 samples each)
    scoring='neg_mean_absolute_error'
)

mae = -mae_scores.mean()  # Expected: ~14 points
r2 = knn.score(X, y)      # Expected: ~0.42
```

---

### KNN Prediction Example

**New Student #11**:
```python
# Factor survey answers
factor_answers = {
    "gpa": "Between 3.0 and 3.5",
    "sat": 1100,
    "family_support": "Yes",
    "start_date": "08/2025",
    "end_date": "05/2029"
}

# Normalize
normalized = {
    "gpa": 8.0,
    "sat": 5.83,  # (1100-400)/(1600-400) * 10
    "family_support": 10.0,
    "duration": 10.0  # 3.75 years
}

# Create feature vector
X_new = np.array([[8.0, 5.83, 10.0, 10.0]])

# Find 3 nearest neighbors
distances, indices = knn.kneighbors(X_new, n_neighbors=3)

# Results:
# Neighbor #1: Student 3, distance=1.2, success=82%
# Neighbor #2: Student 7, distance=1.8, success=74%
# Neighbor #3: Student 12, distance=2.1, success=78%

# Distance-weighted prediction
prediction = knn.predict(X_new)
# Result: 78.5%
```

**Response to Student**:
```json
{
  "prediction": {
    "success_rate": 79,
    "confidence": 0.75,
    "model_type": "knn"
  },
  "nearestNeighbors": [
    {
      "studentId": "student_003",
      "distance": 1.2,
      "success_rate": 82,
      "similarity_factors": [
        "Similar GPA range (3.0-3.5)",
        "Same family support status (Yes)",
        "Comparable program timeline"
      ]
    }
  ]
}
```

---

### Performance Expectations (KNN Phase)

| Student Count | k | MAE (Expected) | R² (Expected) | Inference Time |
|---------------|---|----------------|---------------|----------------|
| 10 | 3 | 14.2 ± 3.5 | 0.42 | <10ms |
| 25 | 5 | 12.8 ± 2.8 | 0.51 | <25ms |
| 50 | 7 | 11.8 ± 2.1 | 0.54 | <50ms |
| 100 | 10 | 10.5 ± 1.8 | 0.61 | <100ms |

**Retraining Strategy**:
- **Every 10 new students**: Retrain KNN with updated dataset
- **Emergency trigger**: If average feedback rating <3.5 over last 20 predictions

---

## Phase 3: GAN Training (Student 100)

**Goal**: Generate synthetic data to augment small real dataset

**Challenge**: Neural networks need ~1000+ samples, we only have 100 real students

**Solution**: Conditional GAN generates 400 synthetic students (4× multiplier)

**Total Training Data**: 100 real + 400 synthetic = 500 samples

---

### Why GAN?

**The Neural Network Problem**:
```
Neural Network Requirements:
  - Minimum samples: 100-1000 (depends on complexity)
  - Rule of thumb: 10× samples per parameter
  - Our NN: ~5,000 parameters → need 50,000 samples ❌

Our Reality:
  - Have: 100 real students ✅
  - Need: 1000+ students for reliable NN training ❌

Solution:
  - GAN generates 400 synthetic students
  - Combined: 500 samples (5× improvement)
  - Enables NN training without waiting years ✅
```

---

### Conditional GAN Architecture

**Generator Network**:
```
Input: [Noise vector (100-dim)] + [Success rate bin (one-hot)]
       ↓
Hidden Layer 1: 128 neurons, activation=ReLU
       ↓
Hidden Layer 2: 256 neurons, activation=ReLU
       ↓
Hidden Layer 3: 128 neurons, activation=ReLU
       ↓
Output: [Normalized features (5-10 dim, range 0-10)]
```

**Discriminator Network**:
```
Input: [Feature vector (5-10 dim)] + [Success rate (continuous)]
       ↓
Hidden Layer 1: 128 neurons, activation=LeakyReLU(0.2)
       ↓
Hidden Layer 2: 64 neurons, activation=LeakyReLU(0.2)
       ↓
Hidden Layer 3: 32 neurons, activation=LeakyReLU(0.2)
       ↓
Output: [Real/Fake probability (0-1)]
```

---

### GAN Training Process

```python
# Training Configuration
epochs = 5000
batch_size = 16
latent_dim = 100
learning_rate = 0.0002

# Success rate bins (conditioning)
bins = {
    "Low": [0, 40],     # At-risk students
    "Medium": [41, 70], # Average students
    "High": [71, 100]   # High-performing students
}

# Training loop (simplified)
for epoch in range(5000):
    # Phase 1: Train Discriminator
    # (a) Real students
    real_features, real_success = sample_real_students(batch_size=16)
    real_labels = ones(16)  # Label as real (1)
    d_loss_real = train_discriminator(real_features, real_success, real_labels)
    
    # (b) Fake students
    noise = random_normal(16, 100)
    success_bins = sample_bins(16)
    fake_features = generator.predict([noise, success_bins])
    fake_labels = zeros(16)  # Label as fake (0)
    d_loss_fake = train_discriminator(fake_features, success_bins, fake_labels)
    
    d_loss = (d_loss_real + d_loss_fake) / 2
    
    # Phase 2: Train Generator
    noise = random_normal(16, 100)
    success_bins = sample_bins(16)
    misleading_labels = ones(16)  # Fool discriminator
    g_loss = train_generator(noise, success_bins, misleading_labels)
    
    if epoch % 500 == 0:
        print(f"Epoch {epoch}: D_loss={d_loss:.4f}, G_loss={g_loss:.4f}")

# Expected convergence: ~3000 epochs
```

---

### Synthetic Data Generation

**Proportional Generation** (match real data distribution):
```python
# Count real students in each bin
real_distribution = {
    "Low": 20 students (20%),
    "Medium": 50 students (50%),
    "High": 30 students (30%)
}

# Generate 400 synthetic (4× multiplier)
synthetic_generation = {
    "Low": 80 students (20% of 400),
    "Medium": 200 students (50% of 400),
    "High": 120 students (30% of 400)
}

# Total training data
total = {
    "Low": 20 + 80 = 100,
    "Medium": 50 + 200 = 250,
    "High": 30 + 120 = 150,
    "Total": 500 samples
}
```

---

### Quality Validation

**CRITICAL**: Validate synthetic data before using for training

```python
# Metric 1: Correlation Similarity
real_corr = correlation_matrix(real_features)
synthetic_corr = correlation_matrix(synthetic_features)
corr_diff = abs(real_corr - synthetic_corr)
assert corr_diff.mean() < 0.2  # Pass: correlations preserved

# Metric 2: Distribution Match (Kolmogorov-Smirnov Test)
from scipy.stats import ks_2samp
for feature in features:
    statistic, p_value = ks_2samp(real[feature], synthetic[feature])
    assert p_value > 0.05  # Pass: distributions statistically similar

# Metric 3: Feature Mean Similarity
real_means = real_features.mean(axis=0)
synthetic_means = synthetic_features.mean(axis=0)
mean_diff = abs(real_means - synthetic_means)
assert (mean_diff < 0.1).all()  # Pass: means within 0.1 per feature
```

**If quality checks fail** → Retrain GAN with adjusted hyperparameters

---

## Phase 4: Neural Network Training (Students 100+)

**Goal**: Maximum prediction accuracy with GAN-augmented data

**Model**: Feedforward Neural Network

**Training Trigger**: Immediately after GAN training completes

---

### Neural Network Architecture

```
Input Layer: 5-10 features (normalized 0-10)
       ↓
Hidden Layer 1: 128 neurons
  - Activation: ReLU
  - Dropout: 0.2
       ↓
Hidden Layer 2: 64 neurons
  - Activation: ReLU
  - Dropout: 0.2
       ↓
Hidden Layer 3: 32 neurons
  - Activation: ReLU
  - Dropout: 0.1
       ↓
Output Layer: 1 neuron
  - Activation: Sigmoid (0-1, scaled to 0-100%)
```

---

### Training Process (CRITICAL: Real-Only Validation)

```python
# Step 1: Split REAL students FIRST
X_real, y_real = load_real_students()  # 100 students
X_real_train, X_real_val, y_real_train, y_real_val = train_test_split(
    X_real, y_real,
    test_size=0.2,
    random_state=42
)  # 80 train, 20 validation

# Step 2: Generate synthetic data
X_synthetic, y_synthetic = gan.generate(n_samples=400)

# Step 3: Combine for training (real + synthetic)
X_train = np.vstack([X_real_train, X_synthetic])  # 80 + 400 = 480
y_train = np.concatenate([y_real_train, y_synthetic])

# Step 4: Train on mixed data, validate on REAL ONLY
model.compile(
    optimizer='adam',
    loss='mean_squared_error',
    metrics=['mae']
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_real_val, y_real_val),  # Real validation only!
    epochs=100,
    batch_size=32,
    callbacks=[
        EarlyStopping(monitor='val_loss', patience=10),
        ModelCheckpoint('best_model.h5', save_best_only=True)
    ]
)

# Step 5: Evaluate on real validation set
predictions = model.predict(X_real_val)
mae = mean_absolute_error(y_real_val, predictions)
r2 = r2_score(y_real_val, predictions)

# Expected results:
# MAE: ~9 points (improvement from KNN's ~11)
# R²: ~0.71 (improvement from KNN's ~0.61)
```

**Why Validate on Real Students ONLY?**
- Synthetic data reflects GAN's understanding of real data
- Validating on synthetic = circular dependency (testing model on its own assumptions)
- Real validation ensures generalization to actual students
- Production predictions serve real people, not synthetic profiles

---

### Performance Comparison

| Model | Training Data | MAE | R² | Inference Time |
|-------|---------------|-----|-----|----------------|
| **KNN** | 100 real | 10.5 | 0.61 | 100ms |
| **NN (no GAN)** | 100 real | 13.2 | 0.48 | 5ms |
| **NN + GAN** | 100 real + 400 syn | **8.7** | **0.73** | 5ms |

**Key Insight**: GAN augmentation reduces MAE by 17% compared to NN without augmentation!

---

### Continuous Improvement (Students 101+)

**Retraining Strategy**:

| Trigger | Frequency | Action | Duration |
|---------|-----------|--------|----------|
| **10 new students** | Every ~2-3 weeks | Retrain NN only | 5 min |
| **50 new students** | Every ~3-4 months | Retrain GAN + NN | 30 min |
| **Avg rating <3.5** | As needed | Emergency NN retrain | 5 min |

```python
# Backend monitors student count
async function checkRetrainingTriggers() {
  const studentCount = await getStudentCount();
  const lastTraining = await getLastTrainingTimestamp();
  
  if (studentCount >= lastTraining.studentCount + 10) {
    // Every 10 students: Retrain NN
    await triggerModelTraining('neural');
  }
  
  if (studentCount >= lastTraining.studentCount + 50) {
    // Every 50 students: Retrain GAN + NN
    await triggerModelTraining('gan');
    await triggerModelTraining('neural');
  }
}
```

---

## Speaking Points Summary

**Key Messages**:

1. **Progressive Evolution**: "ACOSUS starts simple with KNN at 10 students, then automatically upgrades to neural networks at 100+ students."

2. **GAN Innovation**: "We use GANs to generate 400 synthetic students from 100 real ones, enabling neural network training years earlier."

3. **Validation Rigor**: "Critically, we validate neural networks ONLY on real students, never synthetic, ensuring predictions generalize to actual people."

4. **Continuous Learning**: "The system retrains automatically every 10 students, continuously improving without manual intervention."

5. **Performance Gains**: "GAN augmentation improves accuracy by 17% compared to neural networks without augmentation - that's the difference between MAE of 13 and MAE of 9 points."
