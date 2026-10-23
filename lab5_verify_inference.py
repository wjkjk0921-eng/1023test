#!/usr/bin/env python3
"""Verify that Python inference matches golden cases."""
import torch
import json
import math
import sys

# Load models
ai4i_model = torch.load('models/ai4i_nn.pth', weights_only=False)
iris_model = torch.load('models/iris_nn.pth', weights_only=False)

# Load golden cases
with open('tests/golden.json', 'r', encoding='utf-8') as f:
    golden_cases = json.load(f)

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
        'confidence': float(max(probabilities)),
        'probabilities': [float(p) for p in probabilities]
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

# Verify each golden case
print("LAB5: Inference Verification vs Golden Cases")
print("=" * 50)

all_passed = True
total_cases = len(golden_cases)
passed_cases = 0
failed_cases = 0

for i, case in enumerate(golden_cases):
    case_id = case['case_id']
    model_type = case['model']
    input_data = case['input']
    expected_probs = case['probabilities']
    expected_class = case['predicted_class']
    
    # Run Python inference
    if model_type == 'AI4I 2020':
        input_vec = [input_data['air_temp'], input_data['process_temp'], 
                     input_data['rot_speed'], input_data['torque'], input_data['tool_wear']]
        result = infer_ai4i(input_vec, ai4i_model)
        actual_probs = result['probabilities']
        actual_class = 'Failure' if result['failure'] else 'No Failure'
        
        # Check probability match (within 1e-6 tolerance)
        prob_match = all(abs(a - e) < 1e-6 for a, e in zip(actual_probs, expected_probs))
        class_match = actual_class == expected_class
        
    elif model_type == 'Iris':
        input_vec = [input_data['sepal_length'], input_data['sepal_width'],
                     input_data['petal_length'], input_data['petal_width']]
        result = infer_iris(input_vec, iris_model)
        actual_probs = [result['probabilities']['setosa'], 
                       result['probabilities']['versicolor'],
                       result['probabilities']['virginica']]
        actual_class = result['class']
        
        # Check probability match (within 1e-6 tolerance)
        prob_match = all(abs(a - e) < 1e-6 for a, e in zip(actual_probs, expected_probs))
        class_match = actual_class == expected_class
    
    # Results
    passed = prob_match and class_match
    status = "PASS" if passed else "FAIL"
    
    print(f"\nCase {case_id} ({model_type}):")
    print(f"  Expected class: {expected_class}, Actual class: {actual_class}")
    print(f"  Prob match: {prob_match}, Class match: {class_match}")
    print(f"  Status: {status}")
    
    if passed:
        passed_cases += 1
    else:
        failed_cases += 1
        all_passed = False

# Summary
print("\n" + "=" * 50)
print("VERIFICATION SUMMARY")
print("=" * 50)
print(f"Total cases: {total_cases}")
print(f"Passed: {passed_cases}")
print(f"Failed: {failed_cases}")
print(f"Success rate: {passed_cases/total_cases*100:.1f}%")

if all_passed:
    print("\n ALL INFERENCE TESTS PASSED - Python inference matches golden cases")
    sys.exit(0)
else:
    print("\n SOME INFERENCE TESTS FAILED - need to diagnose discrepancies")
    sys.exit(1)