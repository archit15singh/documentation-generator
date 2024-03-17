```markdown
# Scanner Class

## Overview
The `Scanner` class serves as an abstract base class for all scanner classes within the `dataherald` project. It inherits from the `Component` class and Python's built-in `ABC` (Abstract Base Class) module, indicating that it provides a template for subclasses but is not intended to be instantiated directly.

## Attributes
The `Scanner` class does not define any attributes directly. It relies on attributes defined in the `Component` class it inherits from and the abstract methods it declares.

## Methods

### `scan`
```python
@abstractmethod
def scan(
    self,
    db_engine: SQLDatabase,
    db_connection_id: str,
    table_names: list[str] | None,
    repository: TableDescriptionRepository,
    query_history_repository: QueryHistoryRepository,
) -> None:
```
- **Description**: Abstract method that must be implemented by subclasses to scan a database.
- **Parameters**:
  - `db_engine`: An instance of `SQLDatabase` that represents the database engine to be scanned.
  - `db_connection_id`: A string representing the unique identifier for the database connection.
  - `table_names`: An optional list of strings representing the names of tables to be scanned. If `None`, all tables in the database may be considered.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
  - `query_history_repository`: An instance of `QueryHistoryRepository` used to interact with the query history.
- **Returns**: None. The method is expected to perform the scanning operation and handle the results internally.

### `synchronizing`
```python
@abstractmethod
def synchronizing(
    self,
    scanner_request: ScannerRequest,
    repository: TableDescriptionRepository,
) -> list[TableDescription]:
```
- **Description**: Abstract method that must be implemented by subclasses to update the status of `table_description` based on a `ScannerRequest`.
- **Parameters**:
  - `scanner_request`: An instance of `ScannerRequest` containing the details of the scanning request.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
- **Returns**: A list of `TableDescription` instances that have been updated.

### `create_tables`
```python
@abstractmethod
def create_tables(
    self,
    tables: list[str],
    db_connection_id: str,
    repository: TableDescriptionRepository,
    metadata: dict = None,
) -> None:
```
- **Description**: Abstract method that must be implemented by subclasses to create tables in the database.
- **Parameters**:
  - `tables`: A list of strings representing the names of tables to be created.
  - `db_connection_id`: A string representing the unique identifier for the database connection.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
  - `metadata`: An optional dictionary containing additional metadata for table creation.
- **Returns**: None. The method is expected to perform the table creation operation.

### `refresh_tables`
```python
@abstractmethod
def refresh_tables(
    self,
    tables: list[str],
    db_connection_id: str,
    repository: TableDescriptionRepository,
    metadata: dict = None,
) -> list[TableDescription]:
```
- **Description**: Abstract method that must be implemented by subclasses to refresh the metadata of existing tables.
- **Parameters**:
  - `tables`: A list of strings representing the names of tables to be refreshed.
  - `db_connection_id`: A string representing the unique identifier for the database connection.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
  - `metadata`: An optional dictionary containing additional metadata for refreshing tables.
- **Returns**: A list of `TableDescription` instances that have been refreshed.

## Usage
Subclasses of the `Scanner` class must implement the abstract methods to provide functionality for scanning databases, synchronizing table descriptions, creating tables, and refreshing table metadata. These subclasses are used within the `dataherald` project to interact with different types of databases and to maintain an up-to-date representation of the database schema and structure.

## Subclassing
To create a new scanner class, one must subclass `Scanner` and provide concrete implementations for all the abstract methods. This new subclass can then be integrated into the `dataherald` project to extend its database scanning capabilities.
```