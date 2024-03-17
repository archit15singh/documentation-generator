```markdown
# `types.py` Module Documentation

## Overview

The `types.py` module defines a set of classes that represent the structure and metadata of database tables and their relationships, as well as the history of queries executed against those tables. These classes are used to model and validate data using the Pydantic library, which provides data parsing and validation using Python type annotations.

## Classes

### `ForeignKeyDetail`

Represents the details of a foreign key relationship between database columns.

#### Attributes

- `field_name`: `str` - The name of the field that holds the foreign key.
- `reference_table`: `str` - The name of the table that the foreign key references.

### `ColumnDetail`

Represents the details of a single column within a database table.

#### Attributes

- `name`: `str` - The name of the column.
- `is_primary_key`: `bool` - A flag indicating whether the column is a primary key. Defaults to `False`.
- `data_type`: `str` - The data type of the column. Defaults to `"str"`.
- `description`: `str | None` - An optional description of the column.
- `low_cardinality`: `bool` - A flag indicating whether the column has low cardinality. Defaults to `False`.
- `categories`: `list[Any] | None` - An optional list of categories or distinct values that the column can take.
- `foreign_key`: `ForeignKeyDetail | None` - An optional `ForeignKeyDetail` instance if the column is a foreign key.

### `TableDescriptionStatus`

An enumeration of possible statuses for a table description.

#### Members

- `NOT_SCANNED`: The table has not been scanned.
- `SYNCHRONIZING`: The table is currently being synchronized.
- `DEPRECATED`: The table is marked as deprecated.
- `SCANNED`: The table has been successfully scanned.
- `FAILED`: The scanning of the table has failed.

### `TableDescription`

Represents the metadata and schema details of a database table.

#### Attributes

- `id`: `str | None` - An optional unique identifier for the table description.
- `db_connection_id`: `str` - The identifier of the database connection.
- `table_name`: `str` - The name of the table.
- `description`: `str | None` - An optional description of the table.
- `table_schema`: `str | None` - An optional schema name where the table resides.
- `columns`: `list[ColumnDetail]` - A list of `ColumnDetail` instances representing the columns of the table. Defaults to an empty list.
- `examples`: `list` - A list of example records from the table. Defaults to an empty list.
- `last_schema_sync`: `datetime | None` - The timestamp of the last schema synchronization. Can be `None`.
- `status`: `str` - The status of the table description, represented by a value from `TableDescriptionStatus`. Defaults to `SCANNED`.
- `error_message`: `str | None` - An optional error message if the table description encountered an error.
- `metadata`: `dict | None` - An optional dictionary containing additional metadata about the table.
- `created_at`: `datetime` - The timestamp when the table description was created. Defaults to the current time.

#### Validators

- `parse_datetime_with_timezone` - Ensures that the `last_schema_sync` attribute, if present, is set with UTC timezone information.

### `QueryHistory`

Represents the history of a query executed against a database table.

#### Attributes

- `id`: `str | None` - An optional unique identifier for the query history record.
- `db_connection_id`: `str` - The identifier of the database connection where the query was executed.
- `table_name`: `str` - The name of the table against which the query was executed.
- `query`: `str` - The SQL query string that was executed.
- `user`: `str` - The identifier of the user who executed the query.
- `occurrences`: `int` - The number of times the query was executed. Defaults to `0`.

## Usage

These classes are typically used to:

- Define the structure of database tables and their columns.
- Store and validate metadata about database tables, such as descriptions and synchronization status.
- Record and track the history of queries executed against the database, including the frequency of execution and the user who executed them.

The classes utilize Pydantic's BaseModel to leverage automatic data validation and parsing based on Python type annotations. This ensures that instances of these classes are created with valid data and can be easily serialized/deserialized to and from JSON, databases, or other formats.
```