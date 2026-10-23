import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import xgboost as xgb

# Load dataset
df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
print(f"Dataset shape: {df.shape}")

# Features and target
X = df.drop('Machine failure', axis=1)
y = df['Machine failure']

print(f"Class distribution: {y.value_counts().to_dict()}")
print(f"Class imbalance ratio: {y.value_counts()[0] / y.value_counts()[1]:.1f}:1")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Calculate class weight for imbalance handling
class_weights = {0: 1.0, 1: len(y_train[y_train==0]) / len(y_train[y_train==1])}
print(f"Class weight for failure class: {class_weights[1]:.2f}")

results = []

# 1. Logistic Regression with class_weight
print("\n=== Training Logistic Regression ===")
lr = LogisticRegression(max_iter=1000, class_weight='balanced')
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)
acc_lr = accuracy_score(y_test, y_pred_lr)
cm_lr = confusion_matrix(y_test, y_pred_lr)
print(f"Logistic Regression Accuracy: {acc_lr:.4f}")
print(f"Classification Report:\n{classification_report(y_test, y_pred_lr, digits=4)}")
results.append({
    'model': 'Logistic Regression',
    'accuracy': acc_lr,
    'confusion_matrix': cm_lr.tolist(),
    'classification_report': classification_report(y_test, y_pred_lr, digits=4)
})

# 2. Random Forest with class_weight
print("\n=== Training Random Forest ===")
rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced', n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
cm_rf = confusion_matrix(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {acc_rf:.4f}")
print(f"Classification Report:\n{classification_report(y_test, y_pred_rf, digits=4)}")
# Feature importance
importances = rf.feature_importances_
feature_names = X.columns.tolist()
print(f"Feature importances: {list(zip(feature_names, importances))}")
results.append({
    'model': 'Random Forest',
    'accuracy': acc_rf,
    'confusion_matrix': cm_rf.tolist(),
    'classification_report': classification_report(y_test, y_pred_rf, digits=4)
})

# 3. XGBoost with scale_pos_weight for imbalance
print("\n=== Training XGBoost ===")
# XGBoost doesn't support column names with [, ] characters
# Rename columns to remove brackets
X_train_xgb = X_train.copy()
X_test_xgb = X_test.copy()
new_col_names = [col.replace('[', '(').replace(']', ')') for col in X_train_xgb.columns]
X_train_xgb.columns = new_col_names
X_test_xgb.columns = new_col_names

scale_pos = len(y_train[y_train==0]) / len(y_train[y_train==1])
xgb_model = xgb.XGBClassifier(
    n_estimators=100, 
    random_state=42, 
    eval_metric='logloss',
    scale_pos_weight=scale_pos,
    n_jobs=-1
)
xgb_model.fit(X_train_xgb, y_train)
# Predict - need to use the transformed test data
y_pred_xgb = xgb_model.predict(X_test_xgb)
acc_xgb = accuracy_score(y_test, y_pred_xgb)
cm_xgb = confusion_matrix(y_test, y_pred_xgb)
print(f"XGBoost Accuracy: {acc_xgb:.4f}")
print(f"Classification Report:\n{classification_report(y_test, y_pred_xgb, digits=4)}")
results.append({
    'model': 'XGBoost',
    'accuracy': acc_xgb,
    'confusion_matrix': cm_xgb.tolist(),
    'classification_report': classification_report(y_test, y_pred_xgb, digits=4)
})

# 4. MLP with class weight balancing
print("\n=== Training MLP ===")
mlp = MLPClassifier(
    hidden_layer_sizes=(64, 32), 
    max_iter=500, 
    random_state=42,
    early_stopping=True,
    validation_fraction=0.1
)
mlp.fit(X_train_scaled, y_train)
y_pred_mlp = mlp.predict(X_test_scaled)
acc_mlp = accuracy_score(y_test, y_pred_mlp)
cm_mlp = confusion_matrix(y_test, y_pred_mlp)
print(f"MLP Accuracy: {acc_mlp:.4f}")
print(f"Classification Report:\n{classification_report(y_test, y_pred_mlp, digits=4)}")
results.append({
    'model': 'MLP',
    'accuracy': acc_mlp,
    'confusion_matrix': cm_mlp.tolist(),
    'classification_report': classification_report(y_test, y_pred_mlp, digits=4)
})

# Summary comparison
print("\n\n=== MODEL COMPARISON SUMMARY ===")
summary_df = pd.DataFrame({
    'Model': [r['model'] for r in results],
    'Accuracy': [r['accuracy'] for r in results]
})
print(summary_df.sort_values('Accuracy', ascending=False))

# Plot comparison
plt.figure(figsize=(10, 6))
sns.barplot(data=summary_df.sort_values('Accuracy', ascending=False), x='Model', y='Accuracy')
plt.title('Model Accuracy Comparison - AI4I 2020 Dataset')
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig('reports/model_comparison.png', dpi=150, bbox_inches='tight')
plt.close()

# Plot confusion matrices
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
models_names = [r['model'] for r in results]
for i, result in enumerate(results):
    row, col = divmod(i, 2)
    im = sns.heatmap(result['confusion_matrix'], annot=True, fmt='d', cmap='Blues', ax=axes[row, col])
    axes[row, col].set_title(f"{result['model']} - Confusion Matrix")
    axes[row, col].set_xlabel('Predicted')
    axes[row, col].set_ylabel('Actual')

plt.tight_layout()
plt.savefig('reports/confusion_matrices.png', dpi=150, bbox_inches='tight')
plt.close()

# Save results to CSV
results_summary = pd.DataFrame({
    'Model': [r['model'] for r in results],
    'Accuracy': [r['accuracy'] for r in results]
})
results_summary.to_csv('reports/model_results.csv', index=False)

print("\nResults saved to reports/ directory")
print("model_comparison.png, confusion_matrices.png, model_results.csv")