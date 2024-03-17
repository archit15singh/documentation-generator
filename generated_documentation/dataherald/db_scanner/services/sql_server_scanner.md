```markdown
# SqlServerScanner Class

## Overview

The `SqlServerScanner` class is a subclass of `AbstractScanner` and is designed to interact with SQL Server databases. It provides methods to estimate the cardinality of values in a database column and to retrieve logs related to database queries. This class is part of the `dataherald.db_scanner` module and is used for scanning SQL Server databases to gather metadata and statistics that can be used for data profiling and analysis.

## Constants

- `MIN_CATEGORY_VALUE`: The minimum value used to determine if a column should be considered categorical based on its distinct count.
- `MAX_CATEGORY_VALUE`: The maximum value used to determine if a column should be considered categorical based on its distinct count.
- `MAX_LOGS`: The maximum number of logs to retrieve from the database.

## Methods

### cardinality_values

#### Signature

```python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None
```

#### Description

Estimates the cardinality of values in a specified column of a SQL Server database table. It uses an approximate count distinct query to determine if the column has a number of distinct values within a specified range, making it potentially categorical. If the column qualifies, it retrieves a list of distinct values up to a limit.

#### Parameters

- `column`: An instance of `sqlalchemy.sql.schema.Column` representing the database column for which to estimate cardinality.
- `db_engine`: An instance of `dataherald.sql_database.base.SQLDatabase` representing the database engine to execute queries against.

#### Returns

- A list of distinct values from the column if the number of distinct values is within the specified range (`MIN_CATEGORY_VALUE` to `MAX_CATEGORY_VALUE`).
- `None` if an error occurs during query execution or if the number of distinct values is outside the specified range.

#### Implementation Details

1. Constructs a count query using the `APPROX_COUNT_DISTINCT` function to estimate the number of distinct values in the column.
2. Executes the count query using the provided `db_engine`.
3. If the count is within the specified range, constructs a query to retrieve the top 101 distinct values from the column.
4. Executes the query to retrieve the distinct values.
5. Returns a list of the distinct values as strings.

### get_logs

#### Signature

```python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]
```

#### Description

Retrieves a list of query logs related to a specified table from the SQL Server database. Currently, this method is implemented to return an empty list and may be intended for future development or extension.

#### Parameters

- `table`: A string representing the name of the database table for which to retrieve logs.
- `db_engine`: An instance of `dataherald.sql_database.base.SQLDatabase` representing the database engine to execute queries against.
- `db_connection_id`: A string representing the identifier for the database connection.

#### Returns

- An empty list of type `list[QueryHistory]`.

#### Implementation Details

1. The method is currently a stub and does not perform any operations. It simply returns an empty list.

## Usage

The `SqlServerScanner` class is used within the project to perform operations specific to SQL Server databases. It can be instantiated and used to call the `cardinality_values` method to determine if a column is categorical based on the number of distinct values it contains. The `get_logs` method is available for future implementation to retrieve query logs for a given table.

## Notes

- The `cardinality_values` method uses raw SQL queries with string interpolation, which may be prone to SQL injection if not used carefully. The `noqa` comments indicate that linters should ignore specific warnings related to this practice.
- The `get_logs` method is not fully implemented and serves as a placeholder for future functionality.
- The `override` decorator is used to ensure that the methods are correctly overriding methods from the `AbstractScanner` base class.
```