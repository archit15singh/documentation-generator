```markdown
# CodeMonkey.py

## Overview

`CodeMonkey.py` is a Python module that defines the `CodeMonkey` class, which inherits from the `Agent` class. This class is responsible for handling code changes within a project, including identifying the file to change, implementing code changes, reviewing changes, and applying patches to files.

## Dependencies

- `os.path`: For file path manipulations.
- `re`: For regular expression operations.
- `typing`: For type hinting.
- `traceback`: For formatting exceptions.
- `difflib`: For generating unified diffs between file versions.
- `helpers.AgentConvo`: For managing conversations with a language model.
- `helpers.Agent`: The base class for `CodeMonkey`.
- `helpers.files`: For reading file contents.
- `const.function_calls`: For constants representing function call actions.
- `utils.exit`: For tracing code events.
- `utils.telemetry`: For telemetry data collection.

## Constants

- `NO_EOL`: A string indicating the absence of a newline at the end of a file in a diff.
- `PATCH_HEADER_PATTERN`: A compiled regular expression pattern for matching hunk headers in diffs.
- `MAX_REVIEW_RETRIES`: The maximum number of retries allowed for reviewing changes.

## Class: CodeMonkey

### Attributes

- `save_dev_steps`: A boolean indicating whether to save development steps.

### Methods

#### `__init__(self, project)`
Constructor for the `CodeMonkey` class.

#### `get_original_file(self, code_changes_description: str, step: dict[str, str], files: list[dict]) -> tuple[str, str]`
Retrieves the original file content and name based on the provided code changes description, step information, and list of files.

#### `implement_code_changes(self, convo: Optional[AgentConvo], step: dict[str, str]) -> AgentConvo`
Implements code changes described in the `code_changes_description` attribute of the `step` dictionary.

#### `replace_complete_file(self, convo: AgentConvo, file_content: str, file_name: str, files: list[dict]) -> str`
Replaces the complete file content as a fallback if individual code block replacements fail.

#### `identify_file_to_change(self, code_changes_description: str, files: list[dict]) -> str`
Identifies the file to change based on the code changes description.

#### `review_change(self, convo: AgentConvo, instructions: str, file_name: str, old_content: str, new_content: str) -> str`
Reviews changes applied to a file, deciding which parts of the diff should be kept or removed.

#### `get_diff_hunks(file_name: str, old_content: str, new_content: str) -> list[str]`
Generates a list of diff hunks between two versions of a file.

#### `apply_diff(self, file_name: str, old_content: str, hunks: list[str], fallback: str)`
Applies approved diff hunks to the original file content.

#### `_apply_patch(original: str, patch: str, revert: bool = False)`
Applies a patch to a string to recover a newer version of the string.

## Usage

The `CodeMonkey` class is used within a project to manage code changes. It is instantiated with a reference to the project and then used to:

1. Identify the file that needs to be changed based on a description of code changes.
2. Retrieve the original content of the file to be modified.
3. Implement the code changes by either updating the existing file or creating a new one.
4. Review the changes made to the file, with the option to retry the review process up to a maximum number of times.
5. Apply the changes to the file, either by using the entire new content or only the approved parts of the diff.

The class interacts with a language model through the `AgentConvo` class to receive instructions for code changes and reviews. It also handles edge cases such as binary files, missing files, and errors during the patch application process.

Telemetry data is collected for the number of lines created during the file update process, and code events are traced for significant actions or errors.
```