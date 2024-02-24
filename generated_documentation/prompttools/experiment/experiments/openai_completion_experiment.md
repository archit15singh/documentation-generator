```markdown
## OpenAICompletionExperiment Class

### Overview
The `OpenAICompletionExperiment` class is designed to facilitate experiments with OpenAI's completion API. It allows users to pass lists of parameters to the API and performs a cartesian product of these parameters to test different combinations. The class is part of a larger project that includes a module for selecting prompts and a mock function for simulating OpenAI completions.

### Initialization
The `__init__` method initializes the `OpenAICompletionExperiment` class with a variety of parameters that correspond to the options available in the OpenAI API for text completions.

#### Parameters
- `model`: A list of strings representing the model IDs to be used for the completions.
- `prompt`: A list of strings or a list of `PromptSelector` objects representing the prompts for which completions will be generated.
- `suffix`: An optional list of strings representing the suffixes to append after the completion. Defaults to `[None]`.
- `max_tokens`: An optional list of integers specifying the maximum number of tokens to generate. Defaults to `[float("inf")]`.
- `temperature`: An optional list of floats that control the randomness of the output. Defaults to `[1.0]`.
- `top_p`: An optional list of floats for nucleus sampling. Defaults to `[1.0]`.
- `n`: An optional list of integers indicating the number of completions to generate for each input. Defaults to `[1]`.
- `stream`: An optional list of booleans indicating whether to stream partial completions. Defaults to `[False]`.
- `logprobs`: An optional list of integers specifying the number of log probabilities to include. Defaults to `[None]`.
- `echo`: An optional list of booleans indicating whether to echo the prompt with the completion. Defaults to `[False]`.
- `stop`: An optional list of lists of strings specifying sequences where the API should stop generating tokens. Defaults to `[None]`.
- `presence_penalty`: An optional list of floats for penalizing new tokens based on their presence. Defaults to `[0.0]`.
- `frequency_penalty`: An optional list of floats for penalizing new tokens based on their frequency. Defaults to `[0.0]`.
- `best_of`: An optional list of integers for generating multiple completions and returning the best. Defaults to `[1]`.
- `logit_bias`: An optional list of dictionaries for modifying the likelihood of specific tokens. Defaults to `[None]`.
- `azure_openai_service_configs`: An optional dictionary for configuring the use of Azure OpenAI Service. Defaults to `None`.

### Attributes
- `completion_fn`: The function used to create completions. Defaults to `openai.completions.create` but can be overridden with a mock function for testing.
- `prompt_keys`: A dictionary mapping prompts to their keys, used when `PromptSelector` objects are provided.
- `all_args`: A dictionary containing all the arguments that will be passed to the OpenAI API.

### Methods
- `_extract_responses`: A static method that extracts the text from the completion choices returned by the OpenAI API.
- `_get_model_names`: A method that retrieves the model names from the argument combinations generated for the experiment.

### Usage
To use the `OpenAICompletionExperiment` class, instantiate it with the desired parameters and then call its methods to perform the experiment. The class handles the creation of all possible combinations of parameters and interacts with the OpenAI API to generate completions based on these combinations.

### Notes
- The class assumes that all parameters are provided as lists, even if a single value is desired (e.g., `temperature=[1.0]`).
- If the `DEBUG` environment variable is set, the class will use a mock completion function instead of the actual OpenAI API.
- Certain parameters (`echo`, `logit_bias`, `best_of`) are removed from the `all_args` dictionary if they are set to their default values, as they are not supported by the `gpt-3.5-turbo` model.
- If `azure_openai_service_configs` is provided, the class will configure the OpenAI API to use Azure OpenAI Service instead of the standard OpenAI service.
```