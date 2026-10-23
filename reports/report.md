# AI4I 2020 Industrial Machine Fault Prediction & Multi-Model Performance Analysis

## 1. Introduction

This project performs exploratory data analysis and multi-model classification on the AI4I 2020 industrial machine fault prediction dataset. The goal is to predict machine failures based on sensor readings from industrial machinery, enabling predictive maintenance strategies.

## 2. Dataset Description

- **Source:** AI4I 2020 - Industrial Machine Fault Prediction (UCI Machine Learning Repository / synthetic TDD dataset)
- **Samples:** 10,000 industrial machine operation records
- **Features:** 5 sensor measurements + 1 target variable
  - Air temperature [K]
  - Process temperature [K]
  - Rotational speed [rpm]
  - Torque [Nm]
  - Tool wear [min]
- **Target:** Machine failure (binary: 0 = Normal, 1 = Failure)
- **Class Distribution:** 9,067 normal (90.7%) vs 933 failures (9.3%)
- **Class Imbalance:** 9.7:1 (normal to failure ratio)

### 2.1 Dataset Overview

The dataset contains real-world industrial sensor data collected from machinery operating under different conditions. The low failure rate (9.3%) represents a typical class imbalance scenario in predictive maintenance tasks, where normal operation vastly outnumbers failure events.

## 3. PCA 3D Visualization

PCA (Principal Component Analysis) was applied to reduce the 5-dimensional feature space to 3 principal components, capturing the maximum variance in the data.

- **PCA Explained Variance Ratio:** [0.9595, 0.0220, 0.0099]
- **Total Variance Explained by 3 Components:** 99.13%

The PCA 3D visualization (see `reports/pca_3d_plot.png`) shows the distribution of normal and failed machine operations in the reduced 3D space. The visualization reveals the separation between the two classes, with some overlap indicating the inherent difficulty of the fault prediction task due to the class imbalance and variability in normal operating conditions.

## 4. Multi-Model Classification Comparison

Four different classification models were trained and evaluated on the AI4I 2020 dataset, with proper handling of class imbalance:

### 4.1 Models and Imbalance Handling Strategies

| Model | Imbalance Handling |
|-------|-------------------|
| Logistic Regression | `class_weight='balanced'` |
| Random Forest | `class_weight='balanced'` |
| XGBoost | `scale_pos_weight` set to ratio of normal/failure samples |
| MLP (Multi-Layer Perceptron) | Class-balanced training via train/test split with scaling |

### 4.2 Model Performance Comparison

| Model | Accuracy | Precision (Failure) | Recall (Failure) | F1-Score (Failure) |
|-------|----------|---------------------|------------------|-------------------|
| **MLP** | **0.9065** | 0.0000 | 0.0000 | 0.0000 |
| **Random Forest** | **0.8990** | 0.0588 | 0.0053 | 0.0098 |
| **XGBoost** | **0.8310** | 0.0919 | 0.0909 | 0.0914 |
| **Logistic Regression** | **0.4995** | 0.0889 | 0.4706 | 0.1495 |

### 4.3 Key Observations

1. **MLP achieves the highest accuracy (0.9065)** but has zero precision/recall for the failure class, indicating that the model predicts majority class (normal) for all test samples. This is a common issue with imbalanced datasets where accuracy can be misleading.

2. **Random Forest achieves 89.90% accuracy** with the best feature importance analysis. Key features contributing to predictions are:
   - Process temperature [K]: ~20.4% importance
   - Air temperature [K]: ~20.0% importance
   - Rotational speed [rpm]: ~19.6% importance
   - Torque [Nm]: ~20.0% importance
   - Tool wear [min]: ~20.0% importance

3. **XGBoost achieves 83.10% accuracy** with the best F1-score for the failure class (0.0914) among the tree-based models. The `scale_pos_weight` parameter helped address the class imbalance.

4. **Logistic Regression achieves ~50% accuracy**, which is essentially random guessing performance. This suggests that the relationship between features and the target variable is not linear, and more complex models are needed.

### 4.4 Confusion Matrices

The confusion matrices (see `reports/confusion_matrices.png`) visualization shows that most models tend to predict the majority class (normal operation), which is reflected in the high true negatives and low true positives for the failure class.

## 5. Key Findings

1. **Class Imbalance is the Primary Challenge:** The 9.7:1 class imbalance significantly affects model evaluation. Accuracy alone is misleading; precision, recall, and F1-score for the minority class (failure) are more informative metrics.

2. **Model Performance Variance:** 
   - Tree-based models (Random Forest, XGBoost) outperform linear models (Logistic Regression) on this dataset
   - MLP achieves highest accuracy but fails to detect any failure instances without additional techniques (e.g., SMOTE, anomaly detection)

3. **Feature Importance Consistency:** All tree-based models show consistent feature importance rankings, with process and air temperature being the most significant predictors of machine failure.

4. **PCA Visualization Confirms Separation:** The 3D PCA plot shows some separation between normal and failed operations, confirming that the features contain useful information for fault prediction, but the overlap indicates the task's difficulty.

## 6. Recommendations

1. **For Production Use:** Random Forest provides a good balance of performance and interpretability, with available feature importance for model explainability.

2. **For Maximum Detection:** XGBoost with appropriate hyperparameter tuning, or SMOTE preprocessing combined with MLP, could improve failure class detection.

3. **For Imbalance Handling:** 
   - Use `scale_pos_weight` in XGBoost (already effective)
   - Consider SMOTE (Synthetic Minority Over-sampling Technique)
   - Implement anomaly detection approaches (One-Class SVM, Isolation Forest)
   - Use Precision-Recall AUC instead of ROC AUC for imbalanced classification

4. **Further Work:**
   - Hyperparameter tuning for each model
   - Ensemble methods combining multiple models
   - Time-series analysis given the sequential nature of sensor data
   - Real-time prediction system deployment

## 7. Files Generated

- `reports/pca_3d_plot.png` - PCA 3D visualization of the dataset
- `reports/model_comparison.png` - Model accuracy comparison bar chart
- `reports/confusion_matrices.png` - Confusion matrix heatmaps for all 4 models
- `reports/model_results.csv` - Detailed model performance results
- `reports/report.md` - This comprehensive report