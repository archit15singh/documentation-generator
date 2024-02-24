```markdown
# Technical Documentation for `main.py`

## Overview
`main.py` serves as the entry point for the GPT Pilot application. It initializes the application environment, handles command-line arguments, manages the application lifecycle, and ensures proper shutdown procedures. The script is responsible for setting up the database, handling user input, and executing the core functionality of the project.

## Dependencies
- `builtins`: Provides access to a list of built-in functions and variables available in Python.
- `json`: Used for encoding and decoding JSON data.
- `os`: Provides a way to use operating system-dependent functionality.
- `sys`: Provides access to some variables used or maintained by the interpreter.
- `traceback`: Provides a standard interface to extract, format, and print stack traces of Python programs.
- `dotenv`: A third-party module to load environment variables from a `.env` file.
- `utils.style`: Contains utility functions for styling terminal output.
- `utils.custom_print`: Provides a custom print function that can be used for inter-process communication (IPC).
- `helpers.Project`: Contains the `Project` class which encapsulates the project's core functionality.
- `utils.arguments`: Contains functions to parse and handle command-line arguments.
- `utils.exit`: Contains the `exit_gpt_pilot` function to handle the application's exit procedures.
- `logger.logger`: Provides logging functionality.
- `database.database`: Contains functions related to database operations.
- `utils.settings`: Contains settings management functionality.
- `utils.telemetry`: Contains telemetry-related functions for tracking application usage.
- `helpers.exceptions`: Defines custom exceptions used within the application.

## Main Execution Flow
1. The script checks for the presence of the `python-dotenv` package and raises a `RuntimeError` if it is missing.
2. The `.env` file is loaded to set environment variables.
3. The `init` function is defined to check for the existence of the database and its tables, and to parse command-line arguments.
4. The `__main__` block is executed if the script is run as the main program.
5. The script initializes variables for feedback, project instance, and exit function flag.
6. The `init` function is called to perform initial setup and retrieve arguments.
7. The script enters a `try` block to handle the main application logic.
8. Custom print functionality is set up, and IPC client instance is retrieved.
9. API key and endpoint are set from arguments if provided.
10. The script handles various command-line arguments to perform specific actions like displaying created apps with steps, showing version information, running UX tests, or starting the main project workflow.
11. Telemetry setup is performed, and various telemetry data points are set based on the arguments and application state.
12. The `Project` class is instantiated, and IPC checks are performed.
13. The project is started, and upon successful completion, the `finish` method is called.
14. The script handles custom exceptions like `ApiError` and `TokenLimitError` by recording the crash in telemetry and setting the exit function flag to `False`.
15. A `KeyboardInterrupt` is caught to handle user interruption and set the telemetry accordingly.
16. A `GracefulExit` exception is caught to handle a graceful shutdown without calling `project.finish_loading`.
17. Any other exceptions are caught, and an error message is printed along with the stack trace. Telemetry records the crash.
18. The `finally` block ensures that the current task is exited, loading is finished without cleanup if necessary, and the `exit_gpt_pilot` function is called if the exit function flag is `True`.

## Functions
### `init()`
- Checks for the existence of the database and tables, creating them if necessary.
- Parses command-line arguments and logs the start of the application with the arguments.
- Returns the parsed arguments.

## Command-Line Arguments Handling
- `--api-key`: Sets the OpenAI API key in the environment.
- `--api-endpoint`: Sets the OpenAI API endpoint in the environment.
- `--get-created-apps-with-steps`: Retrieves and prints the created apps with their steps.
- `--version`: Prints the application version.
- `--ux-test`: Runs user experience tests.
- Other arguments are used to set telemetry data and control the flow of the project.

## Exception Handling
- Custom exceptions like `ApiError` and `TokenLimitError` are handled specifically.
- `KeyboardInterrupt` is caught to handle user interruption.
- `GracefulExit` is caught to handle a graceful shutdown.
- All other exceptions are caught, and an error message with a stack trace is printed.

## Telemetry
- Telemetry data is set up and sent based on user actions and application state.
- Crashes are recorded, and telemetry is sent before exiting.

## Shutdown Procedures
- The `finally` block ensures that the application exits cleanly by calling `exit_gpt_pilot` with appropriate flags.
- Telemetry is sent if necessary, and feedback is requested based on the application state.
```