```markdown
# autoeval_scoring.py

## Overview
The `autoeval_scoring.py` module is part of the `prompttools` utility package within the `documentation-generator` project. It provides functionality to automatically evaluate and score a model's response against a given fact using a high-quality chat model, such as `claude-2`. The module leverages the `anthropic` package to interact with the Anthropic API for generating scores.

## Dependencies
- `os`: Standard library module to interact with the operating system.
- `pandas.core.series`: Part of the `pandas` library, used for handling data in Series format.
- `jinja2`: Templating engine for Python, used to generate prompts dynamically.
- `anthropic`: A third-party package (optional) for interacting with the Anthropic API.

## Constants
- `AUTO_EVAL_PROMPT_TEMPLATE`: A Jinja2 template string that defines the structure of the prompt to be sent to the evaluation model. It includes placeholders for a human prompt, an AI prompt, a fact, and a model answer.

## Functions

### `_generate_auto_eval_prompt(fact: str, model_answer: str) -> str`
A private function that generates an auto-evaluation prompt using the `AUTO_EVAL_PROMPT_TEMPLATE`. It takes a fact and a model answer as input and returns a string with the rendered prompt.

#### Parameters
- `fact (str)`: The fact to be evaluated against.
- `model_answer (str)`: The answer provided by the model.

#### Returns
- `str`: The rendered auto-evaluation prompt.

### `compute(fact: str, model_answer: str, model: str = "claude-2") -> float`
This function uses a specified chat model to automatically score a given fact/response pair. The score is an integer ranging from 1 to 7.

#### Parameters
- `fact (str)`: The fact (truth) against which the response is evaluated.
- `model_answer (str)`: The model's response to be scored.
- `model (str)`: The name of the model used for evaluation, defaulting to "claude-2".

#### Returns
- `float`: The score as an integer from 1 to 7.

#### Raises
- `RuntimeError`: If the `ANTHROPIC_API_KEY` environment variable is not set.

### `autoeval_scoring(row: pandas.core.series.Series, expected: str, response_column_name: str = "response") -> float`
This function scores a model's response using auto-evaluation.

#### Parameters
- `row (pandas.core.series.Series)`: A row from a DataFrame containing various data, including the model's response.
- `expected (str)`: The expected correct response.
- `response_column_name (str)`: The column name in the DataFrame that contains the model's response, defaulting to "response".

#### Returns
- `float`: The score as an integer from 1 to 7.

#### Raises
- `ModuleNotFoundError`: If the `anthropic` package is not installed.

## Usage
The `autoeval_scoring.py` module is used to automatically score the accuracy of a model's response to a prompt. It is typically used in the context of evaluating AI-generated text, where the correctness of the response is critical. The module requires an API key for the Anthropic API to be set in the environment and the `anthropic` package to be installed.

## Example
To use the `autoeval_scoring` function, one would typically have a DataFrame with a column containing model responses. The function can be applied to each row of the DataFrame to obtain a score for the response:

```python
import pandas as pd
from prompttools.utils.autoeval_scoring import autoeval_scoring

# Assuming df is a DataFrame with a 'response' column
df['score'] = df.apply(autoeval_scoring, expected='The correct answer', axis=1)
```
```