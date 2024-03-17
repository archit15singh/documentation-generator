```markdown
# AbstractScanner Class

## Overview

The `AbstractScanner` class serves as an abstract base class (ABC) for creating scanner services that interact with a database. It defines a common interface for scanner services that can be implemented for different types of databases or different scanning strategies. The class is part of the `dataherald.db_scanner.services` module.

## Dependencies

- `abc`: The `ABC` and `abstractmethod` are imported from the `abc` module to define the abstract base class and abstract methods.
- `sqlalchemy.sql.schema`: The `Column` class is imported from `sqlalchemy.sql.schema` to represent a column in a SQL database.
- `dataherald.db_scanner.models.types`: The `QueryHistory` class is imported from `dataherald.db_scanner.models.types` to represent the structure of query logs.
- `dataherald.sql_database.base`: The `SQLDatabase` class is imported from `dataherald.sql_database.base` to represent the SQL database engine.

## Class Definition

### AbstractScanner

The `AbstractScanner` class inherits from `ABC`, making it an abstract base class that cannot be instantiated directly. It provides a template for subclasses to implement specific functionality for scanning databases.

#### Methods

##### `cardinality_values`

```python
@abstractmethod
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None:
    """Returns a list if it is a catalog otherwise return None"""
    pass
```

- **Parameters**:
  - `column` (`Column`): An instance of `Column` representing the database column to be scanned for cardinality values.
  - `db_engine` (`SQLDatabase`): An instance of `SQLDatabase` representing the database engine to be used for the query.
- **Returns**: A list of cardinality values if the column is a catalog; otherwise, `None`.
- **Description**: This method is an abstract method that must be implemented by subclasses. It is intended to retrieve the cardinality values (i.e., the number of distinct values) for a given column in the database. The method should return a list of these values if the column is a catalog (a column with a limited set of possible values), or `None` if the column is not a catalog.

##### `get_logs`

```python
@abstractmethod
def get_logs(
    self, table: str, db_engine: SQLDatabase, db_connection_id: str
) -> list[QueryHistory]:
    """Returns a list of logs"""
    pass
```

- **Parameters**:
  - `table` (`str`): The name of the database table for which query logs are to be retrieved.
  - `db_engine` (`SQLDatabase`): An instance of `SQLDatabase` representing the database engine to be used for the query.
  - `db_connection_id` (`str`): A string identifier for the database connection.
- **Returns**: A list of `QueryHistory` instances representing the logs of queries executed against the specified table.
- **Description**: This method is an abstract method that must be implemented by subclasses. It is intended to retrieve a list of query logs for a specific table. Each log entry is represented by an instance of `QueryHistory`, which contains details about the query such as the timestamp, the query text, and other relevant metadata.

## Usage

The `AbstractScanner` class is used as a base for creating concrete scanner classes that implement the `cardinality_values` and `get_logs` methods. Subclasses must provide the logic for these methods according to the specific requirements of the database or scanning strategy they support. Once implemented, these scanner services can be used to scan database tables for cardinality information and retrieve query logs for analysis or monitoring purposes.

## Subclassing Example

To create a concrete scanner service, a subclass of `AbstractScanner` would be defined with implementations for the `cardinality_values` and `get_logs` methods:

```python
class ConcreteScanner(AbstractScanner):
    def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None:
        # Implementation specific to the concrete scanner
        pass

    def get_logs(
        self, table: str, db_engine: SQLDatabase, db_connection_id: str
    ) -> list[QueryHistory]:
        # Implementation specific to the concrete scanner
        pass
```

The `ConcreteScanner` class would then be instantiated and used to perform scanning operations on a database.
```