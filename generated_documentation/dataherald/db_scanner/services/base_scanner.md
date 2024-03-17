```markdown
# BaseScanner Class

## Overview

The `BaseScanner` class is a concrete implementation of the `AbstractScanner` class, which is part of the `dataherald.db_scanner` package. This class provides functionality to scan a database and perform operations such as calculating the cardinality of values in a database column. It is designed to be used within a larger project that requires database scanning capabilities.

## Attributes

- `MIN_CATEGORY_VALUE`: An integer constant representing the minimum number of distinct values in a column to be considered for cardinality calculation.
- `MAX_CATEGORY_VALUE`: An integer constant representing the maximum number of distinct values in a column to be considered for cardinality calculation.

## Methods

### cardinality_values

```python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None
```

#### Description

Calculates the cardinality of values in a specified database column. It retrieves a distinct list of values from the column and determines if the number of distinct values falls within a specified range defined by `MIN_CATEGORY_VALUE` and `MAX_CATEGORY_VALUE`.

#### Parameters

- `column`: A `Column` object from the `sqlalchemy.sql.schema` module representing the database column for which the cardinality is to be calculated.
- `db_engine`: An instance of `SQLDatabase` from the `dataherald.sql_database.base` module, which provides the database engine to execute the query.

#### Returns

- A list of distinct values from the column as strings if the number of distinct values is within the specified range.
- `None` if the number of distinct values is outside the specified range.

#### Implementation Details

1. Constructs a `SELECT` query using `sqlalchemy.select` to retrieve distinct values from the specified column, limited to 101 entries to check against the `MAX_CATEGORY_VALUE`.
2. Executes the query using the provided `db_engine`'s `engine` attribute.
3. Fetches all results from the executed query.
4. Checks if the number of distinct values is within the range defined by `MIN_CATEGORY_VALUE` and `MAX_CATEGORY_VALUE`.
5. If within range, returns a list of the distinct values converted to strings.
6. If not within range, returns `None`.

### get_logs

```python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]
```

#### Description

A placeholder method that is intended to retrieve a list of query logs from a specified database table. Currently, this method is not implemented and simply returns an empty list.

#### Parameters

- `table`: A string representing the name of the database table from which to retrieve query logs.
- `db_engine`: An instance of `SQLDatabase`, providing the database engine to execute the query.
- `db_connection_id`: A string representing the unique identifier for the database connection.

#### Returns

- An empty list of `QueryHistory` objects, indicating no implementation is currently provided.

#### Implementation Details

1. The method signature includes the `override` decorator, indicating that it overrides a method from the base class `AbstractScanner`.
2. The method currently does not perform any operations and returns an empty list.

## Usage

The `BaseScanner` class is used within the project to perform database scanning operations, particularly to calculate the cardinality of database columns. It can be instantiated and its methods called by passing the required parameters, such as a `Column` object and an `SQLDatabase` instance. The `get_logs` method is not currently functional and serves as a template for future implementation.

## Integration

The `BaseScanner` class integrates with the SQLAlchemy library for database operations and the `overrides` library to ensure method signatures match the abstract base class. It also utilizes the `QueryHistory` model from the `dataherald.db_scanner.models.types` module, although the usage is not yet implemented in the `get_logs` method.
```
