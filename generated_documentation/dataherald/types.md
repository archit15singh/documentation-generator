```markdown
# Types.py Module Documentation

## Overview
The `types.py` module defines a collection of classes that represent various data structures and enumerations used throughout the `dataherald` project. These classes are primarily used for data validation, serialization, and deserialization of information related to database connections, SQL queries, instructions, and machine learning model configurations.

## Classes

### `DBConnectionValidation`
- **Description**: A base model for validating a database connection identifier.
- **Attributes**:
  - `db_connection_id`: A string representing the database connection ID.
- **Validators**:
  - `object_id_validation`: Ensures that the `db_connection_id` is a valid `ObjectId`.

### `SQLQueryResult`
- **Description**: Represents the result of an SQL query.
- **Attributes**:
  - `columns`: A list of strings representing the column names.
  - `rows`: A list of dictionaries, each representing a row of data.

### `UpdateInstruction`
- **Description**: Encapsulates an update instruction and its associated metadata.
- **Attributes**:
  - `instruction`: A string containing the update instruction.
  - `metadata`: An optional dictionary containing additional information.

### `InstructionRequest`
- **Description**: Represents a request for an instruction, inheriting from `DBConnectionValidation`.
- **Attributes**:
  - `instruction`: An optional string containing the instruction (minimum length of 3 characters).
  - `metadata`: An optional dictionary containing additional information.

### `RefreshTableDescriptionRequest`
- **Description**: A request to refresh the description of a table, inheriting from `DBConnectionValidation`.

### `Instruction`
- **Description**: Represents an instruction with associated metadata.
- **Attributes**:
  - `id`: An optional string identifier for the instruction.
  - `instruction`: A string containing the instruction.
  - `db_connection_id`: A string representing the database connection ID.
  - `created_at`: A `datetime` object representing the creation time.
  - `metadata`: An optional dictionary containing additional information.

### `GoldenSQLRequest`
- **Description**: Represents a request for a golden SQL query, inheriting from `DBConnectionValidation`.
- **Attributes**:
  - `prompt_text`: An optional string containing the prompt text (minimum length of 3 characters).
  - `sql`: An optional string containing the SQL query (minimum length of 3 characters).
  - `metadata`: An optional dictionary containing additional information.

### `GoldenSQL`
- **Description**: Represents a golden SQL query with associated metadata.
- **Attributes**:
  - `id`: An optional string identifier for the golden SQL.
  - `prompt_text`: A string containing the prompt text.
  - `sql`: A string containing the SQL query.
  - `db_connection_id`: A string representing the database connection ID.
  - `created_at`: A `datetime` object representing the creation time.
  - `metadata`: An optional dictionary containing additional information.

### `SQLGenerationStatus`
- **Description**: An enumeration of possible statuses for SQL generation.
- **Values**: `NONE`, `VALID`, `INVALID`.

### `SupportedDatabase`
- **Description**: An enumeration of supported database types.
- **Values**: `POSTGRES`, `DATABRICKS`, `SNOWFLAKE`, `SQLSERVER`, `BIGQUERY`.

### `ScannerRequest`
- **Description**: Represents a request to scan database tables, inheriting from `DBConnectionValidation`.
- **Attributes**:
  - `table_names`: An optional list of strings representing table names.
  - `metadata`: An optional dictionary containing additional information.

### `DatabaseConnectionRequest`
- **Description**: Represents a request to connect to a database.
- **Attributes**:
  - `alias`: A string representing the alias for the connection.
  - `use_ssh`: A boolean indicating whether to use SSH for the connection.
  - `connection_uri`: A string containing the connection URI.
  - `path_to_credentials_file`: An optional string representing the path to the credentials file.
  - `llm_api_key`: An optional string representing the API key for the language model.
  - `ssh_settings`: An optional `SSHSettings` object containing SSH configuration.
  - `file_storage`: An optional `FileStorage` object containing file storage configuration.
  - `metadata`: An optional dictionary containing additional information.

### `ForeignKeyDetail`
- **Description**: Represents the details of a foreign key in a database.
- **Attributes**:
  - `field_name`: A string representing the field name of the foreign key.
  - `reference_table`: A string representing the reference table for the foreign key.

### `ColumnDescriptionRequest`
- **Description**: Represents a request to describe a database column.
- **Attributes**:
  - `name`: A string representing the column name.
  - `description`: An optional string representing the column description.
  - `is_primary_key`: An optional boolean indicating if the column is a primary key.
  - `data_type`: An optional string representing the data type of the column.
  - `low_cardinality`: An optional boolean indicating if the column has low cardinality.
  - `categories`: An optional list of strings representing the categories for the column.
  - `foreign_key`: An optional `ForeignKeyDetail` object representing the foreign key details.

### `TableDescriptionRequest`
- **Description**: Represents a request to describe a database table.
- **Attributes**:
  - `description`: An optional string representing the table description.
  - `columns`: An optional list of `ColumnDescriptionRequest` objects representing the columns of the table.
  - `metadata`: An optional dictionary containing additional information.

### `FineTuningStatus`
- **Description**: An enumeration of possible statuses for fine-tuning a language model.
- **Values**: `QUEUED`, `RUNNING`, `SUCCEEDED`, `FAILED`, `CANCELLED`, `VALIDATING_FILES`.

### `BaseLLM`
- **Description**: Represents the base configuration for a language learning model (LLM).
- **Attributes**:
  - `model_provider`: An optional string representing the model provider.
  - `model_name`: An optional string representing the name of the model.
  - `model_parameters`: An optional dictionary of strings representing model parameters.
- **Validators**:
  - `validate_model_name`: Ensures that the `model_name` is supported.

### `Finetuning`
- **Description**: Represents the fine-tuning configuration for a language model.
- **Attributes**:
  - `id`: An optional string identifier for the fine-tuning configuration.
  - `alias`: An optional string representing the alias for the fine-tuning.
  - `db_connection_id`: An optional string representing the database connection ID.
  - `status`: A string representing the status of the fine-tuning (default is `QUEUED`).
  - `error`: An optional string representing any error that occurred.
  - `base_llm`: An optional `BaseLLM` object representing the base language model configuration.
  - `finetuning_file_id`: An optional string representing the ID of the fine-tuning file.
  - `finetuning_job_id`: An optional string representing the ID of the fine-tuning job.
  - `model_id`: An optional string representing the ID of the model.
  - `created_at`: A `datetime` object representing the creation time.
  - `golden_sqls`: An optional list of strings representing golden SQL queries.
  - `metadata`: An optional dictionary containing additional information.

### `FineTuningRequest`
- **Description**: Represents a request to fine-tune a language model.
- **Attributes**:
  - `db_connection_id`: A string representing the database connection ID.
  - `alias`: An optional string representing the alias for the fine-tuning.
  - `base_llm`: An optional `BaseLLM` object representing the base language model configuration.
  - `golden_sqls`: An optional list of strings representing golden SQL queries.
  - `metadata`: An optional dictionary containing additional information.

### `CancelFineTuningRequest`
- **Description**: Represents a request to cancel fine-tuning of a language model.
- **Attributes**:
  - `finetuning_id`: A string representing the ID of the fine-tuning configuration.
  - `metadata`: An optional dictionary containing additional information.

### `Prompt`
- **Description**: Represents a prompt used for generating SQL or natural language.
- **Attributes**:
  - `id`: An optional string identifier for the prompt.
  - `text`: A string containing the prompt text.
  - `db_connection_id`: A string representing the database connection ID.
  - `created_at`: A `datetime` object representing the creation time.
  - `metadata`: An optional dictionary containing additional information.

### `LLMConfig`
- **Description**: Represents the configuration for a language learning model.
- **Attributes**:
  - `llm_name`: A string representing the name of the language learning model (default is obtained from the environment variable `LLM_NAME`).
  - `api_base`: An optional string representing the base URL for the API.

### `SQLGeneration`
- **Description**: Represents the generation of an SQL query from a prompt.
- **Attributes**:
  - `id`: An optional string identifier for the SQL generation.
  - `prompt_id`: A string representing the ID of the associated prompt.
  - `finetuning_id`: An optional string representing the ID of the fine-tuning configuration.
  - `low_latency_mode`: A boolean indicating if low latency mode is enabled (default is `False`).
  - `llm_config`: An optional `LLMConfig` object representing the language model configuration.
  - `evaluate`: A boolean indicating if the SQL should be evaluated (default is `False`).
  - `sql`: An optional string containing the generated SQL query.
  - `status`: A string representing the status of the SQL generation (default is `INVALID`).
  - `completed_at`: An optional `datetime` object representing the completion time.
  - `tokens_used`: An optional integer representing the number of tokens used.
  - `confidence_score`: An optional float representing the confidence score.
  - `error`: An optional string representing any error that occurred.
  - `created_at`: A `datetime` object representing the creation time.
  - `metadata`: An optional dictionary containing additional information.

### `NLGeneration`
- **Description**: Represents the generation of natural language from an SQL query.
- **Attributes**:
  - `id`: An optional string identifier for the natural language generation.
  - `sql_generation_id`: A string representing the ID of the associated SQL generation.
  - `llm_config`: An optional `LLMConfig` object representing the language model configuration.
  - `text`: An optional string containing the generated natural language.
  - `created_at`: A `datetime` object representing the creation time.
  - `metadata`: An optional dictionary containing additional information.

## Usage
The classes defined in this module are used throughout the `dataherald` project to facilitate the following:
- Validation of input data for API endpoints and internal functions.
- Serialization of data to JSON for API responses.
- Deserialization of JSON data into Python objects for processing.
- Configuration of language learning models and fine-tuning processes.
- Representation of SQL and natural language generation requests and results.

Each class is equipped with Pydantic's `BaseModel`, which provides automatic validation, serialization, and deserialization capabilities. Enumerations are used to define a set of valid constants for certain fields, ensuring that only allowed values are used.

The validators, such as `object_id_validation` and `validate_model_name`, provide additional constraints and checks that are specific to the project's requirements, such as ensuring the validity of MongoDB `ObjectId` strings or checking if a model name is supported for fine-tuning.

The module also utilizes environment variables (e.g., `LLM_NAME`) to configure default values for certain fields, allowing for flexibility and configurability without hardcoding values within the codebase.
```