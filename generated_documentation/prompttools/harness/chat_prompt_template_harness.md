```markdown
## ChatPromptTemplateExperimentationHarness

### Overview
`ChatPromptTemplateExperimentationHarness` is a class that extends `ExperimentationHarness` and is designed to facilitate the testing of various prompt templates for chat models using `jinja` templating. It allows for the creation of prompts from templates, execution of experiments, and analysis of results.

### Attributes
- `_experiment_type`: A string indicating the type of experiment, set to "Template".
- `PIVOT_COLUMNS`: A list of column names used for pivoting data in the DataFrame, set to ["prompt_template", "user_input"].

### Initialization
The `__init__` method initializes the harness with the following parameters:
- `experiment`: A constructor for the experiment class to be executed within the harness.
- `model_name`: A string representing the name of the model.
- `message_templates`: A list of lists of dictionaries, where each list contains `jinja`-styled templates for system and user messages.
- `user_inputs`: A list of dictionaries representing user inputs.
- `model_arguments`: An optional dictionary of additional arguments for the model.

The method sets up the `jinja2` environment, stores the experiment class constructor, model name, message templates, user inputs, and model arguments. It then calls the superclass initializer.

### Methods

#### `prepare`
Prepares the experiment by creating prompts from templates and initializing the experiment with the appropriate arguments. It renders messages using the `_render_messages_openai_chat` function and sets up the experiment instance.

#### `run`
Executes the experiment and processes the results. It adds user inputs and prompt templates to the resulting DataFrame for analysis. It can clear previous results if specified.

#### `get_table`
Returns a DataFrame with the results of the experiment. It can return all columns or a subset by hiding specific columns. The method determines which columns to hide based on whether `get_all_cols` is `True` or `False`.

#### `visualize`
Displays the results of the experiment in a table format. If the environment is interactive (e.g., Jupyter Notebook), it uses `display.display`. Otherwise, it logs the table using the `logging` module and `tabulate`.

#### `aggregate`
Aggregates data based on a specified column and method (e.g., 'mean', 'sum', 'count', etc.). It can handle special cases for user inputs and templates by converting them to a suitable format for aggregation.

#### `_get_state`
Captures the current state of the experiment, including the experiment class constructor, model name, message templates, user inputs, model arguments, and the state of the child experiment. It returns this state as a tuple.

#### `_load_state`
A class method that loads the state of an experiment from a given state tuple. It reconstructs the harness and associated experiment from the saved state parameters.

### Usage
The `ChatPromptTemplateExperimentationHarness` is used in a project to test different chat prompt templates against a chat model. It allows for systematic experimentation with various user inputs and prompt styles, and it provides tools for analyzing the performance and responses of the model.

### Internal Functions

#### `_render_messages_openai_chat`
A helper function that takes a message template, user input, and a `jinja2` environment to render a complete message. It deep copies the template, renders the system and user messages with the provided user input, and returns the rendered message.

### Dependencies
- `typing`: For type annotations.
- `jinja2`: For rendering `jinja` templates.
- `pandas`: For handling data in DataFrame format.
- `copy`: For deep copying data structures.
- `IPython.display`: For displaying results interactively.
- `tabulate`: For formatting tables.
- `logging`: For logging information.
```