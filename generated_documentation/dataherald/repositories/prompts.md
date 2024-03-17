```markdown
# `prompts.py` Module Documentation

## Overview

The `prompts.py` module defines a `PromptRepository` class that provides an abstraction layer for interacting with a database collection named `prompts`. This class is responsible for performing CRUD (Create, Read, Update, Delete) operations on `Prompt` objects within the database. The module also defines a custom exception `PromptNotFoundError` for handling cases where a prompt is not found in the database.

## Dependencies

- `bson.objectid`: Used for handling MongoDB ObjectIds.
- `dataherald.types`: Contains the `Prompt` class definition which is a data type used throughout this module.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the database collection used by the `PromptRepository` class.

## Classes

### `PromptNotFoundError`

A custom exception class that inherits from Python's base `Exception` class. This exception is raised when a prompt cannot be found in the database.

### `PromptRepository`

A repository class that provides methods to interact with the `prompts` collection in the database.

#### Attributes

- `storage`: An instance of a storage class that provides low-level database operations. It is expected to have methods like `insert_one`, `find_one`, `find`, and `update_or_create`.

#### Methods

##### `__init__(self, storage)`

The constructor for the `PromptRepository` class.

- Parameters:
  - `storage`: An instance of a storage class that will be used to perform database operations.

##### `insert(self, prompt: Prompt) -> Prompt`

Inserts a new `Prompt` object into the database.

- Parameters:
  - `prompt`: An instance of the `Prompt` class to be inserted into the database.
- Returns:
  - The `Prompt` instance with its `id` attribute set to the newly created ObjectId in string format.

##### `find_one(self, query: dict) -> Prompt | None`

Finds a single `Prompt` object in the database that matches the given query.

- Parameters:
  - `query`: A dictionary representing the query to be used for finding a prompt.
- Returns:
  - A `Prompt` instance if a matching document is found, otherwise `None`.

##### `find_by_id(self, id: str) -> Prompt | None`

Finds a single `Prompt` object in the database by its ObjectId.

- Parameters:
  - `id`: A string representation of the ObjectId of the prompt to be found.
- Returns:
  - A `Prompt` instance if a matching document is found, otherwise `None`.

##### `find_by(self, query: dict, page: int = 0, limit: int = 0) -> list[Prompt]`

Finds all `Prompt` objects that match the given query, with optional pagination.

- Parameters:
  - `query`: A dictionary representing the query to be used for finding prompts.
  - `page`: An integer representing the page number for pagination (optional).
  - `limit`: An integer representing the number of items per page for pagination (optional).
- Returns:
  - A list of `Prompt` instances that match the query.

##### `update(self, prompt: Prompt) -> Prompt`

Updates an existing `Prompt` object in the database.

- Parameters:
  - `prompt`: An instance of the `Prompt` class with updated values.
- Returns:
  - The `Prompt` instance that was updated.

## Usage

The `PromptRepository` class is used to manage `Prompt` objects in a MongoDB database. It provides a high-level interface for other parts of the project to perform database operations without needing to directly interact with the database or write raw queries. The class methods handle the conversion between `Prompt` instances and their dictionary representations suitable for database storage, as well as the translation of MongoDB ObjectIds to and from string format.
```
