```markdown
# MongoDB Class

## Overview
The `MongoDB` class is a subclass of the `DB` class and provides an interface for interacting with a MongoDB database. It encapsulates the logic for connecting to the database and performing CRUD operations on collections within the database.

## Attributes
- `client`: An instance of `MongoClient` that represents the connection to the MongoDB server.

## Constructor
- `__init__(self, system: System)`: Initializes a new instance of the `MongoDB` class.
  - `system`: An instance of the `System` class from the `dataherald.config` module, which contains the application's configuration settings.
  - The constructor retrieves the MongoDB URI (`db_uri`) and database name (`db_name`) from the system settings and establishes a connection to the specified database, which is timezone-aware.

## Methods

### find_one
- `find_one(self, collection: str, query: dict) -> dict`: Retrieves a single document from the specified collection that matches the given query.
  - `collection`: The name of the collection to query.
  - `query`: A dictionary representing the query to be executed.
  - Returns a dictionary representing the found document or `None` if no document matches the query.

### insert_one
- `insert_one(self, collection: str, obj: dict) -> int`: Inserts a new document into the specified collection.
  - `collection`: The name of the collection where the document will be inserted.
  - `obj`: A dictionary representing the document to be inserted.
  - Returns the `ObjectId` of the inserted document.

### rename
- `rename(self, old_collection_name: str, new_collection_name) -> None`: Renames an existing collection.
  - `old_collection_name`: The current name of the collection.
  - `new_collection_name`: The new name for the collection.
  - This method does not return any value.

### rename_field
- `rename_field(self, collection_name: str, old_field_name: str, new_field_name: str) -> None`: Renames a field within all documents in the specified collection.
  - `collection_name`: The name of the collection containing the documents.
  - `old_field_name`: The current name of the field to be renamed.
  - `new_field_name`: The new name for the field.
  - This method does not return any value.

### update_or_create
- `update_or_create(self, collection: str, query: dict, obj: dict) -> int`: Updates an existing document or creates a new one if it does not exist.
  - `collection`: The name of the collection to be updated.
  - `query`: A dictionary representing the query to find the document.
  - `obj`: A dictionary representing the updated fields or the new document to be inserted.
  - If the document exists, it is updated with the provided fields (excluding `created_at` if present), and the method returns the `ObjectId` of the updated document.
  - If the document does not exist, a new document is inserted, and the method returns the `ObjectId` of the new document.

### find_by_id
- `find_by_id(self, collection: str, id: str) -> dict`: Retrieves a document by its `ObjectId`.
  - `collection`: The name of the collection to query.
  - `id`: The string representation of the document's `ObjectId`.
  - Returns a dictionary representing the found document or `None` if no document matches the `ObjectId`.

### find
- `find(self, collection: str, query: dict, sort: list = None, page: int = 0, limit: int = 0) -> list`: Retrieves a list of documents that match the given query, with optional sorting and pagination.
  - `collection`: The name of the collection to query.
  - `query`: A dictionary representing the query to be executed.
  - `sort`: An optional list of sorting tuples (field, direction).
  - `page`: The page number for pagination (1-indexed).
  - `limit`: The number of documents per page.
  - Returns a list of dictionaries representing the found documents.

### find_all
- `find_all(self, collection: str, page: int = 0, limit: int = 0) -> list`: Retrieves all documents from the specified collection, with optional pagination.
  - `collection`: The name of the collection to query.
  - `page`: The page number for pagination (1-indexed).
  - `limit`: The number of documents per page.
  - Returns a list of dictionaries representing the found documents.

### delete_by_id
- `delete_by_id(self, collection: str, id: str) -> int`: Deletes a document from the specified collection by its `ObjectId`.
  - `collection`: The name of the collection from which the document will be deleted.
  - `id`: The string representation of the document's `ObjectId`.
  - Returns the count of deleted documents (0 or 1).

## Usage
The `MongoDB` class is used within the project to interact with MongoDB collections. It provides a consistent interface for database operations, abstracting the details of the MongoDB API. This class is typically instantiated with the system configuration and then used to perform database operations throughout the project.
```