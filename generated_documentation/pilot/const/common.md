```markdown
# `common.py` Module Documentation

## Overview

The `common.py` module is part of the `/workspaces/documentation-generator/target_code/pilot/` directory and serves as a configuration file containing constants that are used throughout the project. It defines several lists and dictionaries that categorize application types, roles, steps in the development process, and file paths to ignore during certain operations, such as documentation generation or file system analysis.

## Constants

### `APP_TYPES`

- **Type**: `List[str]`
- **Description**: This list defines the different types of applications that the project may involve. It is used to categorize applications into one of the predefined types.
- **Values**:
  - `'Web App'`
  - `'Script'`
  - `'Mobile App'`
  - `'Chrome Extension'`

### `ROLES`

- **Type**: `Dict[str, List[str]]`
- **Description**: This dictionary maps roles within the project team to a list of responsibilities or tasks associated with each role. It is used to define what each role is expected to contribute to the project.
- **Keys and Values**:
  - `'product_owner'`: Responsible for `'project_description'`, `'user_stories'`, `'user_tasks'`.
  - `'architect'`: Responsible for `'architecture'`.
  - `'tech_lead'`: Responsible for `'development_planning'`.
  - `'full_stack_developer'`: Responsible for `'coding'`.
  - `'dev_ops'`: Responsible for `'environment_setup'`.
  - `'code_monkey'`: Responsible for `'coding'`.

### `STEPS`

- **Type**: `List[str]`
- **Description**: This list defines the sequential steps typically followed in the development process of the project. It is used to track the progress of the project from inception to completion.
- **Values**:
  - `'project_description'`
  - `'user_stories'`
  - `'user_tasks'`
  - `'architecture'`
  - `'environment_setup'`
  - `'development_planning'`
  - `'coding'`
  - `'finished'`

### `DEFAULT_IGNORE_PATHS`

- **Type**: `List[str]`
- **Description**: This list contains default file and directory paths that should be ignored by the project's tools, such as documentation generators or file system analyzers. It is used to prevent unnecessary processing of files that are not relevant to the project's core functionality.
- **Values**: Paths such as `.git`, `.idea`, `node_modules`, and file patterns like `*.min.js`.

### `IGNORE_PATHS`

- **Type**: `List[str]`
- **Description**: This list extends `DEFAULT_IGNORE_PATHS` with additional paths to ignore, which are retrieved from the `IGNORE_PATHS` environment variable. It allows for dynamic exclusion of files and directories based on the project's environment.
- **Values**: A combination of `DEFAULT_IGNORE_PATHS` and any additional paths specified in the `IGNORE_PATHS` environment variable, split by commas.

### `IGNORE_SIZE_THRESHOLD`

- **Type**: `int`
- **Description**: This integer value defines the file size threshold (in bytes) above which files are ignored by default. It is used to exclude large files that may be cumbersome to process and are likely not essential to the project's core operations.
- **Value**: `50000` (50 KB)

### `PROMPT_DATA_TO_IGNORE`

- **Type**: `Set[str]`
- **Description**: This set contains keys representing data that should be ignored when prompting for information. It is used to filter out non-essential data that should not be included in prompts or documentation.
- **Values**: `'directory_tree'`, `'name'`

## Usage

The constants defined in the `common.py` module are used throughout the project to maintain consistency and to provide a centralized location for configuration settings. For example:

- `APP_TYPES` could be used in a user interface to allow users to select the type of application they are working on.
- `ROLES` might be referenced to determine the tasks assigned to each team member based on their role.
- `STEPS` could be used to visualize the progress of the project in a dashboard or to enforce a workflow.
- `IGNORE_PATHS` and `DEFAULT_IGNORE_PATHS` are likely used by file scanning utilities to filter out files and directories that should not be included in analyses or documentation.
- `IGNORE_SIZE_THRESHOLD` could be used by a script to skip processing of files that exceed the size limit.
- `PROMPT_DATA_TO_IGNORE` might be used by a command-line tool to decide which pieces of information to exclude from user prompts.

The constants in this module provide a foundation for various functionalities within the project, ensuring that all components adhere to the same standards and configurations.
```