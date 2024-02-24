```markdown
# ComparisonWidgetProvider Class

## Overview

The `ComparisonWidgetProvider` class is designed to facilitate the comparison of different models within an interactive Jupyter Notebook environment. It provides a user interface for displaying model outputs side by side and collecting user feedback on these outputs.

## Attributes

- `completion_fn`: A callable that is executed when the comparison is complete.
- `agg_fn`: A callable that aggregates the comparison data.
- `eval_listener_fn`: A callable that listens for evaluation events (e.g., user feedback).
- `models`: A list of strings representing the models being compared.
- `row_len`: An integer representing the number of columns in the widget grid, including the input, models, and feedback columns.

## Methods

### `__init__(self, completion_fn, agg_fn, eval_listener_fn)`

The constructor initializes the `ComparisonWidgetProvider` with the provided functions for completion, aggregation, and evaluation listening.

### `_get_comparison_submission_listener(self, table: pd.DataFrame, models: List[str]) -> Callable`

A private method that returns a callable to be used as an event listener for the submit button. When the submit button is clicked, it aggregates the scores using `agg_fn`, creates a DataFrame with the results, and displays it.

### `set_models(self, models: List[str]) -> None`

Sets the `models` attribute with a list of model names and calculates the `row_len` based on the number of models.

### `get_header_widgets(self) -> List[object]`

Returns a list of `ipywidgets.Label` objects to be used as headers in the comparison grid. The headers include "Input", one label for each model, and "Feedback".

### `get_row_widgets(self, index, row)`

Generates a list of widgets for a single row in the comparison grid. The row includes an HTML widget for the input, HTML widgets for each model's output, and a dropdown widget for user feedback.

### `get_footer_widgets(self, table)`

Creates the footer widgets for the comparison grid, which includes a submit button that triggers the comparison submission listener.

### `display(self, items)`

Displays the comparison grid using the provided list of items. It creates a `widgets.GridBox` with a layout that has a column for each element in the grid (input, models, feedback).

## Usage

The `ComparisonWidgetProvider` class is used within a Jupyter Notebook to create an interactive comparison interface. The user can view model outputs and provide feedback, which can then be aggregated and processed for model evaluation.

1. An instance of `ComparisonWidgetProvider` is created with the necessary completion, aggregation, and evaluation listener functions.
2. The `set_models` method is called with a list of model names to set up the comparison grid.
3. The `get_header_widgets`, `get_row_widgets`, and `get_footer_widgets` methods are used to generate the widgets for the comparison grid.
4. The `display` method is called with the list of widgets to render the grid in the notebook.
5. User interactions with the feedback dropdowns trigger the evaluation listener function.
6. Clicking the submit button triggers the aggregation of feedback and displays the results.

## Dependencies

- `typing`: Provides support for type hints.
- `pandas`: Used for handling data in DataFrame format.
- `IPython.display`: Used to display widgets in the Jupyter Notebook.
- `ipywidgets`: Provides interactive widgets for the Jupyter Notebook.

## File Metadata

- **Copyright**: Hegel AI, Inc.
- **License**: The license for the source code can be found in the LICENSE file in the root directory of this source tree.
```