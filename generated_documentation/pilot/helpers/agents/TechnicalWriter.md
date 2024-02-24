```markdown
# TechnicalWriter Class

## Overview

The `TechnicalWriter` class is a subclass of `Agent` and is responsible for generating documentation for a software project. It is designed to be used at certain milestones within the project to create a comprehensive set of documents that describe the project's structure, codebase, and usage.

## Attributes

- `save_dev_steps` (bool): A flag indicating whether to save the development steps or not.

## Methods

### `__init__(self, project)`

The constructor for the `TechnicalWriter` class.

#### Parameters

- `project` (Project): An instance of the `Project` class representing the current project that the `TechnicalWriter` will document.

#### Behavior

- Initializes the `TechnicalWriter` instance by calling the superclass constructor with the name `'technical_writer'` and the provided `project` instance.
- Sets the `save_dev_steps` attribute to `True`.

### `document_project(self, percent)`

Generates documentation for the project when a certain percentage of the project generation is reached.

#### Parameters

- `percent` (int): The percentage of project completion at which documentation should be generated.

#### Behavior

- Retrieves all coded files in the project using `self.project.get_all_coded_files()`.
- Prints a congratulatory message indicating the percentage of project completion.
- Prints the number of files and lines of code in the project.
- Informs the user that GPT Pilot will now create documentation for the project.
- Calls `self.create_license()` to create a LICENSE file if it does not exist.
- Calls `self.create_readme()` to create a README.md file for the project.
- Calls `self.create_api_documentation()` to create API documentation (method currently has no implementation).

### `create_license(self)`

Checks if a LICENSE file exists and creates one if it does not. The method is currently not implemented.

#### Behavior

- Placeholder for future implementation.

### `create_readme(self)`

Generates a README.md file for the project.

#### Behavior

- Prints a message indicating that README.md is being created.
- Creates an instance of `AgentConvo` with `self` as the parameter.
- Sends a message to the conversation agent with the prompt 'documentation/create_readme.prompt' and a dictionary containing project details such as name, app type, summary, user stories, tasks, directory tree, and files.
- The response from the conversation agent (`llm_response`) is expected to be the content for the README.md file.
- Saves the content to the project using `self.project.save_file(llm_response)`.
- Returns the `AgentConvo` instance.

### `create_api_documentation(self)`

Placeholder method for creating API documentation. The method is currently not implemented.

#### Behavior

- Placeholder for future implementation.

## Usage

The `TechnicalWriter` class is instantiated with a `Project` object and is used to generate documentation at specific milestones of the project. The `document_project` method is called with the completion percentage to trigger the documentation generation process. The `create_readme` method is used to generate a README.md file, which is a critical component of project documentation, providing an overview and instructions for the project.

## Dependencies

- `const.function_calls`: Contains constants for function calls, including `GET_DOCUMENTATION_FILE`.
- `helpers.AgentConvo`: Provides a conversational interface for generating documentation content.
- `helpers.Agent`: The superclass for `TechnicalWriter`.
- `utils.files`: Contains utility functions for file operations, including `count_lines_of_code`.
- `utils.style`: Contains utility functions for styling terminal output, including `color_green_bold` and `color_green`.

## Notes

- The `create_license` and `create_api_documentation` methods are placeholders and do not have an implementation in the provided code snippet.
- The `document_project` method assumes that the project has methods for retrieving all coded files, getting a directory tree, and saving files, which are not shown in the provided code snippet.
- The `create_readme` method relies on an external conversation agent to generate the content of the README.md file, which suggests that the project may be using AI or machine learning models to assist in documentation creation.
```