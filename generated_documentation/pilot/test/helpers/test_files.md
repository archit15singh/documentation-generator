```markdown
# `test_files.py` Module

## Overview

The `test_files.py` module is part of the test suite for the `pilot` project, specifically testing the functionality provided by the `pilot.helpers.files` module. It contains unit tests that verify the behavior of file manipulation functions such as `update_file`, `get_file_contents`, and `get_directory_contents`.

## Dependencies

- `os`: Provides a portable way of using operating system-dependent functionality.
- `pathlib.Path`: Offers classes representing filesystem paths with semantics appropriate for different operating systems.
- `tempfile.NamedTemporaryFile`: Creates a temporary file with a unique name.
- `unittest.mock.patch`: Used for patching module and class-level attributes within the scope of a test.
- `unittest.mock.call`: Represents a call to a mock object.
- `pytest`: A framework for writing small tests.
- `pilot.helpers.files`: The module containing the functions under test.

## Test Cases

### `test_update_file_creates_directories`

Verifies that the `update_file` function creates intermediate directories if they do not exist when attempting to write to a file.

- Mocks:
  - `pilot.helpers.files.open`: To avoid actual file operations.
  - `pilot.helpers.files.os`: To intercept filesystem interactions.

### `test_update_file_creates_text_file`

Ensures that the `update_file` function correctly creates a text file with the specified content and uses UTF-8 encoding.

- Mocks:
  - `pilot.helpers.files.open`: To avoid actual file operations.
  - `pilot.helpers.files.os`: To intercept filesystem interactions.

### `test_update_file_creates_binary_file`

Confirms that the `update_file` function can create a binary file with the given byte content.

- Mocks:
  - `pilot.helpers.files.open`: To avoid actual file operations.
  - `pilot.helpers.files.os`: To intercept filesystem interactions.

### `test_update_file_with_encoded_content`

Tests the `update_file` function with various encoded content to ensure it handles different file encodings correctly.

- Uses `NamedTemporaryFile` to create temporary files for testing.
- Parameterized with different source content and expected encoded results.

### `test_get_file_contents`

Checks the `get_file_contents` function to ensure it reads the contents of a file correctly and returns the expected dictionary with file details.

- Uses `NamedTemporaryFile` to create temporary files for testing.
- Parameterized with different encoded content and expected results.

### `test_get_directory_contents_mocked`

Tests the `get_directory_contents` function to verify that it traverses the directory tree, respects ignore patterns, and correctly handles both text and binary files.

- Mocks:
  - `pilot.helpers.files.open`: To avoid actual file operations.
  - `pilot.helpers.files.os`: To intercept filesystem interactions.
  - `pilot.helpers.files.IgnoreMatcher`: To simulate ignore patterns.

### `test_get_directory_contents_live`

Performs a live test of the `get_directory_contents` function to ensure it correctly processes the contents of a directory, including the current test file, while respecting the specified ignore patterns.

- Uses the actual filesystem to verify the function's behavior in a real environment.

## Usage

The tests in this module are executed as part of the project's test suite to ensure the `pilot.helpers.files` module functions as expected. They are typically run using a test runner like `pytest` that collects and runs tests according to the configurations and command-line options provided.

## Notes

- The tests use the `patch` decorator to replace the actual filesystem and file operations with mock objects, allowing the tests to run without creating, reading, or writing actual files on the disk.
- The `NamedTemporaryFile` is used to create temporary files for testing purposes, which are removed after the test execution.
- The `np` function within `test_get_directory_contents_mocked` is a helper function to normalize file paths according to the operating system's path separators.
- The tests ensure that the functions handle both text and binary data correctly and that they respect the encoding of the files.
- The `test_get_directory_contents_live` function performs a live test, which means it interacts with the actual filesystem and requires the test environment to have the expected directory structure and files.
```