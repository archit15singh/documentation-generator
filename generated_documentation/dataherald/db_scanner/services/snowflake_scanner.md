```markdown
# SnowflakeScanner Class

## Overview

The `SnowflakeScanner` class is a subclass of `AbstractScanner` and provides specific implementations for scanning Snowflake databases. It includes methods for estimating the cardinality of column values and retrieving query logs from a Snowflake database.

## Constants

- `MIN_CATEGORY_VALUE`: The minimum value for a category to be considered in cardinality estimation.
- `MAX_CATEGORY_VALUE`: The maximum value for a category to be considered in cardinality estimation.
- `MAX_LOGS`: The maximum number of log entries to retrieve from the query history.

## Methods

### cardinality_values

#### Description

Estimates the cardinality of values in a given column using HyperLogLog (HLL) and, if the cardinality is within a specified range, retrieves distinct values up to a limit.

#### Parameters

- `column`: An instance of `sqlalchemy.sql.schema.Column` representing the database column for which to estimate cardinality.
- `db_engine`: An instance of `SQLDatabase` representing the database engine to execute the query against.

#### Returns

- A list of distinct values as strings if the cardinality is within the specified range.
- `None` if the cardinality is not within the specified range or if no results are found.

#### Implementation Details

1. Executes a SQL query using `func.HLL` to estimate the cardinality of the specified column.
2. Checks if the result is within the specified range (`MIN_CATEGORY_VALUE` and `MAX_CATEGORY_VALUE`).
3. If within range, executes another SQL query to retrieve up to 101 distinct values from the column.
4. Returns the distinct values as a list of strings.

### get_logs

#### Description

Retrieves the query history for a specific table from the Snowflake database, filtering for successful `SELECT` queries within the last 90 days, excluding queries to the `QUERY_HISTORY` table itself, and orders the results by the number of occurrences.

#### Parameters

- `table`: A string representing the name of the table for which to retrieve query logs.
- `db_engine`: An instance of `SQLDatabase` representing the database engine to execute the query against.
- `db_connection_id`: A string representing the identifier for the database connection.

#### Returns

- A list of `QueryHistory` objects containing the query text, user who executed the query, and the number of occurrences.

#### Implementation Details

1. Extracts the database name from the `db_engine`'s URL.
2. Calculates the date 90 days prior to the current date.
3. Executes a raw SQL query against the `INFORMATION_SCHEMA.QUERY_HISTORY` table to retrieve query logs that match the specified criteria.
4. Constructs a list of `QueryHistory` objects from the query results, each containing the `db_connection_id`, `table_name`, `query`, `user`, and `occurrences`.
5. Limits the number of returned logs to `MAX_LOGS`.

## Usage

The `SnowflakeScanner` class is used within a project to interact with Snowflake databases for the purpose of analyzing database usage and estimating column cardinalities. It is instantiated and called by other components that require access to Snowflake-specific scanning functionality.

## Dependencies

- `datetime`: For calculating dates for log retrieval.
- `sqlalchemy`: For constructing and executing SQL queries.
- `overrides`: For the `@override` decorator to ensure method signatures match the superclass.
- `dataherald.db_scanner.models.types`: For the `QueryHistory` model.
- `dataherald.db_scanner.services.abstract_scanner`: For the `AbstractScanner` base class.
- `dataherald.sql_database.base`: For the `SQLDatabase` class.
```
