```markdown
# ModelComparisonHarness Class

## Overview
`ModelComparisonHarness` is a subclass of `ExperimentationHarness` designed to facilitate the comparison of different models by running experiments with various system prompts and user messages. It allows for the execution of multiple runs and the evaluation of results using custom metrics.

## Attributes
- `model_names` (List[str]): Names of the models to be compared.
- `system_prompts` (List[str]): System messages corresponding to each model.
- `model_arguments` (List[Optional[dict]]): Arguments for each model, if any.
- `user_messages` (List[str]): User messages to be tested across all models.
- `runs` (int): Number of runs for the experiment.
- `experiments` (List[OpenAIChatExperiment]): List of experiments, one for each model.
- `_experiment_type` (str): Type of the experiment, set to "Comparison".
- `PIVOT_COLUMNS` (List[str]): Columns used for pivoting data in the DataFrame.

## Methods

### `__init__(self, model_names, system_prompts, user_messages, model_arguments=[], runs=1)`
Constructor for the `ModelComparisonHarness` class. It initializes the attributes and validates the lengths of `model_names`, `system_prompts`, and `model_arguments`.

### `prepare(self)`
Initializes and prepares the experiments by creating an `OpenAIChatExperiment` for each model with the corresponding system prompt and user messages.

### `_create_system_prompt(content)`
Static method that creates a dictionary representing a system prompt with the given content.

### `_create_human_message(content)`
Static method that creates a dictionary representing a human message with the given content.

### `full_df(self)`
Property that returns the full DataFrame containing all experiment results.

### `partial_df(self)`
Property that returns the partial DataFrame with a subset of the experiment results.

### `score_df(self)`
Property that returns the DataFrame containing the scores of the experiments.

### `run(self, clear_previous_results=False)`
Executes the experiments. If `clear_previous_results` is set to `True`, previous results are cleared before running.

### `evaluate(self, metric_name, eval_fn, static_eval_fn_kwargs={}, **eval_fn_kwargs)`
Evaluates the experiments using the provided evaluation function and metric name. Additional keyword arguments can be passed to the evaluation function.

### `get_table(self, get_all_cols=False)`
Returns a DataFrame with the experiment results. If `get_all_cols` is `True`, all columns are included; otherwise, certain columns are hidden based on their uniqueness across the results.

### `_update_dfs(self)`
Updates the full, partial, and score DataFrames by concatenating the results from all experiments.

### `visualize(self, get_all_cols=False)`
Displays the results table. If running in an interactive environment, the table is displayed inline; otherwise, it is logged using the `logging` module.

### `_get_state(self)`
Returns the state of the experiment, including model names, system prompts, user messages, model arguments, and the states of child experiments.

### `_load_state(cls, state, experiment_id, revision_id, experiment_type_str)`
Class method that loads the state of a `ModelComparisonHarness` from the provided state parameters. It validates the experiment type and reconstructs the harness and its experiments.

## Usage
The `ModelComparisonHarness` class is used in a project to compare the performance of different models by running them with specified system prompts and user messages. It allows for the evaluation of models using custom metrics and provides methods for visualizing and saving the state of the experiments.

## Example
```python
# Initialize the harness with model names, system prompts, and user messages
harness = ModelComparisonHarness(
    model_names=["model1", "model2"],
    system_prompts=["Welcome to model1!", "Welcome to model2!"],
    user_messages=["Hello, how are you?", "What's the weather like today?"],
    runs=3
)

# Prepare the experiments
harness.prepare()

# Run the experiments
harness.run()

# Evaluate the experiments with a custom metric
harness.evaluate(metric_name="accuracy", eval_fn=my_custom_eval_function)

# Visualize the results
harness.visualize()
```
```