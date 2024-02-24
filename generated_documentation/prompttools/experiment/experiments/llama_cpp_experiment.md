```markdown
# LlamaCppExperiment Class

## Overview
`LlamaCppExperiment` is a class derived from the `Experiment` base class, designed to facilitate experimentation with different parameter combinations for a local model supported by LlamaCpp and GGML. It allows users to specify a range of parameters for both model initialization and model completion calls, and then runs the model with every possible combination of these parameters.

## Attributes
- `MODEL_PARAMETERS`: A tuple containing the names of all parameters that can be used to initialize the model.
- `CALL_PARAMETERS`: A tuple containing the names of all parameters that can be used when calling the model's completion function.
- `DEFAULT`: A dictionary providing default values for all parameters in `MODEL_PARAMETERS` and `CALL_PARAMETERS`.

## Constructor
The `__init__` method initializes the `LlamaCppExperiment` instance with the following arguments:
- `model_path`: A list of strings representing paths to the models to be run.
- `prompt`: A list of strings or `PromptSelector` instances representing the prompts to test.
- `model_params`: A dictionary where keys are parameter names and values are lists of objects representing the parameters for initializing the model.
- `call_params`: A dictionary where keys are parameter names and values are lists of objects representing the parameters for calling the model completion function.

The constructor checks for the presence of the `Llama` class from the `llama_cpp` module and raises an error if it is not found. It also sets default values for any parameters not explicitly provided.

## Methods
### `prepare`
The `prepare` method generates all possible combinations of model and call parameters by taking the cartesian product of the values provided in the `model_params` and `call_params` dictionaries.

### `llama_completion_fn`
The `llama_completion_fn` method is a helper function that takes a `client` (an instance of `Llama`) and additional call parameters, and then calls the client with those parameters to get a response.

### `run`
The `run` method takes an optional `runs` parameter (defaulting to 1) and executes the experiment for each combination of model and call parameters. It runs the model the specified number of times for each combination and records the results and latencies.

### `_extract_responses`
The `_extract_responses` static method takes the output dictionary from a model call and extracts the text responses.

### `_get_model_names`
The `_get_model_names` method returns a list of model names based on the `model_path` parameter from the argument combinations.

### `_get_prompts`
The `_get_prompts` method returns a list of prompts based on the `prompt` parameter from the argument combinations.

## Usage
To use the `LlamaCppExperiment` class, one must instantiate it with the required parameters and then call the `run` method to execute the experiment. The results can be analyzed to understand the impact of different parameter combinations on the model's performance.

## Exceptions
- Raises `ModuleNotFoundError` if the `llama_cpp` module is not installed.
- Raises `NotImplementedError` if the `initialize` class method is called, as it is not compatible with `LlamaCppExperiment`.
- Raises `PromptExperimentException` if no results are obtained after running the experiment.

## Dependencies
- `os`: For handling file paths.
- `itertools`: For creating cartesian products of parameter combinations.
- `logging`: For logging information and errors.
- `perf_counter` from `time`: For measuring latencies.
- `Llama` from `llama_cpp`: The local model client used for running experiments.
- `PromptSelector` from `prompttools.selector.prompt_selector`: For handling prompt selection if required.

## Notes
- The class assumes that all arguments provided in `model_params` and `call_params` are lists, even if they contain only a single value.
- The class is designed to work with local models and runs experiments in a single thread.
```