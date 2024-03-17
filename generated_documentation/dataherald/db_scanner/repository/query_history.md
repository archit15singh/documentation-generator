```markdown
# QueryHistoryRepository Class

## Overview

The `QueryHistoryRepository` class is a data access layer component designed to interact with a storage system that contains a collection of query history records. It provides an abstraction over the underlying database operations, specifically tailored to handle `QueryHistory` model instances.

## Attributes

- `storage`: An instance of a storage class that provides methods for database operations such as `insert_one` and `find`.

## Methods

### `__init__(self, storage)`

The constructor initializes a new instance of the `QueryHistoryRepository` class.

#### Parameters

- `storage`: An object that provides the necessary methods to interact with the database.

#### Description

- The `storage` parameter is stored as an instance attribute for later use in other methods.

### `insert(self, query_history: QueryHistory) -> QueryHistory`

Inserts a new `QueryHistory` record into the database.

#### Parameters

- `query_history`: An instance of the `QueryHistory` model representing the query history data to be inserted.

#### Returns

- Returns the `QueryHistory` instance with its `id` attribute set to the identifier assigned by the database.

#### Description

- Converts the `QueryHistory` instance to a dictionary, excluding the `id` field.
- Explicitly converts the `db_connection_id` to a string and adds it to the dictionary.
- Inserts the dictionary into the database collection specified by `DB_COLLECTION`.
- Retrieves the inserted document's identifier, converts it to a string, and assigns it to the `id` attribute of the `QueryHistory` instance.
- Returns the updated `QueryHistory` instance.

### `find_by(self, query: dict, page: int = 1, limit: int = 10) -> list[QueryHistory]`

Retrieves a list of `QueryHistory` records from the database based on a query filter.

#### Parameters

- `query`: A dictionary representing the filter criteria for the query.
- `page`: An integer representing the page number for pagination (default is 1).
- `limit`: An integer representing the number of records to return per page (default is 10).

#### Returns

- Returns a list of `QueryHistory` instances that match the query filter.

#### Description

- Uses the `storage` instance to perform a `find` operation on the `DB_COLLECTION` with the provided `query`, `page`, and `limit` parameters.
- Iterates over the returned rows from the database.
- For each row, converts the `_id` field to a string and assigns it to the `id` attribute.
- Converts the `db_connection_id` to a string.
- Creates a new `QueryHistory` instance using the row data and appends it to the result list.
- Returns the list of `QueryHistory` instances.

## Usage

The `QueryHistoryRepository` class is used to interact with the `query_history` collection in the database. It provides methods to insert new records and retrieve existing records based on specific criteria. This class is typically used by services or controllers that require access to query history data within the application.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the database collection that stores query history records. Its value is `"query_history"`.

## Dependencies

- `dataherald.db_scanner.models.types.QueryHistory`: The `QueryHistory` class is a model that represents the structure of a query history record. It is used as the data type for the records handled by the `QueryHistoryRepository`.

## Notes

- The `storage` instance is expected to provide `insert_one` and `find` methods that are compatible with the repository's usage.
- The `QueryHistory` model should have a `dict` method that allows conversion to a dictionary and an `id` attribute that can be set after insertion.
- The `find_by` method assumes that the `storage` instance's `find` method supports pagination through `page` and `limit` parameters.
- The `insert` and `find_by` methods handle the conversion of MongoDB's ObjectId to a string for the `id` field, ensuring compatibility with the `QueryHistory` model.
```