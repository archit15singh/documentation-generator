```markdown
# SQLGenerationService Class

## Description
The `SQLGenerationService` class is responsible for managing the lifecycle of SQL generation requests within the DataHerald application. It provides methods to create, retrieve, update, and execute SQL generations based on user prompts and other input parameters. The service interacts with various repositories to store and retrieve data, and it uses SQL generators to create SQL queries from natural language prompts.

## Attributes
- `system`: An instance of the `System` class, which provides access to system-wide configurations and utilities.
- `storage`: A storage backend used to persist data related to SQL generations.
- `sql_generation_repository`: An instance of `SQLGenerationRepository` used to interact with the storage backend for SQL generation objects.

## Methods

### `__init__(self, system: System, storage)`
Constructor for the `SQLGenerationService` class. It initializes the service with the provided system configuration and storage backend.

### `update_error(self, sql_generation: SQLGeneration, error: str) -> SQLGeneration`
Updates the error message of a given `SQLGeneration` object and persists the changes to the storage.

### `generate_response_with_timeout(self, sql_generator, user_prompt, db_connection)`
Generates a SQL response using the provided SQL generator, user prompt, and database connection, with a timeout mechanism.

### `create(self, prompt_id: str, sql_generation_request: SQLGenerationRequest) -> SQLGeneration`
Creates a new SQL generation based on the provided prompt ID and SQL generation request. It handles the entire process, including retrieving the prompt, establishing a database connection, generating the SQL query, and evaluating the result if required.

### `start_streaming(self, prompt_id: str, sql_generation_request: SQLGenerationRequest, queue: Queue)`
Starts streaming SQL generation responses to a provided queue. It is similar to the `create` method but designed for streaming responses.

### `get(self, query) -> list[SQLGeneration]`
Retrieves a list of `SQLGeneration` objects based on the provided query parameters.

### `execute(self, sql_generation_id: str, max_rows: int = 100) -> tuple[str, dict]`
Executes the SQL query associated with the given SQL generation ID and returns the result limited to the specified maximum number of rows.

### `update_metadata(self, sql_generation_id, metadata_request) -> SQLGeneration`
Updates the metadata of an existing SQL generation object based on the provided metadata request.

### `create_dataframe(self, sql_generation_id)`
Creates a pandas DataFrame from the results of the SQL query associated with the given SQL generation ID.

## Exceptions
- `SQLGenerationError`: Custom exception raised when there is an error during the SQL generation process.
- `EmptySQLGenerationError`: Custom exception raised when the SQL generation results in an empty dataset.

## Usage
The `SQLGenerationService` class is used within the DataHerald application to facilitate the generation of SQL queries from natural language prompts. It is typically used by controllers or other services that handle user requests for SQL generation. The service ensures that the SQL generation process is executed correctly, handles errors, and provides the necessary responses or data to the calling functions.
```