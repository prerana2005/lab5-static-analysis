# lab5-static-analysis

# 🧾 Static Analysis Issues Table

| **Issue Type** | **Line(s)** | **Description** | **Fix Approach** |
|-----------------|-------------|-----------------|------------------|
| Mutable default argument | 8 | Function `addItem` had `items=[]` as a default parameter, which is shared across function calls. | Changed default argument to `None` and initialized inside the function. |
| Bare except | 19 | Used `except:` without specifying an exception type. | Replaced with `except KeyError:` to catch the specific error safely. |
| Use of `eval()` | 59 | Insecure use of `eval()` that could execute arbitrary code. | Removed `eval()` and replaced with a safe print statement. |
| Missing docstrings | Multiple | Several functions lacked docstrings, reducing code readability and maintainability. | Added proper docstrings for all functions and at the top of the module. |
| Non–snake_case names | Multiple (`addItem`, `removeItem`, etc.) | Function names didn’t follow PEP 8 naming conventions. | Renamed all to follow `snake_case` (e.g., `add_item`, `remove_item`). |
| Global variable usage | 27 | Used a global statement to modify shared data. | Refactored functions to return updated data instead of modifying a global variable. |
| Unspecified encoding in file handling | 26, 32 | `open()` used without specifying encoding. | Added `encoding='utf-8'` to all file read/write operations. |
| Old string formatting | 12 | Used old `%` or `.format()` string formatting. | Replaced with modern f-strings for better readability. |
| Missing input validation | 51 | Function accepted invalid input types without checks. | Added type checks and error handling for input arguments. |
| Unused import / missing logging setup | 2 | Imported `logging` but never used or configured. | Configured logging properly and used it for key events and errors. |

