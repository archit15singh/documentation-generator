```markdown
# CLI Helper Module

This module provides a set of functions to execute shell commands within a Python environment, manage running processes, and interact with the user through a command-line interface. It is designed to be used within a larger project that requires executing system commands, capturing their output, and handling user input.

## Dependencies

- `psutil`: Used for process management.
- `subprocess`: Used for running commands in subprocesses.
- `os`: Used for operating system dependent functionality.
- `signal`: Used for handling signals.
- `threading`: Used for running operations in separate threads.
- `queue`: Used for inter-thread communication.
- `time`: Used for time-related functions.
- `platform`: Used for getting the running platform's information.
- `typing`: Used for type hinting.

## Imported Modules

- `logger`: Custom logging module.
- `utils.style`: Provides functions for coloring text output.
- `utils.ignore`: Provides functionality to ignore files and directories based on patterns.
- `database.database`: Provides functionality to save command execution data.
- `helpers.exceptions`: Custom exception classes.
- `prompts.prompts`: Provides functions to prompt the user for input.
- `const.code_execution`: Constants related to command execution timing and output length.
- `const.messages`: Constants for affirmative and negative answers.

## Global Variables

- `interrupted`: A flag to indicate if the execution has been interrupted.
- `running_processes`: A dictionary that maps command IDs to tuples containing the command string and process ID.

## Functions

### `enqueue_output(out, q)`

Reads lines from a file-like object `out` and puts them into a queue `q`. Stops if `interrupted` is set to True.

### `run_command(command, root_path, q_stdout, q_stderr) -> subprocess.Popen`

Executes a command in a subprocess and captures its stdout and stderr into queues. Returns the subprocess object.

### `terminate_named_process(command_id: str) -> None`

Terminates a process with the given command ID.

### `terminate_running_processes()`

Terminates all running processes tracked in `running_processes`.

### `term_proc_windows(pid: int)`

Terminates a process with the given PID on Windows systems.

### `term_proc_unix_like(pid: int)`

Terminates a process with the given PID on Unix-like systems.

### `is_process_running(pid: int) -> bool`

Checks if a process with the given PID is currently running.

### `terminate_process(pid: int, name=None) -> None`

Terminates a process with the given PID and removes it from `running_processes`.

### `read_queue_line(q, stdout=True)`

Reads a line from the queue `q` and prints it to stdout or stderr based on the `stdout` flag.

### `read_remaining_queue(q, stdout=True)`

Reads all remaining lines from the queue `q` and returns them as a string.

### `execute_command(project, command, timeout=None, success_message=None, command_id: str = None, force=False) -> (str, str, int)`

Executes a command and captures its output. Handles user confirmation, timeout, and success message detection. Returns the command output, a status message, and the exit code.

### `check_if_command_successful(convo, command, cli_response, response, exit_code, additional_message=None, task_steps=None, step_index=None)`

Checks if a command execution was successful based on the CLI response and exit code. Sends a message to the LLM for further processing.

### `build_directory_tree(path, prefix='', root_path=None) -> str`

Builds a string representation of the directory tree starting from the given path.

### `execute_command_and_check_cli_response(convo, command: dict, task_steps=None, step_index=None)`

Executes a command and checks its CLI response. Returns the CLI response and the agent's response.

### `run_command_until_success(convo, command, timeout: Union[int, None], command_id: Union[str, None] = None, success_message=None, additional_message=None, force=False, return_cli_response=False, success_with_cli_response=False, is_root_task=False, task_steps=None, step_index=None)`

Runs a command until it succeeds or reaches a timeout. Handles user input, success message detection, and debugging. Returns a dictionary with success status, CLI response, and user input.

## Usage

This module is intended to be used within a larger project that requires executing system commands, capturing their output, and handling user input. It provides a high-level interface for running commands, managing processes, and interacting with the user through prompts. It also includes functionality for building a directory tree representation and handling exceptions related to command execution.

The functions in this module can be used to:

- Execute shell commands with or without user confirmation.
- Capture the output of commands in real-time.
- Terminate running processes by ID or PID.
- Check if a command execution was successful based on its output and exit code.
- Build a simplified representation of a directory tree.
- Run a command repeatedly until it succeeds or a timeout is reached.
- Handle user objections to running commands and provide debugging assistance.

The module is designed to be flexible and can be integrated into various types of projects that require command-line interaction and process management.
```