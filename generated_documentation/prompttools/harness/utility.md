```markdown
# Utility Module Documentation

## Module: `utility.py`

Located at `/workspaces/documentation-generator/target_code/prompttools/harness/`, the `utility.py` module provides utility functions for the larger project. This module contains functions that are used across various parts of the project to perform common tasks.

### Function: `is_interactive`

#### Description

The `is_interactive` function is designed to check the environment in which the code is running to determine if it is being executed within an interactive environment, such as a Jupyter notebook.

#### Usage

This function is typically used to conditionally format or present output, such as visualizations, differently when the code is run in an interactive environment versus a non-interactive script or command-line interface.

#### Signature

```python
def is_interactive() -> bool:
```

#### Returns

- `bool`: Returns `True` if the code is running in an interactive environment (like a Jupyter notebook), and `False` otherwise.

#### Implementation Details

- The function imports the `__main__` module, which is the top-level script environment.
- It checks for the presence of the `__file__` attribute within the `__main__` module.
- If the `__file__` attribute does not exist, it implies that the code is running in an interactive environment where the `__file__` attribute is typically not set, such as a Jupyter notebook.
- The function returns `True` if the `__file__` attribute is not found, indicating an interactive environment, and `False` otherwise.

#### Example

```python
if is_interactive():
    # Code to display interactive visualizations
else:
    # Code for non-interactive presentation of results
```

### License

The source code in `utility.py` is proprietary and owned by Hegel AI, Inc. The license for this source code can be found in the `LICENSE` file located in the root directory of the source tree.

---

**Note:** This documentation is for the `utility.py` module as of the last update and may change as the project evolves.
```
