```markdown
# llm_connection.py

## Overview

The `llm_connection.py` module is part of a larger project and is responsible for handling the connection and communication with a language model API, such as OpenAI's GPT-3 or GPT-4. It includes functions to encode messages into tokens, test API access, create chat completions, handle rate limiting, and retry failed requests. The module also contains utility functions for token counting, JSON response validation, and error handling.

## Dependencies

- `re`: Regular expression operations.
- `requests`: HTTP library for making API requests.
- `os`: Miscellaneous operating system interfaces.
- `sys`: System-specific parameters and functions.
- `time`: Time access and conversions.
- `json`: JSON encoder and decoder.
- `tiktoken`: Tokenizer for encoding messages.
- `prompt_toolkit.styles`: Styling for command-line interfaces.
- `jsonschema`: JSON Schema validation library.
- `utils.style`: Custom styling functions.
- `typing`: Support for type hints.
- `const.llm`: Constants related to the language model.
- `const.messages`: Constants for messages.
- `logger.logger`: Custom logging.
- `helpers.exceptions`: Custom exception classes.
- `utils.utils`: Utility functions.
- `utils.function_calling`: Handling function calls in requests.
- `utils.questionary`: Custom command-line prompts.
- `telemetry`: Telemetry for monitoring and analytics.

## Functions

### get_tokens_in_messages

Calculates the total number of tokens in a list of messages.

### num_tokens_from_functions

Calculates the number of tokens used by a list of functions, including their names, descriptions, parameters, and properties.

### test_api_access

Tests the API access by sending a request to the API and returns a boolean indicating success or failure.

### create_gpt_chat_completion

Creates a GPT chat completion request with the provided messages, request type, project, optional function calls, prompt data, and temperature settings.

### delete_last_n_lines

Deletes the last `n` lines from the terminal output.

### count_lines_based_on_width

Counts the number of lines required to display content within a given terminal width.

### get_tokens_in_messages_from_openai_error

Extracts the token count from an OpenAI error message.

### retry_on_exception

A decorator that retries a function call on exception, with special handling for JSON decode errors and validation errors.

### rate_limit_exceeded_sleep

Handles rate limiting by sleeping for the duration specified in the error message plus an additional buffer time.

### trace_token_limit_error

Traces token limit errors by logging the event with relevant information.

### stream_gpt_completion

Streams the GPT completion response from the API and handles the incoming data.

### get_api_key_or_throw

Retrieves the API key from the environment or raises an exception if it's not defined.

### assert_json_response

Asserts that the response from the LLM is JSON.

### clean_json_response

Cleans the JSON response from the LLM to ensure it's valid JSON.

### assert_json_schema

Asserts that the JSON response matches the expected schema.

### postprocessing

Performs postprocessing on the GPT response.

### load_data_to_json

Loads a string into JSON, fixing any issues with the JSON format.

## Usage

The functions in this module are used to interact with a language model API. They are typically called from other parts of the project, such as an agent conversation handler or a command-line interface. The module handles the complexities of tokenization, API communication, error handling, and retries, abstracting these details away from the rest of the application.

## Error Handling

Custom exceptions such as `TokenLimitError`, `ApiKeyNotDefinedError`, and `ApiError` are used to handle specific error conditions. The module includes robust error handling to ensure that the application can gracefully recover from or report errors encountered during API communication.

## Telemetry

The module includes telemetry calls to record API requests, responses, and errors. This data is used for monitoring and analytics purposes.

## Environment Variables

The module relies on environment variables to configure API endpoints, model names, and API keys. These variables include `ENDPOINT`, `MODEL_NAME`, `OPENROUTER_ENDPOINT`, `AZURE_ENDPOINT`, `OPENAI_ENDPOINT`, `AZURE_API_KEY`, `OPENROUTER_API_KEY`, `OPENAI_API_KEY`, and `RATE_LIMIT_EXTRA_BUFFER`.

## Tokenizer

The `tiktoken` library is used to tokenize messages before sending them to the API. This is necessary to calculate the number of tokens in a request and ensure it does not exceed the API's limits.

## Logging

The `logger` module is used to log information, warnings, and errors. This is crucial for debugging and maintaining the application.

## Decorators

The `retry_on_exception` decorator is used to automatically retry API requests that fail due to transient errors or rate limiting.

## JSON Validation

The `jsonschema` library is used to validate JSON responses against predefined schemas, ensuring that the data received from the API is in the expected format.
```