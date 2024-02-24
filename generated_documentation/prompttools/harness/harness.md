```markdown
# ExperimentationHarness Class

## Overview
The `ExperimentationHarness` class serves as a base class for creating experimentation harnesses within a project. It is designed to manage and facilitate the execution of experiments, including preparation, running, evaluation, visualization, ranking, and saving/loading of experiments. This class should not be directly instantiated; instead, it is intended to be subclassed to create specific experimentation harnesses tailored to particular needs.

## Attributes
- `experiment`: An instance of the `Experiment` class that represents the underlying experiment to be run.
- `PIVOT_COLUMNS`: A list of column names used for pivoting data during visualization and ranking.
- `input_pairs_dict`: A dictionary to store input pairs for feedback gathering (commented out in the current version).
- `runs`: An integer representing the number of times the experiment should be run.
- `_experiment_id`: A string representing the unique identifier of the experiment.
- `_revision_id`: A string representing the unique identifier of the experiment's revision.

## Methods

### `__init__(self) -> None`
Constructor for the `ExperimentationHarness` class. Initializes the `input_pairs_dict`, `experiment`, `runs`, `_experiment_id`, and `_revision_id` attributes.

### `_prepare_arguments(arguments: dict[str, object]) -> dict[str, list[object]]`
A static method that prepares the arguments for the experiment by converting each argument value into a list containing that value.

### `prepare(self) -> None`
Prepares the underlying experiment by calling the `prepare` method of the `Experiment` instance.

### `run(self, clear_previous_results: bool = False) -> None`
Runs the underlying experiment with the specified number of runs and an option to clear previous results.

### `evaluate(self, metric_name: str, eval_fn: Callable, static_eval_fn_kwargs: dict = {}, **eval_fn_kwargs) -> None`
Evaluates the results of the underlying experiment using a specified evaluation function and metric name.

### `visualize(self, pivot: bool = False) -> None`
Displays a visualization of the experiment results, with an option to pivot the data based on `PIVOT_COLUMNS`.

### `rank(self, metric_name: str, is_average: bool = False) -> dict[str, float]`
Scores and ranks the experiment inputs using the pivot columns and returns a dictionary of scores.

### `aggregate(self, groupby_column: str, aggregate_columns: Union[str, list[str]], method: str, custom_df: Optional[pd.DataFrame] = None) -> pd.DataFrame`
Aggregates data based on the specified column and method, returning a pandas DataFrame with the aggregated results.

### `save_experiment(self, name: Optional[str] = None)`
Saves the current state of the experiment to a backend service using an HTTP POST request. Requires an experiment name or an existing `_experiment_id`.

### `load_experiment(cls, experiment_id: str)`
Class method that loads an experiment from a backend service using an HTTP GET request based on the provided experiment ID.

### `load_revision(cls, revision_id: str)`
Class method that loads a specific revision of an experiment from a backend service using an HTTP GET request based on the provided revision ID.

### `_get_state(self)`
An abstract method that should be implemented by subclasses to return the current state of the experiment.

### `_load_state(cls, state, experiment_id: str, revision_id: str, experiment_type_str: str)`
An abstract class method that should be implemented by subclasses to load the state of an experiment.

## Properties
- `full_df`: Returns the full DataFrame of the experiment results.
- `partial_df`: Returns the partial DataFrame of the experiment results.
- `score_df`: Returns the DataFrame of the experiment scores.

## Usage
This class is used as a base for creating specific experimentation harnesses. Subclasses should implement the `_get_state` and `_load_state` methods to handle the saving and loading of experiment states. The class provides functionality to run experiments, evaluate results, visualize data, and rank inputs based on specified metrics. It also supports saving experiments to and loading experiments from a backend service, which requires an API key set in the environment variable `HEGELAI_API_KEY`.

## Dependencies
- `typing`: Provides type hints for function arguments and return types.
- `prompttools.experiment`: Contains the `Experiment` class used for running experiments.
- `prompttools.common`: Contains common constants and functions, such as `HEGEL_BACKEND_URL`.
- `os`: Provides functions for interacting with the operating system.
- `pickle`: Used for serializing and deserializing Python object structures.
- `requests`: Allows sending HTTP requests to a backend service.
- `pandas`: Used for data manipulation and analysis.

## Notes
- The `gather_feedback` method is commented out in the current version of the class.
- The class interacts with a backend service, and the base URL for this service is obtained from `prompttools.common.HEGEL_BACKEND_URL`.
- The class requires an API key (`HEGELAI_API_KEY`) to be set in the environment for saving and loading experiments.
- The class is designed to be flexible and extensible, allowing for customization through subclassing.
```