```markdown
# PromptTemplateExperimentationHarness Class

## Overview
The `PromptTemplateExperimentationHarness` class is a specialized experimentation harness designed for testing various prompt templates using the Jinja templating engine. It extends the `ExperimentationHarness` class and is tailored to work with experiments that involve generating prompts from templates and collecting responses from a model.

## Attributes
- `environment`: An instance of `jinja2.Environment` used to manage the Jinja templating environment.
- `experiment_cls_constructor`: A constructor for the experiment class that will be executed within the harness.
- `model_name`: A string representing the name of the model to be used in the experiment.
- `prompt_templates`: A list of strings, each a Jinja-styled template for generating prompts.
- `user_inputs`: A list of dictionaries, where each dictionary represents user inputs that will be rendered into the prompt templates.
- `model_arguments`: An optional dictionary of additional arguments for the model. Defaults to an empty dictionary if `None` is provided.
- `input_pairs_dict`: A dictionary that maps rendered prompts to their corresponding template and user input pair.
- `experiment`: An instance of the experiment class specified by `experiment_cls_constructor`.

## Constants
- `PIVOT_COLUMNS`: A list of strings defining the columns used to pivot data in the experiment results. It includes `"prompt_template"` and `"user_input"`.

## Methods

### `__init__`
The constructor initializes the harness with the necessary parameters for the experiment.

#### Parameters
- `experiment`: The experiment class constructor to be executed within the harness.
- `model_name`: The name of the model to be used in the experiment.
- `prompt_templates`: A list of Jinja-styled prompt templates.
- `user_inputs`: A list of dictionaries representing user inputs.
- `model_arguments`: Additional arguments for the model, if any.

### `prepare`
The `prepare` method is responsible for creating prompts from the provided templates and user inputs. It then initializes and prepares the experiment with these prompts.

#### Process
1. Initializes an empty dictionary for `input_pairs_dict`.
2. Iterates over each prompt template and user input pair.
3. Renders the prompt using the Jinja template and user input.
4. Appends the rendered prompt to the `rendered_inputs` list.
5. Maps the rendered prompt to its template and user input in `input_pairs_dict`.
6. Constructs the experiment instance with the model name, rendered inputs, and model arguments.
7. Calls the `prepare` method of the superclass (`ExperimentationHarness`).

### `run`
The `run` method executes the experiment. It ensures that the experiment is prepared before running it.

#### Process
1. Checks if the `experiment` instance is not initialized and calls `prepare` if necessary.
2. Calls the `run` method of the superclass (`ExperimentationHarness`).

## Usage
The `PromptTemplateExperimentationHarness` class is used in a project to conduct experiments on different prompt templates. It automates the process of generating prompts, running them through a specified model, and collecting the results. This is particularly useful for evaluating the performance of language models on a variety of templated prompts and user inputs.

## Example
To use the `PromptTemplateExperimentationHarness`, one would need to:

1. Define a list of Jinja-styled prompt templates.
2. Create a list of dictionaries representing different user inputs.
3. Specify the model name and any additional model arguments.
4. Instantiate the `PromptTemplateExperimentationHarness` with the appropriate experiment class, model name, prompt templates, user inputs, and model arguments.
5. Call the `prepare` method to set up the experiment.
6. Call the `run` method to execute the experiment and collect results.
```