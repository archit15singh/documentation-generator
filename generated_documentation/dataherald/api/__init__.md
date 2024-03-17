```markdown
# API Class

The `API` class is an abstract base class that defines a set of abstract methods for interacting with a data processing and generation system. It inherits from `Component` and `ABC` (Abstract Base Class) from the Python standard library. The class serves as a contract for implementing various API endpoints that handle operations related to database scanning, connection management, table descriptions, prompts, golden SQLs, instructions, fine-tuning jobs, SQL generation, and natural language (NL) generation.

## Methods

### `heartbeat(self) -> int`
- **Description**: Returns the current server time in nanoseconds to check if the server is alive.
- **Returns**: An integer representing the current server time in nanoseconds.

### `scan_db(self, scanner_request: ScannerRequest, background_tasks: BackgroundTasks) -> list[TableDescriptionResponse]`
- **Parameters**:
  - `scanner_request`: An instance of `ScannerRequest` containing the parameters for the database scan.
  - `background_tasks`: An instance of `BackgroundTasks` for running operations in the background.
- **Returns**: A list of `TableDescriptionResponse` objects containing the results of the database scan.

### `refresh_table_description(self, refresh_table_description: RefreshTableDescriptionRequest) -> list[TableDescriptionResponse]`
- **Parameters**:
  - `refresh_table_description`: An instance of `RefreshTableDescriptionRequest` containing the parameters for refreshing the table description.
- **Returns**: A list of `TableDescriptionResponse` objects containing the updated table descriptions.

### `create_database_connection(self, database_connection_request: DatabaseConnectionRequest) -> DatabaseConnectionResponse`
- **Parameters**:
  - `database_connection_request`: An instance of `DatabaseConnectionRequest` containing the parameters for creating a new database connection.
- **Returns**: A `DatabaseConnectionResponse` object containing the details of the created database connection.

### `list_database_connections(self) -> list[DatabaseConnection]`
- **Returns**: A list of `DatabaseConnection` objects representing all existing database connections.

### `update_database_connection(self, db_connection_id: str, database_connection_request: DatabaseConnectionRequest) -> DatabaseConnection`
- **Parameters**:
  - `db_connection_id`: A string representing the unique identifier of the database connection to update.
  - `database_connection_request`: An instance of `DatabaseConnectionRequest` containing the updated parameters for the database connection.
- **Returns**: An updated `DatabaseConnection` object.

### `update_table_description(self, table_description_id: str, table_description_request: TableDescriptionRequest) -> TableDescriptionResponse`
- **Parameters**:
  - `table_description_id`: A string representing the unique identifier of the table description to update.
  - `table_description_request`: An instance of `TableDescriptionRequest` containing the updated parameters for the table description.
- **Returns**: An updated `TableDescriptionResponse` object.

### `list_table_descriptions(self, db_connection_id: str, table_name: str | None = None) -> list[TableDescriptionResponse]`
- **Parameters**:
  - `db_connection_id`: A string representing the unique identifier of the database connection.
  - `table_name`: An optional string representing the name of the table to filter descriptions.
- **Returns**: A list of `TableDescriptionResponse` objects for the specified database connection and optional table name.

### `get_table_description(self, table_description_id: str) -> TableDescriptionResponse`
- **Parameters**:
  - `table_description_id`: A string representing the unique identifier of the table description to retrieve.
- **Returns**: A `TableDescriptionResponse` object containing the details of the requested table description.

### `create_prompt(self, prompt_request: PromptRequest) -> PromptResponse`
- **Parameters**:
  - `prompt_request`: An instance of `PromptRequest` containing the parameters for creating a new prompt.
- **Returns**: A `PromptResponse` object containing the details of the created prompt.

### `get_prompt(self, prompt_id) -> PromptResponse`
- **Parameters**:
  - `prompt_id`: A string representing the unique identifier of the prompt to retrieve.
- **Returns**: A `PromptResponse` object containing the details of the requested prompt.

### `update_prompt(self, prompt_id: str, update_metadata_request: UpdateMetadataRequest) -> PromptResponse`
- **Parameters**:
  - `prompt_id`: A string representing the unique identifier of the prompt to update.
  - `update_metadata_request`: An instance of `UpdateMetadataRequest` containing the updated metadata for the prompt.
- **Returns**: An updated `PromptResponse` object.

### `get_prompts(self, db_connection_id: str | None = None) -> List[PromptResponse]`
- **Parameters**:
  - `db_connection_id`: An optional string representing the unique identifier of the database connection to filter prompts.
- **Returns**: A list of `PromptResponse` objects for the specified database connection.

### `add_golden_sqls(self, golden_sqls: List[GoldenSQLRequest]) -> List[GoldenSQLResponse]`
- **Parameters**:
  - `golden_sqls`: A list of `GoldenSQLRequest` objects containing the parameters for adding new golden SQLs.
- **Returns**: A list of `GoldenSQLResponse` objects containing the details of the added golden SQLs.

### `execute_sql_query(self, sql_generation_id: str, max_rows: int = 100) -> list`
- **Parameters**:
  - `sql_generation_id`: A string representing the unique identifier of the SQL generation to execute.
  - `max_rows`: An optional integer specifying the maximum number of rows to return.
- **Returns**: A list containing the results of the executed SQL query.

### `export_csv_file(self, sql_generation_id: str) -> io.StringIO`
- **Parameters**:
  - `sql_generation_id`: A string representing the unique identifier of the SQL generation to export as a CSV file.
- **Returns**: An `io.StringIO` object containing the CSV data.

### `get_query_history(self, db_connection_id: str) -> list[QueryHistory]`
- **Parameters**:
  - `db_connection_id`: A string representing the unique identifier of the database connection to retrieve the query history for.
- **Returns**: A list of `QueryHistory` objects containing the history of queries executed against the specified database connection.

### `delete_golden_sql(self, golden_sql_id: str) -> dict`
- **Parameters**:
  - `golden_sql_id`: A string representing the unique identifier of the golden SQL to delete.
- **Returns**: A dictionary containing the result of the deletion operation.

### `get_golden_sqls(self, db_connection_id: str = None, page: int = 1, limit: int = 10) -> List[GoldenSQL]`
- **Parameters**:
  - `db_connection_id`: An optional string representing the unique identifier of the database connection to filter golden SQLs.
  - `page`: An optional integer representing the page number for pagination.
  - `limit`: An optional integer representing the number of items per page for pagination.
- **Returns**: A list of `GoldenSQL` objects for the specified database connection and pagination parameters.

### `update_golden_sql(self, golden_sql_id: str, update_metadata_request: UpdateMetadataRequest) -> GoldenSQL`
- **Parameters**:
  - `golden_sql_id`: A string representing the unique identifier of the golden SQL to update.
  - `update_metadata_request`: An instance of `UpdateMetadataRequest` containing the updated metadata for the golden SQL.
- **Returns**: An updated `GoldenSQL` object.

### `add_instruction(self, instruction_request: InstructionRequest) -> InstructionResponse`
- **Parameters**:
  - `instruction_request`: An instance of `InstructionRequest` containing the parameters for adding a new instruction.
- **Returns**: An `InstructionResponse` object containing the details of the added instruction.

### `get_instructions(self, db_connection_id: str = None, page: int = 1, limit: int = 10) -> List[InstructionResponse]`
- **Parameters**:
  - `db_connection_id`: An optional string representing the unique identifier of the database connection to filter instructions.
  - `page`: An optional integer representing the page number for pagination.
  - `limit`: An optional integer representing the number of items per page for pagination.
- **Returns**: A list of `InstructionResponse` objects for the specified database connection and pagination parameters.

### `delete_instruction(self, instruction_id: str) -> dict`
- **Parameters**:
  - `instruction_id`: A string representing the unique identifier of the instruction to delete.
- **Returns**: A dictionary containing the result of the deletion operation.

### `update_instruction(self, instruction_id: str, instruction_request: UpdateInstruction) -> InstructionResponse`
- **Parameters**:
  - `instruction_id`: A string representing the unique identifier of the instruction to update.
  - `instruction_request`: An instance of `UpdateInstruction` containing the updated parameters for the instruction.
- **Returns**: An updated `InstructionResponse` object.

### `create_finetuning_job(self, fine_tuning_request: FineTuningRequest, background_tasks: BackgroundTasks) -> Finetuning`
- **Parameters**:
  - `fine_tuning_request`: An instance of `FineTuningRequest` containing the parameters for creating a new fine-tuning job.
  - `background_tasks`: An instance of `BackgroundTasks` for running operations in the background.
- **Returns**: A `Finetuning` object containing the details of the created fine-tuning job.

### `cancel_finetuning_job(self, cancel_fine_tuning_request: CancelFineTuningRequest) -> Finetuning`
- **Parameters**:
  - `cancel_fine_tuning_request`: An instance of `CancelFineTuningRequest` containing the parameters for canceling a fine-tuning job.
- **Returns**: A `Finetuning` object containing the details of the canceled fine-tuning job.

### `get_finetunings(self, db_connection_id: str | None = None) -> list[Finetuning]`
- **Parameters**:
  - `db_connection_id`: An optional string representing the unique identifier of the database connection to filter fine-tuning jobs.
- **Returns**: A list of `Finetuning` objects for the specified database connection.

### `delete_finetuning_job(self, finetuning_job_id: str) -> dict`
- **Parameters**:
  - `finetuning_job_id`: A string representing the unique identifier of the fine-tuning job to delete.
- **Returns**: A dictionary containing the result of the deletion operation.

### `get_finetuning_job(self, finetuning_job_id: str) -> Finetuning`
- **Parameters**:
  - `finetuning_job_id`: A string representing the unique identifier of the fine-tuning job to retrieve.
- **Returns**: A `Finetuning` object containing the details of the requested fine-tuning job.

### `update_finetuning_job(self, finetuning_job_id: str, update_metadata_request: UpdateMetadataRequest) -> Finetuning`
- **Parameters**:
  - `finetuning_job_id`: A string representing the unique identifier of the fine-tuning job to update.
  - `update_metadata_request`: An instance of `UpdateMetadataRequest` containing the updated metadata for the fine-tuning job.
- **Returns**: An updated `Finetuning` object.

### `create_sql_generation(self, prompt_id: str, sql_generation_request: SQLGenerationRequest) -> SQLGenerationResponse`
- **Parameters**:
  - `prompt_id`: A string representing the unique identifier of the prompt associated with the SQL generation.
  - `sql_generation_request`: An instance of `SQLGenerationRequest` containing the parameters for creating a new SQL generation.
- **Returns**: A `SQLGenerationResponse` object containing the details of the created SQL generation.

### `create_prompt_and_sql_generation(self, prompt_sql_generation_request: PromptSQLGenerationRequest) -> SQLGenerationResponse`
- **Parameters**:
  - `prompt_sql_generation_request`: An instance of `PromptSQLGenerationRequest` containing the parameters for creating a new prompt and associated SQL generation.
- **Returns**: A `SQLGenerationResponse` object containing the details of the created prompt and SQL generation.

### `get_sql_generations(self, prompt_id: str | None = None) -> list[SQLGenerationResponse]`
- **Parameters**:
  - `prompt_id`: An optional string representing the unique identifier of the prompt to filter SQL generations.
- **Returns**: A list of `SQLGenerationResponse` objects for the specified prompt.

### `get_sql_generation(self, sql_generation_id: str) -> SQLGenerationResponse`
- **Parameters**:
  - `sql_generation_id`: A string representing the unique identifier of the SQL generation to retrieve.
- **Returns**: A `SQLGenerationResponse` object containing the details of the requested SQL generation.

### `update_sql_generation(self, sql_generation_id: str, update_metadata_request: UpdateMetadataRequest) -> SQLGenerationResponse`
- **Parameters**:
  - `sql_generation_id`: A string representing the unique identifier of the SQL generation to update.
  - `update_metadata_request`: An instance of `UpdateMetadataRequest` containing the updated metadata for the SQL generation.
- **Returns**: An updated `SQLGenerationResponse` object.

### `create_nl_generation(self, sql_generation_id: str, nl_generation_request: NLGenerationRequest) -> NLGenerationResponse`
- **Parameters**:
  - `sql_generation_id`: A string representing the unique identifier of the SQL generation associated with the NL generation.
  - `nl_generation_request`: An instance of `NLGenerationRequest` containing the parameters for creating a new NL generation.
- **Returns**: A `NLGenerationResponse` object containing the details of the created NL generation.

### `create_sql_and_nl_generation(self, prompt_id: str, nl_generation_sql_generation_request: NLGenerationsSQLGenerationRequest) -> NLGenerationResponse`
- **Parameters**:
  - `prompt_id`: A string representing the unique identifier of the prompt associated with the SQL and NL generation.
  - `nl_generation_sql_generation_request`: An instance of `NLGenerationsSQLGenerationRequest` containing the parameters for creating a new SQL and NL generation.
- **Returns**: A `NLGenerationResponse` object containing the details of the created SQL and NL generation.

### `create_prompt_sql_and_nl_generation(self, request: PromptSQLGenerationNLGenerationRequest) -> NLGenerationResponse`
- **Parameters**:
  - `request`: An instance of `PromptSQLGenerationNLGenerationRequest` containing the parameters for creating a new prompt, SQL generation, and NL generation.
- **Returns**: A `NLGenerationResponse` object containing the details of the created prompt, SQL generation, and NL generation.

### `get_nl_generations(self, sql_generation_id: str | None = None) -> list[NLGenerationResponse]`
- **Parameters**:
  - `sql_generation_id`: An optional string representing the unique identifier of the SQL generation to filter NL generations.
- **Returns**: A list of `NLGenerationResponse` objects for the specified SQL generation.

### `get_nl_generation(self, nl_generation_id: str) -> NLGenerationResponse`
- **Parameters**:
  - `nl_generation_id`: A string representing the unique identifier of the NL generation to retrieve.
- **Returns**: A `NLGenerationResponse` object containing the details of the requested NL generation.

### `update_nl_generation(self, nl_generation_id: str, update_metadata_request: UpdateMetadataRequest) -> NLGenerationResponse`
- **Parameters**:
  - `nl_generation_id`: A string representing the unique identifier of the NL generation to update.
  - `update_metadata_request`: An instance of `UpdateMetadataRequest` containing the updated metadata for the NL generation.
- **Returns**: An updated `NLGenerationResponse` object.

### `stream_create_prompt_and_sql_generation(self, request: StreamPromptSQLGenerationRequest)`
- **Parameters**:
  - `request`: An instance of `StreamPromptSQLGenerationRequest` containing the parameters for creating a new prompt and associated SQL generation in a streaming fashion.
- **Returns**: This method is asynchronous and does not return a value directly. It is intended to be used for streaming responses back to the client.

## Usage

The `API` class is designed to be subclassed by concrete implementations that provide the functionality for each abstract method. These implementations will be used to handle API requests in a web server context, typically with a framework like FastAPI. The methods correspond to various endpoints that clients can call to perform operations related to data processing and generation.

Each method is marked with the `@abstractmethod` decorator, indicating that subclasses must provide an implementation for the method. The methods cover a wide range of functionalities, from managing database connections and table descriptions to generating SQL and natural language responses based on prompts.

The class also makes use of Python's type hinting feature to specify the expected types for parameters and return values, providing clear documentation and enabling better static analysis of the code.

The `API` class is a central part of the project's backend architecture, serving as the interface between the client applications and the underlying data processing and generation logic.
```