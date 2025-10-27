# lab5-static-analysis

# 🧾 Static Analysis Issues Table

## Table 1: Issues Identified and Fixed During 1st Run

| **Issue** | **Type** | **Line(s)** | **Tool** | **Description** | **Fix Approach** |
|------------|-----------|-------------|-----------|------------------|------------------|
| Try–Except–Pass | Code Quality | 19 | **Bandit** | Used `except:` followed by `pass`, which hides all errors and weakens debugging and security. | Replaced with specific exception handling (`except KeyError`, `except TypeError`) and printed error messages. |
| Use of `eval()` | Security | 59 | **Bandit** | `eval()` can execute arbitrary code and cause severe security vulnerabilities. | Removed `eval()` completely. |
| Unused import (`logging`) | Code Style | 2 | **Flake8** | Imported `logging` but never used anywhere in the file. | Removed the unused import. |
| Missing blank lines | Style | 8, 14, 22, 25, 31, 36, 41, 48 | **Flake8** | Functions not separated by two blank lines, violating PEP 8 guidelines. | Added blank lines between all function definitions. |
| Bare `except` | Bug | 19 | **Flake8** | Used bare `except:` instead of specifying exception type. | Replaced with `except KeyError` and `except TypeError`. |
| Mutable default argument | Bug | 8 | **Pylint** | Function `addItem` used `logs=[]` — shared across all function calls. | Changed default to `None` and initialized inside the function. |
| Function naming style | Style | Multiple | **Pylint** | Function names (`addItem`, `removeItem`, etc.) not in `snake_case` as per PEP 8. | Renamed to `add_item`, `remove_item`, `get_qty`, etc. |
| Missing docstrings | Documentation | Multiple | **Pylint** | No docstrings for functions or module, reducing readability. | Added descriptive docstrings for every function and at top of module. |
| Old string formatting | Readability | 12 | **Pylint** | Used `%s` formatting instead of modern f-strings. | Replaced with f-strings for clarity. |
| Global variable usage | Design | 27 | **Pylint** | Used `global stock_data` — unsafe and not scalable. | Passed `stock_data` as function parameter and returned updated version. |
| File encoding not specified | Bug | 26, 32 | **Pylint** | Opened files without specifying encoding. | Added `encoding="utf-8"` in file open statements. |
| Hidden error with `pass` | Bug | 20 | **Bandit / Pylint** | Silently ignored all exceptions with `pass`. | Replaced with proper exception-specific print messages. |
| Missing main guard | Design | End of file | **Pylint** | Code executed automatically on import. | Added `if __name__ == "__main__": main()` guard. |

✅ **Result after 1st run:**
- **Pylint:** 9.81 / 10  
- **Flake8:** Only `E501` (line too long) warnings left  
- **Bandit:** All major issues fixed  


---

## Table 2: Issues Identified and Fixed During 2nd Run (Final Cleanup)

| **Issue** | **Type** | **Line(s)** | **Tool** | **Description** | **Fix Approach** |
|------------|-----------|-------------|-----------|------------------|------------------|
| Global statement warning (W0603) | Code Design | 48 | **Pylint** | Still using `global` statement in one place. | Removed remaining global variable usage and refactored code fully. |
| Line too long (E501) | Style | 3, 11, 24 | **Flake8** | Lines exceeded 79 characters as per PEP 8 guidelines. | Broke long lines into multiple shorter lines for readability. |
| Minor docstring / blank line formatting | Style | — | **Flake8 / Pylint** | Minor inconsistency in spacing and blank lines between functions. | Added consistent two-blank-line spacing and properly formatted all docstrings. |

✅ **Final Result after 2nd run:**
- **Pylint:** 10 / 10  
- **Flake8:** 0 warnings  
- **Bandit:** 0 vulnerabilities  
- Code is now **clean, secure, readable, and fully PEP 8 compliant.**
