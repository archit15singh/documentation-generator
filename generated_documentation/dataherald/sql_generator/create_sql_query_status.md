```markdown
# `create_sql_query_status.py` Module

## Overview

The `create_sql_query_status.py` module is part of the `dataherald` project and is responsible for validating SQL queries and updating the status of SQL generation objects. It includes functionality to execute SQL queries against a database with a timeout, handle potential SQL injection attempts, and format error messages.

## Dependencies

- `os`: Standard library module to interact with the operating system.
- `dataherald.sql_database.base`: Custom module providing `SQLDatabase` class and `SQLInjectionError` exception.
- `dataherald.types`: Custom module defining `SQLGeneration` type.
- `dataherald.utils.timeout_utils`: Custom module providing `run_with_timeout` function.

## Functions

### `format_error_message(sql_generation: SQLGeneration, error_message: str) -> SQLGeneration`

#### Description

This function takes an `SQLGeneration` object and an error message string, formats the error message by removing the complete SQL query between square brackets, updates the `SQLGeneration` object's status to "INVALID", and sets the error message.

#### Parameters

- `sql_generation`: An instance of `SQLGeneration` that holds the status and error message of the SQL generation process.
- `error_message`: A string containing the error message that may include the SQL query.

#### Returns

- An updated `SQLGeneration` object with the formatted error message and status set to "INVALID".

### `create_sql_query_status(db: SQLDatabase, query: str, sql_generation: SQLGeneration) -> SQLGeneration`

#### Description

This function determines the status of an SQL query by attempting to execute it against a database. It populates the `sql_generation` object with the result of the execution, the status of the SQL generation, and any error messages encountered during the process.

#### Parameters

- `db`: An instance of `SQLDatabase` that provides methods to interact with the database and parse/filter SQL commands.
- `query`: A string containing the SQL query to be executed.
- `sql_generation`: An instance of `SQLGeneration` that will be updated with the status and error message of the SQL generation process.

#### Returns

- An updated `SQLGeneration` object with the status set to either "VALID" or "INVALID" and the error message populated if applicable.

#### Behavior

1. Checks if the `query` string is empty. If it is, sets the `sql_generation` status to "INVALID" and sets the error message to indicate that SQL could not be generated from the prompt.
2. If the `query` is not empty, it proceeds to:
   - Parse and filter the query using `db.parser_to_filter_commands`.
   - Execute the query with a timeout using `run_with_timeout`, with the timeout duration fetched from the environment variable `SQL_EXECUTION_TIMEOUT` or defaulting to 60 seconds.
   - If the query executes successfully within the timeout, sets the `sql_generation` status to "VALID" and clears any error message.
3. Handles exceptions:
   - `TimeoutError`: Calls `format_error_message` to set the status to "INVALID" and sets the error message to indicate a timeout.
   - `SQLInjectionError`: Reraises the exception with a message indicating a sensitive SQL keyword was detected.
   - Any other `Exception`: Calls `format_error_message` with the exception message to set the status to "INVALID" and populate the error message.

#### Usage

This function is used within the `dataherald` project to validate SQL queries generated from user prompts or other sources. It ensures that the queries are safe to execute and provides feedback on any issues encountered during the validation process.
```