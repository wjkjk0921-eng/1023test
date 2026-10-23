#!/usr/bin/env python3
"""Create golden cases for Lab5 testing - fixed 3 inputs, model predictions."""
import torch
import json
import os
import math

# Load AI4I NN model
print("Loading AI4I NN model...")
ai4i_model = torch.load('models/ai4i_nn.pth', weights_only=False)

# Load Iris NN model
print("Loading Iris NN model...")
iris_model = torch.load('models/iris_nn.pth', weights_only=False)

# AI4I 3 golden cases
case1_ai4i = {'air_temp': 300.0, 'process_temp': 350.0, 'rot_speed': 1500.0, 'torque': 50.0, 'tool_wear': 50.0}
case2_ai4i = {'air_temp': 320.0, 'process_temp': 370.0, 'rot_speed': 1800.0, 'torque': 80.0, 'tool_wear': 90.0}
case3_ai4i = {'air_temp': 310.0, 'process_temp': 360.0, 'rot_speed': 1600.0, 'torque': 60.0, 'tool_wear': 70.0}

# Iris 3 golden cases (sepal length, sepal width, petal length, petal width)
case1_iris = {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2}  # setosa
case2_iris = {'sepal_length': 7.0, 'sepal_width': 3.2, 'petal_length': 4.7, 'petal_width': 1.4}  # versicolor
case3_iris = {'sepal_length': 6.3, 'sepal_width': 3.3, 'petal_length': 6.0, 'petal_width': 2.5}  # virginica

# Inference functions (same as in docs/app.js)
def linear(input_vec, weight, bias):
    out_features = len(weight)
    in_features = len(input_vec)
    result = [0] * out_features
    for i in range(out_features):
        sum_val = bias[i]
        for j in range(in_features):
            sum_val += input_vec[j] * weight[i][j]
        result[i] = sum_val
    return result

def relu(x):
    return [max(0, v) for v in x]

def softmax(x):
    max_val = max(x)
    exps = [math.exp(v - max_val) for v in x]
    sum_exps = sum(exps)
    return [v / sum_exps for v in exps]


def infer_ai4i(input_vec, model):
    h1 = linear(input_vec, model['fc1.weight'].tolist(), model['fc1.bias'].tolist())
    h1 = relu(h1)
    h2 = linear(h1, model['fc2.weight'].tolist(), model['fc2.bias'].tolist())
    h2 = relu(h2)
    output = linear(h2, model['fc3.weight'].tolist(), model['fc3.bias'].tolist())
    probabilities = softmax(output)
    predicted_idx = probabilities.index(max(probabilities))
    return {
        'failure': predicted_idx == 1,
        'probabilityFailure': float(probabilities[1]),
        'probabilityNoFailure': float(probabilities[0]),
        'confidence': float(max(probabilities))
    }


def infer_iris(input_vec, model):
    h1 = linear(input_vec, model['fc1.weight'].tolist(), model['fc1.bias'].tolist())
    h1 = relu(h1)
    h2 = linear(h1, model['fc2.weight'].tolist(), model['fc2.bias'].tolist())
    h2 = relu(h2)
    output = linear(h2, model['fc3.weight'].tolist(), model['fc3.bias'].tolist())
    probabilities = softmax(output)
    predicted_idx = probabilities.index(max(probabilities))
    class_names = ['setosa', 'versicolor', 'virginica']
    return {
        'class': class_names[predicted_idx],
        'probabilities': {
            'setosa': float(probabilities[0]),
            'versicolor': float(probabilities[1]),
            'virginica': float(probabilities[2])
        }
    }


# Generate AI4I golden cases
print("Generating AI4I Golden Cases...")
ai4i_golden = []
for idx, case in enumerate([case1_ai4i, case2_ai4i, case3_ai4i], 1):
    input_vec = [case['air_temp'], case['process_temp'], case['rot_speed'], case['torque'], case['tool_wear']]
    result = infer_ai4i(input_vec, ai4i_model)
    ai4i_golden.append({
        'case_id': idx,
        'model': 'AI4I 2020',
        'input': case,
        'probabilities': [result['probabilityNoFailure'], result['probabilityFailure']],
        'predicted_class': 'Failure' if result['failure'] else 'No Failure',
        'confidence': result['confidence']
    })
    print(f"  AI4I Case {idx}: predicted={result['failure']}, P(Failure)={result['probabilityFailure']:.6f}, confidence={result['confidence']:.6f}")

# Generate Iris golden cases
print("\nGenerating Iris Golden Cases...")
iris_golden = []
for idx, case in enumerate([case1_iris, case2_iris, case3_iris], 1):
    input_vec = [case['sepal_length'], case['sepal_width'], case['petal_length'], case['petal_width']]
    result = infer_iris(input_vec, iris_model)
    iris_golden.append({
        'case_id': idx,
        'model': 'Iris',
        'input': case,
        'probabilities': [result['probabilities']['setosa'], result['probabilities']['versicolor'], result['probabilities']['virginica']],
        'predicted_class': result['class'],
        'confidence': 0.0  # Iris uses different confidence calculation
    })
    print(f"  Iris Case {idx}: predicted={result['class']}, P(setosa)={result['probabilities']['setosa']:.6f}, P(versicolor)={result['probabilities']['versicolor']:.6f}, P(virginica)={result['probabilities']['virginica']:.6f}")

# Combine all golden cases
all_golden = ai4i_golden + iris_golden

# Save to tests/golden.json
os.makedirs('tests', exist_ok=True)
with open('tests/golden.json', 'w', encoding='utf-8') as f:
    json.dump(all_golden, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 60)
print("✅ Golden cases saved to tests/golden.json")
print(f"Total cases: {len(all_golden)} (AI4I: {len(ai4i_golden)}, Iris: {len(iris_golden)})")
print("=" * 60)