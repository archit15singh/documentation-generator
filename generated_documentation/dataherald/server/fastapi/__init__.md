```markdown
# `__init__.py` Technical Documentation

## Overview

This file defines the `FastAPI` class, which is a subclass of `dataherald.server.Server`. It sets up the FastAPI application, defines API routes, and implements the logic for each endpoint by delegating to the `dataherald.api.API` client.

## Class: `FastAPI`

### Initialization

- Inherits from `dataherald.server.Server`.
- Initializes a new FastAPI application with debugging enabled.
- Creates an instance of `dataherald.api.API` using the provided settings.
- Defines an API router and adds various API routes to it.
- Includes the router in the FastAPI application.
- Sets operation IDs for the routes to match their names for easier client generation.

### Methods

#### `app() -> fastapi.FastAPI`
Returns the FastAPI application instance.

#### `scan_db(scanner_request: ScannerRequest, background_tasks: BackgroundTasks) -> list[TableDescriptionResponse]`
Initiates a scan of the database to synchronize table schemas and returns a list of table descriptions.

#### `refresh_table_description(refresh_table_description: RefreshTableDescriptionRequest) -> list[TableDescriptionResponse]`
Refreshes the table descriptions and returns the updated list.

#### `create_prompt(prompt_request: PromptRequest) -> PromptResponse`
Creates a new prompt and returns the created prompt's details.

#### `get_prompt(prompt_id: str) -> PromptResponse`
Retrieves a prompt by its ID and returns its details.

#### `update_prompt(prompt_id: str, update_metadata_request: UpdateMetadataRequest) -> PromptResponse`
Updates a prompt's metadata and returns the updated prompt's details.

#### `get_prompts(db_connection_id: str | None = None) -> list[PromptResponse]`
Retrieves a list of prompts, optionally filtered by database connection ID.

#### `create_sql_generation(prompt_id: str, sql_generation_request: SQLGenerationRequest) -> SQLGenerationResponse`
Creates an SQL generation task for a given prompt and returns the details of the generated SQL.

#### `create_prompt_and_sql_generation(prompt_sql_generation_request: PromptSQLGenerationRequest) -> SQLGenerationResponse`
Creates a prompt and an associated SQL generation task in one step and returns the details of the generated SQL.

#### `get_sql_generations(prompt_id: str | None = None) -> list[SQLGenerationResponse]`
Retrieves a list of SQL generations, optionally filtered by prompt ID.

#### `get_sql_generation(sql_generation_id: str) -> SQLGenerationResponse`
Retrieves an SQL generation by its ID and returns its details.

#### `update_sql_generation(sql_generation_id: str, update_metadata_request: UpdateMetadataRequest) -> SQLGenerationResponse`
Updates an SQL generation's metadata and returns the updated details.

#### `create_nl_generation(sql_generation_id: str, nl_generation_request: NLGenerationRequest) -> NLGenerationResponse`
Creates a natural language (NL) generation task based on an SQL generation and returns the details of the NL generation.

#### `create_sql_and_nl_generation(prompt_id: str, nl_generation_sql_generation_request: NLGenerationsSQLGenerationRequest) -> NLGenerationResponse`
Creates an SQL generation and an associated NL generation task for a given prompt and returns the details of the NL generation.

#### `create_prompt_sql_and_nl_generation(request: PromptSQLGenerationNLGenerationRequest) -> NLGenerationResponse`
Creates a prompt, an SQL generation, and an NL generation task in one step and returns the details of the NL generation.

#### `get_nl_generations(sql_generation_id: str | None = None) -> list[NLGenerationResponse]`
Retrieves a list of NL generations, optionally filtered by SQL generation ID.

#### `get_nl_generation(nl_generation_id: str) -> NLGenerationResponse`
Retrieves an NL generation by its ID and returns its details.

#### `update_nl_generation(nl_generation_id: str, update_metadata_request: UpdateMetadataRequest) -> NLGenerationResponse`
Updates an NL generation's metadata and returns the updated details.

#### `root() -> dict[str, int]`
Returns a heartbeat response with the current nanosecond timestamp.

#### `heartbeat() -> dict[str, int]`
Alias for the `root()` method, providing a heartbeat response.

#### `create_database_connection(database_connection_request: DatabaseConnectionRequest) -> DatabaseConnectionResponse`
Creates a new database connection and returns its details.

#### `list_database_connections() -> list[DatabaseConnection]`
Lists all database connections.

#### `update_database_connection(db_connection_id: str, database_connection_request: DatabaseConnectionRequest) -> DatabaseConnection`
Updates a database connection and returns the updated details.

#### `update_table_description(table_description_id: str, table_description_request: TableDescriptionRequest) -> TableDescriptionResponse`
Updates a table description and returns the updated details.

#### `list_table_descriptions(db_connection_id: str, table_name: str | None = None) -> list[TableDescriptionResponse]`
Lists table descriptions, optionally filtered by database connection ID and table name.

#### `get_table_description(table_description_id: str) -> TableDescriptionResponse`
Retrieves a table description by its ID and returns its details.

#### `get_query_history(db_connection_id: str) -> list[QueryHistory]`
Retrieves the query history for a given database connection ID.

#### `execute_sql_query(sql_generation_id: str, max_rows: int = 100) -> list`
Executes an SQL query associated with an SQL generation ID and returns the result set, limited to a maximum number of rows.

#### `export_csv_file(sql_generation_id: str) -> StreamingResponse`
Exports the results of an SQL generation as a CSV file and returns a streaming response.

#### `delete_golden_sql(golden_sql_id: str) -> dict`
Deletes a golden SQL record.

#### `add_golden_sqls(golden_sqls: List[GoldenSQLRequest]) -> List[GoldenSQLResponse]`
Adds multiple golden SQL records and returns their details.

#### `get_golden_sqls(db_connection_id: str = None, page: int = 1, limit: int = 10) -> List[GoldenSQL]`
Retrieves a paginated list of golden SQL records, optionally filtered by database connection ID.

#### `update_golden_sql(golden_sql_id: str, update_metadata_request: UpdateMetadataRequest) -> GoldenSQL`
Updates a golden SQL record and returns the updated details.

#### `add_instruction(instruction_request: InstructionRequest) -> InstructionResponse`
Adds an instruction and returns its details.

#### `get_instructions(db_connection_id: str = None, page: int = 1, limit: int = 10) -> List[InstructionResponse]`
Retrieves a paginated list of instructions, optionally filtered by database connection ID.

#### `delete_instruction(instruction_id: str) -> dict`
Deletes an instruction.

#### `update_instruction(instruction_id: str, instruction_request: UpdateInstruction) -> InstructionResponse`
Updates an instruction and returns the updated details.

#### `create_finetuning_job(fine_tuning_request: FineTuningRequest, background_tasks: BackgroundTasks) -> Finetuning`
Creates a fine-tuning job and returns its details.

#### `cancel_finetuning_job(cancel_fine_tuning_request: CancelFineTuningRequest) -> Finetuning`
Cancels a fine-tuning job and returns its details.

#### `get_finetuning_job(finetuning_id: str) -> Finetuning`
Retrieves a fine-tuning job by its ID and returns its details.

#### `get_fintunings(db_connection_id: str = None) -> list[Finetuning]`
Retrieves a list of fine-tuning jobs, optionally filtered by database connection ID.

#### `delete_finetuning_job(finetuning_id: str) -> dict`
Deletes a fine-tuning job.

#### `update_finetuning_job(finetuning_id: str, update_metadata_request: UpdateMetadataRequest) -> Finetuning`
Updates a fine-tuning job and returns the updated details.

#### `stream_sql_generation(request: StreamPromptSQLGenerationRequest) -> StreamingResponse`
Streams the creation of a prompt and SQL generation task as a server-sent event (SSE) and returns a streaming response.

## Helper Function

### `use_route_names_as_operation_ids(app: _FastAPI) -> None`
Sets the operation ID of each API route to match its name for easier client generation. This function should be called after all routes have been added to the application.
```