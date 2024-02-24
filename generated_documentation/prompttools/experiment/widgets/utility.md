```markdown
# Utility Module Documentation

## Overview

The `utility.py` module is part of the `prompttools.experiment.widgets` package within the `documentation-generator` project. This module provides utility functions that are used across the experiment widgets subpackage. Currently, it contains a single function `is_interactive()`.

## Function: is_interactive

### Purpose

The `is_interactive` function is designed to check the environment in which the code is running to determine if it is an interactive environment, such as a Jupyter notebook. This is important for the project as it affects how visualizations and interactive widgets are presented to the user.

### Signature

```python
def is_interactive() -> bool:
```

The function signature indicates that `is_interactive` takes no parameters and returns a boolean value.

### Implementation Details

#### Import Statement

```python
import __main__ as main
```

At the beginning of the function, the `__main__` module is imported and aliased as `main`. This module represents the environment in which the top-level script is running.

#### Function Logic

```python
return not hasattr(main, "__file__")
```

The function uses the built-in `hasattr` function to check if the `__main__` module has the attribute `__file__`. The `__file__` attribute is set by the Python interpreter when a script is run as a file. However, in interactive environments like Jupyter notebooks, this attribute is typically not set.

- If `__file__` is not present in the `__main__` module, it implies that the code is running in an interactive environment, and the function returns `True`.
- If `__file__` is present, it implies that the code is running as a script in a non-interactive environment, and the function returns `False`.

### Usage

The `is_interactive` function is used within the `prompttools.experiment.widgets` package to conditionally execute code that is specific to interactive environments. For example, it can be used to decide whether to display inline plots or to use interactive widgets that are only compatible with Jupyter notebooks.

### Example

```python
from prompttools.experiment.widgets.utility import is_interactive

if is_interactive():
    # Code specific to Jupyter notebooks or other interactive environments
    pass
else:
    # Code for non-interactive environments
    pass
```

In the example above, the function is used in a conditional statement to execute different blocks of code based on the environment detected.

## License

The source code's license information for `utility.py` can be found in the `LICENSE` file located in the root directory of the source tree. The copyright notice at the beginning of the file indicates that the code is owned by Hegel AI, Inc. and that all rights are reserved.
```
