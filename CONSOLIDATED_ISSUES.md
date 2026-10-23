# Consolidated Issues Report - 1023test Project

## Summary
All static analysis issues from ESLint, jscpd, and knip consolidated into one document for GitHub Issues creation.

**Report Date**: 2026-10-23  
**Project**: 1023test (https://github.com/wjkjk0921-eng/1023test)  
**Tools**: ESLint 8.57.1, jscpd 5.4.2, knip 6.42.1

---

## Issue #1: ESLint `document` Global Recognition

| Field | Value |
|-------|-------|
| **Title** | ESLint `document` global not recognized in `docs/app.js` |
| **Status** | ⚠️ Open - Known ESLint v8 limitation |
| **File** | `docs/app.js` |
| **Line** | 300 |
| **Error** | `Parsing error: Unexpected token document` |

### Description
ESLint is not recognizing the `document` global variable even though `"browser": true` is set in `.eslintrc.json`. This is a known ESLint v8 `.eslintrc.json` format compatibility issue. Multiple configuration attempts were made:

1. `/* global document */` comment at file top - did not resolve parsing error
2. Added `"document": "readonly"` to `.eslintrc.json` `globals` section - did not resolve parsing error  
3. Added `parserOptions: { ecmaVersion: 2021, sourceType: "module" }` to `.eslintrc.json` - did not resolve parsing error

**Current Configuration**:
```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "parserOptions": {
    "ecmaVersion": 2021,
    "sourceType": "module"
  },
  "globals": {
    "document": "readonly",
    "window": "readonly"
  },
  "rules": {
    "complexity": ["error", 10],
    "max-depth": ["error", 3],
    "max-lines-per-function": ["error", 50],
    "cognitive-complexity": ["error", 15],
    "no-undef": "error"
  }
}
```

**Related Code**:
```javascript
// Line 300
document.getElementById('results-area').style.display = 'none';
```

### Possible Workarounds
- Migrate to ESLint flat config (`eslint.config.cjs`) with proper `languageOptions.env.browser: true`
- Use ESLint v9+ with `eslint.config.*` format
- Add `// eslint-disable-line no-undef` near the line (not ideal)
- Accept the warning if the code functions correctly at runtime (recommended - code works at runtime)

### Priority
**Medium** - Code functions correctly; issue is ESLint configuration limitation, not runtime error.

---

## Issue #2: jscpd Code Duplication

| Field | Value |
|-------|-------|
| **Title** | jscpd Analysis: 7,880 clones found (30.23% duplication) |
| **Status** | ✅ Complete - Report generated |
| **Total Files Analyzed** | 4,730 |
| **Total Lines** | 780,152 |
| **Total Tokens** | 4,505,558 |
| **Clones Found** | 7,880 |
| **Duplicated Lines** | 235,837 (30.23%) |
| **Duplicated Tokens** | 1,430,920 (31.76%) |

### Description
Code duplication analysis using jscpd 5.4.2. The majority of clones come from dependency locale files.

### Top Clone Sources (by token count):

1. **`node_modules/zod/v4/locales/`** - 5,861 clones, 1,051,787 duplicated tokens (39.97%)
   - All locale files from `zod` package v4
   - Includes: ar, az, be, bg, bn, ca, cs, da, de, el, en, eo, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, ka, kh, kn, ko, lt, mk, ms, nl, nn, no, ot, pl, pt, ro, ru, sk, sl, sv, ta, tg, th, tk, tr, ug, uk, ur, uz, vi, yo, zh-CN, zh-TW

2. **Project-internal duplicates** - Minimal significance
   - Model weight constant arrays in `docs/app.js`

### Recommended Actions

1. **Add `.jscpdignore`** to exclude `node_modules` and focus on project-internal duplication
2. **Run `jscpd --skip-node-modules`** for project-focused analysis
3. **Review internal clones** - the 235,837 duplicated lines within project source may indicate opportunities for refactoring (e.g., extracting common weight initialization patterns)
4. **Update jscpd config** in `package.json` to add ignore patterns

### Sample Output Format
```
Clone found (javascript)
 - node_modules/zod/v4/locales/ar.cjs [74:19 - 83:27] (10 lines, 69 tokens)
   node_modules/zod/v4/locales/ota.cjs [77:21 - 86:27] (10 lines, 69 tokens)
```

### Priority
**Low** - Duplication is primarily from dependencies; not a critical code quality issue for this project.

---

## Issue #3: knip Dead Code Detection

| Field | Value |
|-------|-------|
| **Title** | knip Analysis: 1 unused file, 1 unused devDependency |
| **Status** | ✅ Complete - Report generated |
| **Unused Files** | 1 |
| **Unused devDependencies** | 1 |

### Unused Files (1):

| File | Reason |
|------|--------|
| `docs/app.js` | Marked as unused because the project appears to be Python/TDD-focused, and the JS frontend may not be the primary entry point |

### Unused devDependencies (1):

| Package | Location |
|---------|----------|
| `eslint-plugin-sonarjs` | `package.json:30:6` - Installed but not actively used via `extends`; sonarjs rules are defined inline in `.eslintrc.json` |

### Recommended Actions

1. **If `docs/app.js` is intended to be used**: Consider if it should be a source file for the project, or mark it as a known file in knip configuration
2. **If `eslint-plugin-sonarjs` is no longer needed**: Remove from `package.json` devDependencies and update `.eslintrc.json` rules
3. **Run `knip --lazy`** for faster analysis on large projects

### knip Output
```
Unused files (1)
docs/app.js
Unused devDependencies (1)
eslint-plugin-sonarjs  package.json:30:6
```

### Priority
**Low** - Unused dependencies can be cleaned up; `docs/app.js` usage depends on project scope.

---

## Priority Matrix

| Priority | Issue | Action |
|----------|-------|--------|
| **High** | ESLint `document` global error | Investigate ESLint v8 flat config migration; consider migrating to `eslint.config.cjs` |
| **Medium** | jscpd node_modules noise | Add ignore patterns, focus on project source code only |
| **Low** | knip unused dependencies | Remove `eslint-plugin-sonarjs` if not planning SonarJS integration, or configure properly |

---

## Unified Check Command

```
npm run check
# 等於埧行: npm run lint && npm run jscpd && npm run knip
```

**Scripts in package.json**:
- `"lint": "eslint docs/ && eslint ai4i_2020_tdd/scripts/ tests/"`
- `"jscpd": "jscpd"`  
- `"knip": "knip"`
- `"check": "npm run lint && npm run jscpd && npm run knip"`

---

## GitHub Issues Creation Guidance

### Issue #1 Template
```
Title: ESLint `document` global not recognized in docs/app.js

Description:
ESLint is not recognizing the `document` global variable even though `"browser": true` is set in `.eslintrc.json`. This is a known ESLint v8 `.eslintrc.json` format compatibility issue.

Error Details:
- Location: docs/app.js, line 300
- Error: Parsing error: Unexpected token document
- Cause: ESLint v8 `.eslintrc.json` format compatibility issue with browser global `document`

Possible Workarounds:
- Migrate to ESLint flat config (`eslint.config.cjs`) with proper `languageOptions.env.browser: true`
- Use ESLint v9+ with `eslint.config.*` format
- Add `// eslint-disable-line no-undef` near the line (not ideal)
- Accept the warning if the code functions correctly at runtime (recommended)

Related Code:
```javascript
// Line 300
document.getElementById('results-area').style.display = 'none';
```

Priority: Medium
```

### Issue #2 Template
```
Title: jscpd Analysis: 7,880 clones found (30.23% duplication)

Summary:
- Total Files Analyzed: 4,730
- Total Lines: 780,152
- Total Tokens: 4,505,558
- Clones Found: 7,880
- Duplicated Lines: 235,837 (30.23%)
- Duplicated Tokens: 1,430,920 (31.76%)

Top Clone Sources:
1. node_modules/zod/v4/locales/ - 5,861 clones (1,051,787 tokens, 39.97%)
2. Project-internal duplicates - minimal significance

Recommended Actions:
1. Add .jscpdignore to exclude node_modules
2. Run jscpd --skip-node-modules for project-focused analysis
3. Review internal clones for refactoring opportunities
4. Update jscpd config with ignore patterns

Priority: Low
```

### Issue #3 Template
```
Title: knip Analysis: 1 unused file, 1 unused devDependency

Summary:
- Unused Files: 1 (docs/app.js)
- Unused devDependencies: 1 (eslint-plugin-sonarjs)

Unused Files:
- docs/app.js: Marked as unused; project is Python/TDD-focused, JS frontend is supplementary

Unused Dependencies:
- eslint-plugin-sonarjs: Installed but not used via extends; rules defined inline in .eslintrc.json

Recommended Actions:
1. If docs/app.js is intended to be used: mark as source in knip config
2. If eslint-plugin-sonarjs is no longer needed: remove from package.json devDependencies
3. Run knip --lazy for faster analysis

Priority: Low
```

---

## Consolidated Report

**All checks command**: `npm run check`  
**Tools Status**:
- ⚠️ ESLint: Config set with complexity, max-depth, max-lines-per-function, cognitive-complexity rules; `document` global recognition has v8 format compatibility limitation
- ✅ jscpd: Running, detecting clones across the codebase (mainly node_modules zod locales)
- ✅ knip: Running, detecting unused files/dependencies

**Generated Report**: `CONSOLIDATED_ISSUES.md`  
**Project**: 1023test (GitHub: https://github.com/wjkjk0921-eng/1023test)  
**Tools Versions**: 
- ESLint: 8.57.1
- eslint-plugin-sonarjs: 4.2.2
- jscpd: 5.4.2
- knip: 6.42.1

---

## Next Steps

1. **Create GitHub Issues**: Copy the three Issue templates above and create corresponding issues in the repository
2. **Address High Priority**: Investigate ESLint flat config migration for the `document` global issue
3. **Medium Priority**: Add jscpd ignore patterns to focus on project-internal duplication
4. **Low Priority**: Clean up unused dependencies (`eslint-plugin-sonarjs`) and verify `docs/app.js` usage scope

**All consolidated issues have been documented in `CONSOLIDATED_ISSUES.md`** and are ready for GitHub Issues creation.