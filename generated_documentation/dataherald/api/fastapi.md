```markdown
# FastAPI Class Documentation

## Overview

The `FastAPI` class is a subclass of the `API` class and provides a concrete implementation of various API endpoints for a FastAPI web service. It is designed to handle database scanning, SQL and natural language (NL) generation, prompt management, and fine-tuning of language models. The class interacts with a variety of repositories, services, and utilities to perform its tasks.

## Class Methods

### `__init__(self, system: System)`

Initializes the `FastAPI` instance with a reference to the `System` object, which provides access to system-wide configurations and instances of other components such as the database (`DB`).

### `heartbeat(self) -> int`

Returns the current server time in nanoseconds to check if the server is alive.

### `scan_db(self, scanner_request: ScannerRequest, background_tasks: BackgroundTasks) -> list[TableDescriptionResponse]`

Scans the database tables and columns based on the provided `scanner_request`. It adds the scanning task to the background to be processed asynchronously.

### `create_database_connection(self, database_connection_request: DatabaseConnectionRequest) -> DatabaseConnectionResponse`

Creates a new database connection using the provided `database_connection_request` and returns a response with the connection details.

### `refresh_table_description(self, refresh_table_description: RefreshTableDescriptionRequest) -> list[TableDescriptionResponse]`

Refreshes the table descriptions for a given database connection.

### `list_database_connections(self) -> list[DatabaseConnectionResponse]`

Lists all database connections available in the system.

### `update_database_connection(self, db_connection_id: str, database_connection_request: DatabaseConnectionRequest) -> DatabaseConnectionResponse`

Updates an existing database connection with the provided details.

### `update_table_description(self, table_description_id: str, table_description_request: TableDescriptionRequest) -> TableDescriptionResponse`

Updates the description of a specific table.

### `list_table_descriptions(self, db_connection_id: str, table_name: str | None = None) -> list[TableDescriptionResponse]`

Lists the table descriptions for a given database connection, optionally filtered by table name.

### `get_table_description(self, table_description_id: str) -> TableDescriptionResponse`

Retrieves the description of a specific table.

### `create_prompt(self, prompt_request: PromptRequest) -> PromptResponse`

Creates a new prompt based on the provided `prompt_request`.

### `get_prompt(self, prompt_id) -> PromptResponse`

Retrieves a specific prompt by its ID.

### `update_prompt(self, prompt_id: str, update_metadata_request: UpdateMetadataRequest) -> PromptResponse`

Updates the metadata of a specific prompt.

### `get_prompts(self, db_connection_id: str | None = None) -> List[PromptResponse]`

Retrieves all prompts, optionally filtered by database connection ID.

### `get_query_history(self, db_connection_id: str) -> list[QueryHistory]`

Retrieves the query history for a given database connection.

### `add_golden_sqls(self, golden_sqls: List[GoldenSQLRequest]) -> List[GoldenSQLResponse]`

Adds a list of NL <> SQL pairs (golden SQLs) to be used in prompts for the language model.

### `execute_sql_query(self, sql_generation_id: str, max_rows: int = 100) -> list`

Executes a SQL query and returns the results.

### `export_csv_file(self, sql_generation_id: str) -> io.StringIO`

Exports the results of a SQL query to a CSV file.

### `delete_golden_sql(self, golden_sql_id: str) -> dict`

Deletes a specific golden SQL record.

### `get_golden_sqls(self, db_connection_id: str = None, page: int = 1, limit: int = 10) -> List[GoldenSQL]`

Retrieves golden SQL records, optionally filtered by database connection ID and paginated.

### `update_golden_sql(self, golden_sql_id: str, update_metadata_request: UpdateMetadataRequest) -> GoldenSQL`

Updates the metadata of a specific golden SQL record.

### `add_instruction(self, instruction_request: InstructionRequest) -> InstructionResponse`

Adds a new instruction based on the provided `instruction_request`.

### `get_instructions(self, db_connection_id: str = None, page: int = 1, limit: int = 10) -> List[InstructionResponse]`

Retrieves instructions, optionally filtered by database connection ID and paginated.

### `delete_instruction(self, instruction_id: str) -> dict`

Deletes a specific instruction.

### `update_instruction(self, instruction_id: str, instruction_request: UpdateInstruction) -> InstructionResponse`

Updates a specific instruction.

### `create_finetuning_job(self, fine_tuning_request: FineTuningRequest, background_tasks: BackgroundTasks) -> Finetuning`

Creates a fine-tuning job for a language model and adds it to the background tasks.

### `cancel_finetuning_job(self, cancel_fine_tuning_request: CancelFineTuningRequest) -> Finetuning`

Cancels an ongoing fine-tuning job.

### `get_finetunings(self, db_connection_id: str | None = None) -> list[Finetuning]`

Retrieves fine-tuning jobs, optionally filtered by database connection ID.

### `delete_finetuning_job(self, finetuning_job_id: str) -> dict`

Deletes a specific fine-tuning job.

### `get_finetuning_job(self, finetuning_job_id: str) -> Finetuning`

Retrieves a specific fine-tuning job.

### `update_finetuning_job(self, finetuning_job_id: str, update_metadata_request: UpdateMetadataRequest) -> Finetuning`

Updates the metadata of a specific fine-tuning job.

### `create_sql_generation(self, prompt_id: str, sql_generation_request: SQLGenerationRequest) -> SQLGenerationResponse`

Creates a new SQL generation based on the provided `sql_generation_request`.

### `create_prompt_and_sql_generation(self, prompt_sql_generation_request: PromptSQLGenerationRequest) -> SQLGenerationResponse`

Creates a new prompt and associated SQL generation.

### `get_sql_generations(self, prompt_id: str | None = None) -> list[SQLGenerationResponse]`

Retrieves SQL generations, optionally filtered by prompt ID.

### `get_sql_generation(self, sql_generation_id: str) -> SQLGenerationResponse`

Retrieves a specific SQL generation.

### `update_sql_generation(self, sql_generation_id: str, update_metadata_request: UpdateMetadataRequest) -> SQLGenerationResponse`

Updates the metadata of a specific SQL generation.

### `create_nl_generation(self, sql_generation_id: str, nl_generation_request: NLGenerationRequest) -> NLGenerationResponse`

Creates a new NL generation based on the provided `nl_generation_request`.

### `create_sql_and_nl_generation(self, prompt_id: str, nl_generation_sql_generation_request: NLGenerationsSQLGenerationRequest) -> NLGenerationResponse`

Creates a new SQL generation and associated NL generation.

### `create_prompt_sql_and_nl_generation(self, request: PromptSQLGenerationNLGenerationRequest) -> NLGenerationResponse`

Creates a new prompt, SQL generation, and associated NL generation.

### `get_nl_generations(self, sql_generation_id: str | None = None) -> list[NLGenerationResponse]`

Retrieves NL generations, optionally filtered by SQL generation ID.

### `update_nl_generation(self, nl_generation_id: str, update_metadata_request: UpdateMetadataRequest) -> NLGenerationResponse`

Updates the metadata of a specific NL generation.

### `get_nl_generation(self, nl_generation_id: str) -> NLGenerationResponse`

Retrieves a specific NL generation.

### `stream_create_prompt_and_sql_generation(self, request: StreamPromptSQLGenerationRequest)`

Streams the creation of a prompt and SQL generation in real-time.

## Helper Functions

### `async_scanning(scanner, database, scanner_request, storage)`

Performs asynchronous scanning of the database.

### `async_fine_tuning(storage, model)`

Performs asynchronous fine-tuning of a language model.

### `delete_file(file_location: str)`

Deletes a file at the specified location.

## Constants

### `MAX_ROWS_TO_CREATE_CSV_FILE`

Defines the maximum number of rows to create a CSV file.

## Usage

The `FastAPI` class is instantiated with a `System` object and provides methods that are typically bound to HTTP endpoints in a FastAPI application. Each method corresponds to a specific API functionality, such as managing database connections, generating SQL queries, handling prompts, and fine-tuning language models.

## Error Handling

The class methods handle various exceptions, such as `InvalidId`, `DatabaseConnectionNotFoundError`, `SQLGenerationNotFoundError`, `SQLInjectionError`, `SQLAlchemyError`, `GoldenSQLNotFoundError`, `PromptNotFoundError`, and `NLGenerationNotFoundError`. HTTP exceptions are raised with appropriate status codes and details when errors occur.

## Dependencies

The class relies on several external modules and internal components, including:

- `asyncio`
- `datetime`
- `io`
- `json`
- `logging`
- `os`
- `time`
- `queue.Queue`
- `typing.List`
- `bson.objectid`
- `fastapi.BackgroundTasks`
- `fastapi.HTTPException`
- `overrides.override`
- `sqlalchemy.exc.SQLAlchemyError`
- Various internal modules and repositories for handling database operations, scanning, prompts, SQL/NL generations, and fine-tuning.

## Security Considerations

Sensitive information such as database connection URIs and SSH settings are encrypted using `FernetEncrypt` before being included in error responses to prevent leakage of sensitive data.
```