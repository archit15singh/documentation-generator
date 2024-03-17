```markdown
# DB Class

The `DB` class is an abstract base class (ABC) that defines a common interface for database operations within the `dataherald` project. It inherits from the `Component` class and the `ABC` class from the `abc` module. The `DB` class is designed to be subclassed by concrete database implementations that provide specific functionality for different types of databases.

## Attributes

- `system` (System): An instance of the `System` class from the `dataherald.config` module. This attribute is intended to hold system-wide configurations and dependencies.

## Methods

### `__init__(self, system: System)`

The constructor method for the `DB` class. It initializes a new instance of a database component with the provided system configuration.

#### Parameters

- `system` (System): The system configuration object.

### `insert_one(self, collection: str, obj: dict) -> int`

An abstract method that must be implemented by subclasses to insert a single document into a specified collection.

#### Parameters

- `collection` (str): The name of the collection where the document will be inserted.
- `obj` (dict): The document to be inserted as a dictionary.

#### Returns

- `int`: The number of documents inserted.

### `rename(self, old_collection_name: str, new_collection_name: str) -> None`

An abstract method that must be implemented by subclasses to rename an existing collection.

#### Parameters

- `old_collection_name` (str): The current name of the collection.
- `new_collection_name` (str): The new name for the collection.

### `rename_field(self, collection_name: str, old_field_name: str, new_field_name: str) -> None`

An abstract method that must be implemented by subclasses to rename a field within a collection.

#### Parameters

- `collection_name` (str): The name of the collection containing the field to be renamed.
- `old_field_name` (str): The current name of the field.
- `new_field_name` (str): The new name for the field.

### `update_or_create(self, collection: str, query: dict, obj: dict) -> int`

An abstract method that must be implemented by subclasses to update an existing document or create a new one if it does not exist.

#### Parameters

- `collection` (str): The name of the collection to update or insert the document into.
- `query` (dict): The query criteria to locate the document to be updated.
- `obj` (dict): The document to be updated or inserted.

#### Returns

- `int`: The number of documents updated or inserted.

### `find_one(self, collection: str, query: dict) -> dict`

An abstract method that must be implemented by subclasses to find a single document in a collection that matches the query.

#### Parameters

- `collection` (str): The name of the collection to search.
- `query` (dict): The query criteria to locate the document.

#### Returns

- `dict`: The found document or `None` if no document matches the query.

### `find_by_id(self, collection: str, id: str) -> dict`

An abstract method that must be implemented by subclasses to find a single document by its identifier.

#### Parameters

- `collection` (str): The name of the collection to search.
- `id` (str): The identifier of the document to find.

#### Returns

- `dict`: The found document or `None` if no document matches the identifier.

### `find(self, collection: str, query: dict, sort: list = None, page: int = 0, limit: int = 0) -> list`

An abstract method that must be implemented by subclasses to find documents in a collection that match the query, with optional sorting and pagination.

#### Parameters

- `collection` (str): The name of the collection to search.
- `query` (dict): The query criteria to locate the documents.
- `sort` (list, optional): A list of tuples specifying the field(s) and direction to sort the results.
- `page` (int, optional): The page number for pagination (starting from 0).
- `limit` (int, optional): The maximum number of documents to return.

#### Returns

- `list`: A list of found documents.

### `find_all(self, collection: str, page: int = 0, limit: int = 0) -> list`

An abstract method that must be implemented by subclasses to find all documents in a collection, with optional pagination.

#### Parameters

- `collection` (str): The name of the collection to search.
- `page` (int, optional): The page number for pagination (starting from 0).
- `limit` (int, optional): The maximum number of documents to return.

#### Returns

- `list`: A list of all found documents.

### `delete_by_id(self, collection: str, id: str) -> int`

An abstract method that must be implemented by subclasses to delete a single document by its identifier.

#### Parameters

- `collection` (str): The name of the collection from which the document will be deleted.
- `id` (str): The identifier of the document to delete.

#### Returns

- `int`: The number of documents deleted.
```