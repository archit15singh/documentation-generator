```markdown
# `data_loader.py` Module Documentation

## Overview

The `data_loader.py` module is part of the `prompttools` package within the `playground` subpackage. It provides functionality to load and process data for use in various machine learning experiments, particularly those involving language models. The module includes functions to render prompts using Jinja2 templates, load data for individual experiments, and run multiple experiments across different model types.

## Dependencies

- `os`: Standard library module to interact with the operating system.
- `jinja2`: Templating engine for Python.
- `streamlit`: An open-source app framework for Machine Learning and Data Science projects.
- `prompttools.selector.prompt_selector`: A custom module providing the `PromptSelector` class used to pair instructions with user inputs.
- `prompttools.playground.constants`: A module containing constants such as `ENVIRONMENT_VARIABLE` and `EXPERIMENTS`.

## Functions

### `render_prompts(templates, vars)`

Renders a list of prompts based on provided Jinja2 templates and variables.

#### Parameters

- `templates`: A list of Jinja2 template strings.
- `vars`: A list of dictionaries, where each dictionary contains variables to be rendered in the templates.

#### Returns

- `prompts`: A list of strings, where each string is a rendered prompt.

#### Process

1. Initialize an empty list `prompts`.
2. Iterate over each template in `templates`.
3. For each template, iterate over each variable set in `vars`.
4. Create a new Jinja2 `Environment`.
5. Convert the current template string into a `jinja_template`.
6. Render the `jinja_template` with the current variable set and append the result to `prompts`.
7. Return the list of rendered prompts.

### `load_data(model_type, model, instructions, user_inputs, temperature, top_p, max_tokens, frequency_penalty, presence_penalty, api_key)`

Loads data for a single experiment based on the specified parameters.

#### Parameters

- `model_type`: A string indicating the type of model to be used.
- `model`: The specific model to be used for the experiment.
- `instructions`: A list of instruction strings.
- `user_inputs`: A list of user input strings.
- `temperature`: A float representing the sampling temperature.
- `top_p`: A float representing the nucleus sampling parameter.
- `max_tokens`: An integer representing the maximum number of tokens to generate.
- `frequency_penalty`: A float representing the frequency penalty parameter.
- `presence_penalty`: A float representing the presence penalty parameter.
- `api_key`: An optional string representing the API key for the model's service.

#### Returns

- A pandas DataFrame containing the results of the experiment.

#### Process

1. If an `api_key` is provided, set the corresponding environment variable for the `model_type`.
2. Create a list of `PromptSelector` objects by pairing each instruction with each user input.
3. Depending on the `model_type`, initialize the appropriate experiment with the relevant parameters.
4. Convert the experiment results to a pandas DataFrame and return it.

### `run_multiple(model_types, models, instructions, prompts, openai_api_key, anthropic_api_key, google_api_key, hf_api_key, replicate_api_key)`

Runs multiple experiments across different model types and aggregates the results.

#### Parameters

- `model_types`: A list of strings indicating the types of models to be used.
- `models`: A list of models to be used for the experiments.
- `instructions`: A dictionary mapping instruction indices to instruction strings.
- `prompts`: A list of prompt strings.
- `openai_api_key`: An optional string representing the OpenAI API key.
- `anthropic_api_key`: An optional string representing the Anthropic API key.
- `google_api_key`: An optional string representing the Google PaLM API key.
- `hf_api_key`: An optional string representing the HuggingFace Hub API token.
- `replicate_api_key`: An optional string representing the Replicate API token.

#### Returns

- A list of pandas DataFrames, each containing the results of an experiment.

#### Process

1. Set the environment variables for each provided API key.
2. Initialize an empty list `dfs` to store the DataFrames.
3. Iterate over the `models` list.
4. For each model, check if there are corresponding instructions and create `PromptSelector` objects or use the provided `prompts`.
5. Depending on the `model_type`, initialize the appropriate experiment with the relevant parameters.
6. Convert the experiment results to a pandas DataFrame and append it to `dfs`.
7. Return the list of DataFrames.

## Decorators

- `@st.cache_data`: A decorator provided by Streamlit to cache the output of the decorated function, preventing unnecessary recomputation.

## Usage

The functions in this module are typically used within a Streamlit application to interactively run experiments with language models. Users can input different parameters and API keys to test various models and compare their outputs.

## Notes

- The module contains a `TODO` comment indicating that support for additional parameters such as temperature should be considered for the `run_multiple` function.
- The module assumes the existence of a `to_pandas_df` method on the experiment objects, which is used to convert the experiment results into pandas DataFrames.
- The module sets environment variables for API keys, which implies that the experiments are likely making calls to external services requiring authentication.
```