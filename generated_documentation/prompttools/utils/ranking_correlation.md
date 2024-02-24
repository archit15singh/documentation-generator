```markdown
# `ranking_correlation.py` Module

## Overview

The `ranking_correlation.py` module is part of the `prompttools/utils` package within the `documentation-generator` project. It provides a utility function to compute the Spearman's rank correlation coefficient between an expected ranking and an actual ranking produced by a model. This function is typically used to evaluate the performance of ranking models in information retrieval, recommendation systems, or any other domain where items are ranked according to their relevance or importance.

## Dependencies

- `scipy.stats`: This module from the SciPy library provides functions for statistical calculations, including the Spearman's rank correlation. It is a required dependency for the `ranking_correlation` function to work. If `scipy.stats` is not installed, the function will raise a `ModuleNotFoundError`.
- `pandas`: The function expects input in the form of a `pandas.core.series.Series` object, which is a one-dimensional array with axis labels from the pandas library.

## Function: `ranking_correlation`

### Description

The `ranking_correlation` function compares an expected ranking list with an actual ranking produced by a model to determine how well the model's ranking aligns with the expected outcome. It calculates the Spearman's rank correlation coefficient, which assesses how well the relationship between two rankings can be described using a monotonic function.

### Parameters

- `row` (`pandas.core.series.Series`): A single row of data from a pandas DataFrame. This row should include the actual ranking produced by the model, along with other relevant data such as input features and model responses.
- `expected_ranking` (`list`): A list representing the expected ranking of items. Each element in the list is an identifier (such as a document ID) that corresponds to the ranked items.
- `ranking_column_name` (`str`, optional): The name of the column in `row` that contains the actual ranking produced by the model. The default value for this parameter is `"top doc ids"`.

### Returns

- `float`: The Spearman's rank correlation coefficient between the expected ranking and the actual ranking. The value ranges from -1 to 1, where 1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no correlation.

### Usage Example

```python
EXPECTED_RANKING_LIST = [
    ["id1", "id3", "id2"],
    ["id2", "id3", "id1"],
    ["id1", "id3", "id2"],
    ["id2", "id3", "id1"],
]
experiment.evaluate("ranking_correlation", ranking_correlation, expected_ranking=EXPECTED_RANKING_LIST)
```

In the example above, `EXPECTED_RANKING_LIST` is a list of expected rankings, and `experiment.evaluate` is a hypothetical method that evaluates the ranking correlation for each row in a dataset.

### Error Handling

If the `scipy.stats` module is not available, the function will raise a `ModuleNotFoundError` with instructions to install the SciPy package.

### Special Cases

- If both the expected ranking and the actual ranking contain only one item each, the function will return 1.0 if they match, or -1.0 if they do not match, without performing a correlation calculation.

### Implementation Details

The function first checks if the `scipy.stats` module is available. If not, it raises an error. It then retrieves the actual ranking from the specified column in the input `row`. If there is only one item in both the expected and actual rankings, it returns 1.0 or -1.0 based on a direct comparison. Otherwise, it calculates the Spearman's rank correlation coefficient using the `spearmanr` function from `scipy.stats` and returns the correlation value.
```