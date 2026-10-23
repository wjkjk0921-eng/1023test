import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np

# Load AI4I 2020 dataset
df = pd.read_csv('ai4i_2020_tdd/data/ai4i_2020.csv')
X = df.drop('Machine failure', axis=1).values
y = df['Machine failure'].values

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert to tensors
X_train_t = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_t = torch.tensor(y_train, dtype=torch.long)
X_test_t = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_t = torch.tensor(y_test, dtype=torch.long)

# Define simple neural network for AI4I 2020
class AI4INN(nn.Module):
    def __init__(self, input_dim, hidden_dim1=32, hidden_dim2=16, num_classes=2):
        super(AI4INN, self).__init__()
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

model = AI4INN(input_dim=5)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 50
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train_t)
    loss = criterion(outputs, y_train_t)
    loss.backward()
    optimizer.step()

# Evaluation
model.eval()
with torch.no_grad():
    test_outputs = model(X_test_t)
    test_pred = torch.argmax(test_outputs, dim=1).cpu().numpy()
    test_acc = accuracy_score(y_test, test_pred)
    print(f"Test Accuracy: {test_acc:.4f}")

# Save model
torch.save(model.state_dict(), 'models/ai4i_nn.pth')
print("Saved model to models/ai4i_nn.pth")

# Extract and print parameters
params = model.state_dict()
print("\n=== Model Parameters ===")
for k, v in params.items():
    print(f"{k}: shape {v.shape}")
    print(v[:4] if v.shape[0] >= 4 else v)