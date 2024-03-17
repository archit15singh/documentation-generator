```markdown
# SQLGenerationRepository Class

## Overview

The `SQLGenerationRepository` class is a data access layer designed to interact with a database collection named `sql_generations`. It provides methods to insert, update, and retrieve `SQLGeneration` objects from the database. The class requires a `storage` object that handles the actual database operations.

## Attributes

- `storage`: An instance of a storage class that provides methods for interacting with the database.

## Methods

### `__init__(self, storage)`

The constructor initializes the `SQLGenerationRepository` with a given `storage` object.

#### Parameters

- `storage`: An object that provides the interface for database operations.

### `insert(self, sql_generation: SQLGeneration) -> SQLGeneration`

Inserts a new `SQLGeneration` object into the database.

#### Parameters

- `sql_generation`: An instance of `SQLGeneration` to be inserted into the database.

#### Returns

- The `SQLGeneration` object with its `id` attribute set to the newly created database entry's ID.

#### Process

1. Converts the `SQLGeneration` object to a dictionary, excluding the `id` field.
2. Converts the `prompt_id` attribute to a string.
3. Inserts the dictionary into the database using the `storage` object's `insert_one` method.
4. Sets the `id` attribute of the `SQLGeneration` object to the string representation of the inserted ID.
5. Returns the updated `SQLGeneration` object.

### `update(self, sql_generation: SQLGeneration) -> SQLGeneration`

Updates an existing `SQLGeneration` object in the database.

#### Parameters

- `sql_generation`: An instance of `SQLGeneration` to be updated in the database.

#### Returns

- The `SQLGeneration` object after the update operation.

#### Process

1. Converts the `SQLGeneration` object to a dictionary, excluding the `id` field.
2. Converts the `prompt_id` attribute to a string.
3. Updates the database entry identified by the `id` of the `SQLGeneration` object using the `storage` object's `update_or_create` method.
4. Returns the `SQLGeneration` object.

### `find_one(self, query: dict) -> SQLGeneration | None`

Finds a single `SQLGeneration` object in the database that matches the given query.

#### Parameters

- `query`: A dictionary representing the query to be used for finding the object.

#### Returns

- An instance of `SQLGeneration` if found, otherwise `None`.

#### Process

1. Uses the `storage` object's `find_one` method to retrieve a single document from the database that matches the query.
2. If a document is found, converts the `_id` field to a string and assigns it to the `id` attribute.
3. Returns an instance of `SQLGeneration` created from the retrieved document.

### `find_by_id(self, id: str) -> SQLGeneration | None`

Finds a `SQLGeneration` object in the database by its ID.

#### Parameters

- `id`: A string representing the ID of the `SQLGeneration` object to be retrieved.

#### Returns

- An instance of `SQLGeneration` if found, otherwise `None`.

#### Process

1. Uses the `storage` object's `find_one` method to retrieve a document from the database by its `_id`.
2. If a document is found, converts the `_id` field to a string and assigns it to the `id` attribute.
3. Returns an instance of `SQLGeneration` created from the retrieved document.

### `find_by(self, query: dict, page: int = 0, limit: int = 0) -> list[SQLGeneration]`

Finds a list of `SQLGeneration` objects in the database that match the given query, with optional pagination.

#### Parameters

- `query`: A dictionary representing the query to be used for finding the objects.
- `page`: An integer representing the page number for pagination (optional).
- `limit`: An integer representing the number of items per page for pagination (optional).

#### Returns

- A list of `SQLGeneration` instances that match the query.

#### Process

1. If both `page` and `limit` are greater than 0, uses the `storage` object's `find` method with pagination to retrieve documents from the database.
2. If pagination is not used, retrieves all documents that match the query.
3. Iterates over the retrieved documents, converts the `_id` field to a string, and assigns it to the `id` attribute.
4. Creates instances of `SQLGeneration` from the retrieved documents and appends them to a result list.
5. Returns the list of `SQLGeneration` instances.

## Exceptions

### `SQLGenerationNotFoundError`

A custom exception class that is raised when a `SQLGeneration` object is not found in the database.

## Constants

- `DB_COLLECTION`: A string representing the name of the database collection used by the repository (`"sql_generations"`).
```
