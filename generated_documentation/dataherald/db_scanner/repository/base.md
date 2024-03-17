```markdown
# TableDescriptionRepository

## Overview

`TableDescriptionRepository` is a Python class that provides an interface for interacting with a MongoDB collection that stores metadata about database tables. The class is designed to abstract the underlying database operations and provide a set of methods to perform CRUD operations on `TableDescription` objects.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the MongoDB collection that stores the table descriptions.

## Exceptions

- `InvalidColumnNameError`: A custom exception class that is raised when an operation is attempted on a column name that does not exist in the table description.

## Class Definition

### `__init__(self, storage)`

Constructor for the `TableDescriptionRepository` class.

#### Parameters

- `storage`: An instance of a storage class that provides methods for interacting with the MongoDB database.

### `find_by_id(self, id: str) -> TableDescription | None`

Retrieves a `TableDescription` object by its MongoDB ObjectId.

#### Parameters

- `id`: A string representation of the MongoDB ObjectId.

#### Returns

- A `TableDescription` object if found, otherwise `None`.

### `get_table_info(self, db_connection_id: str, table_name: str) -> TableDescription | None`

Retrieves a `TableDescription` object by database connection ID and table name.

#### Parameters

- `db_connection_id`: A string representing the database connection ID.
- `table_name`: A string representing the name of the table.

#### Returns

- A `TableDescription` object if found, otherwise `None`.

### `get_all_tables_by_db(self, query: dict) -> List[TableDescription]`

Retrieves all `TableDescription` objects that match a given query.

#### Parameters

- `query`: A dictionary representing the query to filter the table descriptions.

#### Returns

- A list of `TableDescription` objects.

### `save_table_info(self, table_info: TableDescription) -> TableDescription`

Saves or updates a `TableDescription` object in the database.

#### Parameters

- `table_info`: A `TableDescription` object to be saved or updated.

#### Returns

- The `TableDescription` object with its ID updated to reflect the saved record.

### `update(self, table_info: TableDescription) -> TableDescription`

Updates an existing `TableDescription` object in the database.

#### Parameters

- `table_info`: A `TableDescription` object to be updated.

#### Returns

- The updated `TableDescription` object.

### `find_all(self) -> list[TableDescription]`

Retrieves all `TableDescription` objects from the database.

#### Returns

- A list of all `TableDescription` objects.

### `find_by(self, query: dict) -> list[TableDescription]`

Retrieves all `TableDescription` objects that match a given query and sorts them by table name.

#### Parameters

- `query`: A dictionary representing the query to filter the table descriptions.

#### Returns

- A sorted list of `TableDescription` objects.

### `update_fields(self, table: TableDescription, table_description_request)`

Updates specific fields of a `TableDescription` object based on a request.

#### Parameters

- `table`: The `TableDescription` object to be updated.
- `table_description_request`: An object containing the fields to be updated.

#### Returns

- The updated `TableDescription` object.

#### Raises

- `InvalidColumnNameError`: If a column name provided in the request does not exist in the table description.

## Usage

The `TableDescriptionRepository` class is used to manage table metadata within a project that requires storing and retrieving information about database tables. It is typically used by services or components that need to access or modify this metadata, such as a database schema management tool or a data cataloging system.

The class methods allow for:

- Finding a table description by its ID or by a combination of database connection ID and table name.
- Retrieving all table descriptions for a specific database or based on a query.
- Saving new or updating existing table descriptions.
- Updating specific fields of a table description, with validation to ensure column names exist.

The repository ensures that all interactions with the `table_descriptions` collection are performed through a consistent interface, abstracting the details of the MongoDB operations from the rest of the application.
```