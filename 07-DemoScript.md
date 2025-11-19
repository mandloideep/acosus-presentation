# Live Demo Script (10 Minutes)

## Demo Overview

**Duration**: 10 minutes
**Format**: Live demonstration on acosus.neiu.edu
**Backup**: Screenshots ready in case of network issues

**Structure**:
1. Admin Portal (3 min) - Quiz creation, model configuration
2. Student Portal (4 min) - Surveys, predictions (future state)
3. Analytics Dashboard (3 min) - Data tracking, metrics

---

## Pre-Demo Checklist

### Setup (5 minutes before presentation)

```bash
# Open browser tabs (in this order):
Tab 1: https://acosus.neiu.edu/admin (logged in as admin)
Tab 2: https://acosus.neiu.edu/student (logged in as student)
Tab 3: https://acosus.neiu.edu/admin/dashboard
Tab 4: Backup screenshots folder (just in case)

# Demo accounts:
Admin: admin@neiu.edu / [password]
Student: student_demo@neiu.edu / [password]

# Clear any test data (optional):
# - Delete test quizzes
# - Reset student demo account
# OR keep 1-2 sample entries for demonstration
```

### Equipment Check

- [ ] Projector/screen sharing working
- [ ] Browser zoom set to 100% (for readability)
- [ ] Audio muted (avoid notification sounds)
- [ ] Dark mode enabled (better visibility)
- [ ] Mouse cursor visible and large enough

---

## Part 1: Admin Portal (3 minutes)

### Minute 1: Login & Overview (30 seconds)

**Script**:
> "Let me show you the admin portal where faculty configure ACOSUS. I'm logged in as an administrator."

**Actions**:
1. Show admin dashboard homepage
2. Point out key sections:
   - Quiz Management
   - Model Configuration
   - Student Analytics
   - System Status

**Narration**:
> "Admins can create surveys, configure ML models, and track system performance - all without writing code."

---

### Minute 2: Create Target Survey (1.5 minutes)

**Script**:
> "First, I'll create a target survey to collect success rates. We support two types: single-question for simplicity, or multi-question for comprehensive assessment."

**Actions**:

1. **Click "Create New Quiz"**
2. **Fill in basic info**:
   ```
   Title: "CS Program Success Assessment"
   Description: "Self-assessment of academic success likelihood"
   Quiz Type: [Select: Target]
   Target Type: [Select: Single Question]
   ```

3. **Configure single-question**:
   ```
   Question: "What is your self-assessed success rate (0-100%)?"
   Input Type: Slider (0-100)
   ```

4. **Click "Save Quiz"**

**Narration**:
> "For this demo, I'm using a single-question survey for speed. In practice, administrators can create multi-question surveys with the PWRS formula I explained earlier - assigning priority scores and option weightages to each question."

**Alternative** (if time permits):
> "Let me briefly show the multi-question option..."
- Click "Add Question"
- Show priority score slider (1-10)
- Show option weightage fields
- Don't save (just demonstrate UI)

---

### Minute 3: Create Factor Survey + Model Config (1 minute)

**Script**:
> "Now I'll create a factor survey - this collects predictive features without asking about success rate."

**Actions**:

1. **Click "Create New Quiz"** (again)
2. **Fill in basic info**:
   ```
   Title: "CS Academic Background Survey"
   Quiz Type: [Select: Factor]
   Link to Target Quiz: [Select: "CS Program Success Assessment"]
   ```

3. **Add 2-3 sample questions** (quick):
   ```
   Question 1:
     Text: "What is your high school GPA?"
     Type: String (multi-option)
     Priority: 9
     Options:
       - "Below 2.0" (weightage: 2)
       - "2.0-3.0" (weightage: 4)
       - "3.0-3.5" (weightage: 8)
       - ">3.5" (weightage: 10)
   
   Question 2:
     Text: "Do you have family financial support?"
     Type: String
     Priority: 7
     Options:
       - "Yes" (weightage: 10)
       - "No" (weightage: 2)
   ```

4. **Scroll to Model Configuration section**
5. **Show KNN settings** (don't modify, just point out):
   ```
   n_neighbors: auto
   weights: distance
   metric: euclidean
   ```

6. **Click "Save & Publish"**

**Narration**:
> "Notice the priority scores - GPA has priority 9/10 because it's a strong predictor. Family support is 7/10. The model will weight these questions accordingly using the PWRS formula."

> "Below, I can configure KNN parameters. The system uses sensible defaults, but admins can tune these for their specific context."

---

## Part 2: Student Portal (4 minutes)

### Minute 4: Student Login & Profile (1 minute)

**Script**:
> "Now let's see the student perspective. I'll log in as a demo student."

**Actions**:

1. **Switch to student tab** (Tab 2)
2. **Show student dashboard**:
   - Welcome message
   - Profile completion status
   - Assigned quizzes (0/2 complete)

3. **Navigate to Profile section**
4. **Show demographic fields**:
   ```
   Name: Jane Doe
   Email: student_demo@neiu.edu
   Age Group: 18-22
   Gender: Female
   Degree: Bachelor's in Computer Science
   Start Date: 08/2025
   Expected Graduation: 05/2029
   ```

**Narration**:
> "Students first complete their profile with basic demographics and academic information. This takes about 2-3 minutes."

---

### Minute 5-6: Take Target Survey (1.5 minutes)

**Script**:
> "Now the student takes the target survey we just created."

**Actions**:

1. **Navigate to "Assigned Quizzes"**
2. **Click "Start" on "CS Program Success Assessment"**
3. **Show single-question interface**:
   ```
   ┌─────────────────────────────────────────────┐
   │  CS Program Success Assessment              │
   │                                             │
   │  What is your self-assessed success rate?   │
   │                                             │
   │  0% ──────────●──────────── 100%            │
   │             75%                             │
   │                                             │
   │  [Submit]                                   │
   └─────────────────────────────────────────────┘
   ```

4. **Drag slider to 75%**
5. **Click "Submit"**
6. **Show confirmation**: "Success rate recorded: 75%"

**Narration**:
> "This single-question format is fast - students can complete it in 30 seconds. The alternative multi-question format takes 8-10 minutes but provides more comprehensive assessment."

---

### Minute 7-8: Take Factor Survey (1.5 minutes)

**Script**:
> "Next, the factor survey collects predictive features."

**Actions**:

1. **Click "Start" on "CS Academic Background Survey"**
2. **Walk through questions** (actually click through):
   ```
   Question 1/7: What is your high school GPA?
   [Select: "Between 3.0 and 3.5"]
   [Click Next]
   
   Question 2/7: Do you have family financial support?
   [Select: "Yes"]
   [Click Next]
   
   ... (show 1-2 more, then skip to end)
   
   Question 7/7: When do you expect to graduate?
   [Enter: 05/2029]
   [Click Submit]
   ```

3. **Show completion confirmation**:
   ```
   "Thank you for completing the survey!
   Your responses have been recorded."
   ```

**Narration**:
> "The factor survey takes 3-5 minutes. Notice we're NOT asking about success rate here - we're collecting features to PREDICT it."

---

### Minute 9: View Prediction (Future State Demo)

**Script**:
> "Now I'll show what happens when 10 students complete surveys and the model is trained. This is a mockup since we haven't enrolled 10 students yet."

**Actions**:

1. **Navigate to "My Predictions" section**
2. **Show mockup UI**:
   ```
   ┌─────────────────────────────────────────────┐
   │  Your Predicted Success Rate: 74%          │
   │                                             │
   │  ████████████████████░░░░░░░░               │
   │                                             │
   │  Students Similar to You:                  │
   │  • Student #3: 82% (similar GPA)           │
   │  • Student #7: 71% (similar support)       │
   │  • Student #12: 68% (similar timeline)     │
   │                                             │
   │  How accurate is this?                     │
   │  ☆ ☆ ☆ ☆ ☆  (Rate 1-5 stars)               │
   │                                             │
   │  [Current Status: Waiting for 10 students] │
   └─────────────────────────────────────────────┘
   ```

**Narration**:
> "Once the model is trained, students see their predicted success rate with similar student profiles. They rate the prediction, and if they give 4-5 stars, we use it as a training label - avoiding another survey. If they give 1-3 stars, we ask for correction."

**Point out key features**:
- Prediction: 74%
- Similar students (interpretability)
- Feedback rating mechanism
- Current status indicator

---

## Part 3: Analytics Dashboard (3 minutes)

### Minute 10: Admin Dashboard Overview (1.5 minutes)

**Script**:
> "Finally, let's look at the analytics dashboard where admins monitor system performance."

**Actions**:

1. **Switch to admin dashboard tab** (Tab 3)
2. **Show Bootstrap Progress**:
   ```
   ┌─────────────────────────────────────────────┐
   │  Bootstrap Phase: 0 / 10 Students           │
   │  [░░░░░░░░░░░░░░░░░░░░░░░░] 0%              │
   │                                             │
   │  ┌───────────┐ ┌───────────┐ ┌────────────┐│
   │  │ Enrolled  │ │ Completed │ │Predictions ││
   │  │     0     │ │     0     │ │     0      ││
   │  └───────────┘ └───────────┘ └────────────┘│
   └─────────────────────────────────────────────┘
   ```

3. **Point out active quizzes**:
   ```
   Active Quizzes:
   • CS Program Success Assessment (Target) - 0 attempts
   • CS Academic Background Survey (Factor) - 0 attempts
   ```

4. **Show model status**:
   ```
   Model Status:
   • Current: None (waiting for 10 students)
   • Training Queue: Empty
   • Next Training: At 10 students
   ```

**Narration**:
> "The dashboard shows bootstrap progress. We're at 0 out of 10 students. Once 10 enroll, the system automatically trains the KNN model within seconds."

---

### Minute 11-12: Future State Metrics (1.5 minutes)

**Script**:
> "Let me show what this dashboard will look like once the model is trained and making predictions."

**Actions**:

1. **Show mockup of trained state**:
   ```
   ┌─────────────────────────────────────────────┐
   │  Model Performance (After 50 students)      │
   │                                             │
   │  Current Model: KNN v3_20260215_103045      │
   │  MAE: 11.8 points                           │
   │  R²: 0.54                                   │
   │  Avg Feedback: 3.6/5.0 ⭐⭐⭐⭐                │
   │                                             │
   │  Last Trained: Feb 15, 2026                 │
   │  Next Retrain: At 60 students               │
   │                                             │
   │  ┌─────────────────────────────────────┐   │
   │  │  MAE Trend (Improving)              │   │
   │  │  15 ┤╮                               │   │
   │  │  14 ┤ ╰╮                             │   │
   │  │  13 ┤  ╰─╮                           │   │
   │  │  12 ┤    ╰─●                         │   │
   │  │     └────────────────────            │   │
   │  │     10  20  30  40  50 students     │   │
   │  └─────────────────────────────────────┘   │
   │                                             │
   │  Pseudo-Label Rate: 62% ✅                  │
   │  Survey Time Reduction: 68% ✅              │
   └─────────────────────────────────────────────┘
   ```

2. **Point out key metrics**:
   - MAE trending downward (improving)
   - Feedback ratings improving
   - Pseudo-label rate (62%)
   - Survey time reduction (68%)

**Narration**:
> "Once operational, admins see MAE trending downward as the model learns, feedback ratings improving as predictions get better, and pseudo-label rate increasing - all indicators of a healthy feedback loop."

---

## Demo Wrap-Up (30 seconds)

**Script**:
> "To summarize what we've seen:"
> 
> "**Admins** can create target and factor surveys, configure ML models, and monitor performance - all through an intuitive interface."
> 
> "**Students** complete quick surveys (3-5 minutes for factor, 30 seconds for single-question target), and once 10 enroll, they receive predictions with explanations."
> 
> "**The system** automatically trains models, collects feedback, and continuously improves - all without manual intervention."
> 
> "ACOSUS is live at acosus.neiu.edu and ready to start collecting real student data."

---

## Backup Plan: Network Issues

**If live demo fails**:

1. **Switch to backup screenshots** (Tab 4)
2. **Apologize briefly**: "Looks like we're having network issues. Let me show you screenshots instead."
3. **Walk through same flow** using static images
4. **Keep narration identical** to live demo script

**Screenshots to prepare**:
- [ ] Admin dashboard homepage
- [ ] Quiz creation form (filled)
- [ ] Model configuration panel
- [ ] Student dashboard
- [ ] Survey UI (target + factor)
- [ ] Prediction display (mockup)
- [ ] Analytics dashboard (current + future state)

---

## Anticipated Demo Questions

### Q: "Can you show the multi-question PWRS formula in action?"

**A**: "Absolutely. Let me navigate to the question builder..."
- Show priority score slider
- Show option weightage fields
- Walk through example calculation (briefly)
- Mention correlation validation

### Q: "How long does model training take?"

**A**: "Excellent question. Let me check the system logs..."
- Show training queue status
- Mention KNN: <1 second
- GAN: ~20 minutes
- Neural Network: ~5 minutes
- Emphasize automatic triggering

### Q: "What happens if a student gives a bad rating?"

**A**: "Great question. Let me show the feedback flow..."
- Navigate to feedback UI mockup
- Show rating <4 path
- Demonstrate target survey request
- Explain error tracking

---

## Time Management

**If running ahead**:
- Show additional quiz configuration options
- Demonstrate model parameter tuning
- Walk through data export features

**If running behind**:
- Skip multi-question demo (just mention it)
- Show factor survey for 1-2 questions only
- Skip future state analytics (just describe verbally)

**Critical path** (must show):
1. Admin creates target survey (1 min)
2. Admin creates factor survey (1 min)
3. Student takes surveys (2 min)
4. Show prediction mockup (1 min)
5. Admin dashboard (1 min)

---

## Post-Demo Actions

**If committee asks to explore**:
- Be ready to navigate anywhere in the system
- Know where all features are located
- Have admin password memorized (don't fumble)

**If technical questions arise**:
- Refer to detailed files (01-06)
- Offer to show code (if appropriate)
- Explain architecture (refer to 02-SystemArchitecture.md)

---

## Speaking Points Summary

**Key Messages**:

1. **Production Ready**: "This is a live system, not a prototype - it's deployed and operational."

2. **User-Friendly**: "Admins configure everything through the UI - no coding required."

3. **Fast Surveys**: "Students complete factor surveys in 3-5 minutes, target surveys in 30 seconds to 10 minutes."

4. **Automatic Training**: "When the 10th student submits, the system automatically trains KNN within seconds."

5. **Feedback Loop**: "Students rate predictions, and high ratings become training labels - reducing survey burden by 50-70%."

6. **Transparent**: "We're at 0/10 students currently, but the system is ready to collect real data starting today."
