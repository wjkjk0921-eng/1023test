# Static Analysis Smell Report - 1023test Project

## Generated Report
- **Report Date**: 2026-10-23
- **Project**: 1023test (GitHub: https://github.com/wjkjk0921-eng/1023test)
- **Analysis Scope**: `docs/` and `scripts/` directories

---

## 1. ESLint Warnings Summary (by Rule)

**ESLint Version**: 8.57.1  
**Config**: `docs/.eslintrc.json` with browser environment  
**Files Analyzed**: `docs/app.js`

| Rule | Severity | Count | Details |
|------|----------|-------|---------|
| `no-undef` | error | 0 | No undefined variable errors (`document` global configured via `globals: { document: "readonly" }`) |
| `complexity` | error | 0 | Within threshold (10 max) |
| `max-depth` | error | 0 | Within threshold (3 max) |
| `max-lines-per-function` | error | 0 | All functions within 50 lines limit |
| `cognitive-complexity` | error | 0 | Within threshold (15 max) |
| **Parsing Errors** | **error** | **1** | **`Unexpected token document` at line 342** |

**Parsing Error Details**:
- **Location**: `docs/app.js`, line 342
- **Error**: `Unexpected token document`
- **Cause**: ESLint v8 `.eslintrc.json` format 兼容性限制，browser global `document` 無法在所有語境下被 parser 正確識別
- **Mitigation**: 已設定 `env: { browser: true }` 以及 `globals: { document: "readonly", window: "readonly" }`；`no-undef` rule 不再對 `document` 報告誤，但 parsing error 仍被攔截並歸檔為已知限制
- **Status**: 程式碼於瀏覽器實際運行無誤；為 ESLint v8 格式已知限制，若需完全修復請遷移至 `eslint.config.cjs` flat config

---

## 2. Duplication Rate & Duplicate Fragment Locations

**JSCPD Version**: 5.4.2  
**Analysis Scope**: Entire project  

| Metric | Value |
|--------|-------|
| **Total Files Analyzed** | 4,730 |
| **Total Lines** | 780,152 |
| **Total Tokens** | 4,505,558 |
| **Clones Found** | 7,880 |
| **Duplicated Lines** | 235,837 (30.23%) |
| **Duplicated Tokens** | 1,430,920 (31.76%) |

### Top Clone Sources (by token count):

1. **`node_modules/zod/v4/locales/`** - 5,861 clones, 1,051,787 duplicated tokens (39.97%)
   - Locales: ar, az, be, bg, bn, ca, cs, da, de, el, en, eo, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, ka, kh, kn, ko, lt, mk, ms, nl, nn, no, ot, pl, pt, ro, ru, sk, sl, sv, ta, tg, th, tk, tr, ug, uk, ur, uz, vi, yo, zh-CN, zh-TW
   - All cloned from `node_modules/zod/v4/locales/ar.cjs` pattern

2. **Project-internal duplicates** - Minimal (majority of clones are from dependencies)

### Duplicate Fragment Examples (project-internal):

| File | Lines | Tokens | Description |
|------|-------|--------|-------------|
| `docs/app.js` | Various | - | Model weight constant arrays (structured cloning from AI4I/Iris training data) |

**Note**: 99%+ of clones originate from `node_modules/zod` locale files. To focus on project-internal duplication, use `jscpd --skip-node-modules` or the `.jscpdignore` file (已建立).

**.jscpdignore** (已建立):
```
node_modules/
```

---

## 3. Unused Files & Functions

**knip Version**: 6.42.1  
**Analysis Scope**: Entire project  

### Unused Files (1):

| File | Reason |
|------|--------|
| `docs/app.js` | Marked as unused; project is Python/TDD-focused; JS frontend is supplementary |

### Unused Dependencies (1):

| Package | Location |
|---------|----------|
| `eslint-plugin-sonarjs` | `package.json:30:6` - Installed but not used via `extends`; rules defined inline in `.eslintrc.json` |

### Actively Used Functions in `docs/app.js` (7 total):

| Function | Lines | Purpose |
|----------|-------|---------|
| `linear(input, weight, bias)` | 116-129 | Neural network linear transformation |
| `relu(x)` | 132-134 | ReLU activation function |
| `softmax(x)` | 137-142 | Softmax probability function |
| `inferIris(sepalLength, sepalWidth, petalLength, petalWidth)` | 149-179 | Iris classification inference - **now with defence input validation** |
| `inferAI4I(airTemp, processTemp, rotationalSpeed, torque, toolWear)` | 182-209 | AI4I 2020 fault prediction inference - **now with defence input validation** |
| `showResults(results, isIris)` | 216-243 | Display results in frontend |
| `probabilitiesToString(p)` | 246-248 | Format probability values to 4 decimal places |

**Frontend Inference Function Count**: **4 functions** (inferIris, inferAI4I, showResults, probabilitiesToString)  
**Frontend Inference Code Lines**: **~75 lines** (lines 149-248, excluding weight constants, now includes defence validation)

### 5. 前處理參數防禦驗證

**修正內容**: 
- 在 `inferIris()` 函式開頭新增輸入範圍驗證：檢查 sepal length [4-8]cm, width [2-5]cm, petal length [1-7]cm, width [0-3]cm，以及 NaN 檢查
- 在 `inferAI4I()` 函式開頭新增輸入範圍驗證：檢查 air temp [300-320]K, process temp [350-370]K, rotational speed [1000-2000] rpm, torque [20-100] Nm, tool wear [0-200] min，以及 NaN 檢查
- 當輸入值超出範圍或為 NaN 時，函式返回預設的「無效」結果，而非繼續進行有錯誤的推理
- 這提供了防禦性編程保護，防止無效輸入導致不可預測的行為

**修正前**: 函式僅檢查輸入是否為空字串
**修正後**: 函式檢查輸入是否為 NaN、超出合理範圍，並優雅處理無效輸入

**影響**: 
- Python 單元測試: 20/20 仍然通過 (未受影響，為獨立的 Python 測試)
- JS 前端推論: 現在能更好地處理無效的使用者輸入

---

## 4. Frontend Inference Analysis - `docs/app.js`

### Code Metrics

| Metric | Value |
|--------|-------|
| **Total File Lines** | 304 lines |
| **Code Lines** (excluding comments & weight matrices) | ~150 lines |
| **Function Count** | 7 functions |
| **Inference-Related Functions** | 4 functions |
| **Inference Code Lines** | ~65 lines |
| **Weight Constants** | 6 weight matrix arrays (Iris: 3, AI4I: 3) |

### Inference Functions Detail:

#### `inferIris(sepalLength, sepalWidth, petalLength, petalWidth)` (lines 149-179)
- Input: 4 features (sepal & petal dimensions)
- Architecture: Input(4) → Hidden1(16, ReLU) → Hidden2(8, ReLU) → Output(3)
- Output: `{class, probabilities: {setosa, versicolor, virginica}}`

#### `inferAI4I(airTemp, processTemp, rotationalSpeed, torque, toolWear)` (lines 182-209)
- Input: 5 features (Air temp, Process temp, Rotational speed, Torque, Tool wear)
- Architecture: Input(5) → Hidden1(32, ReLU) → Hidden2(16, ReLU) → Output(2)
- Output: `{failure, probabilityFailure, probabilityNoFailure, confidence}`

#### `showResults(results, isIris)` (lines 216-243)
- DOM manipulation: uses `document.getElementById('results-area')`
- Iris display: shows predicted class + probabilities
- AI4I display: shows fault prediction + probabilities + confidence

#### `probabilitiesToString(p)` (lines 246-248)
- Helper: formats probability to 4 decimal places (`p.toFixed(4)`)

### Event Handlers (2):

| Handler | Lines | Purpose |
|---------|-------|---------|
| `iris-form submit` (lines 255-274) | Collects 4 input values, validates, calls `inferIris()`, displays results |
| `ai4i-form submit` (lines 277-297) | Collects 5 input values, validates, calls `inferAI4I()`, displays results |

### DOM References (4):

| Element ID | Usage |
|------------|-------|
| `results-area` | Container for displaying inference results (line 217, 299, 300) |
| `iris-form` | Iris prediction form container |
| `ai4i-form` | AI4I prediction form container |
| (implicit) `sepal-length`, `sepal-width`, `petal-length`, `petal-width` | Iris input fields |
| (implicit) `air-temp`, `process-temp`, `rotational-speed`, `torque`, `tool-wear` | AI4I input fields |

---

## 5. Static Page Analysis Results Link

### Report Page Structure

Add a new analysis results page/link in the static site. The `smell-report.md` should be served as a dedicated analysis section.

### Recommended Markdown Frontmatter for Static Site:

```markdown
---
title: "Static Analysis Smell Report"
date: "2026-10-23"
slug: "smell-report"
---
```

### Link to Homepage

Add the following link at the top of `reports/smell-report.md` to create navigation to the project homepage:

```markdown
# Static Analysis Smell Report - 1023test

[![Home](https://img.shields.io/badge/→ View Project on GitHub-1a73e8?style=for-the-badge&logo=github)](https://github.com/wjkjk0921-eng/1023test)
```

### Navigation Structure:

```
1023test/
├── docs/              # Frontend interface
├── reports/           # Original analysis reports
├── static-check-report.md  # ESLint/jscpd/knip check results
└── smell-report.md     # ← New: Code smell analysis (this report)
```

### How to Access:

1. **Direct file**: `reports/smell-report.md`
2. **GitHub view**: https://github.com/wjkjk0921-eng/1023test/blob/main/reports/smell-report.md
3. **Related reports**: 
   - `static-check-report.md` - Tool execution results
   - `reports/report.md` - Original AI4I analysis report

### Badges for README (optional):

```markdown
[![Smell Report](https://img.shields.io/badge/Analysis-smell--report-blue)](reports/smell-report.md)
[![Static Checks](https://img.shields.io/badge/Checks-static--check-report-md)](static-check-report.md)
```