```markdown
# BigQueryScanner Class

## Overview
`BigQueryScanner` is a Python class that extends the `AbstractScanner` class, providing specific implementations for scanning Google BigQuery databases. It is part of a larger project aimed at analyzing and monitoring database usage and schema. The class includes methods for estimating the cardinality of column values and retrieving logs of query activities.

## Attributes
- `MIN_CATEGORY_VALUE`: The minimum threshold value for considering a column as categorical.
- `MAX_CATEGORY_VALUE`: The maximum threshold value for considering a column as categorical.
- `MAX_LOGS`: The maximum number of log entries to retrieve.

## Methods

### cardinality_values
```python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None
```
#### Description
Estimates the cardinality of a given column in a BigQuery table and returns a list of distinct values if the cardinality is within a specified range.

#### Parameters
- `column`: An instance of `sqlalchemy.sql.schema.Column` representing the database column to be scanned.
- `db_engine`: An instance of `SQLDatabase` that provides the database engine for executing SQL queries.

#### Returns
- A list of distinct values from the column if the cardinality is within the specified range (`MIN_CATEGORY_VALUE` < cardinality <= `MAX_CATEGORY_VALUE`).
- `None` if the cardinality is outside the specified range or if an error occurs during query execution.

#### Implementation Details
1. Constructs a query to estimate the approximate count of distinct values in the specified column using `APPROX_COUNT_DISTINCT`.
2. Executes the query using the provided database engine.
3. If the result indicates that the cardinality is within the specified range, constructs and executes another query to retrieve up to 101 distinct values from the column.
4. Converts the retrieved values to strings and returns them as a list.
5. If an error occurs during query execution, the method returns `None`.

### get_logs
```python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]
```
#### Description
Retrieves a list of query logs for a specified table from BigQuery's `INFORMATION_SCHEMA.JOBS`.

#### Parameters
- `table`: A string representing the name of the table for which to retrieve query logs.
- `db_engine`: An instance of `SQLDatabase` that provides the database engine for executing SQL queries.
- `db_connection_id`: A string representing the identifier of the database connection.

#### Returns
- A list of `QueryHistory` objects, each containing information about a specific query log entry.

#### Implementation Details
1. Calculates a filter date, which is 90 days before the current date.
2. Constructs a query to retrieve the top `MAX_LOGS` query logs from the `INFORMATION_SCHEMA.JOBS` table, filtering by the specified table name, job type (`QUERY`), statement type (`SELECT`), job state (`DONE`), and creation time after the filter date.
3. Executes the query using the provided database engine.
4. Parses the result set and creates a list of `QueryHistory` objects with the retrieved data.
5. Returns the list of `QueryHistory` objects.

## Usage
The `BigQueryScanner` class is used within the project to interact with Google BigQuery databases. It provides methods to estimate the cardinality of columns and to retrieve query logs, which can be used for monitoring and analyzing database usage patterns. The class relies on the `SQLDatabase` abstraction to execute SQL queries and handle database connections.

## Notes
- The class uses raw SQL queries with string formatting, which could be vulnerable to SQL injection if not used carefully (`noqa: S608`).
- The `get_logs` method uses a hardcoded region (`region-us`) in the query, which may need to be adjusted for different BigQuery regions.
- The `get_logs` method assumes that the `INFORMATION_SCHEMA.JOBS` table contains the necessary fields and that the BigQuery setup conforms to the expected schema.
- The `cardinality_values` method uses a limit of 101 in the query to ensure that the method only returns values for columns with cardinality within the specified range.
- The `noqa: E501` comment indicates that the line length exceeds the recommended limit, which is typically ignored for readability in the context of SQL queries.
```