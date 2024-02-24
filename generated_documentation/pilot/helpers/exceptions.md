```markdown
# Exceptions Module Documentation

## Overview

The `exceptions.py` module defines custom exception classes that are used throughout the project to handle specific error conditions. These exceptions are designed to provide more context and control over error handling compared to generic exceptions.

## Custom Exception Classes

### ApiKeyNotDefinedError

- **Description**: This exception is raised when an API key required for operation is not configured in the environment.
- **Attributes**:
  - `env_key` (str): The name of the environment variable expected to contain the API key.
- **Usage**: An instance of `ApiKeyNotDefinedError` is created and raised when the application detects that the necessary API key is missing from the environment variables.

### CommandFinishedEarly

- **Description**: This exception is raised when a command finishes execution before a predefined timeout period.
- **Attributes**:
  - `message` (str): A message describing the early completion of the command. Defaults to 'Command finished before timeout. Handling early completion...'.
- **Usage**: An instance of `CommandFinishedEarly` is created and raised to signal that a command has finished its execution earlier than expected, allowing the application to handle this scenario appropriately.

### TokenLimitError

- **Description**: This exception is raised when the number of tokens in a message exceeds the maximum allowed by the GPT model.
- **Attributes**:
  - `tokens_in_messages` (int): The number of tokens present in the message.
  - `max_tokens` (int): The maximum number of tokens allowed, defaulting to `MAX_GPT_MODEL_TOKENS` from the `const.llm` module.
- **Usage**: An instance of `TokenLimitError` is created and raised when the token count in a message surpasses the `max_tokens` threshold, indicating that the message is too long for the GPT model to process.

### TooDeepRecursionError

- **Description**: This exception is raised when a recursive operation exceeds a safe depth, potentially leading to a stack overflow.
- **Attributes**:
  - `message` (str): A message indicating that the recursion depth is excessive. Defaults to 'Recursion is too deep!'.
- **Usage**: An instance of `TooDeepRecursionError` is created and raised to prevent the application from entering an unsafe recursive depth, which could cause runtime errors.

### ApiError

- **Description**: This exception is raised when an API call results in an error.
- **Attributes**:
  - `message` (str): A message describing the API error.
  - `response` (Optional[Response]): The response object from the API call, if available.
  - `response_json` (Optional[dict]): A JSON representation of the response text, parsed if the response contains valid JSON text.
- **Usage**: An instance of `ApiError` is created and raised when an API call fails. The exception captures both the error message and the response from the API, providing additional context for debugging.

### GracefulExit

- **Description**: This exception is used to signal a controlled and intentional shutdown of the application.
- **Attributes**:
  - `message` (str): A message indicating that a graceful exit is occurring. Defaults to 'Graceful exit'.
- **Usage**: An instance of `GracefulExit` is created and raised to initiate a clean shutdown process, allowing the application to terminate without error and perform any necessary cleanup operations.

## Module Location

- **Path**: `/workspaces/documentation-generator/target_code/pilot/helpers/exceptions.py`

## Importing the Module

To use these custom exceptions in other parts of the project, the module can be imported using the following syntax:

```python
from pilot.helpers.exceptions import (
    ApiKeyNotDefinedError,
    CommandFinishedEarly,
    TokenLimitError,
    TooDeepRecursionError,
    ApiError,
    GracefulExit
)
```

## Handling Exceptions

These custom exceptions can be caught and handled using `try-except` blocks. For example:

```python
try:
    # Code that may raise a custom exception
except ApiKeyNotDefinedError as e:
    # Handle missing API key
    print(e.env_key)
```

By catching these exceptions, the application can provide more informative error messages and take appropriate actions based on the specific exception raised.
```