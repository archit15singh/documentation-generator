```markdown
# SystemPromptExperimentationHarness Class

## Overview
The `SystemPromptExperimentationHarness` class is a subclass of `ExperimentationHarness` designed to facilitate the testing of various system prompts in conjunction with human (user) messages. It is used to create, run, and analyze experiments that involve sending sequences of system-generated prompts and user messages to a model and observing the model's responses.

## Attributes
- `_experiment_type` (str): A class attribute that defines the type of experiment, set to "Instruction".
- `PIVOT_COLUMNS` (List[str]): A class attribute that specifies the columns to pivot on when displaying results, set to ["system_prompt", "user_input"].

## Constructor
The constructor takes the following parameters:
- `experiment` (Type[Experiment]): The class of the experiment to execute.
- `model_name` (str): The name of the model to be used in the experiment.
- `system_prompts` (List[str]): A list of system-generated prompts to test.
- `human_messages` (List[str]): A list of human messages to pair with system prompts.
- `model_arguments` (Optional[Dict[str, object]]): Additional arguments for the model, with default `None`.

The constructor initializes the following instance variables:
- `experiment_cls_constructor`: Stores the experiment class passed to the constructor.
- `model_name`: Stores the name of the model.
- `system_prompts`: Stores the list of system prompts.
- `human_messages`: Stores the list of human messages.
- `model_arguments`: Stores the model arguments as a dictionary, defaulting to an empty dictionary if `None` is passed.

## Methods

### `_create_system_prompt(content: str) -> Dict[str, str]`
A static method that creates a dictionary representing a system prompt with the given content.

### `_create_human_message(content: str) -> Dict[str, str]`
A static method that creates a dictionary representing a human message with the given content.

### `prepare() -> None`
Prepares the experiment by creating message pairs from system prompts and human messages, initializing the experiment with these pairs, and then calling the `prepare` method of the superclass.

### `run(clear_previous_results: bool = False)`
Runs the experiment. If the experiment is not already prepared, it calls the `prepare` method. It then calls the `run` method of the superclass with the `clear_previous_results` parameter.

### `_get_state()`
Retrieves the current state of the experiment, including the constructor of the experiment class, model name, system prompts, human messages, model arguments, and the state of the child experiment. It returns a tuple containing the state parameters and the full DataFrame of results.

### `_load_state(state, experiment_id: str, revision_id: str, experiment_type_str: str)`
A class method that loads the state of an experiment from the given parameters. It checks if the experiment type matches the current class and raises an error if not. It then reconstructs the harness and experiment from the state parameters.

### `get_table(get_all_cols: bool = False) -> pd.DataFrame`
Returns a DataFrame representing the results of the experiment. If `get_all_cols` is `True`, it returns the full DataFrame; otherwise, it returns a DataFrame with certain columns hidden.

### `visualize(get_all_cols: bool = False)`
Visualizes the results of the experiment. If the environment is interactive (e.g., a Jupyter notebook), it displays the table directly. Otherwise, it logs the table using the `logging` module and the `tabulate` library.

## Usage
The `SystemPromptExperimentationHarness` class is used in a project to conduct experiments on how different system prompts and human messages affect the responses of a model. It is instantiated with the necessary parameters, and then the `prepare` and `run` methods are called to execute the experiment. The results can be visualized or retrieved for further analysis.
```