```markdown
# TestVectorStore Class

## Overview

The `TestVectorStore` class is a subclass of `VectorStore` that is designed for testing purposes within the `dataherald` project. It provides a mock implementation of the `VectorStore` interface, allowing for the simulation of vector storage operations without the need for a live database connection or actual data persistence.

## Class Definition

### Constructor

```python
def __init__(self, system: System):
    super().__init__(system)
```

#### Parameters

- `system`: An instance of the `System` class from the `dataherald.config` module, which contains configuration settings for the system.

#### Description

The constructor initializes the `TestVectorStore` instance by calling the constructor of the parent `VectorStore` class with the provided `system` configuration.

### Methods

#### query

```python
@override
def query(
    self,
    query_texts: List[str],
    db_connection_id: str,
    collection: str,
    num_results: int,
) -> list:
    return [{"id": "64ade8ed3445882cedc06ab6", "score": 0.1}]
```

##### Parameters

- `query_texts`: A list of strings representing the query texts to be used for retrieving vectors.
- `db_connection_id`: A string identifier for the database connection.
- `collection`: The name of the collection from which to retrieve vectors.
- `num_results`: The number of results to return.

##### Returns

- A list of dictionaries, each representing a mock vector record. In this mock implementation, it always returns a single record with a fixed `id` and `score`.

##### Description

The `query` method is a mock implementation that simulates the retrieval of vector records from a vector store. It ignores the input parameters and returns a predefined list of results.

#### add_record

```python
@override
def add_record(
    self,
    documents: str,
    db_connection_id: str,
    collection: str,
    metadata: Any,
    ids: List,
):
    pass
```

##### Parameters

- `documents`: A string representing the documents to be added to the vector store.
- `db_connection_id`: A string identifier for the database connection.
- `collection`: The name of the collection to which the documents will be added.
- `metadata`: Additional metadata associated with the documents.
- `ids`: A list of identifiers for the documents.

##### Description

The `add_record` method is a mock implementation that simulates the addition of vector records to a vector store. It performs no operation and is used for testing purposes.

#### delete_record

```python
@override
def delete_record(self, collection: str, id: str):
    pass
```

##### Parameters

- `collection`: The name of the collection from which the record will be deleted.
- `id`: The identifier of the record to be deleted.

##### Description

The `delete_record` method is a mock implementation that simulates the deletion of a vector record from a vector store. It performs no operation and is used for testing purposes.

#### delete_collection

```python
@override
def delete_collection(self, collection: str):
    pass
```

##### Parameters

- `collection`: The name of the collection to be deleted.

##### Description

The `delete_collection` method is a mock implementation that simulates the deletion of an entire collection from a vector store. It performs no operation and is used for testing purposes.

#### create_collection

```python
@override
def create_collection(self, collection: str):
    pass
```

##### Parameters

- `collection`: The name of the collection to be created.

##### Description

The `create_collection` method is a mock implementation that simulates the creation of a new collection in a vector store. It performs no operation and is used for testing purposes.

## Usage

The `TestVectorStore` class is used in test cases to simulate interactions with a `VectorStore` without the need for an actual database. It allows developers to test the behavior of their code in a controlled environment where the outcomes of vector store operations are predictable and do not have side effects on a real database.
```
