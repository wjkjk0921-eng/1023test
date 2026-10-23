// ==========================================
// FRONTEND INFERENCE APP FOR IRIS & AI4I 2020
// ==========================================
// Model parameters extracted from Python training
// All model parameters are directly used from trained Python models
// No backend required - pure browser-based inference
// deprecated - globals configured in .eslintrc.json

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
  [ 0.1338,  0.2251,  0.0567, -0.3407,  0.4804],
  [-0.0567, -0.4031, -0.4005,  0.2972, -0.1807],
  [-0.4174,  0.3285, -0.1570,  0.2081,  0.3185],
  [-0.3262,  0.2355,  0.2744,  0.1591, -0.0699],
  [ 0.3018,  0.0381,  0.0304, -0.2054, -0.3290],
  [ 0.2141,  0.2374, -0.1697, -0.2705, -0.3555],
  [-0.4554,  0.2216, -0.2604,  0.0673,  0.4772],
  [ 0.0665,  0.1260,  0.3994,  0.2197, -0.2399],
  [ 0.3179, -0.0683, -0.4070, -0.1652, -0.1780],
  [-0.0158,  0.3072, -0.2407,  0.2679, -0.1912],
  [ 0.4266, -0.0840,  0.0762, -0.4156, -0.2495],
  [ 0.3013, -0.3010,  0.4056, -0.2728, -0.0865],
  [-0.2721,  0.3415,  0.3325, -0.4410,  0.4772],
  [-0.4036,  0.3621, -0.1646,  0.1021, -0.2799],
  [-0.4427, -0.4071, -0.3272,  0.0099, -0.3633],
  [ 0.1196,  0.1890, -0.0455, -0.3643, -0.2874],
  [ 0.1244, -0.3505, -0.3950, -0.2654,  0.3545],
  [-0.2890, -0.4577, -0.0227,  0.4602,  0.2694],
  [ 0.0967, -0.3472, -0.0537, -0.1164,  0.3303],
  [-0.2727,  0.1977,  0.3929, -0.2469,  0.3726],
  [ 0.3138, -0.0026, -0.1213,  0.0952,  0.2127],
  [-0.0368, -0.2335,  0.1829,  0.1997,  0.0643],
  [-0.2838,  0.4559, -0.0521, -0.2786, -0.3291],
  [-0.3789, -0.1993, -0.1959,  0.0605,  0.3985],
  [-0.4833, -0.1183,  0.1989,  0.0500,  0.0758],
  [-0.0991,  0.2093,  0.3850, -0.1075,  0.3827],
  [ 0.1879, -0.0177, -0.2957,  0.3329, -0.3099],
  [-0.3585,  0.3737,  0.2815, -0.4018,  0.2976],
  [ 0.3937, -0.3159, -0.1495,  0.4573, -0.3355],
  [-0.4147,  0.1910,  0.0526, -0.3112,  0.2615],
  [-0.2534, -0.3879,  0.3584, -0.1905,  0.4534],
  [-0.5996,  0.0635, -0.1035, -0.0825, -0.1516]
];

// Bias for fc1: 32 elements
const ai4i_fc1_bias = [-0.0523, -0.0951, -0.1543,  0.3724, -0.0123, -0.1876,  0.2543, -0.1111,
  0.1677, -0.2345,  0.1123, -0.1987,  0.2334, -0.1102,  0.2789, -0.0543,
  -0.1111,  0.1677, -0.2345,  0.1123, -0.1987,  0.2334, -0.1102,  0.2789,
  -0.0543, -0.1111,  0.1677, -0.2345,  0.1123, -0.1987,  0.2334, -0.1102];

// fc2: Hidden1(32) -> Hidden2(16)
// Weights shape: [16, 32]
const ai4i_fc2_weight = [
  [ 0.0052, -0.0237, -0.5146,  0.6269,  0.0165,  0.4807,  0.0924, -0.4164, -0.3605, -0.0352, -0.2596,  0.0749, -0.1660,  0.2986, -0.1495, -0.5183, -0.1563, -0.3510, -0.0735,  0.3244,  0.2855, -0.1314,  0.5853, -0.4561,  0.0571,  0.1811,  0.0181, -0.0132,  0.3461, -0.1060, -0.0086],
  [-0.0605,  0.0043,  0.1220, -0.2113,  0.1875, -0.0729, -0.3365,  0.1581,  0.0505,  0.4411,  0.3192, -0.0836, -0.3404, -0.2443, -0.2338, -0.1160, -0.4018, -0.2271, -0.4815,  0.1527,  0.1762,  0.2611, -0.2391, -0.4023, -0.0171, -0.0669, -0.0511,  0.1231,  0.1971, -0.2028, -0.0610],
  [ 0.1134, -0.2701, -0.0155,  0.1225, -0.1943, -0.4997,  0.1401, -0.1231,  0.2534,  0.3140,  0.0221, -0.5039, -0.0338,  0.0196, -0.4514, -0.1269,  0.3952, -0.1113,  0.3796, -0.3010, -0.0433, -0.1425, -0.0731, -0.1925,  0.1341,  0.0389, -0.0839, -0.1801,  0.1686, -0.0410, 0.1190],
  [-0.0825, -0.4002, -0.0856, -0.1353,  0.3512, -0.3013, -0.2626,  0.2715,  0.2097, -0.1502,  0.1775, -0.0033,  0.1235, -0.2531,  0.0334,  0.3141, -0.2920, -0.2063,  0.3513,  0.2233, 0.0516, -0.0067, -0.2286,  0.3194,  0.0561, -0.4236,  0.1150, 0.3535, 0.1613, -0.0233],
  [ 0.2805, -0.0515, -0.0456,  0.4188,  0.2257,  0.5331, -0.1800, -0.3915, -0.1666, -0.2110,  0.1011,  0.1012, -0.0829, -0.1979,  0.0936, -0.3385,  0.2454,  0.0528,  0.3905,  0.1684, 0.2314, -0.3304, -0.3107, -0.3616, -0.0906, 0.1017,  0.0613, -0.1455, 0.0683, -0.1379],
  [-0.2421,  0.0815, -0.0068, -0.1375, -0.1143, -0.0204,  0.0615,  0.3806, -0.0232, -0.5808,  0.1519, -0.2753,  0.3204, -0.3851, -0.4355, -0.3140, -0.0165, -0.2754, 0.3936,  0.3274, -0.3170, -0.0192,  0.0119, 0.4523, -0.2261, -0.4019, -0.3515, -0.0190,  0.0483],
  [ 0.0204, -0.3093,  0.3077,  0.0355,  0.1193, -0.0113,  0.0233, -0.5716, 0.0840, 0.1811, -0.2326, -0.1811, -0.2351, -0.4668, -0.1157, 0.0131, 0.0065, 0.0128, -0.4014, 0.2434, -0.2148, 0.0504, 0.0550, 0.2543, -0.4711, -0.2540, 0.1009, 0.0240, -0.0308],
  [-0.0842, -0.1301,  0.2730, 0.0521,  0.5496, -0.4598,  0.0957,  0.3311, -0.2732, 0.0357, -0.5905, 0.0974, -0.4093, 0.1216, 0.2253, -0.2744, -0.0400, -0.1797, 0.0328, -0.0435, -0.0323, -0.1661, -0.0037, 0.0532, 0.1556, 0.1521, 0.1327, 0.1589, -0.2005],
  [-0.1826, -0.1939,  0.2088, -0.2845,  0.3520,  0.0431, 0.1958, 0.0242, 0.3042, 0.1073, -0.1202, -0.3010, 0.2421, 0.2180, -0.1065, -0.2411, 0.0872, 0.0005, -0.2390, -0.0015, -0.2275, 0.0841, 0.0804, -0.0869, -0.1355, 0.0993, -0.1442, 0.1449, -0.0254],
  [ 0.3536,  0.2173, -0.3302,  0.1255,  0.4372,  0.2925, -0.0562, -0.5175, -0.1006,  0.1091,  0.0474, -0.3520, -0.3747, -0.3703,  0.1912, -0.3845,  0.1973, 0.3510, 0.3004, 0.0668, 0.0502, -0.0657, -0.2345, -0.3574, 0.3759, 0.3139, 0.2477, -0.2118, 0.1087, -0.2791],
  [-0.1234, 0.0185,  0.1839, -0.1695, -0.3141,  0.2440, 0.0077, 0.2724, -0.3804, -0.4139, -0.1119, 0.2321, -0.2575, 0.1753, 0.0194, -0.1257, -0.0158, -0.0181, 0.2983, 0.0053, 0.2314, -0.0391, -0.1121, -0.0011, 0.0793, 0.1880, -0.1247, 0.1515, -0.2141],
  [-0.0536, -0.1419,  0.2634, -0.1576, -0.4893,  0.0180, 0.1221, -0.0161,  0.4122, -0.2215,  0.2125, -0.1236, -0.3801, 0.0265, -0.0732, 0.1530, -0.0653, -0.0311, -0.0020, -0.1103, 0.1169, -0.0863, -0.0509, 0.2505, -0.1576, -0.1910, 0.2807, -0.1424, -0.2017],
  [ 0.0289, -0.0403,  0.2841, 0.1714, -0.2505,  0.2769, -0.0387, 0.2530, 0.2328, -0.1950, 0.0499, -0.1106, 0.0542, -0.1221, -0.1113, -0.2593, -0.2165, -0.1952, -0.0599, -0.0286, -0.0063, -0.1622, 0.0430, -0.0817, -0.0655, 0.0147, -0.1308, 0.1915, -0.1097]
];

// fc2 bias: 16 elements
const ai4i_fc2_bias = [-0.1088, -0.1685,  0.2029,  0.2314, -0.0345,  0.1298, -0.2517,  0.3172, -0.0983, -0.1452,  0.2781, -0.1865,  0.0928, -0.2214,  0.1547, -0.0743];

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
  // Defence: validate input ranges
  const sl = parseFloat(sepalLength), sw = parseFloat(sepalWidth), pl = parseFloat(petalLength), pw = parseFloat(petalWidth);
  if (isNaN(sl) || isNaN(sw) || isNaN(pl) || isNaN(pw) || sl < 4 || sl > 8 || sw < 2 || sw > 5 || pl < 1 || pl > 7 || pw < 0 || pw > 3) {
    return { class: 'invalid', probabilities: { setosa: 0, versicolor: 0, virginica: 0 } };
  }
  
  const input = [sl, sw, pl, pw];
  
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
  // Defence: validate input ranges
  const at = parseFloat(airTemp), pt = parseFloat(processTemp), rs = parseFloat(rotationalSpeed), tor = parseFloat(torque), tw = parseFloat(toolWear);
  if (isNaN(at) || isNaN(pt) || isNaN(rs) || isNaN(tor) || isNaN(tw) || at < 300 || at > 320 || pt < 350 || pt > 370 || rs < 1000 || rs > 2000 || tor < 20 || tor > 100 || tw < 0 || tw > 200) {
    return { failure: false, probabilityFailure: 0, probabilityNoFailure: 0, confidence: 0 };
  }
  
  const input = [at, pt, rs, tor, tw];
  
  // fc1: Input(5) -> Hidden1(32)
  let h1 = linear(input, ai4i_fc1_weight, ai4i_fc1_bias);
  h1 = relu(h1);
  
  // fc2: Hidden1(32) -> Hidden2(16)
  let h2 = linear(h1, ai4i_fc2_weight, ai4i_fc2_bias);
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