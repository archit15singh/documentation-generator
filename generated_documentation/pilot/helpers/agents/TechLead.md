```markdown
# TechLead Class

## Overview
The `TechLead` class is a subclass of `Agent` that specializes in creating development plans and feature plans for a software project. It is designed to interact with a conversational AI to generate these plans based on the project's requirements and existing architecture.

## Attributes
- `save_dev_steps` (bool): A flag to determine whether to save development steps.
- `convo_feature_plan` (AgentConvo): An instance of `AgentConvo` to handle conversations related to feature planning.
- `convo_development_plan` (AgentConvo): An instance of `AgentConvo` to handle conversations related to development planning.
- `convo_feature_summary` (AgentConvo): An instance of `AgentConvo` to handle conversations related to feature summary creation.

## Methods

### `__init__(self, project)`
Constructor for the `TechLead` class.
- Initializes the superclass `Agent` with the role 'tech_lead' and the provided project.
- Sets `save_dev_steps` to `False`.
- Initializes `convo_feature_plan` with an instance of `AgentConvo`.

### `create_development_plan(self)`
Creates a development plan for the project.
- Sets the current step of the project to `DEVELOPMENT_PLANNING_STEP`.
- Checks if the development planning step has already been completed for the given `app_id`. If so, it retrieves the data from the database and does not prompt the user again.
- Applies a project template to the existing project summary.
- Logs and prints the start of the development planning process.
- Sends a message to the conversational AI with the project details and receives a development plan in response.
- Logs the creation of the development plan.
- Saves the development plan progress to the database.

### `create_feature_plan(self, feature_description)`
Creates a feature plan for a specific feature within the project.
- Sets `save_dev_steps` to `True`.
- Retrieves previous features for the given `app_id` from the database.
- Sends a message to the conversational AI with the project details, including the feature description, and receives a feature plan in response.
- Logs the creation of the feature development plan.

### `create_feature_summary(self, feature_description)`
Creates a summary for a new feature within the project.
- Sets `save_dev_steps` to `True`.
- Sends a message to the conversational AI with the project details, including the feature description, and receives a feature summary in response.
- Saves the feature summary to the project instance.
- If `skip_steps` is not enabled, saves the feature summary to the database.
- Logs the creation of the feature summary.

## Usage
The `TechLead` class is used within a project to generate and manage development plans and feature plans. It interacts with a conversational AI to automate the planning process based on the project's specifications and existing work. The class methods are typically called by other parts of the project to initiate the planning for the entire project or for specific features.

## Dependencies
- `utils.utils`: Contains utility functions like `step_already_finished`, `should_execute_step`, and `generate_app_data`.
- `helpers.Agent`: The base class for `TechLead`.
- `utils.style`: Provides styling functions like `color_green_bold`.
- `helpers.AgentConvo`: Used to handle conversations with the AI.
- `database.database`: Contains functions to interact with the database, such as `save_progress`, `get_progress_steps`, `save_feature`, and `get_features_by_app_id`.
- `logger.logger`: Used for logging information.
- `const.function_calls`: Contains constants for function calls, such as `DEVELOPMENT_PLAN`.
- `templates`: Used to apply project templates.
- `utils.exit`: Contains functions like `trace_code_event`.

## Constants
- `DEVELOPMENT_PLANNING_STEP`: A constant representing the development planning step within the project workflow.
```