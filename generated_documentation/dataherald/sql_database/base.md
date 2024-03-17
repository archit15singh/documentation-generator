```markdown
# SQLDatabase Class

## Overview

The `SQLDatabase` class is a wrapper around the SQLAlchemy engine, providing a simplified interface for interacting with SQL databases. It includes methods for creating database connections, executing SQL commands, and retrieving metadata about the database.

## Attributes

- `_engine`: An instance of `sqlalchemy.engine.Engine` that represents the core interface to the database.

## Properties

- `engine`: Returns the SQLAlchemy engine instance.

- `dialect`: Returns a string representation of the database dialect in use.

## Methods

### `__init__(self, engine: Engine)`

Constructor that initializes the `SQLDatabase` instance with an SQLAlchemy engine.

### `from_uri(cls, database_uri: str, engine_args: dict | None = None) -> "SQLDatabase"`

Class method that constructs a SQLAlchemy engine from a given database URI and optional engine arguments. It supports special handling for DuckDB connections.

### `get_sql_engine(cls, database_info: DatabaseConnection, refresh_connection=False) -> "SQLDatabase"`

Class method that establishes a connection to the database using the provided `DatabaseConnection` object. It handles SSH connections and decrypts the database URI if necessary. It also manages the reuse of existing connections.

### `extract_parameters(cls, input_string)`

Class method that extracts database connection parameters from a URI string using a regular expression pattern.

### `from_uri_ssh(cls, database_info: DatabaseConnection)`

Class method that creates a database connection over SSH by setting up an SSH tunnel using the `SSHTunnelForwarder` class.

### `parser_to_filter_commands(cls, command: str) -> str`

Class method that parses a SQL command and raises an `SQLInjectionError` if it contains sensitive keywords that could lead to SQL injection attacks.

### `run_sql(self, command: str, top_k: int = None) -> tuple[str, dict]`

Instance method that executes a SQL command and returns the results as a string and a dictionary. It supports limiting the number of rows returned (`top_k`).

### `get_tables_and_views(self) -> List[str]`

Instance method that retrieves a list of table and view names from the database. It raises an `EmptyDBError` if the database is empty or if there are permission issues.

## Custom Exception Classes

- `SQLInjectionError`: Raised when a potential SQL injection is detected in a command.
- `InvalidDBConnectionError`: Raised when the database connection cannot be established.
- `EmptyDBError`: Raised when the database is empty or there are permission issues.
- `SSHInvalidDatabaseConnectionError`: Raised when an SSH connection to the database cannot be established.

## DBConnections Class

A nested class that maintains a dictionary of database connections, allowing for the reuse of existing connections.

### Attributes

- `db_connections`: A dictionary that maps database URIs to their respective SQLAlchemy engine instances.

### Methods

#### `add(uri, engine)`

Static method that adds a new connection to the `db_connections` dictionary.

## Usage

The `SQLDatabase` class is used to interact with SQL databases within the project. It abstracts away the complexity of database connections and SQL command execution, providing a secure and efficient way to perform database operations.

## Integration with Other Components

- `DatabaseConnection`: A model class that contains information required to connect to a database.
- `FernetEncrypt`: A utility class used for encrypting and decrypting sensitive information such as database URIs.
- `S3`: A utility class for interacting with Amazon S3, used for downloading credentials files stored in S3 buckets.
- `SSHTunnelForwarder`: A class from the `sshtunnel` module used to establish SSH tunnels for database connections.
- `sqlparse`: A library used to parse and sanitize SQL commands to prevent SQL injection attacks.
- `sqlalchemy`: An SQL toolkit and Object-Relational Mapping (ORM) library used for database interaction.
```