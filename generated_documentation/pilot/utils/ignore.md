```markdown
# IgnoreMatcher Class

## Overview

The `IgnoreMatcher` class is a utility designed to determine whether a given file or directory should be ignored based on predefined patterns, file size, and binary file status. It is typically used in projects to filter out files that should not be processed or included, such as temporary files, binaries, or files that are too large.

## Initialization

```python
def __init__(self,
    ignore_paths: Optional[list[str]] = None,
    *,
    root_path: Optional[None] = None,
    ignore_binaries: bool = True,
    ignore_large_files: bool = True,
):
```

### Parameters

- `ignore_paths`: An optional list of file or directory paths that should be ignored. These paths are added to the default ignore paths defined in `const.common.IGNORE_PATHS`.
- `root_path`: An optional root path that, if provided, is used to resolve relative paths to their absolute form.
- `ignore_binaries`: A boolean flag indicating whether binary files should be ignored.
- `ignore_large_files`: A boolean flag indicating whether files exceeding a certain size threshold should be ignored.

### Attributes

- `self.ignore_paths`: A combined list of default ignore paths and any additional paths provided during initialization.
- `self.ignore_binaries`: Stores the value of the `ignore_binaries` parameter.
- `self.ignore_large_files`: Stores the value of the `ignore_large_files` parameter.
- `self.root_path`: Stores the root path, if provided.

## Methods

### ignore

```python
def ignore(self, path: str) -> bool:
```

#### Description

Determines if the specified file or directory should be ignored based on the ignore patterns, file size, and binary status.

#### Parameters

- `path`: The path to the file or directory to check.

#### Returns

- `True` if the path should be ignored, `False` otherwise.

#### Logic

1. Converts the provided path to an absolute path if a `root_path` is set.
2. Checks if the path is in the ignore list using `is_in_ignore_list`.
3. Checks if the file is larger than the threshold using `is_large_file`.
4. Checks if the file is binary using `is_binary`.
5. Returns `True` if any of the above checks are `True`, otherwise returns `False`.

### is_in_ignore_list

```python
def is_in_ignore_list(self, path: str) -> bool:
```

#### Description

Checks if the given path matches any of the ignore patterns.

#### Parameters

- `path`: The path to the file or directory to check.

#### Returns

- `True` if the path matches any of the ignore patterns, `False` otherwise.

### is_large_file

```python
def is_large_file(self, path: str) -> bool:
```

#### Description

Determines if the file at the given path is larger than the predefined size threshold.

#### Parameters

- `path`: The full path to the file to check.

#### Returns

- `True` if the file is larger than the threshold or not accessible, `False` otherwise.

### is_binary

```python
def is_binary(self, path: str) -> bool:
```

#### Description

Checks if the file at the given path is a binary file.

#### Parameters

- `path`: The full path to the file to check.

#### Returns

- `True` if the file is binary or cannot be opened, `False` otherwise.

## Usage

The `IgnoreMatcher` class is instantiated with optional parameters to customize the ignore behavior. Once instantiated, the `ignore` method can be called with a file or directory path to determine if it should be ignored according to the class's rules.

## Error Handling

The methods `is_large_file` and `is_binary` are designed to return `True` when an exception occurs during file size retrieval or file reading, respectively. This ensures that files causing such exceptions are ignored by default.
```
