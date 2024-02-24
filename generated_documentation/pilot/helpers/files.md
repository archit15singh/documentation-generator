```markdown
# `files.py` Module Documentation

## Overview

The `files.py` module is part of the `/workspaces/documentation-generator/target_code/pilot/helpers/` package and provides utility functions for file and directory manipulation within a project. It includes functions to update file contents, retrieve file and directory contents, and clear a directory while optionally respecting ignore patterns.

## Functions

### `update_file`

```python
def update_file(path: str, new_content: Union[str, bytes], project=None):
```

#### Description

Updates the content of a file at a specified path with new content. If the file does not exist, it will be created along with any necessary intermediate directories.

#### Parameters

- `path` (str): The full path to the file that needs to be updated.
- `new_content` (Union[str, bytes]): The new content to write to the file. Can be a string or bytes.
- `project` (Optional): An optional Project object that may contain additional context or settings for the file update. Defaults to `None`.

#### Behavior

- Directories leading up to the file will be created if they do not exist (`os.makedirs` with `exist_ok=True`).
- If `new_content` is a string, the file is opened in text mode with UTF-8 encoding; if it is bytes, the file is opened in binary mode.
- If a `project` object is provided and `skip_steps` is `False`, an 'openFile' event is printed.
- If `project.check_ipc()` returns `False`, a success message is printed in green indicating the file has been updated.

### `get_file_contents`

```python
def get_file_contents(path: str, project_root_path: str) -> dict[str, Union[str, bytes]]:
```

#### Description

Retrieves the contents and metadata of a file, including its name, path, content, and full path.

#### Parameters

- `path` (str): The full path to the file.
- `project_root_path` (str): The full path to the project root directory.

#### Returns

A dictionary with the following keys:
- `name`: The name of the file.
- `path`: The relative path to the file from the project root.
- `content`: The content of the file, either as a string (if text) or bytes (if binary).
- `full_path`: The normalized full path to the file.
- `lines_of_code`: The number of lines in the file.

#### Behavior

- The file is first attempted to be read as a text file with UTF-8 encoding.
- If a `UnicodeDecodeError` occurs, it is then read as a binary file.
- Exceptions such as `NotADirectoryError`, `FileNotFoundError`, and others are caught and re-raised with a custom message.

### `get_directory_contents`

```python
def get_directory_contents(directory: str, ignore: Optional[list[str]] = None) -> list[dict[str, Union[str, bytes]]]:
```

#### Description

Retrieves the contents of all files within a specified directory, optionally ignoring certain files or directories.

#### Parameters

- `directory` (str): The full path to the directory whose contents are to be retrieved.
- `ignore` (Optional[list[str]]): A list of file or directory patterns to ignore.

#### Returns

A list of file objects, each of which is a dictionary as returned by `get_file_contents`.

#### Behavior

- Uses `os.walk()` to traverse the directory tree.
- Applies ignore patterns using `IgnoreMatcher`.
- For each file not ignored, it appends the result of `get_file_contents` to the return list.

### `clear_directory`

```python
def clear_directory(directory: str, ignore: Optional[list[str]] = None):
```

#### Description

Deletes all files and directories within a specified directory, except for those that match the ignore patterns.

#### Parameters

- `directory` (str): The full path to the directory to clear.
- `ignore` (Optional[list[str]]): A list of file or directory patterns to ignore.

#### Behavior

- Uses `os.walk()` to traverse the directory tree in a top-down manner.
- Applies ignore patterns using `IgnoreMatcher`.
- Removes files that are not ignored.
- Removes empty subdirectories that are not ignored.

## Dependencies

- `pathlib.Path`: Used for path manipulation.
- `os`: Used for file and directory operations.
- `typing`: Provides type hints.
- `utils.style.color_green`: Used to print success messages in green.
- `utils.ignore.IgnoreMatcher`: Used to apply ignore patterns.

## Usage Notes

- The module assumes UTF-8 encoding for text files.
- The module does not currently prevent writing files outside the project root (as indicated by the TODO comment).
- The module is designed to be used within a larger project context, potentially interacting with a `Project` object and IPC mechanisms.
```