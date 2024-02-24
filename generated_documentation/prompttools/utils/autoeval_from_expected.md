```markdown
# autoeval_from_expected.py

This Python module is part of a larger project and is responsible for automatically evaluating responses to prompts based on expected answers. It leverages the OpenAI GPT-4 model to perform this evaluation. The module contains several functions that work together to achieve this functionality.

## Dependencies

- `os`: Standard Python module to interact with the operating system.
- `openai`: Python client library for the OpenAI API.
- `jinja2`: A modern and designer-friendly templating language for Python.
- `pandas`: An open-source data analysis and manipulation tool.

## Constants

- `EVALUATION_SYSTEM_PROMPT`: A string that defines the instructions for the GPT-4 model to evaluate responses. It tells the model to grade the response as either RIGHT or WRONG based on whether the ACTUAL answer matches the EXPECTED answer.

- `EVALUATION_USER_TEMPLATE`: A Jinja2 template string that formats the prompt, expected answer, and actual answer for evaluation by the model.

## Functions

### `_get_messages`

This private function uses the Jinja2 template to create a formatted message that includes the prompt, expected answer, and actual response. It returns a list of dictionaries, each representing a message with a role (either "system" or "user") and content.

#### Parameters

- `prompt (str)`: The original prompt given to the model.
- `expected (str)`: The expected correct answer to the prompt.
- `response (str)`: The actual response from the model that needs to be evaluated.

#### Returns

- `List[Dict[str, str]]`: A list of message dictionaries ready to be used by the OpenAI API.

### `compute`

This function calls the OpenAI API to evaluate a response using the GPT-4 model. It returns a score of 1.0 if the response is correct (RIGHT) or 0.0 if it is incorrect (WRONG).

#### Parameters

- `prompt (str)`: The input prompt.
- `expected (str)`: The expected correct answer.
- `response (str)`: The actual response from the model.
- `model (str)`: The identifier for the OpenAI chat model to use. Defaults to "gpt-4".

#### Returns

- `float`: The evaluation score, either 1.0 or 0.0.

#### Raises

- `PromptToolsUtilityError`: If the `OPENAI_API_KEY` environment variable is not set.

### `evaluate`

This function is a wrapper around the `compute` function, providing a consistent interface for auto-evaluation.

#### Parameters

- `prompt (str)`: The input prompt.
- `response (str)`: The actual response from the model.
- `metadata (dict)`: A dictionary containing metadata for the evaluation. (Unused in the current implementation)
- `expected (str)`: The expected correct answer.

#### Returns

- `float`: The evaluation score from the `compute` function.

### `autoeval_from_expected_response`

This function is designed to be applied to a pandas DataFrame. It evaluates the response in each row of the DataFrame against an expected answer.

#### Parameters

- `row (pandas.core.series.Series)`: A row from a pandas DataFrame.
- `expected (str)`: The expected correct answer.
- `prompt_column_name (str)`: The name of the column in the DataFrame that contains the prompts. Defaults to the column name provided.
- `response_column_name (str)`: The name of the column in the DataFrame that contains the responses. Defaults to "response".

#### Returns

- `float`: The evaluation score for the response in the given row.

## Usage

The module is used to automatically evaluate responses to prompts by comparing them with expected answers. It is particularly useful in scenarios where responses from a language model like GPT-4 need to be graded or validated at scale. The module can be integrated into a larger system that processes and evaluates large datasets, such as student responses to math questions or automated testing of chatbot outputs.
```
