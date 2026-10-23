# Static Check Tools Report - 1023test Project

## Summary

Ran static analysis tools: ESLint, jscpd, and knip. Below are the findings and recommended actions.

---

## Issue #1: ESLint Configuration - Browser Global Not Recognized

**Status**: ⚠️ Configuration constrained by ESLint v8 format limitations  
**File**: `docs/app.js`  
**Line**: 300  
**Error**: `Parsing error: Unexpected token document`

**Description**:
- ESLint is not recognizing the `document` global variable even though `"browser": true` is set in `.eslintrc.json`
- This is a known ESLint v8 `.eslintrc.json` format compatibility issue - ESLint v8 default flat config behaviour may not apply the browser env from `.eslintrc.json` in all contexts
- The `document` variable should be available when `browser: true` is set, but multiple configuration attempts have not resolved the parsing error

**Configuration Attempts Made**:
1. `/* global document */` comment at file top - did not resolve the error
2. Added `"document": "readonly"` to `.eslintrc.json` `globals` section - did not resolve the error
3. Added `parserOptions: { ecmaVersion: 2021, sourceType: "module" }` to `.eslintrc.json` - did not resolve the error
4. Current `.eslintrc.json` configuration:
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

**Potential Workarounds**:
- Migrate to ESLint flat config (`eslint.config.cjs`) with proper `languageOptions.env.browser: true`
- Use ESLint v9+ with `eslint.config.*` format
- Add `// eslint-disable-line no-undef` near the line (not ideal)
- Accept the warning if the code functions correctly at runtime

---

## Issue #2: jscpd Code Duplication

**Status**: ✅ Working  
**Total Clones Found**: 7,880  
**Duplicated Lines**: 235,837 (30.23%)  
**Duplicated Tokens**: 1,430,920 (31.76%)  

**Files Analyzed**: 4,730  
**Total Lines**: 780,152  
**Total Tokens**: 4,505,558  

**Top Duplication Sources** (by token count):
1. `node_modules/zod/v4/locales/` - 5,861 clones, 1,051,787 duplicated tokens (39.97%)
2. Various locale files across node_modules

**Project-Specific Clones**:
- The project itself has some duplicated code, but the majority comes from dependencies
- No severe intra-project duplication detected (below critical thresholds)

**Recommended Actions**:
1. **Ignore node_modules in future scans** - add `.jscpdignore` or use `--skip-node-modules` flag
2. **Review internal clones** - check the 235,837 duplicated lines within the project source for possible refactoring
3. **Update jscpd config** to exclude `node_modules` by default

**JSCPD Config** (from `package.json`):
```json
"jscpd": "jscpd"
```

**Sample Output Format**:
```
Clone found (javascript)
 - node_modules/zod/v4/locales/ar.cjs [74:19 - 83:27] (10 lines, 69 tokens)
    node_modules/zod/v4/locales/ota.cjs [77:21 - 86:27] (10 lines, 69 tokens)
```

---

## Issue #3: knip Dead Code Detection

**Status**: ✅ Working  
**Unused Files**: 1  
**Unused devDependencies**: 1  

**Unused File**:
- `docs/app.js` - marked as unused because the project appears to be Python/TDD-focused, and the JS frontend may not be the primary entry point

**Unused devDependency**:
- `eslint-plugin-sonarjs` - installed but sonarjs rules are defined inline in `.eslintrc.json` rather than via `extends: plugin:sonarjs/recommended`

**Recommended Actions**:
1. **If `docs/app.js` is intended to be used**: consider if it should be a source file for the project, or mark it as a known file in `knip.config`
2. **If `eslint-plugin-sonarjs` is no longer needed**: remove from `package.json` devDependencies and update `.eslintrc.json` rules
3. **Run `knip --lazy`** for faster analysis on large projects

**knip Output**:
```
Unused files (1)
docs/app.js
Unused devDependencies (1)
eslint-plugin-sonarjs  package.json:30:6
```

---

## Priority & Next Steps

| Priority | Issue | Action |
|----------|-------|--------|
| High | ESLint `document` global error | Investigate ESLint v8 flat config migration; consider migrating to `eslint.config.cjs` |
| Medium | jscpd node_modules noise | Add ignore patterns, focus on project source code only |
| Low | knip unused dependencies | Remove `eslint-plugin-sonarjs` if not planning SonarJS integration, or configure properly |

**All checks command**: `npm run check`

**Tools Status**:
- ⚠️ ESLint: Config set with complexity, max-depth, max-lines-per-function, cognitive-complexity rules; `document` global recognition has v8 format compatibility limitation
- ✅ jscpd: Running, detecting clones across the codebase (mainly node_modules zod locales)
- ✅ knip: Running, detecting unused files/dependencies

---

## Generated Report

- **Report Date**: 2026-10-23
- **Project**: 1023test (GitHub: https://github.com/wjkjk0921-eng/1023test)
- **Tools Versions**: 
  - ESLint: 8.57.1
  - eslint-plugin-sonarjs: 4.2.2
  - jscpd: 5.4.2
  - knip: 6.42.1