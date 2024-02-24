```markdown
# SequentialChainExperiment Class

## Description
The `SequentialChainExperiment` class is a subclass of `Experiment` designed to test the functionality of LangChain's sequential chains. It allows for the execution of multiple language model (LLM) chains in sequence, each with its own prompt template and prompt.

## Attributes
- `MODEL_PARAMETERS`: A list of strings representing the parameters related to the model configuration.
- `CALL_PARAMETERS`: A list of strings representing the parameters used when calling the model.
- `completion_fn`: A function that is used to complete the prompts. It defaults to `lc_completion_fn` but can be overridden with `mock_lc_completion_fn` if the `DEBUG` environment variable is set.
- `model_params`: A dictionary containing the model parameters.
- `call_params`: A dictionary containing the call parameters.
- `all_args`: A dictionary that merges `model_params` and `call_params`.

## Methods

### `__init__(self, llm, prompt_template, prompt, **kwargs)`
The constructor initializes the experiment with the provided language models, prompt templates, and prompts. It also accepts additional keyword arguments that are added to the call parameters.

### `prepare(self)`
Prepares the experiment by building combinations of model and call arguments.

### `lc_completion_fn(self, **params)`
A helper function that sends a request to the provided client with the given prompt and returns the response.

### `run(self, runs=1)`
Executes the experiment for each combination of arguments, running each combination a specified number of times (default is 1). It measures the latency of each call and constructs result dataframes with the responses.

### `_extract_responses(output)`
A static method that extracts responses from the output dictionary.

# RouterChainExperiment Class

## Description
The `RouterChainExperiment` class is a subclass of `Experiment` designed to test the functionality of LangChain's router chains. It allows for the execution of a router chain that directs prompts to different destination chains based on the input.

## Attributes
- `MODEL_PARAMETERS`: A list of strings representing the parameters related to the model configuration.
- `CALL_PARAMETERS`: A list of strings representing the parameters used when calling the model.
- `completion_fn`: A function that is used to complete the prompts. It defaults to `lc_completion_fn` but can be overridden with `mock_lc_completion_fn` if the `DEBUG` environment variable is set.
- `model_params`: A dictionary containing the model parameters.
- `call_params`: A dictionary containing the call parameters.
- `all_args`: A dictionary that merges `model_params` and `call_params`.

## Methods

### `__init__(self, llm, prompt_infos, prompt, **kwargs)`
The constructor initializes the experiment with the provided language models, prompt information, and prompts. It also accepts additional keyword arguments that are added to the call parameters.

### `prepare(self)`
Prepares the experiment by building combinations of model and call arguments.

### `lc_completion_fn(self, **params)`
A helper function that sends a request to the provided client with the given prompt and returns the response.

### `run(self, runs=1)`
Executes the experiment for each combination of arguments, running each combination a specified number of times (default is 1). It measures the latency of each call and constructs result dataframes with the responses.

### `_extract_responses(output)`
A static method that returns the output dictionary as is.

## Usage
Both `SequentialChainExperiment` and `RouterChainExperiment` are used to conduct experiments with LangChain's sequential and router chains, respectively. They are instantiated with the necessary parameters and then the `run` method is called to execute the experiment. The results are used to analyze the performance and behavior of the chains under different conditions.
```