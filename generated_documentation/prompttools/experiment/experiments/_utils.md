```markdown
# `_utils.py` Module Documentation

## Overview

The `_utils.py` module is part of the `experiment` package within the `prompttools` namespace. It provides utility functions for handling and processing data within pandas DataFrames, specifically focusing on the uniqueness of column values.

## Functions

### `_check_column_uniqueness`

```python
def _check_column_uniqueness(column: "pd.core.series.Series") -> bool:
```

#### Description

This function checks if all elements in a given pandas Series (column) are equal. It is used to determine if a column contains more than one unique value.

#### Arguments

- `column` (`pandas.core.series.Series`): The column to be checked for uniqueness.

#### Returns

- `bool`: Returns `True` if there is at least one element in the column that is different from the others, indicating that the column has multiple unique values. Returns `False` if all elements are the same.

#### Internal Logic

1. The function initializes by storing the first element of the column in `first_ele`.
2. It then iterates over each element in the column.
3. During iteration, if it finds an element that is not equal to `first_ele`, it immediately returns `True`.
4. If no such element is found by the end of the iteration, it returns `False`.

### `_get_dynamic_columns`

```python
def _get_dynamic_columns(df: pd.DataFrame) -> pd.DataFrame:
```

#### Description

This function identifies and returns a new DataFrame containing only the columns from the input DataFrame that have more than one unique value. It is designed to filter out columns that are static (having the same value across all rows) and keep only dynamic columns.

#### Arguments

- `df` (`pd.DataFrame`): The DataFrame to be examined for dynamic columns.

#### Returns

- `pd.DataFrame`: A new DataFrame consisting of columns from the original DataFrame that have more than one unique value.

#### Internal Logic

1. Two lists, `hashable_columns` and `unhashable_columns`, are initialized to keep track of columns based on whether their first element can be hashed.
2. The function iterates over each column in the input DataFrame.
3. For each column, it attempts to hash the first element.
   - If successful, the column name is added to `hashable_columns`.
   - If a `TypeError` is raised (indicating the element is unhashable), the function calls `_check_column_uniqueness` to check if the column should be considered dynamic. If so, the column name is added to `unhashable_columns`.
4. The function calculates the number of unique values for each hashable column and identifies those with more than one unique value.
5. It prepares a list of DataFrames (`dfs_to_concat`) containing the dynamic columns identified in both hashable and unhashable categories.
6. The function checks if the special columns "prompt" or "messages" exist in the original DataFrame but are not already included in the dynamic columns. If found, they are appended to `dfs_to_concat`.
7. Finally, the function concatenates all DataFrames in `dfs_to_concat` along the columns (axis=1) and returns the resulting DataFrame.

## Usage

The functions in this module are likely used internally within the `experiment` package to preprocess and filter DataFrames before running experiments. The `_check_column_uniqueness` function serves as a helper to `_get_dynamic_columns`, which is the primary function intended for direct use.

## Notes

- The module is intended for internal use within the `experiment` package, as indicated by the underscore prefix in the module name.
- The functions are designed to work with pandas DataFrames and Series, which are common data structures for data analysis in Python.
- The module includes a copyright notice and a license reference, suggesting that it is proprietary software belonging to Hegel AI, Inc.
```