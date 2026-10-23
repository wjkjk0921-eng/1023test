#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Iris Dataset Analysis & Neural Network Classification
"""
import os
import numpy as np

# Ensure output directories exist
os.makedirs('data', exist_ok=True)
os.makedirs('reports', exist_ok=True)
os.makedirs('models', exist_ok=True)

# ----------------------------
# 1. Load and save Iris dataset
# ----------------------------
# ... (rest unchanged)
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # non-GUI backend
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data

# ----------------------------
# 1. Load and save Iris dataset
# ----------------------------
print("=== 1. Loading Iris Dataset ===")
iris = datasets.load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Save to CSV
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y
df['target_name'] = [target_names[i] for i in y]
df.to_csv('data/iris.csv', index=False)
print("Saved to data/iris.csv")

# ----------------------------
# 2. PCA 3D analysis and visualization
# ----------------------------
print("\n=== 2. PCA 3D Feature Analysis ===")
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

# Explained variance
print("PCA explained variance ratio:", pca.explained_variance_ratio_)

# 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=y, cmap='Set1', s=40)
ax.set_xlabel('PCA Component 1')
ax.set_ylabel('PCA Component 2')
ax.set_zlabel('PCA Component 3')
ax.set_title('Iris Dataset PCA 3D Projection')
plt.legend(handles=scatter.legend_elements()[0], labels=target_names, title="Classes")
plt.savefig('reports/pca_3d_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved PCA 3D plot to reports/pca_3d_plot.png")

# ----------------------------
# 3. Neural Network training
# ----------------------------
print("\n=== 3. Neural Network Classification ===")

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert to PyTorch tensors
X_train_t = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_t = torch.tensor(y_train, dtype=torch.long)
X_test_t = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_t = torch.tensor(y_test, dtype=torch.long)

# Define Neural Network
class IrisNN(nn.Module):
    def __init__(self, input_dim, hidden_dim1=16, hidden_dim2=8, num_classes=3):
        super(IrisNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim1)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim1, hidden_dim2)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(hidden_dim2, num_classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        x = self.relu2(x)
        x = self.fc3(x)
        return x

model = IrisNN(input_dim=4)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
num_epochs = 100
train_losses = []
train_accs = []
val_losses = []
val_accs = []

for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train_t)
    loss = criterion(outputs, y_train_t)
    loss.backward()
    optimizer.step()

    # Record training metrics
    train_loss = loss.item()
    train_pred = torch.argmax(outputs, dim=1).item() if False else torch.argmax(outputs, dim=1)
    train_acc = (train_pred == y_train_t).float().mean().item()
    train_losses.append(train_loss)
    train_accs.append(train_acc)

    # Validation
    model.eval()
    with torch.no_grad():
        val_outputs = model(X_test_t)
        val_loss = criterion(val_outputs, y_test_t).item()
        val_pred = torch.argmax(val_outputs, dim=1).cpu().numpy()
        val_acc = accuracy_score(y_test_t.cpu().numpy(), val_pred)
        val_losses.append(val_loss)
        val_accs.append(val_acc)

    if (epoch+1) % 10 == 0:
        print(f"Epoch {epoch+1}/{num_epochs}, Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")

# ----------------------------
# 4. Evaluation and visualization
# ----------------------------
print("\n=== 4. Evaluation & Visualization ===")

# Final evaluation
model.eval()
with torch.no_grad():
    test_outputs = model(X_test_t)
    test_pred = torch.argmax(test_outputs, dim=1).cpu().numpy()
    test_acc = accuracy_score(y_test_t.cpu().numpy(), test_pred)
    print(f"Test Accuracy: {test_acc:.4f}")

    # Confusion matrix
    cm = confusion_matrix(y_test_t.cpu().numpy(), test_pred)
    print("Confusion Matrix:")
    print(cm)

    # Classification report
    print("Classification Report:")
    print(classification_report(y_test_t.cpu().numpy(), test_pred, target_names=target_names))

# Plot training curves
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(train_losses, label='Train Loss')
plt.plot(val_losses, label='Val Loss')
plt.title('Loss Curves')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(train_accs, label='Train Acc')
plt.plot(val_accs, label='Val Acc')
plt.title('Accuracy Curves')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.tight_layout()
plt.savefig('reports/training_curves.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved training curves to reports/training_curves.png")

# Save model
torch.save(model.state_dict(), 'models/iris_nn.pth')
print("Saved model to models/iris_nn.pth")

# ----------------------------
# 5. Generate small paper report (Markdown)
# ----------------------------
print("\n=== 5. Generating Report ===")
report_lines = []
report_lines.append("# Iris Dataset Analysis & Neural Network Classification Report\n")
report_lines.append("## 1. Introduction\n")
report_lines.append("This project performs exploratory data analysis and neural network classification on the Iris dataset.\n")
report_lines.append("## 2. Dataset Description\n")
report_lines.append(f"- **Samples:** {len(X)} iris flowers\n")
report_lines.append(f"- **Features:** sepal length, sepal width, petal length, petal width (cm)\n")
report_lines.append(f"- **Classes:** {', '.join(target_names)}\n")
report_lines.append("## 3. PCA Analysis\n")
report_lines.append(f"- PCA reduced 4 dimensions to 3 components, explaining {pca.explained_variance_ratio_}\n")
report_lines.append("![PCA 3D Plot](pca_3d_plot.png)\n")
report_lines.append("## 4. Neural Network Model\n")
report_lines.append("- Architecture: Input(4) -> Hidden1(16, ReLU) -> Hidden2(8, ReLU) -> Output(3)\n")
report_lines.append(f"- Optimizer: Adam (lr=0.01)\n")
report_lines.append(f"- Epochs: {num_epochs}\n")
report_lines.append(f"- Final Test Accuracy: {test_acc:.4f}\n")
report_lines.append("![Training Curves](training_curves.png)\n")
report_lines.append("## 5. Conclusion\n")
report_lines.append("- The neural network achieves reasonable classification accuracy on the Iris dataset.\n")
report_lines.append("- PCA visualization shows clear separation between the three iris species.\n")
report_lines.append("- Further work could include hyperparameter tuning, deeper architectures, or other datasets.\n")

report_md = "\n".join(report_lines)
with open('reports/report.md', 'w', encoding='utf-8') as f:
    f.write(report_md)
print("Saved report to reports/report.md")

print("\n=== All tasks completed! ===")