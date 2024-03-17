```markdown
# `prompts.py` Module Documentation

## Overview

The `prompts.py` module is part of the `dataherald` package, specifically within the `services` subpackage. It defines the `PromptService` class, which provides an interface for creating, retrieving, and updating prompts in the context of a data reporting or data heralding application.

## Dependencies

- `dataherald.api.types.requests.PromptRequest`: A class representing a request to create a new prompt.
- `dataherald.repositories.database_connections.DatabaseConnectionNotFoundError`: An exception class for handling cases where a database connection is not found.
- `dataherald.repositories.database_connections.DatabaseConnectionRepository`: A repository class for managing database connections.
- `dataherald.repositories.prompts.PromptNotFoundError`: An exception class for handling cases where a prompt is not found.
- `dataherald.repositories.prompts.PromptRepository`: A repository class for managing prompts.
- `dataherald.types.Prompt`: A class representing a prompt entity.

## `PromptService` Class

### Attributes

- `storage`: An instance of a storage mechanism (e.g., a database session or connection) that is passed to the repository classes for data persistence operations.
- `prompt_repository`: An instance of `PromptRepository` initialized with the `storage` attribute for managing prompt entities.

### Methods

#### `__init__(self, storage)`

The constructor initializes the `PromptService` instance with the provided `storage` mechanism and sets up the `prompt_repository` attribute.

#### `create(self, prompt_request: PromptRequest) -> Prompt`

Creates a new prompt based on the provided `PromptRequest` object.

- Parameters:
  - `prompt_request`: An instance of `PromptRequest` containing the necessary data to create a new prompt.
- Returns:
  - A `Prompt` object representing the newly created prompt.
- Raises:
  - `DatabaseConnectionNotFoundError`: If the database connection specified in the `prompt_request` does not exist.
- Process:
  1. Initializes a `DatabaseConnectionRepository` with the current `storage`.
  2. Attempts to find the database connection using the `db_connection_id` from the `prompt_request`.
  3. If the database connection is not found, raises `DatabaseConnectionNotFoundError`.
  4. Creates a new `Prompt` object with the text, database connection ID, and metadata from the `prompt_request`.
  5. Inserts the new prompt into the repository and returns the resulting `Prompt` object.

#### `get(self, query) -> list[Prompt]`

Retrieves a list of prompts based on a given query.

- Parameters:
  - `query`: A query object or parameters used to filter the prompts to be retrieved.
- Returns:
  - A list of `Prompt` objects that match the query.

#### `update_metadata(self, prompt_id, metadata_request) -> Prompt`

Updates the metadata of an existing prompt.

- Parameters:
  - `prompt_id`: The unique identifier of the prompt to be updated.
  - `metadata_request`: An object containing the new metadata to be applied to the prompt.
- Returns:
  - The updated `Prompt` object.
- Raises:
  - `PromptNotFoundError`: If the prompt with the given `prompt_id` does not exist.
- Process:
  1. Finds the prompt by its `prompt_id` using the `prompt_repository`.
  2. If the prompt is not found, raises `PromptNotFoundError`.
  3. Updates the prompt's metadata with the new metadata from `metadata_request`.
  4. Saves the updated prompt using the `prompt_repository` and returns the updated `Prompt` object.

## Usage

The `PromptService` class is used within the `dataherald` project to manage the lifecycle of prompts, which are likely user-defined queries or messages associated with specific database connections. The service allows for the creation of new prompts, retrieval of existing prompts, and updating of prompt metadata, ensuring that the prompts are correctly linked to valid database connections and that their information is up-to-date.
```
