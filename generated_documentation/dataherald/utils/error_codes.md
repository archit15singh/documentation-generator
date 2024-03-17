```markdown
# `error_codes.py` Module

## Overview

The `error_codes.py` module is part of the `dataherald` package, specifically within the `utils` subpackage. It provides utilities for error handling and response formatting in a web application using the FastAPI framework. The module defines a mapping of custom exception names to error codes, a `CustomError` class for raising custom exceptions, and functions to generate standardized error responses.

## ERROR_MAPPING Dictionary

`ERROR_MAPPING` is a Python dictionary that maps the names of custom exception classes to corresponding error code strings. This mapping is used to translate exceptions into human-readable error codes that can be returned in API responses.

Example:
```python
ERROR_MAPPING = {
    "InvalidId": "invalid_object_id",
    # ... other mappings
}
```

## CustomError Class

`CustomError` is a custom exception class that extends the built-in `Exception` class. It allows for the creation of exceptions with an optional description.

### Attributes

- `description` (str, optional): An additional string providing more details about the error.

### `__init__` Method

The constructor takes the following parameters:

- `message` (str): The error message.
- `description` (str, optional): A detailed description of the error.

## error_response Function

The `error_response` function generates a `JSONResponse` object that contains standardized error information. This function is typically used to return an error response from an API endpoint.

### Parameters

- `error` (Exception): The exception that was raised.
- `detail` (dict): A dictionary containing additional details about the error.
- `default_error_code` (str, optional): A default error code string to use if the exception is not found in the `ERROR_MAPPING`.

### Behavior

1. Retrieves the error code from `ERROR_MAPPING` using the exception class name. If not found, uses the `default_error_code`.
2. Extracts the `description` attribute from the error, if present.
3. Logs the error information using the `logging` module.
4. Removes any `metadata` key from the `detail` dictionary.
5. Returns a `JSONResponse` with a status code of 400 and a content dictionary containing the error code, message, description, and detail.

## stream_error_response Function

The `stream_error_response` function is similar to `error_response` but returns a dictionary instead of a `JSONResponse` object. This is useful for streaming responses or other contexts where a `JSONResponse` is not appropriate.

### Parameters

- `error` (Exception): The exception that was raised.
- `detail` (dict): A dictionary containing additional details about the error.
- `default_error_code` (str, optional): A default error code string to use if the exception is not found in the `ERROR_MAPPING`.

### Behavior

1. Retrieves the error code from `ERROR_MAPPING` using the exception class name. If not found, uses the `default_error_code`.
2. Extracts the `description` attribute from the error, if present.
3. Logs the error information using the `logging` module.
4. Removes any `metadata` key from the `detail` dictionary.
5. Returns a dictionary with the error code, message, description, and detail.

## Usage in a Project

In a FastAPI project, these utilities are used to handle exceptions that occur during request processing. When an exception is caught, the `error_response` or `stream_error_response` function can be called to generate a standardized error payload that is then returned to the client. This ensures that all error responses follow a consistent format, making it easier for clients to handle errors and for developers to debug issues.
```