import torch
model = torch.load('C:\\Users\\wjkjk\\OneDrive\\文件\\預設專案\\1023test\\models\\iris_nn.pth', weights_only=False)
print("Type:", type(model))
print("Keys and shapes:")
for k, v in model.items():
    print(f"  {k}: shape {v.shape}")
print("\nFirst layer weights (fc1):")
print(model['fc1.weight'][:4])  # print first 4 rows
print("\nFirst layer bias (fc1.bias):")
print(model['fc1.bias'])
print("\nSecond layer weights (fc2):")
print(model['fc2.weight'])
print("\nSecond layer bias (fc2.bias):")
print(model['fc2.bias'])
print("\nThird layer weights (fc3):")
print(model['fc3.weight'])
print("\nThird layer bias (fc3.bias):")
print(model['fc3.bias'])