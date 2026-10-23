import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load dataset
df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
print(f"Dataset shape: {df.shape}")

# Features and target
X = df.drop('Machine failure', axis=1)
y = df['Machine failure']

# PCA 3D
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

print(f"PCA explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Total variance explained: {sum(pca.explained_variance_ratio_):.4f}")

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=y, cmap='viridis', s=20, alpha=0.6)
ax.set_xlabel('PCA Component 1')
ax.set_ylabel('PCA Component 2')
ax.set_zlabel('PCA Component 3')
ax.set_title('PCA 3D Visualization - AI4I 2020 Dataset')

# Add colorbar
cbar = plt.colorbar(scatter, shrink=0.5, aspect=10)
cbar.set_label('Machine Failure (0=Normal, 1=Failure)')

plt.tight_layout()
plt.savefig('reports/pca_3d_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("PCA 3D plot saved to reports/pca_3d_plot.png")