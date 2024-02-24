```markdown
# Technical Documentation for `test_prompts.py`

## Overview

The `test_prompts.py` module is part of a testing suite designed to verify the functionality of prompt generation within a project. It contains unit tests for the `get_prompt` function, which is responsible for creating formatted text prompts based on a given template and context data. These tests ensure that the `get_prompt` function correctly handles various input scenarios and produces the expected output.

## Test Cases

### `test_prompt_ran_command_None_exit`

#### Purpose

This test case verifies that the `get_prompt` function correctly formats a prompt when the exit code of a command is `None`. This scenario might represent a situation where the exit code is not applicable or was not captured.

#### Implementation

1. A dictionary is created to simulate the context data that would be passed to the `get_prompt` function. This includes:
   - `cli_response`: A string representing the standard output of a command.
   - `command`: The command that was executed.
   - `additional_message`: An additional message to be included in the prompt.
   - `exit_code`: Set to `None` to represent a scenario where the exit code is not provided.

2. The `get_prompt` function is called with the path to the prompt template (`dev_ops/ran_command.prompt`) and the context data dictionary.

3. The output of the `get_prompt` function is compared against the expected prompt text using an `assert` statement. The expected text includes the additional message, the command that was run, and the standard output, followed by instructions for the user to respond with either `DONE` or `BUG`.

### `test_prompt_ran_command_0_exit`

#### Purpose

This test case checks that the `get_prompt` function correctly formats a prompt when the exit code of a command is `0`, which typically indicates successful execution.

#### Implementation

1. A dictionary is created to simulate the context data that would be passed to the `get_prompt` function. This includes:
   - `cli_response`: A string representing the standard output of a command.
   - `command`: The command that was executed.
   - `additional_message`: An additional message to be included in the prompt.
   - `exit_code`: Set to `0` to represent a successful command execution.

2. The `get_prompt` function is called with the path to the prompt template (`dev_ops/ran_command.prompt`) and the context data dictionary.

3. The output of the `get_prompt` function is compared against the expected prompt text using an `assert` statement. The expected text is identical to the one in the `test_prompt_ran_command_None_exit` test case, as the instructions for the user do not change based on the exit code.

### `test_parse_task_no_processes`

#### Purpose

This test case ensures that the `get_prompt` function correctly handles a scenario where there are no running processes to report in the prompt.

#### Implementation

1. A dictionary is created to simulate the context data that would be passed to the `get_prompt` function. This includes:
   - `running_processes`: An empty dictionary to represent the absence of running processes.

2. The `get_prompt` function is called with the path to the prompt template (`development/parse_task.prompt`) and the context data dictionary.

3. The output of the `get_prompt` function is checked to ensure that the phrase 'the following processes' is not present in the prompt using an `assert` statement. This confirms that the prompt does not incorrectly reference running processes when there are none.

## Usage

The `test_prompts.py` module is used within the project's testing framework. It is typically executed as part of a test suite to validate the behavior of the prompt generation system. The tests are automated and are run to ensure that changes to the codebase do not introduce regressions in the prompt generation functionality.
```
