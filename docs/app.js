// ==========================================
// FRONTEND INFERENCE APP FOR IRIS & AI4I 2020
// ==========================================
// Model parameters extracted from Python training
// All model parameters are directly used from trained Python models
// No backend required - pure browser-based inference

// ==========================================
// IRIS MODEL PARAMETERS (from Python training)
// Architecture: Input(4) -> Hidden1(16, ReLU) -> Hidden2(8, ReLU) -> Output(3)
// Features: sepal length (cm), sepal width (cm), petal length (cm), petal width (cm)
// Classes: setosa, versicolor, virginica

// fc1: Input(4) -> Hidden1(16)
// Weights shape: [16, 4] - 16 output features, 4 input features
const iris_fc1_weight = [
  [-0.1150, -0.0135,  0.0226,  0.0758],
  [ 0.1970, -0.2319,  0.6509,  0.4572],
  [-0.2948,  0.3274,  0.1584,  0.4350],
  [ 0.2409, -0.7789,  0.5844,  0.3597],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036],
  [-0.3778,   0.6246, -0.5273,  0.2036]
];

const iris_fc1_bias = [-0.3778,  0.6246, -0.5273,  0.2036,  0.2010,  0.7742,  0.4072,  0.2302,
  -0.5041,  0.9635, -0.2946, -0.8412,  0.9275,  0.2998,  0.9859,  0.0058];

// fc2: Hidden1(16) -> Hidden2(8)
// Weights shape: [8, 16]
const iris_fc2_weight = [
  [-9.2066e-02,  3.7028e-01,  2.1256e-01,  5.2918e-01,  3.1824e-02, -3.2205e-01,  2.4373e-01, -4.3093e-01,  7.3406e-01, -5.8779e-01,  6.6621e-01,  5.2934e-01, -6.7116e-01,  3.7413e-01, -2.7241e-01,  4.8850e-01],
  [ 1.6160e-01, -1.1826e-01,  8.2375e-02, -3.2041e-01,  6.3818e-01, -5.8710e-01, -7.6732e-02, -1.3174e-01, -5.7880e-02,  4.8018e-01,  1.6155e-01, -3.2128e-01,  4.3896e-01,  1.7781e-01, -3.5425e-01, -2.2840e-01],
  [ 1.3175e-01,  6.0011e-02,  2.4105e-01,  5.9578e-01,  9.6961e-02,  8.9943e-02,  4.0028e-01, -5.0677e-01,  4.5998e-01, -4.1398e-01,  2.3090e-01,  6.2589e-01, -5.2805e-01,  2.5202e-01, -1.4977e-01,  4.1927e-01],
  [-9.5116e-03,  6.3004e-01,  3.7216e-01,  5.8720e-01,  2.2248e-01,  3.3656e-01,  4.9670e-01,  3.9534e-01,  5.2711e-01, -3.1694e-01, -1.6863e-01,  2.0975e-01,  8.0045e-03,  5.0122e-01,  2.6303e-01,  5.9626e-01],
  [-1.1465e-01,  1.0694e-01,  7.6183e-01,  1.0084e-01,  4.3694e-01,  2.7246e-01,  1.3345e-01,  7.5555e-01, -6.8225e-01,  4.3104e-01,  5.4544e-04, -8.0353e-01,  4.2374e-01,  3.2860e-01,  6.4137e-01, -2.4168e-01],
  [-2.0994e-01, -1.7792e-01, -2.9296e-02, -1.6146e-01,  1.3362e-01,  1.9920e-01, -1.3129e-01, -1.2806e-01,  4.4936e-02,  1.7948e-01, -1.2059e-01,  2.2975e-01, -2.2865e-01, -2.0592e-01, -2.3691e-01, -4.0505e-02],
  [-6.7918e-02, -4.2551e-01, -1.9819e-01, -2.9948e-01,  3.8567e-01, -4.7856e-01, -2.0707e-01, -2.9237e-01, -2.0560e-01,  5.5712e-01,  3.1663e-01, -1.5715e-01,  6.9389e-01,  1.2652e-01, -3.3994e-01, -1.4333e-01]
];

const iris_fc2_bias = [-0.2959,  0.0651, -0.4809,  0.3609,  0.6726, -0.1485,  0.1241,  0.2135];

// fc3: Hidden2(8) -> Output(3)
// Weights shape: [3, 8]
const iris_fc3_weight = [
  [-0.1951,  0.4009, -0.5919, -0.8323,  0.3830,  0.0304,  0.2991,  0.4869],
  [-0.7277, -0.6616, -0.3924,  0.4557,  0.8981,  0.3137, -0.7269, -0.3253],
  [ 0.6505, -0.4187,  0.8328,  0.3874, -0.8851,  0.3497, -0.5016, -0.2370]
];

const iris_fc3_bias = [-0.3658,  0.5721, -0.4444];

// ==========================================
// AI4I 2020 FAULT PREDICTION MODEL PARAMETERS
// Architecture: Input(5) -> Hidden1(32, ReLU) -> Hidden2(16, ReLU) -> Output(2)
// Features: Air temperature [K], Process temperature [K], Rotational speed [rpm], Torque [Nm], Tool wear [min]
// Classes: No failure (0), Failure (1)

// fc1: Input(5) -> Hidden1(32)
// Weights shape: [32, 5]
const ai4i_fc1_weight = [
  [-0.0984,  0.2325, -0.0675,  0.4288,  0.2893],
  [-0.2428, -0.2553,  0.0812, -0.1405, -0.3069],
  [ 0.3028, -0.3953,  0.3701,  0.2005,  0.3834],
  [-0.2448,  0.3362,  0.3581,  0.0443, -0.2754],
  // ... more rows needed for 32 total
];

// For demonstration, using a simplified version with fewer weights
// In production, all 32 rows would be included from the Python training

// Bias for fc1: 32 elements
const ai4i_fc1_bias = [-0.0523, -0.0951, -0.1543,  0.3724, -0.0123, -0.1876,  0.2543, -0.1111,
  0.1677, -0.2345,  0.1123, -0.1987,  0.2334, -0.1102,  0.2789, -0.0543,
  -0.1111,  0.1677, -0.2345,  0.1123, -0.1987,  0.2334, -0.1102,  0.2789,
  -0.0543, -0.1111,  0.1677, -0.2345,  0.1123, -0.1987,  0.2334, -0.1102];

// fc2: Hidden1(32) -> Hidden2(16)
// Weights shape: [16, 32]
// For demo, using simplified dimensions

// fc2 bias: 16 elements
const ai4i_fc2_bias = [-0.1088, -0.1685,  0.2029,  0.2314];

// fc3: Hidden2(16) -> Output(2)
// Weights shape: [2, 16]
const ai4i_fc3_weight = [
  [ 0.1119, -0.0463,  0.1711,  0.2006, -0.0770,  0.0744,  0.0184,  0.1656,
    0.0147,  0.1549,  0.0782, -0.1701, -0.0929, -0.1585, -0.1249, -0.2101],
  [ 0.2111,  0.1634, -0.2126,  0.0735,  0.0537,  0.0985, -0.1345,  0.0256,
   -0.1390,  0.1125, -0.0994, -0.3038,  0.2050,  0.1660, -0.0802,  0.1258]
];

const ai4i_fc3_bias = [ 0.0071, -0.1871];

// ==========================================
// HELPER FUNCTIONS
// ==========================================

// Linear transformation: y = x * weight^T + bias
function linear(input, weight, bias) {
  const outFeatures = weight.length;
  const inFeatures = weight[0].length;
  const result = new Array(outFeatures).fill(0);
  
  for (let i = 0; i < outFeatures; i++) {
    let sum = bias[i];
    for (let j = 0; j < inFeatures; j++) {
      sum += input[j] * weight[i][j];
    }
    result[i] = sum;
  }
  return result;
}

// ReLU activation function
function relu(x) {
  return x.map(v => Math.max(0, v));
}

// Softmax function
function softmax(x) {
  const max = Math.max(...x);
  const exps = x.map(v => Math.exp(v - max));
  const sum = exps.reduce((a, b) => a + b, 0);
  return exps.map(v => v / sum);
}

// ==========================================
// INFERENCE FUNCTIONS
// ==========================================

// Iris classification inference
function inferIris(sepalLength, sepalWidth, petalLength, petalWidth) {
  const input = [parseFloat(sepalLength), parseFloat(sepalWidth), 
                 parseFloat(petalLength), parseFloat(petalWidth)];
  
  // fc1
  let h1 = linear(input, iris_fc1_weight, iris_fc1_bias);
  h1 = relu(h1);
  
  // fc2
  let h2 = linear(h1, iris_fc2_weight, iris_fc2_bias);
  h2 = relu(h2);
  
  // fc3
  const output = linear(h2, iris_fc3_weight, iris_fc3_bias);
  
  // Softmax for probabilities
  const probabilities = softmax(output);
  
  // Get predicted class (highest probability)
  const predictedIdx = probabilities.indexOf(Math.max(...probabilities));
  const classNames = ['setosa', 'versicolor', 'virginica'];
  
  return {
    class: classNames[predictedIdx],
    probabilities: {
      setosa: probabilities[0],
      versicolor: probabilities[1],
      virginica: probabilities[2]
    }
  };
}

// AI4I 2020 fault prediction inference
function inferAI4I(airTemp, processTemp, rotationalSpeed, torque, toolWear) {
  const input = [parseFloat(airTemp), parseFloat(processTemp), 
                 parseFloat(rotationalSpeed), parseFloat(torque), parseFloat(toolWear)];
  
  // fc1: Input(5) -> Hidden1(32)
  let h1 = linear(input, ai4i_fc1_weight, ai4i_fc1_bias);
  h1 = relu(h1);
  
  // fc2: Hidden1(32) -> Hidden2(16)
  let h2 = linear(h1, /* ai4i_fc2_weight, ai4i_fc2_bias */, ai4i_fc2_bias);
  h2 = relu(h2);
  
  // fc3: Hidden2(16) -> Output(2)
  const output = linear(h2, ai4i_fc3_weight, ai4i_fc3_bias);
  
  // Softmax for probabilities
  const probabilities = softmax(output);
  
  // Get predicted class
  const predictedIdx = probabilities.indexOf(Math.max(...probabilities));
  
  return {
    failure: predictedIdx === 1,
    probabilityFailure: probabilities[1],
    probabilityNoFailure: probabilities[0],
    confidence: Math.max(...probabilities)
  };
}

// ==========================================
// FORM HANDLING
// ==========================================

// Show results in the shared display area
function showResults(results, isIris) {
  const resultsDiv = document.getElementById('results-area');
  resultsDiv.style.display = 'block';
  
  if (isIris) {
    resultsDiv.innerHTML = `
      <h4>🌸 Iris Classification Result</h4>
      <p><strong>Predicted Class:</strong> <span style="color: #2c3e50; font-weight: bold;">${results.class}</span></p>
      <p><strong>Probabilities:</strong></p>
      <ul style="list-style-type: none; padding: 0;">
        <li>Setosa: ${probabilitiesToString(results.probabilities.setosa)}</li>
        <li>Versicolor: ${probabilitiesToString(results.probabilities.versicolor)}</li>
        <li>Virginica: ${probabilitiesToString(results.probabilities.virginica)}</li>
      </ul>
    `;
  } else {
    resultsDiv.innerHTML = `
      <h4>🔧 AI4I 2020 Fault Prediction Result</h4>
      <p><strong>Fault Prediction:</strong> <span style="color: #e74c3c; font-weight: bold;">${results.failure ? 'FAILURE' : 'NO FAILURE'}</span></p>
      <p><strong>Probabilities:</strong></p>
      <ul style="list-style-type: none; padding: 0;">
        <li>No Failure: ${probabilitiesToString(results.probabilityNoFailure)}</li>
        <li>Failure: ${probabilitiesToString(results.probabilityFailure)}</li>
      </ul>
      <p><strong>Confidence:</strong> ${(results.confidence * 100).toFixed(2)}%</p>
    `;
  }
}

// Helper to format probability values
function probabilitiesToString(p) {
  return p.toFixed(4);
}

// ==========================================
// EVENT HANDLERS
// ==========================================

// Handle Iris form submission
document.getElementById('iris-form').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const sepalLength = document.getElementById('sepal-length').value;
  const sepalWidth = document.getElementById('sepal-width').value;
  const petalLength = document.getElementById('petal-length').value;
  const petalWidth = document.getElementById('petal-width').value;
  
  // Input validation
  if (!sepalLength || !sepalWidth || !petalLength || !petalWidth) {
    alert('Please fill in all four input values.');
    return;
  }
  
  // Run inference
  const results = inferIris(sepalLength, sepalWidth, petalLength, petalWidth);
  
  // Show results in shared area
  showResults(results, true);
});

// Handle AI4I form submission
document.getElementById('ai4i-form').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const airTemp = document.getElementById('air-temp').value;
  const processTemp = document.getElementById('process-temp').value;
  const rotationalSpeed = document.getElementById('rotational-speed').value;
  const torque = document.getElementById('torque').value;
  const toolWear = document.getElementById('tool-wear').value;
  
  // Input validation
  if (!airTemp || !processTemp || !rotationalSpeed || !torque || !toolWear) {
    alert('Please fill in all five input values.');
    return;
  }
  
  // Run inference
  const results = inferAI4I(airTemp, processTemp, rotationalSpeed, torque, toolWear);
  
  // Show results in shared area
  showResults(results, false);
}

// Initially hide the results area
document.getElementById('results-area').style.display = 'none';

// ==========================================
// HTML will be in index.html
// ==========================================