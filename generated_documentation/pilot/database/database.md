```markdown
# Database Module Technical Documentation

## Overview

The `database.py` module is part of a larger project that involves managing a database for storing various entities related to a software development process. It provides a set of functions to interact with the database, including creating and retrieving records for apps, users, development steps, and more. The module uses the Peewee ORM for database interactions and supports both PostgreSQL and SQLite databases.

## Dependencies

- `playhouse.shortcuts`: Provides utility functions for Peewee ORM.
- `utils.style`: Contains functions for coloring terminal output.
- `peewee`: The ORM used for database interactions.
- `functools`: Provides higher-order functions and operations on callable objects.
- `operator`: Exports a set of efficient functions corresponding to the intrinsic operators of Python.
- `database.config`: Contains configuration variables for the database connection.
- `const.common`: Contains common constants used throughout the project.
- `logger.logger`: Provides logging functionality.
- `database.models.*`: Contains the Peewee model definitions for the various entities in the database.

## Configuration

The database configuration is imported from `database.config`, which should define the following variables:

- `DB_NAME`
- `DB_HOST`
- `DB_PORT`
- `DB_USER`
- `DB_PASSWORD`
- `DATABASE_TYPE`

Depending on the `DATABASE_TYPE`, the module will import the necessary libraries for PostgreSQL or use the default SQLite.

## Models

The module defines a list of table models that represent the entities in the database. These models are defined in separate modules within the `database.models` package and are imported at the top of the `database.py` module.

## Functions

### `get_created_apps()`

Retrieves a list of apps that have been created, filtering out any apps that do not have a name or status.

### `get_created_apps_with_steps()`

Retrieves a list of created apps along with their associated steps and development steps. It also formats the app IDs as strings and filters out unnecessary fields from the development steps.

### `get_all_app_development_steps(app_id, last_step=None)`

Retrieves all development steps for a given app, optionally up to a specified last step.

### `save_user(user_id, email, password)`

Creates a new user or retrieves an existing user based on the provided user ID or email.

### `update_app_status(app_id, new_status)`

Updates the status of an app with the given app ID.

### `get_user(user_id=None, email=None)`

Retrieves a user by user ID or email, raising a `ValueError` if the user is not found.

### `save_app(project)`

Creates or updates an app record based on the provided project data.

### `save_user_app(user_id, app_id, workspace)`

Creates or updates a user app record associating a user with an app and workspace.

### `save_progress(app_id, step, data)`

Saves progress for a given app and step, creating or updating the corresponding record in the database.

### `get_app(app_id, error_if_not_found=True)`

Retrieves an app by its ID, optionally raising an error if the app is not found.

### `get_app_by_user_workspace(user_id, workspace)`

Retrieves an app associated with a user and workspace.

### `get_progress_steps(app_id, step=None)`

Retrieves progress records for a given app, optionally filtered by a specific step.

### `get_db_model_from_hash_id(model, app_id, previous_step, high_level_step)`

Retrieves a database row based on a composite key of app ID, previous step, and high level step.

### `hash_and_save_step(Model, app_id, unique_data_fields, data_fields, message)`

Creates a new record in the database for a given model, ensuring uniqueness based on specified fields.

### `save_development_step(project, prompt_path, prompt_data, messages, llm_response, exception=None)`

Saves a development step record associated with a project.

### `save_command_run(project, command, cli_response, done_or_error_response, exit_code)`

Saves a command run record associated with a project.

### `save_user_input(project, query, user_input, hint)`

Saves a user input record associated with a project.

### `delete_all_subsequent_steps(project)`

Deletes all subsequent steps in the development process after a specified checkpoint.

### `delete_subsequent_steps(Model, app, step)`

Deletes subsequent steps for a given model, app, and step.

### `get_all_connected_steps(step, previous_step_field_name)`

Recursively retrieves all steps connected to a given step.

### `delete_all_app_development_data(app)`

Deletes all development data associated with an app.

### `delete_unconnected_steps_from(step, previous_step_field_name)`

Deletes unconnected steps from a given step.

### `save_file_description(project, path, name, description)`

Saves a file description associated with a project.

### `save_feature(app_id, summary, messages, previous_step)`

Creates a feature record associated with an app.

### `get_features_by_app_id(app_id)`

Retrieves feature records associated with an app ID.

### `create_tables()`

Creates the database tables based on the defined models.

### `drop_tables()`

Drops the database tables.

### `database_exists()`

Checks if the database exists.

### `create_database()`

Creates a new database.

### `tables_exist()`

Checks if the tables exist in the database.

## Main Execution

If the module is run as the main program, it will drop existing tables and create new ones based on the defined models.

## Usage

This module is used within the project to manage the database for storing and retrieving data related to the software development process. It provides a high-level API for other parts of the project to interact with the database without needing to write raw SQL queries.
```