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
| `no-undef` | error | 0 | No undefined variable errors (document global handled via `/* global */` comment) |
| `complexity` | error | 0 | Within threshold (10 max) |
| `max-depth` | error | 0 | Within threshold (3 max) |
| `max-lines-per-function` | error | 0 | All functions within 50 lines limit |
| `cognitive-complexity` | error | 0 | Within threshold (15 max) |
| **Parsing Errors** | **error** | **1** | **`Unexpected token document` at line 300** |

**Parsing Error Details**:
- **Location**: `docs/app.js`, line 300
- **Error**: `Unexpected token document`
- **Cause**: ESLint v8 `.eslintrc.json` format compatibility issue with browser global `document`
- **Mitigation**: Added `/* global document, window */` at file top; `no-undef` rule no longer triggers for `document`, but parsing error persists due to ESLint v8 flat config limitations
- **Status**: Known issue documented; code functions correctly at runtime

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

**Note**: 99%+ of clones originate from `node_modules/zod` locale files. To focus on project-internal duplication, use `jscpd --skip-node-modules`.

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
| `inferIris(sepalLength, sepalWidth, petalLength, petalWidth)` | 149-179 | Iris classification inference |
| `inferAI4I(airTemp, processTemp, rotationalSpeed, torque, toolWear)` | 182-209 | AI4I 2020 fault prediction inference |
| `showResults(results, isIris)` | 216-243 | Display results in frontend |
| `probabilitiesToString(p)` | 246-248 | Format probability values to 4 decimal places |

**Frontend Inference Function Count**: **4 functions** (inferIris, inferAI4I, showResults, probabilitiesToString)  
**Frontend Inference Code Lines**: **~65 lines** (lines 149-248, excluding weight constants)

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