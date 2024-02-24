```markdown
# autoeval_with_docs.py

## Overview

The `autoeval_with_docs.py` module is part of the `prompttools` package and provides functionality to automatically evaluate the accuracy of a response given a set of documents using a language model such as GPT-4. It is designed to be used within a larger project that requires the assessment of text responses against provided context.

## Functions

### `_get_messages`

```python
def _get_messages(documents: list[str], response: str):
```

#### Description

This private function generates a formatted message for the evaluation system and the user's response using the Jinja2 templating engine.

#### Parameters

- `documents` (list[str]): A list of strings, each representing a document that provides context for the evaluation.
- `response` (str): The response text that needs to be evaluated for accuracy.

#### Returns

- A list of dictionaries, each containing a `role` key (either `"system"` or `"user"`) and a `content` key with the corresponding message content.

#### Usage

This function is used internally to prepare the input for the OpenAI chat model.

### `compute`

```python
def compute(documents: list[str], response: str, model: str = "gpt-4") -> float:
```

#### Description

This function uses an OpenAI chat model, such as GPT-4, to evaluate the accuracy of a response given a set of documents. It returns an integer score representing the accuracy.

#### Parameters

- `documents` (list[str]): A list of documents providing context for the evaluation.
- `response` (str): The response text to be evaluated.
- `model` (str, optional): The identifier for the OpenAI chat model to use. Defaults to `"gpt-4"`.

#### Returns

- An integer score from 0 to 10, where 0 indicates extreme inaccuracy and 10 indicates perfect accuracy.

#### Exceptions

- Raises `PromptToolsUtilityError` if the `OPENAI_API_KEY` environment variable is not set.

#### Usage

This function is called to compute the accuracy score of a response based on the provided documents.

### `autoeval_with_documents`

```python
def autoeval_with_documents(
    row: pandas.core.series.Series,
    documents: list[str],
    response_column_name: str = "response",
) -> float:
```

#### Description

This function scores the accuracy of a model's response given a list of documents, using GPT-4 as the evaluator. It is designed to be used with a pandas DataFrame where each row contains a model response and other data.

#### Parameters

- `row` (pandas.core.series.Series): A row from a pandas DataFrame, which includes the model response and potentially other data.
- `documents` (list[str]): A list of documents that provide context for the evaluation.
- `response_column_name` (str, optional): The name of the column in the DataFrame that contains the model's response. Defaults to `"response"`.

#### Returns

- An integer score from 0 to 10, representing the accuracy of the response.

#### Usage

This function is typically used within a DataFrame apply operation to score each row's response based on the provided documents.

## Dependencies

- `os`: To access environment variables.
- `openai`: To interact with the OpenAI API.
- `pandas.core.series`: To handle data in a pandas Series format.
- `jinja2`: To use templating for message formatting.
- `.error`: To raise custom errors defined within the `prompttools` package.

## Error Handling

- The module defines a custom error `PromptToolsUtilityError` which is raised when the required `OPENAI_API_KEY` environment variable is not set.

## Constants

- `EVALUATION_SYSTEM_PROMPT`: A string constant that defines the prompt for the evaluation system.
- `EVALUATION_USER_TEMPLATE`: A string constant that defines the template for the user's response using Jinja2 syntax.

## Usage Example

```python
import pandas as pd
from prompttools.utils.autoeval_with_docs import autoeval_with_documents

# Example DataFrame with responses
df = pd.DataFrame({
    'response': ["This is a response to evaluate.", "Another response to check."]
})

# Documents providing context
documents = ["Document 1 text.", "Document 2 text."]

# Apply the autoeval_with_documents function to each row
df['accuracy_score'] = df.apply(autoeval_with_documents, axis=1, documents=documents)
```

In the example above, the `autoeval_with_documents` function is applied to each row of a DataFrame to score the accuracy of the responses based on the provided documents.
```