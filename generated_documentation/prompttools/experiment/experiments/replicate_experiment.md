```markdown
# ReplicateExperiment Class

## Overview

The `ReplicateExperiment` class is a subclass of the `Experiment` class designed to perform experiments using the Replicate API. It supports both image models and language models (LLMs). The class requires the `replicate` Python package to be installed and an API token to be set in the environment variable `REPLICATE_API_TOKEN`.

## Initialization

### `__init__(self, models, input_kwargs, model_specific_kwargs={}, use_image_model=False)`

The constructor initializes the `ReplicateExperiment` with the following parameters:

- `models`: A list of strings representing the model identifiers to be used in the experiment (e.g., `"stability-ai/stable-diffusion:27b93a2413e"`).
- `input_kwargs`: A dictionary where keys are argument names and values are lists of argument values. These arguments are common across all models.
- `model_specific_kwargs`: A dictionary where keys are model identifiers and values are dictionaries with keys as argument names and values as lists of argument values. These arguments are specific to each model.
- `use_image_model`: A boolean flag indicating whether the experiment is for an image model. Defaults to `False`.

The constructor checks for the presence of the `replicate` package and the `REPLICATE_API_TOKEN` environment variable. It also handles the conversion of `PromptSelector` objects to prompts if they are used in `input_kwargs`.

## Methods

### `prepare(self)`

The `prepare` method generates all combinations of arguments for each model by combining `input_kwargs` and `model_specific_kwargs`. It populates the `self.argument_combos` list with dictionaries representing each combination of arguments, including the model version.

### `replicate_completion_fn(model_version: str, **kwargs)`

A static method that calls the `replicate.run` function with the specified `model_version` and additional keyword arguments (`kwargs`). It is used to execute the model and obtain the results.

### `_extract_responses(self, output) -> str`

A method to extract responses from the output of the `replicate.run` function. If `self.image_experiment` is `True`, it assumes the output is a list of image URIs. Otherwise, it concatenates text responses from a generator.

### `_image_tag(url, image_width)`

A static method that generates HTML code for rendering an image given its URL and a specified image width.

### `visualize(self, get_all_cols=False, pivot=False, pivot_columns=[], image_width=300)`

The `visualize` method displays the results of the experiment. If `self.image_experiment` is `False`, it calls the `visualize` method of the superclass. If `self.image_experiment` is `True`, it creates an HTML table with image tags to display the images. It supports pivoting the results table based on specified columns.

- `get_all_cols`: A boolean indicating whether to retrieve all columns in the visualization.
- `pivot`: A boolean indicating whether to pivot the table.
- `pivot_columns`: A list of columns to use for pivoting the table.
- `image_width`: An integer specifying the width of the images in the visualization.

## Usage

To use the `ReplicateExperiment` class, one must instantiate it with the required parameters, call the `prepare` method to generate argument combinations, and then call the `visualize` method to display the results. The class is designed to be used in an interactive environment, such as Jupyter notebooks, where the output can be rendered directly. In non-interactive environments, it logs the tabulated results using the `logging` module.

## Dependencies

- `replicate`: The Python package for interacting with the Replicate API.
- `logging`: Used for logging information in non-interactive environments.
- `itertools`: Utilized for generating combinations of arguments.
- `functools.partial`: Used to create partial functions.
- `IPython.display`: For displaying HTML content in interactive environments.
- `tabulate`: For tabulating results in a human-readable format.
- `prompttools.mock.mock`: Contains the `mock_replicate_stable_diffusion_completion_fn` for debugging purposes.
- `prompttools.selector.prompt_selector`: Contains the `PromptSelector` class for handling prompt selection.
- `..widgets.utility`: Contains the `is_interactive` function to check if the environment is interactive.
- `os`: For accessing environment variables.
```