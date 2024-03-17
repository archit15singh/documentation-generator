File Path: /workspaces/documentation-generator/generated_documentation/dataherald/config.md

# `config.py` Module Documentation

## Overview

The `config.py` module is part of the `dataherald` project and is responsible for managing configuration settings, abstract component instantiation, and system-wide component management. It defines classes for loading environment-specific settings, abstract component definitions, and a system class to manage component instances.

## Classes and Functions

### `Settings` Class

The `Settings` class inherits from `BaseSettings` provided by the `pydantic` library. It is used to define and access configuration settings for the `dataherald` project.

#### Attributes

- `api_impl`: Specifies the implementation class for the API server.
- `db_scanner_impl`: Specifies the implementation class for the database scanner.
- `eval_impl`: Specifies the implementation class for the evaluator.
- `db_impl`: Specifies the implementation class for the database.
- `context_store_impl`: Specifies the implementation class for the context store.
- `vector_store_impl`: Specifies the implementation class for the vector store.
- `db_name`: The name of the MongoDB database.
- `db_uri`: The URI for connecting to MongoDB.
- `openai_api_key`: The API key for OpenAI services.
- `encrypt_key`: The encryption key used for secure operations.
- `s3_aws_access_key_id`: The AWS access key ID for S3 services.
- `s3_aws_secret_access_key`: The AWS secret access key for S3 services.
- `only_store_csv_files_locally`: A flag indicating whether to store CSV files only locally.

#### Methods

- `require(key: str) -> Any`: Ensures that a configuration value is present and returns it.
- `__getitem__(key: str) -> Any`: Allows dictionary-like access to configuration attributes.

### `Component` Abstract Class

The `Component` class is an abstract base class that defines a common interface for all components in the system. It enforces method overrides using the `EnforceOverrides` mixin.

#### Attributes

- `_running`: A boolean indicating whether the component is currently running.

#### Methods

- `stop() -> None`: Stops the component and frees associated resources.
- `start() -> None`: Starts the component.

### `System` Class

The `System` class is a concrete implementation of `Component` and is responsible for managing instances of components within the system.

#### Attributes

- `settings`: An instance of the `Settings` class containing configuration settings.
- `_instances`: A dictionary mapping component types to their instances.

#### Methods

- `instance(type: Type[T]) -> T`: Returns an instance of the specified component type, starting it if the system is running.

### `get_class(fqn: str, type: Type[C]) -> Type[C]`

A function that imports a module given its fully qualified name (FQN) and returns the specified class.

### `get_fqn(cls: Type[object]) -> str`

A function that returns the fully qualified name of a given class.

## Usage

1. The `Settings` class is instantiated, typically at the start of the application, to load and access configuration settings from environment variables.
2. The `System` class is instantiated with an instance of `Settings`. It manages component instances and ensures that abstract components are instantiated with their concrete implementations as defined in the settings.
3. Components within the system can be started or stopped using their respective methods, and new component instances can be retrieved using the `System` instance's `instance` method.
4. The `get_class` and `get_fqn` functions are utility functions used internally by the `System` class to handle dynamic importing and instantiation of components based on their fully qualified names.

## Configuration

The module uses environment variables to configure the system. It expects the following environment variables to be set:

- `API_SERVER`
- `DB_SCANNER`
- `EVALUATOR`
- `DB`
- `CONTEXT_STORE`
- `VECTOR_STORE`
- `MONGODB_DB_NAME`
- `MONGODB_URI`
- `OPENAI_API_KEY`
- `ENCRYPT_KEY`
- `S3_AWS_ACCESS_KEY_ID`
- `S3_AWS_SECRET_ACCESS_KEY`
- `ONLY_STORE_CSV_FILES_LOCALLY`

If these variables are not set, default values are used where provided. The `Settings` class uses the `dotenv` library to load these variables from a `.env` file at runtime.

## Abstract Type Keys

The module defines a dictionary `_abstract_type_keys` that maps abstract component types to their corresponding environment variable keys. This mapping is used by the `System` class to resolve and instantiate concrete implementations of abstract components.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/types.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/app.md

# `app.py` Technical Documentation

## Overview

The `app.py` file is a Python script that serves as the entry point for a web application built using the `dataherald` package. It is responsible for initializing the application settings, creating a FastAPI server instance, and exposing the FastAPI application object.

## Dependencies

- `dataherald`: A custom Python package that provides functionality for data processing and web service creation.
- `dataherald.config`: A module within the `dataherald` package that contains configuration management utilities.
- `dataherald.server.fastapi`: A module within the `dataherald` package that provides FastAPI server integration.

## Detailed Steps

1. **Import Modules:**
   The script starts by importing the necessary modules from the `dataherald` package.

   - `import dataherald`: Imports the main `dataherald` package.
   - `import dataherald.config`: Imports the `config` module from `dataherald` for accessing configuration settings.
   - `from dataherald.server.fastapi import FastAPI`: Imports the `FastAPI` class from the `server.fastapi` module within `dataherald`.

2. **Load Settings:**
   An instance of the `Settings` class is created by calling `dataherald.config.Settings()`. This instance is responsible for loading and managing the application's configuration settings, such as environment variables, default values, and any other necessary configuration data.

   - `settings = dataherald.config.Settings()`: Creates a `Settings` object that holds the application's configuration.

3. **Create FastAPI Server Instance:**
   A `FastAPI` server instance is created by passing the `settings` object to the `FastAPI` class constructor. This server instance is responsible for setting up the FastAPI application with the provided settings.

   - `server = FastAPI(settings)`: Instantiates a `FastAPI` server with the loaded settings.

4. **Expose FastAPI Application Object:**
   The FastAPI application object is obtained by calling the `app()` method on the `server` instance. This object is the core of the FastAPI application and is used to register routes, middleware, and event handlers.

   - `app = server.app()`: Retrieves the FastAPI application object from the server instance.

## Usage

The `app.py` file is typically used as the main module that gets executed to start the web application. It can be run directly by a Python interpreter or used with a WSGI server like `uvicorn` to serve the application over a network.

To run the application, one might execute a command such as:

bash
uvicorn workspaces.documentation-generator.target_code.dataherald.app:app --reload


This command would start the FastAPI application and listen for incoming HTTP requests, serving the application's endpoints as defined within the `dataherald` package.

## Integration

The `app.py` file integrates with other parts of the `dataherald` project by using the configuration and server modules to set up the application environment and HTTP server. It is a critical component that brings together various modules to create a cohesive and functional web service.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/__init__.md

# `dataherald` Package

The `dataherald` package is designed to provide an interface for interacting with a data processing and notification system. It is structured as a Python module that can be imported into other Python scripts or applications to leverage its functionality.

## Modules and Sub-packages

The package consists of the following main components:

- `api`: A submodule that contains the `API` class, which provides the methods for interacting with the data processing system.
- `config`: A submodule that contains the `Settings` and `System` classes, which are used for configuring the system's behavior and initializing system components respectively.

## Global Variables

- `__settings`: An instance of the `Settings` class, which holds the default configuration for the system. This instance is used as the default settings when initializing the `API` client.
- `__version__`: A string that represents the current version of the `dataherald` package. This can be used for logging, debugging, or compatibility checks.

## Functions

### `client(settings: Settings = __settings) -> API`

The `client` function is the primary entry point for users of the `dataherald` package to obtain an instance of the `API` class, which is ready to use for interacting with the system.

#### Parameters:

- `settings`: An optional parameter of type `Settings`. If provided, it will be used to configure the system. If not provided, the default `__settings` instance will be used.

#### Returns:

- An instance of the `API` class, which has been initialized and started, ready for use.

#### Behavior:

1. The function accepts an optional `settings` parameter, which allows the caller to specify custom settings for the system. If no custom settings are provided, the default `__settings` instance is used.
2. A `System` instance is created by passing the `settings` to its constructor. The `System` class is responsible for managing the lifecycle and dependencies of system components.
3. The `instance` method of the `System` class is called with the `API` class as its argument. This method is responsible for creating an instance of the `API` class, which serves as the interface for the data processing system.
4. The `start` method of the `System` class is called to initialize and start any necessary components or services required by the `API` instance.
5. The fully initialized `API` instance is returned to the caller.

## Usage

To use the `dataherald` package, a developer would typically import the `client` function from the package and call it to obtain an `API` instance. They can then use this instance to interact with the data processing system.

Example:

python
from dataherald import client

# Initialize the API client with default settings
api = client()

# Use the API instance to perform operations
result = api.some_method()


If custom settings are needed, the developer can create an instance of the `Settings` class, modify it as needed, and pass it to the `client` function.

Example:

python
from dataherald import client
from dataherald.config import Settings

# Create custom settings
custom_settings = Settings()
custom_settings.some_option = 'custom_value'

# Initialize the API client with custom settings
api = client(settings=custom_settings)

# Use the API instance to perform operations
result = api.some_method()


The `dataherald` package abstracts the complexity of system initialization and configuration, providing a simple interface for developers to interact with the data processing system.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/context_store/default.md

# DefaultContextStore Class

## Overview
`DefaultContextStore` is a subclass of `ContextStore` that provides concrete implementations for methods to interact with a context store in the `dataherald` project. This class is responsible for retrieving context for a given question, adding new golden SQL queries to the context store, and removing existing golden SQL queries.

## Attributes
- Inherits all attributes from the `ContextStore` base class.

## Methods

### `__init__(self, system: System)`
Constructor for the `DefaultContextStore` class.

#### Parameters:
- `system` (`System`): An instance of the `System` class containing configuration and state for the current system.

#### Behavior:
- Calls the constructor of the base class `ContextStore` with the `system` parameter.

### `retrieve_context_for_question(self, prompt: Prompt, number_of_samples: int = 3) -> Tuple[List[dict] | None, List[dict] | None]`
Retrieves context for a given question by querying the vector store and fetching related instructions from the database.

#### Parameters:
- `prompt` (`Prompt`): An instance of `Prompt` containing the text of the question and the database connection ID.
- `number_of_samples` (`int`, optional): The number of similar questions to retrieve. Defaults to 3.

#### Returns:
- A tuple containing two lists or `None`:
  - The first list contains dictionaries with keys `prompt_text`, `sql`, and `score` representing similar questions and their associated SQL queries.
  - The second list contains dictionaries with the key `instruction` representing related instructions.

#### Behavior:
- Logs the retrieval attempt for the given prompt.
- Queries the vector store for similar questions based on the prompt text and database connection ID.
- Fetches the golden SQL queries from the `GoldenSQLRepository` using the IDs of the closest questions.
- Compiles a list of samples with the prompt text, SQL, and score of each golden SQL query.
- Fetches all instructions from the `InstructionRepository` and filters them based on the database connection ID.
- Compiles a list of instructions relevant to the prompt.
- Returns the samples and instructions, or `None` if no samples or instructions are found.

### `add_golden_sqls(self, golden_sqls: List[GoldenSQLRequest]) -> List[GoldenSQL]`
Adds new golden SQL queries to the context store and creates embeddings for them.

#### Parameters:
- `golden_sqls` (`List[GoldenSQLRequest]`): A list of `GoldenSQLRequest` instances representing the golden SQL queries to be added.

#### Returns:
- A list of `GoldenSQL` instances that have been successfully added to the context store.

#### Behavior:
- Initializes a `GoldenSQLRepository` to interact with the database.
- Initializes a `DatabaseConnectionRepository` to validate database connections.
- Iterates over the provided golden SQL requests, parsing and validating the SQL syntax.
- Raises `MalformedGoldenSQLError` if the SQL syntax is invalid.
- Checks for the existence of the database connection using the provided ID and raises `DatabaseConnectionNotFoundError` if not found.
- Inserts the golden SQL queries into the `GoldenSQLRepository`.
- Adds the records to the vector store for future querying.
- Returns the list of stored golden SQL instances.

### `remove_golden_sqls(self, ids: List) -> bool`
Removes golden SQL queries from the context store.

#### Parameters:
- `ids` (`List`): A list of IDs representing the golden SQL queries to be removed.

#### Returns:
- `True` indicating the operation was successful.

#### Behavior:
- Initializes a `GoldenSQLRepository` to interact with the database.
- Iterates over the provided IDs, deleting the corresponding records from the vector store and the `GoldenSQLRepository`.
- Logs a warning if a record with the given ID is not found.
- Returns `True` after all specified records have been removed.

## Exceptions

### `MalformedGoldenSQLError`
Custom exception class that is raised when a provided SQL query is malformed.

### `DatabaseConnectionNotFoundError`
Custom exception class that is raised when a specified database connection ID is not found in the repository.

## Usage
The `DefaultContextStore` class is used within the `dataherald` project to manage the context for generating SQL queries based on natural language prompts. It interacts with repositories and vector stores to provide relevant context and maintain the collection of golden SQL queries.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/context_store/__init__.md

# ContextStore Module

## Overview

The `ContextStore` module, located at `/workspaces/documentation-generator/target_code/dataherald/context_store/__init__.py`, is an abstract base class that defines the interface for context storage in the DataHerald project. It is designed to interact with a database and a vector store to manage and retrieve context-related data for given prompts. The module is part of the `dataherald` package and is intended to be subclassed by concrete implementations that provide the actual storage and retrieval logic.

## Dependencies

- `os`: Standard Python module to interact with the operating system.
- `abc.ABC, abc.abstractmethod`: Abstract Base Classes (ABC) module to define abstract base classes and abstract methods.
- `typing.List, typing.Tuple`: Typing module to specify type hints for lists and tuples.
- `dataherald.config.Component, dataherald.config.System`: Configuration classes from the `dataherald.config` module.
- `dataherald.db.DB`: Database class from the `dataherald.db` module.
- `dataherald.types.GoldenSQL, dataherald.types.GoldenSQLRequest, dataherald.types.Prompt`: Custom types from the `dataherald.types` module.
- `dataherald.vector_store.VectorStore`: VectorStore class from the `dataherald.vector_store` module.

## Class Definition

### ContextStore

`ContextStore` is an abstract base class that inherits from `Component` and `ABC`. It defines the structure and required methods for context storage components within the DataHerald project.

#### Attributes

- `DocStore: DB`: A class attribute that specifies the type of document store to be used, which is a database (`DB`).
- `VectorStore: VectorStore`: A class attribute that specifies the type of vector store to be used.
- `doc_store_collection: str`: A class attribute that holds the name of the collection within the document store where table metadata is stored.

#### Abstract Methods

1. `__init__(self, system: System)`: An abstract method that initializes the `ContextStore` with a reference to the `System` instance. It also initializes the database connection and the vector store, and sets the `golden_sql_collection` attribute based on an environment variable or a default value.

2. `retrieve_context_for_question(self, prompt: Prompt, number_of_samples: int = 3) -> Tuple[List[dict] | None, List[dict] | None]`: An abstract method that, when implemented, should retrieve context information for a given prompt. The method takes a `Prompt` object and an optional `number_of_samples` parameter, returning a tuple containing two lists of dictionaries or `None`.

3. `add_golden_sqls(self, golden_sqls: List[GoldenSQLRequest]) -> List[GoldenSQL]`: An abstract method that, when implemented, should add a list of `GoldenSQLRequest` objects to the context store and return a list of `GoldenSQL` objects representing the added SQLs.

4. `remove_golden_sqls(self, ids: List) -> bool`: An abstract method that, when implemented, should remove golden SQL entries based on a list of identifiers. It should return a boolean indicating the success of the operation.

## Usage

The `ContextStore` class is not intended to be instantiated directly. Instead, it serves as a blueprint for concrete subclasses that implement the abstract methods. These subclasses will provide the functionality to store and retrieve context data, manage golden SQL queries, and interact with the document and vector stores as required by the DataHerald project.

Concrete implementations of `ContextStore` must provide the logic for connecting to the appropriate data stores, handling data queries, and managing the lifecycle of context-related data within the system.

## Environment Variables

- `GOLDEN_SQL_COLLECTION`: An environment variable that can be set to specify the name of the collection within the database where golden SQL queries are stored. If not set, the default value is `"dataherald-staging"`.

## Notes

- The `ContextStore` class is designed to be flexible and extensible, allowing for different storage backends and retrieval strategies to be implemented as needed.
- The use of abstract methods enforces a consistent interface for all context store implementations, ensuring that they can be used interchangeably within the DataHerald project.
- The `number_of_samples` parameter in the `retrieve_context_for_question` method allows for control over the amount of context data retrieved, which can be useful for performance tuning or limiting the scope of the context.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/services/nl_generations.md

# NLGenerationService Class

## Overview

`NLGenerationService` is a class within the `dataherald.services.nl_generations` module. It provides services for creating and managing natural language (NL) generations based on SQL generation data. The class interacts with repositories to store and retrieve NL generation records and uses a natural language generator to convert SQL data into human-readable text.

## Attributes

- `system`: An instance of `System` from `dataherald.config`, which likely contains configuration settings for the service.
- `storage`: A storage backend that is used to persist data. The exact type of storage is not specified in the provided code but is expected to be compatible with the repositories used.
- `nl_generation_repository`: An instance of `NLGenerationRepository` that provides an interface to the NL generation data store.

## Methods

### `__init__(self, system: System, storage)`

The constructor initializes the `NLGenerationService` instance.

- **Parameters**:
  - `system`: An instance of `System` containing configuration settings.
  - `storage`: A storage backend for persisting NL generation data.

- **Functionality**:
  - Stores the `system` and `storage` parameters as instance attributes.
  - Initializes the `nl_generation_repository` with the provided `storage`.

### `create(self, sql_generation_id: str, nl_generation_request: NLGenerationRequest) -> NLGeneration`

Creates a new NL generation record based on a SQL generation ID and a request for NL generation.

- **Parameters**:
  - `sql_generation_id`: A string identifier for the associated SQL generation.
  - `nl_generation_request`: An instance of `NLGenerationRequest` containing the configuration and metadata for the NL generation.

- **Returns**:
  - An instance of `NLGeneration` representing the newly created NL generation record.

- **Functionality**:
  - Constructs an initial `NLGeneration` object with the current timestamp, provided SQL generation ID, LLM configuration, and metadata.
  - Inserts the initial NL generation record into the repository.
  - Retrieves the associated SQL generation record using `SQLGenerationRepository`.
  - If the SQL generation is not found, raises `SQLGenerationNotFoundError`.
  - Initializes an `GeneratesNlAnswer` object with the system configuration and LLM configuration.
  - Executes the NL generation process using the retrieved SQL generation and the `top_k` parameter from the request.
  - If an error occurs during NL generation, raises `NLGenerationError`.
  - Updates the initial NL generation record with the generated text and returns the updated record.

### `get(self, query) -> list[NLGeneration]`

Retrieves a list of NL generation records based on a query.

- **Parameters**:
  - `query`: A query object or parameters to filter the NL generation records.

- **Returns**:
  - A list of `NLGeneration` instances that match the query.

- **Functionality**:
  - Uses the `nl_generation_repository` to find records that match the provided query.

### `update_metadata(self, nl_generation_id, metadata_request) -> NLGeneration`

Updates the metadata of an existing NL generation record.

- **Parameters**:
  - `nl_generation_id`: A string identifier for the NL generation to be updated.
  - `metadata_request`: An object containing the new metadata to be applied to the NL generation record.

- **Returns**:
  - The updated `NLGeneration` instance.

- **Functionality**:
  - Retrieves the NL generation record by its ID using the `nl_generation_repository`.
  - If the NL generation is not found, raises `NLGenerationNotFoundError`.
  - Updates the metadata of the retrieved NL generation record with the new metadata from the request.
  - Returns the updated NL generation record after saving the changes to the repository.

## Exceptions

- `NLGenerationError`: A custom exception class that is raised when an error occurs during the NL generation process.
- `NLGenerationNotFoundError`: Raised when an NL generation record cannot be found in the repository.
- `SQLGenerationNotFoundError`: Raised when an associated SQL generation record cannot be found in the repository.

## Usage

The `NLGenerationService` class is used within a project to facilitate the creation and management of NL generation records. It interacts with SQL generation data to produce human-readable text and provides an interface for updating and retrieving NL generation records. The service is likely used by higher-level application logic or API endpoints to process requests related to NL generation.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/services/sql_generations.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/services/__init__.md

# `__init__.py` in `dataherald/services`

## Overview

The `__init__.py` file within the `dataherald/services` directory serves as an initialization script for the `services` package in the `dataherald` project. This file can be used to expose specific classes, functions, or variables from within the package to simplify the import statements in other parts of the project that utilize the `services` package. It can also be used to run any initialization code required for the services to function correctly.

## Usage

When the `services` package is imported in other parts of the `dataherald` project, Python will execute the `__init__.py` file. The contents of this file determine what is available to be imported from the `services` package.

### Importing the Package

To import the `services` package from another module within the `dataherald` project, one would use the following import statement:

python
from dataherald.services import SomeService


In this example, `SomeService` is a class, function, or variable that has been explicitly made available in the `__init__.py` file.

### Exposing Package Contents

The `__init__.py` file can be used to expose specific components of the `services` package. For example:

python
from .service_module import ServiceClass

__all__ = ['ServiceClass']


In this case, `ServiceClass` from the `service_module.py` file within the same package is imported and added to the `__all__` list. This list defines the public interface of the package and what is exported when `import *` is used.

### Initialization Code

If the `services` package requires any setup before being used, such as configuring logging, setting up connections, or initializing state, this code can be placed within the `__init__.py` file.

Example of initialization code:

python
# Initialize logging for the services package
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Initializing the services package')

# Setup code for services
def _setup_services():
    # Code to setup services goes here
    pass

_setup_services()


In this example, a logger is configured for the `services` package, and a private function `_setup_services` is defined and called to perform any necessary setup operations.

## Project Structure Implications

The presence of an `__init__.py` file in the `services` directory indicates that the directory is a Python package. This allows for the organization of code into a modular and reusable structure. The `services` package can contain multiple modules (Python files) that provide various services to the `dataherald` project. The `__init__.py` file acts as the entry point to this package.

## Best Practices

- Keep the `__init__.py` file as simple as possible, only including necessary imports and initialization code.
- Use the `__all__` list to explicitly define the public API of the package.
- Avoid complex logic in the `__init__.py` file to prevent side effects during the import process.
- Document any initialization code or imports to maintain clarity for other developers working on the project.

## Conclusion

The `__init__.py` file in the `dataherald/services` directory is a crucial component for package initialization, exposing a clean interface to the rest of the project, and potentially running setup code required for the services to operate correctly. It should be maintained with care to ensure the maintainability and functionality of the `dataherald` project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/services/prompts.md

# `prompts.py` Module Documentation

## Overview

The `prompts.py` module is part of the `dataherald` package, specifically within the `services` subpackage. It defines the `PromptService` class, which provides an interface for creating, retrieving, and updating prompts in the context of a data reporting or data heralding application.

## Dependencies

- `dataherald.api.types.requests.PromptRequest`: A class representing a request to create a new prompt.
- `dataherald.repositories.database_connections.DatabaseConnectionNotFoundError`: An exception class for handling cases where a database connection is not found.
- `dataherald.repositories.database_connections.DatabaseConnectionRepository`: A repository class for managing database connections.
- `dataherald.repositories.prompts.PromptNotFoundError`: An exception class for handling cases where a prompt is not found.
- `dataherald.repositories.prompts.PromptRepository`: A repository class for managing prompts.
- `dataherald.types.Prompt`: A class representing a prompt entity.

## `PromptService` Class

### Attributes

- `storage`: An instance of a storage mechanism (e.g., a database session or connection) that is passed to the repository classes for data persistence operations.
- `prompt_repository`: An instance of `PromptRepository` initialized with the `storage` attribute for managing prompt entities.

### Methods

#### `__init__(self, storage)`

The constructor initializes the `PromptService` instance with the provided `storage` mechanism and sets up the `prompt_repository` attribute.

#### `create(self, prompt_request: PromptRequest) -> Prompt`

Creates a new prompt based on the provided `PromptRequest` object.

- Parameters:
  - `prompt_request`: An instance of `PromptRequest` containing the necessary data to create a new prompt.
- Returns:
  - A `Prompt` object representing the newly created prompt.
- Raises:
  - `DatabaseConnectionNotFoundError`: If the database connection specified in the `prompt_request` does not exist.
- Process:
  1. Initializes a `DatabaseConnectionRepository` with the current `storage`.
  2. Attempts to find the database connection using the `db_connection_id` from the `prompt_request`.
  3. If the database connection is not found, raises `DatabaseConnectionNotFoundError`.
  4. Creates a new `Prompt` object with the text, database connection ID, and metadata from the `prompt_request`.
  5. Inserts the new prompt into the repository and returns the resulting `Prompt` object.

#### `get(self, query) -> list[Prompt]`

Retrieves a list of prompts based on a given query.

- Parameters:
  - `query`: A query object or parameters used to filter the prompts to be retrieved.
- Returns:
  - A list of `Prompt` objects that match the query.

#### `update_metadata(self, prompt_id, metadata_request) -> Prompt`

Updates the metadata of an existing prompt.

- Parameters:
  - `prompt_id`: The unique identifier of the prompt to be updated.
  - `metadata_request`: An object containing the new metadata to be applied to the prompt.
- Returns:
  - The updated `Prompt` object.
- Raises:
  - `PromptNotFoundError`: If the prompt with the given `prompt_id` does not exist.
- Process:
  1. Finds the prompt by its `prompt_id` using the `prompt_repository`.
  2. If the prompt is not found, raises `PromptNotFoundError`.
  3. Updates the prompt's metadata with the new metadata from `metadata_request`.
  4. Saves the updated prompt using the `prompt_repository` and returns the updated `Prompt` object.

## Usage

The `PromptService` class is used within the `dataherald` project to manage the lifecycle of prompts, which are likely user-defined queries or messages associated with specific database connections. The service allows for the creation of new prompts, retrieval of existing prompts, and updating of prompt metadata, ensuring that the prompts are correctly linked to valid database connections and that their information is up-to-date.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/sqlalchemy.md

# SqlAlchemyScanner Class

## Overview

The `SqlAlchemyScanner` class is a subclass of `Scanner` and is responsible for scanning SQL databases using SQLAlchemy to extract metadata and schema information about the tables and columns within the database. It supports various database engines and integrates with different scanner services for specific databases like Snowflake, BigQuery, PostgreSQL, SQL Server, and ClickHouse.

## Attributes

- `scanner_service`: An instance of `AbstractScanner` that is used to perform database-specific scanning operations.

## Methods

### `__init__(self, *args, **kwargs)`

Constructor for the `SqlAlchemyScanner` class. It initializes the base `Scanner` class and sets the `scanner_service` attribute to `None`.

### `create_tables(self, tables: list[str], db_connection_id: str, repository: TableDescriptionRepository, metadata: dict = None) -> None`

Creates entries in the `repository` for each table in the `tables` list with the status `NOT_SCANNED`. The `db_connection_id` and optional `metadata` are also stored.

### `refresh_tables(self, tables: list[str], db_connection_id: str, repository: TableDescriptionRepository, metadata: dict = None) -> list[TableDescription]`

Updates the status of tables in the `repository`. If a table in the repository is not in the `tables` list, its status is set to `DEPRECATED`. New tables are added with the status `NOT_SCANNED`. Returns a list of `TableDescription` objects representing the refreshed tables.

### `synchronizing(self, scanner_request: ScannerRequest, repository: TableDescriptionRepository) -> list[TableDescription]`

Updates the status of tables in the `repository` to `SYNCHRONIZING` based on the `scanner_request`. Returns a list of `TableDescription` objects representing the tables being synchronized.

### `get_table_examples(self, meta: MetaData, db_engine: SQLDatabase, table: str, rows_number: int = 3) -> List[Any]`

Retrieves a sample of rows (default is 3) from the specified `table` using the provided `meta` and `db_engine`. Returns a list of dictionaries representing the row samples.

### `get_processed_column(self, meta: MetaData, table: str, column: dict, db_engine: SQLDatabase) -> ColumnDetail`

Processes a single column from the specified `table` to determine its characteristics such as data type and cardinality. Returns a `ColumnDetail` object with the column metadata.

### `get_table_schema(self, meta: MetaData, db_engine: SQLDatabase, table: str) -> str`

Generates the schema DDL for the specified `table` using the provided `meta` and `db_engine`. Returns the schema as a string.

### `scan_single_table(self, meta: MetaData, table: str, db_engine: SQLDatabase, db_connection_id: str, repository: TableDescriptionRepository) -> TableDescription`

Scans a single `table` to collect metadata and schema information. It updates the `repository` with the collected information and returns a `TableDescription` object representing the scanned table.

### `scan(self, db_engine: SQLDatabase, db_connection_id: str, table_names: list[str] | None, repository: TableDescriptionRepository, query_history_repository: QueryHistoryRepository) -> None`

Scans the database tables specified in `table_names` (or all tables if `table_names` is `None`) using the provided `db_engine`. It updates the `repository` with the collected metadata and schema information. It also collects query history logs and stores them in the `query_history_repository`.

## Constants

- `MIN_CATEGORY_VALUE`: The minimum value for categorizing a column as low cardinality.
- `MAX_CATEGORY_VALUE`: The maximum value for categorizing a column as low cardinality.
- `MAX_SIZE_LETTERS`: The maximum size of a column's content before it is not considered for low cardinality.

## Usage

The `SqlAlchemyScanner` class is used within a project to scan SQL databases and collect metadata about the tables and columns. It is typically used in conjunction with a `TableDescriptionRepository` to store the table descriptions and a `QueryHistoryRepository` to store query logs. The class supports various database engines and can be extended to include additional scanner services for other databases.

## Dependencies

The class depends on several modules and classes, including:

- `logging`: For logging messages and errors.
- `datetime`: For timestamping the last schema synchronization.
- `typing`: For type annotations.
- `sqlalchemy`: For interacting with SQL databases.
- `clickhouse_sqlalchemy`: For ClickHouse database support.
- `overrides`: For method overriding.
- `dataherald.db_scanner`: For base scanner classes and models.
- `dataherald.sql_database.base`: For the `SQLDatabase` class.
- `dataherald.types`: For the `ScannerRequest` type.

## Error Handling

The `scan` method includes error handling to catch exceptions during the scanning process. If an error occurs while scanning a table, the table's status is set to `FAILED`, and the error message is stored in the `repository`.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/__init__.md

# Scanner Class

## Overview
The `Scanner` class serves as an abstract base class for all scanner classes within the `dataherald` project. It inherits from the `Component` class and Python's built-in `ABC` (Abstract Base Class) module, indicating that it provides a template for subclasses but is not intended to be instantiated directly.

## Attributes
The `Scanner` class does not define any attributes directly. It relies on attributes defined in the `Component` class it inherits from and the abstract methods it declares.

## Methods

### `scan`
python
@abstractmethod
def scan(
    self,
    db_engine: SQLDatabase,
    db_connection_id: str,
    table_names: list[str] | None,
    repository: TableDescriptionRepository,
    query_history_repository: QueryHistoryRepository,
) -> None:

- **Description**: Abstract method that must be implemented by subclasses to scan a database.
- **Parameters**:
  - `db_engine`: An instance of `SQLDatabase` that represents the database engine to be scanned.
  - `db_connection_id`: A string representing the unique identifier for the database connection.
  - `table_names`: An optional list of strings representing the names of tables to be scanned. If `None`, all tables in the database may be considered.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
  - `query_history_repository`: An instance of `QueryHistoryRepository` used to interact with the query history.
- **Returns**: None. The method is expected to perform the scanning operation and handle the results internally.

### `synchronizing`
python
@abstractmethod
def synchronizing(
    self,
    scanner_request: ScannerRequest,
    repository: TableDescriptionRepository,
) -> list[TableDescription]:

- **Description**: Abstract method that must be implemented by subclasses to update the status of `table_description` based on a `ScannerRequest`.
- **Parameters**:
  - `scanner_request`: An instance of `ScannerRequest` containing the details of the scanning request.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
- **Returns**: A list of `TableDescription` instances that have been updated.

### `create_tables`
python
@abstractmethod
def create_tables(
    self,
    tables: list[str],
    db_connection_id: str,
    repository: TableDescriptionRepository,
    metadata: dict = None,
) -> None:

- **Description**: Abstract method that must be implemented by subclasses to create tables in the database.
- **Parameters**:
  - `tables`: A list of strings representing the names of tables to be created.
  - `db_connection_id`: A string representing the unique identifier for the database connection.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
  - `metadata`: An optional dictionary containing additional metadata for table creation.
- **Returns**: None. The method is expected to perform the table creation operation.

### `refresh_tables`
python
@abstractmethod
def refresh_tables(
    self,
    tables: list[str],
    db_connection_id: str,
    repository: TableDescriptionRepository,
    metadata: dict = None,
) -> list[TableDescription]:

- **Description**: Abstract method that must be implemented by subclasses to refresh the metadata of existing tables.
- **Parameters**:
  - `tables`: A list of strings representing the names of tables to be refreshed.
  - `db_connection_id`: A string representing the unique identifier for the database connection.
  - `repository`: An instance of `TableDescriptionRepository` used to interact with table descriptions.
  - `metadata`: An optional dictionary containing additional metadata for refreshing tables.
- **Returns**: A list of `TableDescription` instances that have been refreshed.

## Usage
Subclasses of the `Scanner` class must implement the abstract methods to provide functionality for scanning databases, synchronizing table descriptions, creating tables, and refreshing table metadata. These subclasses are used within the `dataherald` project to interact with different types of databases and to maintain an up-to-date representation of the database schema and structure.

## Subclassing
To create a new scanner class, one must subclass `Scanner` and provide concrete implementations for all the abstract methods. This new subclass can then be integrated into the `dataherald` project to extend its database scanning capabilities.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/postgre_sql_scanner.md

# PostgreSqlScanner Class

## Overview

The `PostgreSqlScanner` class is a Python class that extends the `AbstractScanner` class, providing specific implementations for scanning PostgreSQL databases. It is part of the `dataherald.db_scanner.services` module within the `dataherald` project. This class is used to interact with PostgreSQL databases to retrieve metadata and statistics about the database tables and columns.

## Attributes

- `MIN_CATEGORY_VALUE`: An integer constant set to `1`, representing the minimum threshold for the distinct count of values in a column to be considered for further processing.
- `MAX_CATEGORY_VALUE`: An integer constant set to `100`, representing the maximum threshold for the distinct count of values in a column to be considered for further processing.

## Methods

### cardinality_values

python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None


#### Description

The `cardinality_values` method is used to retrieve the cardinality statistics of a given column from a PostgreSQL database. It returns the most common values of the column if the number of distinct values falls within the defined range (`MIN_CATEGORY_VALUE` and `MAX_CATEGORY_VALUE`).

#### Parameters

- `column`: An instance of `sqlalchemy.sql.schema.Column`, representing the database column for which the cardinality statistics are to be retrieved.
- `db_engine`: An instance of `dataherald.sql_database.base.SQLDatabase`, representing the database engine used to execute the query.

#### Returns

- A list of the most common values for the column if the number of distinct values is within the specified range.
- `None` if the number of distinct values is outside the specified range or if no results are found.

#### Implementation Details

- The method executes a raw SQL query on the PostgreSQL database using the `db_engine.engine.execute` method.
- The query retrieves the number of distinct values (`n_distinct`) and the most common values (`most_common_vals`) from the `pg_catalog.pg_stats` system catalog for the specified column.
- The query results are fetched using the `.fetchall()` method.
- The method checks if the result set is not empty and if the `n_distinct` value is within the specified range.
- If the conditions are met, the method returns the `most_common_vals` as a list.
- The method uses a raw SQL string with string interpolation, which could be a potential security risk (SQL injection) if not handled properly. The `# noqa: S608 E501` comments indicate that the linter should ignore the potential security risk and line length issues.

### get_logs

python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]


#### Description

The `get_logs` method is a stub implementation that currently returns an empty list. It is intended to retrieve a list of query history logs for a given table from the PostgreSQL database. However, the actual implementation is not provided in the input code.

#### Parameters

- `table`: A string representing the name of the database table for which the query history logs are to be retrieved.
- `db_engine`: An instance of `dataherald.sql_database.base.SQLDatabase`, representing the database engine used to execute the query.
- `db_connection_id`: A string representing the identifier for the database connection.

#### Returns

- An empty list of `QueryHistory` objects, indicating that the method has not been implemented yet.

#### Implementation Details

- The method is currently a placeholder and does not perform any database operations.
- The `# noqa: ARG002` comment indicates that the linter should ignore the argument naming convention issue.

## Usage

The `PostgreSqlScanner` class is intended to be used within the `dataherald` project to scan PostgreSQL databases for metadata and statistics. It can be instantiated and used by other components that require information about the cardinality of database columns or query history logs. The actual usage of the `get_logs` method will depend on its future implementation.

## Inheritance

The `PostgreSqlScanner` class inherits from the `AbstractScanner` class, which defines the interface for database scanners. The `@override` decorator is used to indicate that the methods `cardinality_values` and `get_logs` override the abstract methods defined in the parent class.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/big_query_scanner.md

# BigQueryScanner Class

## Overview
`BigQueryScanner` is a Python class that extends the `AbstractScanner` class, providing specific implementations for scanning Google BigQuery databases. It is part of a larger project aimed at analyzing and monitoring database usage and schema. The class includes methods for estimating the cardinality of column values and retrieving logs of query activities.

## Attributes
- `MIN_CATEGORY_VALUE`: The minimum threshold value for considering a column as categorical.
- `MAX_CATEGORY_VALUE`: The maximum threshold value for considering a column as categorical.
- `MAX_LOGS`: The maximum number of log entries to retrieve.

## Methods

### cardinality_values
python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None

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
python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/base_scanner.md

# BaseScanner Class

## Overview

The `BaseScanner` class is a concrete implementation of the `AbstractScanner` class, which is part of the `dataherald.db_scanner` package. This class provides functionality to scan a database and perform operations such as calculating the cardinality of values in a database column. It is designed to be used within a larger project that requires database scanning capabilities.

## Attributes

- `MIN_CATEGORY_VALUE`: An integer constant representing the minimum number of distinct values in a column to be considered for cardinality calculation.
- `MAX_CATEGORY_VALUE`: An integer constant representing the maximum number of distinct values in a column to be considered for cardinality calculation.

## Methods

### cardinality_values

python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None


#### Description

Calculates the cardinality of values in a specified database column. It retrieves a distinct list of values from the column and determines if the number of distinct values falls within a specified range defined by `MIN_CATEGORY_VALUE` and `MAX_CATEGORY_VALUE`.

#### Parameters

- `column`: A `Column` object from the `sqlalchemy.sql.schema` module representing the database column for which the cardinality is to be calculated.
- `db_engine`: An instance of `SQLDatabase` from the `dataherald.sql_database.base` module, which provides the database engine to execute the query.

#### Returns

- A list of distinct values from the column as strings if the number of distinct values is within the specified range.
- `None` if the number of distinct values is outside the specified range.

#### Implementation Details

1. Constructs a `SELECT` query using `sqlalchemy.select` to retrieve distinct values from the specified column, limited to 101 entries to check against the `MAX_CATEGORY_VALUE`.
2. Executes the query using the provided `db_engine`'s `engine` attribute.
3. Fetches all results from the executed query.
4. Checks if the number of distinct values is within the range defined by `MIN_CATEGORY_VALUE` and `MAX_CATEGORY_VALUE`.
5. If within range, returns a list of the distinct values converted to strings.
6. If not within range, returns `None`.

### get_logs

python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]


#### Description

A placeholder method that is intended to retrieve a list of query logs from a specified database table. Currently, this method is not implemented and simply returns an empty list.

#### Parameters

- `table`: A string representing the name of the database table from which to retrieve query logs.
- `db_engine`: An instance of `SQLDatabase`, providing the database engine to execute the query.
- `db_connection_id`: A string representing the unique identifier for the database connection.

#### Returns

- An empty list of `QueryHistory` objects, indicating no implementation is currently provided.

#### Implementation Details

1. The method signature includes the `override` decorator, indicating that it overrides a method from the base class `AbstractScanner`.
2. The method currently does not perform any operations and returns an empty list.

## Usage

The `BaseScanner` class is used within the project to perform database scanning operations, particularly to calculate the cardinality of database columns. It can be instantiated and its methods called by passing the required parameters, such as a `Column` object and an `SQLDatabase` instance. The `get_logs` method is not currently functional and serves as a template for future implementation.

## Integration

The `BaseScanner` class integrates with the SQLAlchemy library for database operations and the `overrides` library to ensure method signatures match the abstract base class. It also utilizes the `QueryHistory` model from the `dataherald.db_scanner.models.types` module, although the usage is not yet implemented in the `get_logs` method.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/click_house_scanner.md

# ClickHouseScanner Class

## Overview

`ClickHouseScanner` is a Python class that extends the `AbstractScanner` class, providing specific implementations for scanning and analyzing ClickHouse databases. It is part of the `dataherald.db_scanner.services` module within the `dataherald` project. The class is designed to interact with a ClickHouse database using SQLAlchemy to perform operations such as estimating the cardinality of values in a column and retrieving logs.

## Constants

- `MIN_CATEGORY_VALUE`: The minimum value used to determine if a column's cardinality is within an acceptable range for distinct value retrieval.
- `MAX_CATEGORY_VALUE`: The maximum value used to determine if a column's cardinality is within an acceptable range for distinct value retrieval.
- `MAX_LOGS`: The maximum number of logs to retrieve from the database.

## Methods

### cardinality_values

#### Signature

python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None


#### Description

Estimates the cardinality (the number of distinct values) of a specified column in a ClickHouse database and retrieves the distinct values if the cardinality is within a specified range.

#### Parameters

- `column`: An instance of `sqlalchemy.sql.schema.Column` representing the database column for which to estimate cardinality.
- `db_engine`: An instance of `dataherald.sql_database.base.SQLDatabase` representing the database engine to use for executing the query.

#### Returns

- A list of strings representing the distinct values in the column if the cardinality is within the specified range (`MIN_CATEGORY_VALUE` < cardinality <= `MAX_CATEGORY_VALUE`).
- `None` if the cardinality is not within the specified range.

#### Implementation Details

1. A SQL query is constructed using SQLAlchemy's `select` and `func.uniqHLL12` functions to estimate the cardinality of the specified column.
2. The query is executed against the ClickHouse database using the provided `db_engine`.
3. The result set is fetched and checked to ensure that at least one row with one field is returned and that the cardinality is within the specified range.
4. If the conditions are met, a second query is constructed to retrieve up to 101 distinct values from the column using `func.distinct` and `limit`.
5. The distinct values are fetched from the database, and a list of these values is returned.

### get_logs

#### Signature

python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]


#### Description

This method is intended to retrieve logs from a specified table in a ClickHouse database. However, the current implementation returns an empty list and does not perform any database operations.

#### Parameters

- `table`: A string representing the name of the database table from which to retrieve logs.
- `db_engine`: An instance of `dataherald.sql_database.base.SQLDatabase` representing the database engine to use for executing the query.
- `db_connection_id`: A string representing the identifier for the database connection.

#### Returns

- An empty list of `QueryHistory` objects, indicating no logs are retrieved.

#### Implementation Details

The method is currently a stub and does not contain any logic to perform the intended operation. It is likely a placeholder for future implementation or may require subclassing to provide the specific log retrieval functionality.

## Usage

The `ClickHouseScanner` class is used within the `dataherald` project to perform database scanning operations specific to ClickHouse databases. It is instantiated and utilized by other components that require information about the cardinality of database columns or need to retrieve logs for analysis or monitoring purposes. The class relies on SQLAlchemy for database interaction, ensuring compatibility with the ClickHouse dialect and SQL syntax.

## Dependencies

- `sqlalchemy`: Used for constructing and executing SQL queries.
- `overrides`: Used for the `@override` decorator to ensure methods are correctly overriding abstract methods from the parent class.
- `dataherald.db_scanner.models.types`: Contains the `QueryHistory` model used in the `get_logs` method.
- `dataherald.db_scanner.services.abstract_scanner`: Contains the `AbstractScanner` class that `ClickHouseScanner` extends.
- `dataherald.sql_database.base`: Contains the `SQLDatabase` class used for database engine interaction.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/sql_server_scanner.md

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

python
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None


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

python
def get_logs(self, table: str, db_engine: SQLDatabase, db_connection_id: str) -> list[QueryHistory]


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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/snowflake_scanner.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/abstract_scanner.md

# AbstractScanner Class

## Overview

The `AbstractScanner` class serves as an abstract base class (ABC) for creating scanner services that interact with a database. It defines a common interface for scanner services that can be implemented for different types of databases or different scanning strategies. The class is part of the `dataherald.db_scanner.services` module.

## Dependencies

- `abc`: The `ABC` and `abstractmethod` are imported from the `abc` module to define the abstract base class and abstract methods.
- `sqlalchemy.sql.schema`: The `Column` class is imported from `sqlalchemy.sql.schema` to represent a column in a SQL database.
- `dataherald.db_scanner.models.types`: The `QueryHistory` class is imported from `dataherald.db_scanner.models.types` to represent the structure of query logs.
- `dataherald.sql_database.base`: The `SQLDatabase` class is imported from `dataherald.sql_database.base` to represent the SQL database engine.

## Class Definition

### AbstractScanner

The `AbstractScanner` class inherits from `ABC`, making it an abstract base class that cannot be instantiated directly. It provides a template for subclasses to implement specific functionality for scanning databases.

#### Methods

##### `cardinality_values`

python
@abstractmethod
def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None:
    """Returns a list if it is a catalog otherwise return None"""
    pass


- **Parameters**:
  - `column` (`Column`): An instance of `Column` representing the database column to be scanned for cardinality values.
  - `db_engine` (`SQLDatabase`): An instance of `SQLDatabase` representing the database engine to be used for the query.
- **Returns**: A list of cardinality values if the column is a catalog; otherwise, `None`.
- **Description**: This method is an abstract method that must be implemented by subclasses. It is intended to retrieve the cardinality values (i.e., the number of distinct values) for a given column in the database. The method should return a list of these values if the column is a catalog (a column with a limited set of possible values), or `None` if the column is not a catalog.

##### `get_logs`

python
@abstractmethod
def get_logs(
    self, table: str, db_engine: SQLDatabase, db_connection_id: str
) -> list[QueryHistory]:
    """Returns a list of logs"""
    pass


- **Parameters**:
  - `table` (`str`): The name of the database table for which query logs are to be retrieved.
  - `db_engine` (`SQLDatabase`): An instance of `SQLDatabase` representing the database engine to be used for the query.
  - `db_connection_id` (`str`): A string identifier for the database connection.
- **Returns**: A list of `QueryHistory` instances representing the logs of queries executed against the specified table.
- **Description**: This method is an abstract method that must be implemented by subclasses. It is intended to retrieve a list of query logs for a specific table. Each log entry is represented by an instance of `QueryHistory`, which contains details about the query such as the timestamp, the query text, and other relevant metadata.

## Usage

The `AbstractScanner` class is used as a base for creating concrete scanner classes that implement the `cardinality_values` and `get_logs` methods. Subclasses must provide the logic for these methods according to the specific requirements of the database or scanning strategy they support. Once implemented, these scanner services can be used to scan database tables for cardinality information and retrieve query logs for analysis or monitoring purposes.

## Subclassing Example

To create a concrete scanner service, a subclass of `AbstractScanner` would be defined with implementations for the `cardinality_values` and `get_logs` methods:

python
class ConcreteScanner(AbstractScanner):
    def cardinality_values(self, column: Column, db_engine: SQLDatabase) -> list | None:
        # Implementation specific to the concrete scanner
        pass

    def get_logs(
        self, table: str, db_engine: SQLDatabase, db_connection_id: str
    ) -> list[QueryHistory]:
        # Implementation specific to the concrete scanner
        pass


The `ConcreteScanner` class would then be instantiated and used to perform scanning operations on a database.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/services/__init__.md

# `__init__.py` in `db_scanner/services` Module

## Overview

The `__init__.py` file within the `db_scanner/services` directory is a part of a Python package named `db_scanner`. This file serves as the initialization script for the `services` subpackage within the `db_scanner` package. The presence of `__init__.py` in a directory indicates to Python that the directory should be treated as a package or subpackage.

## Purpose

The primary purpose of the `__init__.py` file is to initialize the Python package `db_scanner.services`. It can be used to perform package-level setup, such as initializing package-wide variables, importing necessary classes or functions from modules within the subpackage, or setting up logging. It also determines which modules or symbols the package exports as the API by using `__all__` or direct imports.

## Usage

When the `db_scanner.services` package is imported into a Python script or module, the code within `__init__.py` is executed. This can include the instantiation of any objects or the execution of any functions that are necessary for the package's functionality.

### Importing the Package

To use the `services` subpackage in a Python project, one would typically import it as follows:

python
from db_scanner.services import SomeServiceClass


or

python
import db_scanner.services as services


### Package Initialization

The `__init__.py` file can contain any valid Python code. Common initialization tasks might include:

- Setting up a logger for the services.
- Importing submodules or classes for easier access.
- Initializing configuration settings for the services.
- Defining `__all__` to restrict what is exported when `from db_scanner.services import *` is used.

### Example Content

An example `__init__.py` file might look like this:

python
# db_scanner/services/__init__.py

# Import necessary modules or classes from the subpackage
from .service_module import ServiceClass

# Initialize package-wide variables or settings
service_instance = ServiceClass()

# Define what should be available when using 'from db_scanner.services import *'
__all__ = ['ServiceClass', 'service_instance']


## Project Structure

The `db_scanner` project likely has a structure similar to the following:


db_scanner/
│
├── services/
│   ├── __init__.py
│   ├── service_module.py
│   └── ...
│
├── ...
│
└── main.py


In this structure, `service_module.py` would be a module within the `services` subpackage, and `main.py` would be an entry point to the application that might use the services provided by the `db_scanner.services` package.

## Conclusion

The `__init__.py` file in the `db_scanner/services` directory is a crucial component for package initialization and configuration. It dictates how the `services` subpackage is presented to the rest of the Python project and what functionality is exposed for use by other modules or packages.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/repository/base.md

# TableDescriptionRepository

## Overview

`TableDescriptionRepository` is a Python class that provides an interface for interacting with a MongoDB collection that stores metadata about database tables. The class is designed to abstract the underlying database operations and provide a set of methods to perform CRUD operations on `TableDescription` objects.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the MongoDB collection that stores the table descriptions.

## Exceptions

- `InvalidColumnNameError`: A custom exception class that is raised when an operation is attempted on a column name that does not exist in the table description.

## Class Definition

### `__init__(self, storage)`

Constructor for the `TableDescriptionRepository` class.

#### Parameters

- `storage`: An instance of a storage class that provides methods for interacting with the MongoDB database.

### `find_by_id(self, id: str) -> TableDescription | None`

Retrieves a `TableDescription` object by its MongoDB ObjectId.

#### Parameters

- `id`: A string representation of the MongoDB ObjectId.

#### Returns

- A `TableDescription` object if found, otherwise `None`.

### `get_table_info(self, db_connection_id: str, table_name: str) -> TableDescription | None`

Retrieves a `TableDescription` object by database connection ID and table name.

#### Parameters

- `db_connection_id`: A string representing the database connection ID.
- `table_name`: A string representing the name of the table.

#### Returns

- A `TableDescription` object if found, otherwise `None`.

### `get_all_tables_by_db(self, query: dict) -> List[TableDescription]`

Retrieves all `TableDescription` objects that match a given query.

#### Parameters

- `query`: A dictionary representing the query to filter the table descriptions.

#### Returns

- A list of `TableDescription` objects.

### `save_table_info(self, table_info: TableDescription) -> TableDescription`

Saves or updates a `TableDescription` object in the database.

#### Parameters

- `table_info`: A `TableDescription` object to be saved or updated.

#### Returns

- The `TableDescription` object with its ID updated to reflect the saved record.

### `update(self, table_info: TableDescription) -> TableDescription`

Updates an existing `TableDescription` object in the database.

#### Parameters

- `table_info`: A `TableDescription` object to be updated.

#### Returns

- The updated `TableDescription` object.

### `find_all(self) -> list[TableDescription]`

Retrieves all `TableDescription` objects from the database.

#### Returns

- A list of all `TableDescription` objects.

### `find_by(self, query: dict) -> list[TableDescription]`

Retrieves all `TableDescription` objects that match a given query and sorts them by table name.

#### Parameters

- `query`: A dictionary representing the query to filter the table descriptions.

#### Returns

- A sorted list of `TableDescription` objects.

### `update_fields(self, table: TableDescription, table_description_request)`

Updates specific fields of a `TableDescription` object based on a request.

#### Parameters

- `table`: The `TableDescription` object to be updated.
- `table_description_request`: An object containing the fields to be updated.

#### Returns

- The updated `TableDescription` object.

#### Raises

- `InvalidColumnNameError`: If a column name provided in the request does not exist in the table description.

## Usage

The `TableDescriptionRepository` class is used to manage table metadata within a project that requires storing and retrieving information about database tables. It is typically used by services or components that need to access or modify this metadata, such as a database schema management tool or a data cataloging system.

The class methods allow for:

- Finding a table description by its ID or by a combination of database connection ID and table name.
- Retrieving all table descriptions for a specific database or based on a query.
- Saving new or updating existing table descriptions.
- Updating specific fields of a table description, with validation to ensure column names exist.

The repository ensures that all interactions with the `table_descriptions` collection are performed through a consistent interface, abstracting the details of the MongoDB operations from the rest of the application.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/repository/query_history.md

# QueryHistoryRepository Class

## Overview

The `QueryHistoryRepository` class is a data access layer component designed to interact with a storage system that contains a collection of query history records. It provides an abstraction over the underlying database operations, specifically tailored to handle `QueryHistory` model instances.

## Attributes

- `storage`: An instance of a storage class that provides methods for database operations such as `insert_one` and `find`.

## Methods

### `__init__(self, storage)`

The constructor initializes a new instance of the `QueryHistoryRepository` class.

#### Parameters

- `storage`: An object that provides the necessary methods to interact with the database.

#### Description

- The `storage` parameter is stored as an instance attribute for later use in other methods.

### `insert(self, query_history: QueryHistory) -> QueryHistory`

Inserts a new `QueryHistory` record into the database.

#### Parameters

- `query_history`: An instance of the `QueryHistory` model representing the query history data to be inserted.

#### Returns

- Returns the `QueryHistory` instance with its `id` attribute set to the identifier assigned by the database.

#### Description

- Converts the `QueryHistory` instance to a dictionary, excluding the `id` field.
- Explicitly converts the `db_connection_id` to a string and adds it to the dictionary.
- Inserts the dictionary into the database collection specified by `DB_COLLECTION`.
- Retrieves the inserted document's identifier, converts it to a string, and assigns it to the `id` attribute of the `QueryHistory` instance.
- Returns the updated `QueryHistory` instance.

### `find_by(self, query: dict, page: int = 1, limit: int = 10) -> list[QueryHistory]`

Retrieves a list of `QueryHistory` records from the database based on a query filter.

#### Parameters

- `query`: A dictionary representing the filter criteria for the query.
- `page`: An integer representing the page number for pagination (default is 1).
- `limit`: An integer representing the number of records to return per page (default is 10).

#### Returns

- Returns a list of `QueryHistory` instances that match the query filter.

#### Description

- Uses the `storage` instance to perform a `find` operation on the `DB_COLLECTION` with the provided `query`, `page`, and `limit` parameters.
- Iterates over the returned rows from the database.
- For each row, converts the `_id` field to a string and assigns it to the `id` attribute.
- Converts the `db_connection_id` to a string.
- Creates a new `QueryHistory` instance using the row data and appends it to the result list.
- Returns the list of `QueryHistory` instances.

## Usage

The `QueryHistoryRepository` class is used to interact with the `query_history` collection in the database. It provides methods to insert new records and retrieve existing records based on specific criteria. This class is typically used by services or controllers that require access to query history data within the application.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the database collection that stores query history records. Its value is `"query_history"`.

## Dependencies

- `dataherald.db_scanner.models.types.QueryHistory`: The `QueryHistory` class is a model that represents the structure of a query history record. It is used as the data type for the records handled by the `QueryHistoryRepository`.

## Notes

- The `storage` instance is expected to provide `insert_one` and `find` methods that are compatible with the repository's usage.
- The `QueryHistory` model should have a `dict` method that allows conversion to a dictionary and an `id` attribute that can be set after insertion.
- The `find_by` method assumes that the `storage` instance's `find` method supports pagination through `page` and `limit` parameters.
- The `insert` and `find_by` methods handle the conversion of MongoDB's ObjectId to a string for the `id` field, ensuring compatibility with the `QueryHistory` model.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/repository/__init__.md

# `__init__.py` in `db_scanner/repository` Module

## Overview

The `__init__.py` file within the `db_scanner/repository` directory serves as an initializer for the `repository` package in the `db_scanner` module of the `dataherald` project. This file can be used to expose specific classes, functions, or variables from within the package, making them directly accessible when the package is imported elsewhere in the project.

## Usage

When the `repository` package is imported, Python will execute the `__init__.py` file. The contents of this file determine which components of the `repository` package are available to the importer. This can include importing classes or functions from submodules for easier access, initializing package-level variables, or performing any startup configuration necessary for the package to function correctly.

## Structure and Content

The `__init__.py` file can contain several types of statements and definitions:

1. **Import Statements**: These statements import classes, functions, or variables from submodules within the `repository` package. This allows users to access these components directly from the `repository` package without having to import them from their respective submodules.

    python
    from .submodule import SomeClass, some_function
    

2. **Package Initialization Code**: Any code that needs to run when the package is first imported can be placed here. This could include setting up logging, initializing connections to databases, or preparing any necessary resources.

    python
    # Example initialization code
    setup_logging()
    initialize_database_connection()
    

3. **__all__ Variable**: This is a list of strings defining what symbols the package will export when `from repository import *` is used. It controls which names are public and should be used with caution to avoid polluting the namespace.

    python
    __all__ = ['SomeClass', 'some_function', 'ANOTHER_CONSTANT']
    

4. **Package-Level Variables or Constants**: These are variables or constants that are meant to be used across multiple modules within the `repository` package.

    python
    ANOTHER_CONSTANT = 42
    

## Example

Below is an example of what the `__init__.py` file might contain:

python
# Import specific classes from submodules for easier access
from .user_repository import UserRepository
from .product_repository import ProductRepository

# Initialize package-level constants
DEFAULT_CONNECTION_STRING = "postgresql://user:password@localhost/dbname"

# Define what is available to importers using the wildcard import
__all__ = ['UserRepository', 'ProductRepository', 'connect_to_database']

# Define a function to establish a database connection
def connect_to_database(connection_string=DEFAULT_CONNECTION_STRING):
    # Logic to connect to the database
    pass

# Perform any necessary package initialization
connect_to_database()


In this example, when the `repository` package is imported, `UserRepository` and `ProductRepository` classes are directly accessible, and the `connect_to_database` function is available for establishing a database connection with a default or provided connection string. The `__all__` list specifies that only these classes and the `connect_to_database` function are intended for public use when importing with `*`.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/models/types.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db_scanner/models/__init__.md

# `__init__.py` in `db_scanner/models` Module

## Overview

The `__init__.py` file within the `db_scanner/models` directory serves as an initialization script for the `models` package in the `db_scanner` module of the project. This file can be used to set up the package namespace, import necessary classes or functions from submodules, and perform any required initialization code that needs to run when the package is imported.

## Usage

When the `models` package is imported in the project, Python executes the code in `__init__.py`. This can include importing classes or functions from other files within the `models` package, which allows users to access these components directly from the `models` namespace rather than having to import them from their individual modules.

For example, if there are several model classes defined in separate files within the `models` directory, such as `user.py`, `product.py`, and `order.py`, the `__init__.py` file can import these classes so that they can be accessed more conveniently:

python
from .user import User
from .product import Product
from .order import Order


With these imports, other parts of the project can import the models like this:

python
from db_scanner.models import User, Product, Order


## Structure

The `__init__.py` file may also include other initialization code that needs to be run at the package level. This could involve setting up a database connection, initializing a model registry, or any other startup tasks that are relevant to the `models` package.

Here is a hypothetical structure of what the `__init__.py` file might contain:

python
# Import model classes for easy access
from .user import User
from .product import Product
from .order import Order

# Initialize a model registry if needed
model_registry = {}

def register_model(model_cls):
    """Register a model class in the model registry."""
    model_registry[model_cls.__name__] = model_cls

# Register the models
register_model(User)
register_model(Product)
register_model(Order)

# Any additional initialization code
def init_models():
    """Perform any additional initialization required for the models."""
    # Code to initialize models, if necessary
    pass

# Call the initialization function if needed
init_models()


## Conventions

The presence of an `__init__.py` file in a directory indicates to Python that the directory should be treated as a package. This file can be empty, but it is often used to perform setup that is necessary for the package. It is a convention in Python to use this file to make the package's interface clean and to abstract away the internal structure of the package.

## Best Practices

- Keep the `__init__.py` file as simple as possible.
- Use it to handle package-level imports and exports.
- Avoid complex logic or heavy computations in this file to prevent slow import times.
- Use relative imports within the package to avoid namespace issues.

## Conclusion

The `__init__.py` file in the `db_scanner/models` directory is a crucial part of the package structure in Python. It is used to initialize the package, define its namespace, and provide a convenient interface for importing its components.


(Note: As per the instructions, no preamble or conclusion has been added to the response. The provided markdown is a detailed technical description of the potential contents and usage of the `__init__.py` file within the `db_scanner/models` directory.)

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/finetuning/openai_finetuning.md

# OpenAIFineTuning Class

## Overview

The `OpenAIFineTuning` class is a subclass of `FinetuningModel` designed to handle the fine-tuning process of OpenAI's language models for specific datasets. It includes methods for creating a fine-tuning dataset, initiating a fine-tuning job, checking the status of the job, and retrieving or canceling the job.

## Attributes

- `encoding`: An instance of `Encoding` from the `tiktoken` library, used to encode text for token counting.
- `fine_tuning_model`: An instance of `Finetuning`, representing the fine-tuning model configuration.
- `storage`: A storage interface for accessing and storing data.
- `client`: An instance of `OpenAI`, used to interact with OpenAI's API.
- `embedding`: An instance of `OpenAIEmbeddings`, used to generate embeddings for text.

## Methods

### `__init__(self, storage: Any, fine_tuning_model: Finetuning)`

Constructor that initializes the `OpenAIFineTuning` instance with the provided storage interface and fine-tuning model configuration. It sets up the OpenAI embeddings and client using the API key from the database connection associated with the fine-tuning model.

### `cosine_similarity(self, a: List[float], b: List[float]) -> float`

Calculates the cosine similarity between two vectors `a` and `b`.

### `map_finetuning_status(status: str) -> str`

Maps a given fine-tuning status string to the corresponding `FineTuningStatus` enum value.

### `format_columns(self, table: TableDescription, top_k: int = CATEGORICAL_COLUMNS_THRESHOLD) -> str`

Formats the column information of a given `TableDescription` object, including the column names and categories, if available.

### `format_table(self, table: TableDescription) -> str`

Formats the entire table description, including schema, column descriptions, and sample rows.

### `create_table_representation(self, table: TableDescription) -> str`

Creates a string representation of a table, including its name and columns, optionally with descriptions.

### `sort_tables(self, tables: List[TableDescription], table_embeddings: List[List[float]], prompt: str) -> List[TableDescription]`

Sorts a list of `TableDescription` objects based on their similarity to a given prompt, using embeddings.

### `format_dataset(self, db_scan: List[TableDescription], table_embeddings: List[List[float]], prompt: str, token_limit: int, correct_tables: [str] = None) -> str`

Formats the dataset schema for fine-tuning, including only the relevant tables and adhering to a token limit.

### `count_tokens(self, messages: dict) -> int`

Counts the number of tokens in a given set of messages.

### `create_fintuning_dataset(self)`

Creates a fine-tuning dataset file from the database scan and golden SQL queries, ensuring it fits within the token limit.

### `check_file_status(self, file_id: str) -> bool`

Checks the processing status of a file with the given `file_id` on OpenAI's servers.

### `create_fine_tuning_job(self)`

Initiates a fine-tuning job with OpenAI using the created dataset file.

### `retrieve_finetuning_job(self) -> Finetuning`

Retrieves the status of an ongoing fine-tuning job and updates the fine-tuning model with the latest information.

### `cancel_finetuning_job(self) -> Finetuning`

Cancels an ongoing fine-tuning job and updates the fine-tuning model status accordingly.

## Constants

- `FILE_PROCESSING_ATTEMPTS`: The number of attempts to check the file processing status before giving up.
- `EMBEDDING_MODEL`: The name of the embedding model used for generating embeddings.
- `CATEGORICAL_COLUMNS_THRESHOLD`: The threshold for the number of categories to show for categorical columns.

## Usage

The `OpenAIFineTuning` class is used in a project to fine-tune OpenAI's language models on a specific dataset. It is typically instantiated with a storage interface and a fine-tuning model configuration. The class methods are then called to create a fine-tuning dataset, initiate the fine-tuning job, and manage the job's lifecycle.

## Dependencies

- `json`: For handling JSON data.
- `logging`: For logging information during the fine-tuning process.
- `os`: For file system operations.
- `time`: For handling time-related functions like sleep.
- `uuid`: For generating unique identifiers.
- `numpy`: For numerical operations, especially vector calculations.
- `tiktoken`: For encoding text into tokens.
- `langchain_openai`: For embedding functionalities.
- `openai`: For interacting with OpenAI's API.
- `overrides`: For method overriding.
- `sql_metadata`: For parsing SQL queries.
- `dataherald` and `repositories`: For accessing database and fine-tuning configurations.
- `utils`: For utility functions and constants.

## File Path

The class is defined in the file located at `/workspaces/documentation-generator/target_code/dataherald/finetuning/openai_finetuning.py`.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/finetuning/__init__.md

# FinetuningModel Class

## Overview

The `FinetuningModel` class is an abstract base class (ABC) that defines the interface for fine-tuning models within the `dataherald` project. It inherits from the `Component` class defined in the `dataherald.config` module and the `ABC` class from the `abc` module. The class outlines the structure and required methods that any fine-tuning model component must implement to be compatible with the `dataherald` system.

## Attributes

- `storage`: This attribute holds a reference to a storage component that the fine-tuning model will use to access and store data.

## Methods

### `__init__(self, storage)`

The constructor method initializes a new instance of the `FinetuningModel` class.

#### Parameters

- `storage`: A storage component that the fine-tuning model will use for data operations.

### `count_tokens(self, messages: dict) -> int`

An abstract method that must be implemented by subclasses. It should count the number of tokens in the provided messages.

#### Parameters

- `messages`: A dictionary containing the messages to be tokenized and counted.

#### Returns

- An integer representing the total number of tokens in the messages.

### `create_fintuning_dataset(self)`

An abstract method that must be implemented by subclasses. It should handle the creation of a dataset suitable for fine-tuning the model.

### `create_fine_tuning_job(self)`

An abstract method that must be implemented by subclasses. It should initiate a fine-tuning job for the model.

### `retrieve_finetuning_job(self) -> Finetuning`

An abstract method that must be implemented by subclasses. It should retrieve the status or result of a fine-tuning job.

#### Returns

- A `Finetuning` object representing the state or outcome of the fine-tuning job.

### `cancel_finetuning_job(self) -> Finetuning`

An abstract method that must be implemented by subclasses. It should cancel an ongoing fine-tuning job.

#### Returns

- A `Finetuning` object representing the state of the fine-tuning job after the cancellation attempt.

## Usage

The `FinetuningModel` class is not meant to be instantiated directly. Instead, it serves as a blueprint for creating concrete classes that implement the fine-tuning logic specific to different types of models. Subclasses must provide concrete implementations for all the abstract methods defined in this class.

When a subclass is created, it must override the abstract methods with actual working code that performs the necessary tasks for fine-tuning a model, such as counting tokens, creating datasets, managing fine-tuning jobs, and handling job cancellations.

The `FinetuningModel` class ensures that all fine-tuning components within the `dataherald` project adhere to a consistent interface, making it easier to manage and interchange different fine-tuning strategies within the system.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_database/base.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_database/__init__.md

# `__init__.py` in `sql_database` Module

## Overview

The `__init__.py` file within the `sql_database` directory serves as an initializer for the Python package named `sql_database`. This package is likely part of a larger project named `dataherald`. The presence of an `__init__.py` file in a directory tells the Python interpreter that the directory should be treated as a package, allowing the modules within the package to be imported from other parts of the project.

## Purpose

The `__init__.py` file can perform several functions:

- It can be left empty, simply to denote the directory as a Python package.
- It can initialize package-level variables or configurations.
- It can import certain classes, functions, or submodules to make them more accessible to users of the package.

## Usage

### Importing the Package

When other parts of the `dataherald` project need to interact with the SQL database, they would import the `sql_database` package or specific components from it using import statements like:

python
import sql_database


or

python
from sql_database import SomeClassOrFunction


### Package Initialization

If the `__init__.py` file contains any initialization code, this code will be executed the first time the package is imported. This can include setting up a database connection, configuring logging for the package, or performing checks that are necessary before the package can be used.

### Making Submodules Accessible

The `__init__.py` file can also be used to make certain submodules or objects within the package more accessible. For example, if there is a submodule `sql_database.connection` that contains a `DatabaseConnection` class, the `__init__.py` file could import this class so that it can be accessed directly from the package namespace:

python
from .connection import DatabaseConnection


This would allow users of the package to import `DatabaseConnection` like this:

python
from sql_database import DatabaseConnection


instead of having to import it from the submodule directly:

python
from sql_database.connection import DatabaseConnection


## Structure

The structure of the `__init__.py` file depends on the specific needs of the `sql_database` package. It could be as simple as an empty file, or it could contain multiple import statements and initialization code. The exact contents would need to be determined by examining the file or the documentation specific to the `dataherald` project.

## Best Practices

- Keep the `__init__.py` file as simple as possible, importing only what is necessary to expose to the package users.
- Avoid complex initialization logic in the `__init__.py` file that could make the package difficult to import or use.
- Use relative imports within the package to avoid issues with namespace conflicts and to make the code more maintainable.

## Conclusion

The `__init__.py` file in the `sql_database` module is a key component of the `dataherald` project's package structure. It serves to initialize the package and make its components accessible to other parts of the project in a controlled and maintainable way.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_database/models/types.md

# Types Module Documentation

## Overview

The `types.py` module within the `dataherald/sql_database/models` directory defines several Pydantic models and utility classes that are used to represent and manage credentials and settings for various services such as API access, file storage, SSH connections, and database connections. It also includes encryption and validation logic to ensure the security and integrity of sensitive information.

## Classes

### LLMCredentials

`LLMCredentials` is a subclass of `BaseSettings` from the `pydantic` library. It is used to manage credentials for an unspecified service, likely related to an organization's API access.

#### Attributes

- `organization_id`: Optional string representing the organization's identifier.
- `api_key`: Optional string representing the API key for the organization.

#### Validators

- A class-level validator is defined for the `api_key` and `organization_id` attributes. It encrypts the values using `FernetEncrypt` unless they are already encrypted.

#### Methods

- `__getitem__`: Allows access to attribute values using dictionary-like key access.

### FileStorage

`FileStorage` is a subclass of `BaseModel` from the `pydantic` library. It represents the configuration needed to access file storage services.

#### Attributes

- `name`: String representing the name of the file storage.
- `access_key_id`: String representing the access key ID for the file storage service.
- `secret_access_key`: String representing the secret access key for the file storage service.
- `region`: Optional string representing the region where the file storage service is located.
- `bucket`: String representing the bucket name in the file storage service.

#### Config

- Ignores any extra attributes that are not explicitly defined in the model.

#### Validators

- A class-level validator is defined for the `access_key_id` and `secret_access_key` attributes. It encrypts the values using `FernetEncrypt` unless they are already encrypted.

#### Methods

- `__getitem__`: Allows access to attribute values using dictionary-like key access.

### SSHSettings

`SSHSettings` is a subclass of `BaseSettings` from the `pydantic` library. It holds configuration for SSH connections.

#### Attributes

- `host`: Optional string representing the SSH server host.
- `username`: Optional string representing the SSH username.
- `password`: Optional string representing the SSH password.
- `port`: String representing the SSH port, defaulting to "22".
- `private_key_password`: Optional string representing the password for the SSH private key.

#### Config

- Ignores any extra attributes that are not explicitly defined in the model.

#### Validators

- A class-level validator is defined for the `password` and `private_key_password` attributes. It encrypts the values using `FernetEncrypt` unless they are already encrypted.

#### Methods

- `__getitem__`: Allows access to attribute values using dictionary-like key access.

### InvalidURIFormatError

`InvalidURIFormatError` is a custom exception class that is raised when a URI does not match the expected format.

### DatabaseConnection

`DatabaseConnection` is a subclass of `BaseModel` from the `pydantic` library. It represents the configuration needed to establish a connection to a database.

#### Attributes

- `id`: Optional string representing the unique identifier for the database connection.
- `alias`: String representing an alias for the database connection.
- `use_ssh`: Boolean indicating whether SSH should be used for the connection, defaulting to `False`.
- `connection_uri`: Optional string representing the URI used to connect to the database.
- `path_to_credentials_file`: Optional string representing the file path to additional credentials.
- `llm_api_key`: Optional string representing an API key for LLM services.
- `ssh_settings`: Optional `SSHSettings` object representing SSH connection settings.
- `file_storage`: Optional `FileStorage` object representing file storage settings.
- `metadata`: Optional dictionary containing additional metadata.
- `created_at`: `datetime` object representing the creation time of the database connection, defaulting to the current time.

#### Class Methods

- `validate_uri`: Validates the format of the `connection_uri` using a regular expression pattern.

#### Validators

- A class-level validator is defined for the `connection_uri` attribute. It encrypts the value using `FernetEncrypt` unless it is already encrypted and validates the URI format.
- A class-level validator is defined for the `llm_api_key` attribute. It encrypts the value using `FernetEncrypt` unless it is already encrypted.

#### Methods

- `decrypt_api_key`: Decrypts the `llm_api_key` if it is set and not empty, otherwise retrieves the API key from the environment variable `OPENAI_API_KEY`.

## Usage

The models defined in this module are likely used throughout the project to manage and securely store configuration settings for various services. The encryption and decryption of sensitive information ensure that credentials are not stored or transmitted in plain text. The validators provide additional checks to ensure that the data conforms to expected formats and standards.

The `__getitem__` methods in each model allow for easy access to the model's attributes, making it convenient to retrieve settings in a dictionary-like manner. The custom exception `InvalidURIFormatError` is used to provide clear error messages when a URI does not meet the required format, which is particularly important for establishing database connections.

Overall, this module plays a critical role in the security and configuration management aspects of the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_database/models/__init__.md

# `__init__.py` Module in `models` Subpackage

## Overview

The `__init__.py` file is a Python module located within the `models` subpackage of the `sql_database` package, which is part of the `dataherald` project. This file serves as an initializer for the `models` subpackage, allowing the package to be recognized by Python as a package and potentially initializing certain aspects of the package when it is imported.

## Purpose

The primary purpose of the `__init__.py` file is to:

- Make Python treat the directories containing it as packages.
- Provide a place to set up package-level variables or functions.
- Import certain classes or functions from modules within the subpackage to streamline imports elsewhere in the project.

## Usage

When the `models` subpackage is imported into other parts of the `dataherald` project, the `__init__.py` file is executed. The contents of this file determine what is available to be imported from the `models` subpackage.

### Importing the Subpackage

To import the `models` subpackage, one would use the following Python syntax:

python
from dataherald.sql_database.models import SomeModel


In this example, `SomeModel` is a class or function that has been made available through the `__init__.py` file.

### Contents of `__init__.py`

The `__init__.py` file may contain several types of statements:

1. **Import Statements**: These statements import classes, functions, or variables from other modules within the `models` subpackage. This allows users to import these directly from `models` rather than having to navigate through the module structure.

    python
    from .user import User
    from .product import Product
    

2. **Package-level Variables**: These are variables that are set at the package level and can be accessed from anywhere within the package or from outside the package if imported.

    python
    __all__ = ['User', 'Product']
    

3. **Initialization Code**: Any code that needs to run when the package is first imported can be placed here. This could include logging setup, configuration checks, or other preparatory tasks.

    python
    print("Initializing SQL database models...")
    

### Example Structure

Given the path `/workspaces/documentation-generator/target_code/dataherald/sql_database/models/__init__.py`, the `models` subpackage might be structured as follows:


dataherald/
└── sql_database/
    └── models/
        ├── __init__.py
        ├── user.py
        └── product.py


In this structure, `user.py` and `product.py` are modules that define database models, such as ORM (Object-Relational Mapping) classes, which correspond to tables in the SQL database.

## Best Practices

- The `__init__.py` file should be kept minimal to avoid complex import dependencies.
- It is common to define an `__all__` variable, which is a list of strings representing the names of objects that should be importable from the package.

## Conclusion

The `__init__.py` file in the `models` subpackage is a key component for package initialization and import management within the `dataherald` project's `sql_database` package. It dictates how the subpackage exposes its contents to the rest of the application and can include import statements, package-level variables, and initialization code.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/encrypt.md

# FernetEncrypt Class

## Overview

The `FernetEncrypt` class is a utility within the `dataherald` project that provides encryption and decryption functionality using the Fernet symmetric encryption method provided by the `cryptography` Python library. This class is designed to handle string data, ensuring that sensitive information can be securely stored and transmitted.

## Initialization

### `__init__(self)`

The constructor method initializes an instance of the `FernetEncrypt` class.

#### Attributes

- `self.fernet_key`: An instance of the `Fernet` class from the `cryptography.fernet` module, which is initialized with an encryption key obtained from the project's settings.

#### Process

1. An instance of the `Settings` class from `dataherald.config` is created.
2. The `Settings` instance is used to retrieve the encryption key by calling the `require` method with the argument `"encrypt_key"`.
3. The retrieved encryption key is used to create a `Fernet` object, which is assigned to `self.fernet_key`.

## Methods

### `encrypt(self, input: str) -> str`

The `encrypt` method takes a string as input and returns an encrypted version of that string.

#### Parameters

- `input`: A string to be encrypted.

#### Returns

- A string representing the encrypted input.

#### Process

1. If the input string is empty, the method immediately returns an empty string.
2. If the input string is not empty, it is encoded to bytes using the `encode` method with the default encoding (UTF-8).
3. The `self.fernet_key` object's `encrypt` method is called with the encoded byte string, which returns the encrypted data as a byte string.
4. The encrypted byte string is then decoded back into a UTF-8 encoded string and returned.

### `decrypt(self, input: str) -> str`

The `decrypt` method takes an encrypted string as input and returns the decrypted version of that string.

#### Parameters

- `input`: An encrypted string to be decrypted.

#### Returns

- A string representing the decrypted input.

#### Process

1. If the input string is empty, the method immediately returns an empty string.
2. If the input string is not empty, it is assumed to be a byte string encoded in UTF-8 representing the encrypted data.
3. The `self.fernet_key` object's `decrypt` method is called with the encrypted byte string, which returns the original unencrypted data as a byte string.
4. The decrypted byte string is then decoded back into a UTF-8 encoded string and returned.

## Usage

The `FernetEncrypt` class is used within the `dataherald` project to encrypt and decrypt strings that may contain sensitive information. It ensures that this information is stored and transmitted securely. The class is typically instantiated once and then used to encrypt or decrypt strings as needed throughout the project.

## Dependencies

- `cryptography.fernet.Fernet`: Used for encryption and decryption operations.
- `dataherald.config.Settings`: Used to retrieve the encryption key from the project's settings.

## Security Considerations

- The encryption key used by the `FernetEncrypt` class should be kept secret and stored securely.
- The Fernet encryption algorithm is symmetric, meaning the same key is used for both encryption and decryption. If the key is compromised, the security of the encrypted data is also compromised.
- It is important to ensure that the encryption key has sufficient entropy and is generated using a cryptographically secure method.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/strings.md

# `strings.py` Module

## Overview

The `strings.py` module is part of the `dataherald` package, specifically within the `utils` subpackage. This module provides utility functions for string manipulation, particularly focusing on whitespace and line break handling. It is designed to be used throughout the `dataherald` project wherever string processing is required.

## Functions

### `remove_whitespace`

#### Description

The `remove_whitespace` function is designed to normalize the whitespace within a given input string. It replaces one or more consecutive whitespace characters with a single space and trims leading and trailing whitespace from the string.

#### Usage

python
cleaned_string = remove_whitespace(input_string)


#### Parameters

- `input_string` (str): The string from which to remove excess whitespace.

#### Returns

- `str`: A new string with normalized whitespace.

#### Implementation Details

- The function utilizes the `re` module (regular expressions) to identify and replace whitespace.
- It employs the regular expression pattern `r"\s+"` to match any sequence of one or more whitespace characters (including spaces, tabs, and newlines).
- The `re.sub` function replaces all matched patterns in the `input_string` with a single space.
- The `strip` method is then called on the resulting string to remove any leading or trailing whitespace.

### `contains_line_breaks`

#### Description

The `contains_line_breaks` function checks whether the input string contains any line break characters (`\n`).

#### Usage

python
has_line_breaks = contains_line_breaks(input_string)


#### Parameters

- `input_string` (str): The string to check for line breaks.

#### Returns

- `bool`: `True` if the `input_string` contains at least one line break; otherwise, `False`.

#### Implementation Details

- The function simply checks for the presence of the newline character `\n` in the `input_string`.
- It uses the `in` operator to determine if `\n` is part of the string, returning a boolean result.

## Integration in the Project

The `strings.py` module's functions are intended to be imported and used by other modules within the `dataherald` project that require string preprocessing or validation. For example, when reading data from files or user input, the `remove_whitespace` function can be used to clean up the strings before further processing. Similarly, the `contains_line_breaks` function can be used to validate strings to ensure they meet certain criteria, such as not containing multiline input where single-line input is expected.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/timeout_utils.md

# `timeout_utils.py` Module

## Overview

The `timeout_utils.py` module provides a utility function `run_with_timeout` that allows the execution of any callable (function/method) with a specified timeout duration. If the callable does not complete its execution within the given timeout, a `TimeoutError` is raised.

## `run_with_timeout` Function

### Description

The `run_with_timeout` function is designed to execute a given callable with the ability to enforce a timeout. It uses threading to run the callable in a separate thread, allowing the main thread to continue execution and monitor the timeout.

### Parameters

- `func`: The callable (function or method) to be executed with a timeout.
- `args` (optional): A tuple containing positional arguments to pass to the callable. Defaults to an empty tuple `()`.
- `kwargs` (optional): A dictionary containing keyword arguments to pass to the callable. Defaults to `None`, which is then initialized to an empty dictionary `{}`.
- `timeout_duration` (optional): An integer or float specifying the maximum number of seconds to wait for the callable to complete. Defaults to `60` seconds.

### Returns

- The function returns the result of the callable `func` if it completes execution within the specified `timeout_duration`.

### Exceptions

- `TimeoutError`: Raised if the callable does not complete within the `timeout_duration`.
- Any exception raised by the callable `func` during its execution is re-raised by `run_with_timeout`.

### Usage

The function is used to wrap the execution of a callable that may potentially run for an indeterminate amount of time or is at risk of hanging. By setting a timeout, the function ensures that the rest of the application can continue to run or handle the timeout situation appropriately.

### Implementation Details

1. The function first checks if `kwargs` is `None` and initializes it to an empty dictionary if necessary.
2. A nested function `func_wrapper` is defined within `run_with_timeout`. This function takes a single argument `result_container`, which is a list used to store the result or exception from the callable.
3. The `func_wrapper` tries to execute the callable with the provided `args` and `kwargs`. The result or any exception is appended to `result_container`.
4. A list `result_container` is initialized to store the result of the callable.
5. A `Thread` object from the `threading` module is created with the target set to `func_wrapper` and `result_container` passed as an argument.
6. The thread is started with `thread.start()`, which begins the execution of `func_wrapper` in a separate thread.
7. The main thread waits for the callable to complete with `thread.join(timeout=timeout_duration)`. If the callable finishes before the timeout, the main thread resumes execution.
8. If the thread is still alive after the timeout, a `TimeoutError` is raised, indicating that the function execution exceeded the timeout.
9. If `result_container` is not empty, the function checks if the first element is an instance of `Exception`. If it is, the exception is raised; otherwise, the result of the callable is returned.
10. If `result_container` is empty after the thread join, a `TimeoutError` is raised, indicating that the function execution exceeded the timeout.

### Example

python
from dataherald.utils.timeout_utils import run_with_timeout

def long_running_task(param1, param2):
    # Simulate a long-running task
    time.sleep(120)
    return param1 + param2

# This will raise a TimeoutError after 60 seconds
try:
    result = run_with_timeout(long_running_task, args=(10, 20), timeout_duration=60)
except TimeoutError:
    print("The task did not complete in time.")


In this example, `long_running_task` is a function that simulates a long-running operation. The `run_with_timeout` function is used to execute it with a timeout of 60 seconds. Since the task is designed to run longer than the timeout, a `TimeoutError` will be raised.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/agent_prompts.md

# `agent_prompts.py` Technical Documentation

## Overview

The `agent_prompts.py` file contains predefined templates and instructions used by an agent designed to generate SQL queries in response to input questions. The agent interacts with a SQL database and utilizes various tools to ensure the generated SQL queries are syntactically correct and yield the correct results when executed against the database.

## Constants

### `AGENT_PREFIX`

This constant defines a template that outlines the agent's role, the expected format for the SQL query, and the tools available for interaction with the database. It also provides a plan for the agent to follow and restrictions on the use of certain SQL functions.

- **Usage**: This template is used as a prefix to guide the agent's behavior when generating SQL queries.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.
  - `{agent_plan}`: Placeholder for the specific plan the agent should follow.

### `PLAN_WITH_FEWSHOT_EXAMPLES_AND_INSTRUCTIONS`

This constant provides a detailed step-by-step plan for the agent to follow when few-shot examples are available, and database administrator instructions need to be considered.

- **Usage**: This plan is used when the agent has access to similar Question/SQL pairs and must adhere to specific instructions provided by a database administrator.
- **Parameters**:
  - `{max_examples}`: Placeholder for the maximum number of Question/SQL pairs the agent can request.
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `PLAN_WITH_INSTRUCTIONS`

This constant provides a step-by-step plan for the agent to follow when database administrator instructions need to be considered, but few-shot examples are not available.

- **Usage**: This plan is used when the agent must generate SQL queries while following specific instructions but does not have access to similar Question/SQL pairs.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `PLAN_WITH_FEWSHOT_EXAMPLES`

This constant provides a step-by-step plan for the agent to follow when few-shot examples are available, but there are no specific database administrator instructions to consider.

- **Usage**: This plan is used when the agent has access to similar Question/SQL pairs but does not need to follow additional instructions.
- **Parameters**:
  - `{max_examples}`: Placeholder for the maximum number of Question/SQL pairs the agent can request.
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `PLAN_BASE`

This constant provides a base step-by-step plan for the agent to follow when neither few-shot examples nor specific database administrator instructions are available.

- **Usage**: This plan is used as a fallback when the agent must generate SQL queries without additional guidance or examples.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `FORMAT_INSTRUCTIONS`

This constant defines the expected format for the agent's thought process and actions when generating SQL queries.

- **Usage**: This format is used to structure the agent's workflow and ensure consistency in the output.
- **Parameters**:
  - `{tool_names}`: Placeholder for the list of tool names the agent can use.

### `SUFFIX_WITH_FEW_SHOT_SAMPLES`

This constant provides a suffix template for the agent to use when few-shot examples are available.

- **Usage**: This suffix is used to initiate the agent's process when similar Question/SQL pairs are to be considered.
- **Parameters**:
  - `{input}`: Placeholder for the input question.
  - `{agent_scratchpad}`: Placeholder for the agent's scratchpad content.

### `SUFFIX_WITHOUT_FEW_SHOT_SAMPLES`

This constant provides a suffix template for the agent to use when few-shot examples are not available.

- **Usage**: This suffix is used to initiate the agent's process when it needs to find relevant tables without the aid of examples.
- **Parameters**:
  - `{input}`: Placeholder for the input question.
  - `{agent_scratchpad}`: Placeholder for the agent's scratchpad content.

### `FINETUNING_SYSTEM_INFORMATION`

This constant provides additional information for the agent, emphasizing its role as an expert in generating SQL queries and the necessity to follow database administrator instructions.

- **Usage**: This information is used during the fine-tuning phase to reinforce the agent's understanding of its role and responsibilities.

### `FINETUNING_AGENT_SUFFIX`

This constant provides a suffix template for the agent to use during the fine-tuning phase.

- **Usage**: This suffix is used to initiate the agent's process during fine-tuning, with a focus on generating SQL queries.
- **Parameters**:
  - `{input}`: Placeholder for the input question.
  - `{agent_scratchpad}`: Placeholder for the agent's scratchpad content.

### `FINETUNING_AGENT_PREFIX`

This constant defines a template for the agent to use during the fine-tuning phase, outlining the agent's role, restrictions, and instructions from the database administrator.

- **Usage**: This prefix is used to guide the agent's behavior during fine-tuning.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.
  - `{admin_instructions}`: Placeholder for the instructions provided by the database administrator.

### `FINETUNING_AGENT_PREFIX_FINETUNING_ONLY`

This constant defines a template similar to `FINETUNING_AGENT_PREFIX` but is specifically tailored for the fine-tuning phase only.

- **Usage**: This prefix is used to guide the agent's behavior during fine-tuning when the focus is solely on generating and executing SQL queries.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.
  - `{admin_instructions}`: Placeholder for the instructions provided by the database administrator.

### `ERROR_PARSING_MESSAGE`

This constant provides a message to be used when the agent encounters a parsing error.

- **Usage**: This message is returned by the agent when it fails to parse the input correctly or when it needs to return an error message due to consistent parsing issues.

## Usage in the Project

The constants defined in `agent_prompts.py` are used throughout the project to provide structured guidance and instructions to the agent responsible for generating SQL queries. These templates ensure that the agent's output is consistent, follows the required format, and adheres to any specific instructions or constraints. The agent utilizes these prompts during both the fine-tuning phase and the actual query generation process to interact with the database and tools effectively.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/s3.md

# S3 Class

## Overview

The `S3` class provides an interface for uploading and downloading files to and from Amazon S3 storage using the `boto3` library. It supports operations with optional encryption and decryption of credentials using the `FernetEncrypt` class from the `dataherald.utils.encrypt` module.

## Attributes

- `settings`: An instance of the `Settings` class from the `dataherald.config` module, which contains configuration settings for the project.

## Methods

### `__init__(self)`

The constructor initializes the `S3` class by setting the `settings` attribute to an instance of the `Settings` class.

### `upload(self, file_location, file_storage: FileStorage | None = None) -> str`

Uploads a file to an S3 bucket.

#### Parameters

- `file_location`: A string representing the local file path of the file to be uploaded.
- `file_storage`: An optional `FileStorage` object that contains S3 bucket details and encrypted AWS credentials. If not provided, the default settings from the `Settings` instance are used.

#### Returns

- A string representing the S3 URI of the uploaded file in the format `s3://bucket_name/file_name`.

#### Behavior

1. Extracts the file name from the `file_location` by splitting the string on `/` and taking the last element.
2. Sets the default bucket name to `"k2-core"`.
3. If a `FileStorage` object is provided, it initializes a `FernetEncrypt` instance to decrypt the AWS credentials stored in `FileStorage`. It then creates an S3 client with these decrypted credentials and the specified region.
4. If no `FileStorage` object is provided, it creates an S3 client using the AWS credentials from the `settings` attribute.
5. Calls the `upload_file` method of the S3 client to upload the file to the specified bucket using the base name of the file location.
6. Removes the local file after successful upload.
7. Constructs and returns the S3 URI of the uploaded file.

### `download(self, path: str, file_storage: FileStorage | None = None) -> str`

Downloads a file from an S3 bucket.

#### Parameters

- `path`: A string representing the S3 URI of the file to be downloaded.
- `file_storage`: An optional `FileStorage` object that contains S3 bucket details and encrypted AWS credentials. If not provided, the default settings from the `Settings` instance are used.

#### Returns

- A string representing the local file path of the downloaded file.

#### Behavior

1. Initializes a `FernetEncrypt` instance for potential decryption of file content.
2. Splits the `path` string on `/` to separate the bucket name and file key.
3. If a `FileStorage` object is provided, it decrypts the AWS credentials and creates an S3 client with these credentials and the specified region.
4. If no `FileStorage` object is provided, it creates an S3 client using the AWS credentials from the `settings` attribute.
5. Sets the local file location to a temporary directory with the name of the file to be downloaded.
6. Constructs the S3 file key from the remaining elements of the split `path`.
7. Calls the `download_file` method of the S3 client to download the file to the specified local file location.
8. Attempts to decrypt the file content using the `FernetEncrypt` instance. If decryption is successful, it writes the decrypted content back to the file. If decryption fails due to an `InvalidToken` or `UnicodeDecodeError`, it does nothing.
9. Returns the local file path of the downloaded file.

## Usage

The `S3` class is used in the project to handle file uploads and downloads to and from Amazon S3 storage. It abstracts the complexity of AWS credentials management and file encryption/decryption, providing a simple interface for file transfer operations.

## Dependencies

- `os`: Standard Python module for interacting with the operating system.
- `boto3`: Amazon Web Services (AWS) SDK for Python, used for interacting with AWS services.
- `cryptography.fernet.InvalidToken`: Exception class for handling invalid encryption tokens.
- `dataherald.config.Settings`: Configuration settings class for the project.
- `dataherald.sql_database.models.types.FileStorage`: Data model class representing file storage details.
- `dataherald.utils.encrypt.FernetEncrypt`: Utility class for encrypting and decrypting data.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/__init__.md

# `dataherald.utils` Package

## Overview

The `dataherald.utils` package is a utility module within the `dataherald` project. It is designed to provide common helper functions and classes that can be used across different modules of the project. The `__init__.py` file within this package serves as an initializer for the `utils` package, allowing for the organization of utility code and potentially the exposure of utility functions and classes to other packages within the `dataherald` project.

## Usage

The `__init__.py` file is automatically executed whenever the `dataherald.utils` package is imported. This behavior is part of Python's package initialization process. The file can be used to perform the following tasks:

1. Import utility functions and classes from other modules within the `utils` package to create a unified API surface.
2. Define package-level variables and constants that are common to the utilities.
3. Perform any initialization required for the utility functions and classes, such as setting up logging, configuration, or environment checks.
4. Optionally, define utility functions and classes directly within the `__init__.py` file if they are concise and do not warrant a separate module file.

## Structure

The structure of the `__init__.py` file within the `dataherald.utils` package can vary depending on the needs of the project. A typical structure might include:

- Import statements for external libraries that are used by the utility functions.
- Import statements for utility functions and classes from other modules within the `utils` package.
- Definitions of constants or global variables used by multiple utility functions.
- Definitions of any utility functions or classes that are simple enough to be included directly in the `__init__.py` file.
- Initialization code that needs to run when the package is imported.

## Example

Below is a hypothetical example of what the `__init__.py` file might contain:

python
# Import external libraries
import os
import logging

# Import utility modules from within the utils package
from .file_helpers import load_json, save_json
from .string_helpers import sanitize_string

# Define package-level constants
DEFAULT_LOG_LEVEL = logging.INFO

# Set up package-level logging configuration
logging.basicConfig(level=DEFAULT_LOG_LEVEL)
logger = logging.getLogger(__name__)

# Define any utility functions/classes directly in the __init__.py file
def get_project_root():
    """Return the absolute path to the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Perform any necessary package initialization
logger.info("Initializing dataherald.utils package")

# Expose utility functions/classes at the package level
__all__ = ['load_json', 'save_json', 'sanitize_string', 'get_project_root']


In this example, the `__init__.py` file imports necessary external libraries and utility modules, sets up logging, defines a utility function, performs initialization logging, and exposes a list of utility functions and classes that should be available when importing `dataherald.utils`.

## Integration with Other Modules

Other modules within the `dataherald` project can use the utilities provided by the `utils` package by importing them as follows:

python
from dataherald.utils import load_json, get_project_root


This allows for code reuse and helps maintain a clean and organized codebase by centralizing common functionality within the `utils` package.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/error_codes.md

# `error_codes.py` Module

## Overview

The `error_codes.py` module is part of the `dataherald` package, specifically within the `utils` subpackage. It provides utilities for error handling and response formatting in a web application using the FastAPI framework. The module defines a mapping of custom exception names to error codes, a `CustomError` class for raising custom exceptions, and functions to generate standardized error responses.

## ERROR_MAPPING Dictionary

`ERROR_MAPPING` is a Python dictionary that maps the names of custom exception classes to corresponding error code strings. This mapping is used to translate exceptions into human-readable error codes that can be returned in API responses.

Example:
python
ERROR_MAPPING = {
    "InvalidId": "invalid_object_id",
    # ... other mappings
}


## CustomError Class

`CustomError` is a custom exception class that extends the built-in `Exception` class. It allows for the creation of exceptions with an optional description.

### Attributes

- `description` (str, optional): An additional string providing more details about the error.

### `__init__` Method

The constructor takes the following parameters:

- `message` (str): The error message.
- `description` (str, optional): A detailed description of the error.

## error_response Function

The `error_response` function generates a `JSONResponse` object that contains standardized error information. This function is typically used to return an error response from an API endpoint.

### Parameters

- `error` (Exception): The exception that was raised.
- `detail` (dict): A dictionary containing additional details about the error.
- `default_error_code` (str, optional): A default error code string to use if the exception is not found in the `ERROR_MAPPING`.

### Behavior

1. Retrieves the error code from `ERROR_MAPPING` using the exception class name. If not found, uses the `default_error_code`.
2. Extracts the `description` attribute from the error, if present.
3. Logs the error information using the `logging` module.
4. Removes any `metadata` key from the `detail` dictionary.
5. Returns a `JSONResponse` with a status code of 400 and a content dictionary containing the error code, message, description, and detail.

## stream_error_response Function

The `stream_error_response` function is similar to `error_response` but returns a dictionary instead of a `JSONResponse` object. This is useful for streaming responses or other contexts where a `JSONResponse` is not appropriate.

### Parameters

- `error` (Exception): The exception that was raised.
- `detail` (dict): A dictionary containing additional details about the error.
- `default_error_code` (str, optional): A default error code string to use if the exception is not found in the `ERROR_MAPPING`.

### Behavior

1. Retrieves the error code from `ERROR_MAPPING` using the exception class name. If not found, uses the `default_error_code`.
2. Extracts the `description` attribute from the error, if present.
3. Logs the error information using the `logging` module.
4. Removes any `metadata` key from the `detail` dictionary.
5. Returns a dictionary with the error code, message, description, and detail.

## Usage in a Project

In a FastAPI project, these utilities are used to handle exceptions that occur during request processing. When an exception is caught, the `error_response` or `stream_error_response` function can be called to generate a standardized error payload that is then returned to the client. This ensures that all error responses follow a consistent format, making it easier for clients to handle errors and for developers to debug issues.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/utils/models_context_window.md

# Models Context Window Configuration

## Overview

The `models_context_window.py` file contains two Python dictionaries that define the context window sizes for various models. These context window sizes are critical for understanding the maximum number of tokens that a model can process in a single prompt or generation.

## Dictionaries

### OPENAI_CONTEXT_WINDOW_SIZES

This dictionary maps model identifiers to their respective context window sizes, measured in the number of tokens. The context window size is the maximum length of the input that the model can handle when generating text.

#### Key-Value Structure

- **Key**: A string representing the model identifier.
- **Value**: An integer representing the number of tokens in the model's context window.

#### Usage

This dictionary is used to look up the context window size for a specific model, which is necessary when preparing data for input to the model or when handling the model's output. It ensures that the input does not exceed the model's maximum token limit.

### OPENAI_FINETUNING_MODELS_WINDOW_SIZES

This dictionary is similar to `OPENAI_CONTEXT_WINDOW_SIZES` but is specifically tailored for models that are available for fine-tuning. Fine-tuning models might have different context window sizes compared to their base counterparts.

#### Key-Value Structure

- **Key**: A string representing the fine-tuning model identifier.
- **Value**: An integer representing the number of tokens in the fine-tuning model's context window.

#### Usage

This dictionary is used during the fine-tuning process to ensure that the training data fits within the model's context window. It is crucial for optimizing the fine-tuning process and maximizing the effectiveness of the fine-tuned model.

## Model Identifiers and Context Sizes

The dictionaries include various versions of the GPT-3.5 Turbo and GPT-4 models, with context window sizes ranging from 4,000 to 128,000 tokens. The identifiers often include additional information such as the model version or a date code (e.g., "0613" or "0314").

## Integration in the Project

These dictionaries are likely used by other modules within the project to:

1. Validate and preprocess input data to ensure it is within the context window size for the selected model.
2. Configure model parameters when initializing models for tasks such as text generation, fine-tuning, or inference.
3. Handle edge cases where input might be truncated or split into chunks that fit within the model's context window.

## Conclusion

The `models_context_window.py` file serves as a configuration resource within the project, providing essential information about the operational limits of various language models. It is a key component for maintaining the integrity of data processing and model interaction throughout the project's lifecycle.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/server/__init__.md

# Server Module

## Overview

The `Server` module, located at `/workspaces/documentation-generator/target_code/dataherald/server/__init__.py`, defines an abstract base class that serves as a blueprint for server implementations within the `dataherald` project. This module is part of the `dataherald` package, which is assumed to be a data processing or data serving application.

## Dependencies

- `abc`: The `abc` module from the Python standard library provides facilities for defining Abstract Base Classes (ABCs).
- `dataherald.config`: This is a custom module within the `dataherald` package that presumably contains configuration settings, including the `Settings` class.

## Server Class

### Description

The `Server` class is an abstract base class that outlines the required interface for server objects within the `dataherald` project. It enforces that all subclasses must implement the specified abstract methods and properties.

### Attributes

The `Server` class does not define any concrete attributes. It is designed to be subclassed by concrete server implementations that will provide the necessary attributes based on the specific server's requirements.

### Methods

#### `__init__(self, settings: Settings)`

- **Description**: This is an abstract method that serves as the constructor for the `Server` class. It is meant to be overridden by subclasses, which should provide their own initialization logic.
- **Parameters**:
  - `settings` (`Settings`): An instance of the `Settings` class from the `dataherald.config` module. This parameter is expected to contain configuration settings relevant to the server's operation.
- **Returns**: None. As an abstract method, it does not contain any implementation. Subclasses are responsible for providing the implementation.

### Usage

The `Server` class is not meant to be instantiated directly due to its abstract nature. Instead, it should be subclassed by concrete server classes that implement the `__init__` method and any other server-specific functionality.

Concrete subclasses must provide an implementation for the `__init__` method that accepts a `Settings` object and performs any necessary initialization for the server.

Example of subclassing the `Server` class:

python
from dataherald.server import Server
from dataherald.config import Settings

class ConcreteServer(Server):
    def __init__(self, settings: Settings):
        # Implement initialization logic specific to ConcreteServer
        self.port = settings.port
        self.host = settings.host
        # Additional initialization code as required

# Usage of the ConcreteServer class
settings = Settings(port=8080, host='localhost')
server = ConcreteServer(settings)


In the above example, `ConcreteServer` is a hypothetical implementation of the `Server` class that initializes server-specific settings such as `port` and `host`.

## Notes

- The `Server` class is part of a larger project structure and is expected to interact with other components within the `dataherald` package.
- The actual server logic, such as starting and stopping the server, handling requests, and other server-related tasks, is not defined in this abstract class and must be implemented by the subclasses.
- The `Settings` class is assumed to be a custom class that encapsulates configuration settings. The structure and attributes of the `Settings` class are not detailed in this documentation and should be referred to in the `dataherald.config` module documentation.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/server/fastapi/__init__.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/smart_cache/__init__.md

# SmartCache Module

## Overview

The `SmartCache` module, located at `/workspaces/documentation-generator/target_code/dataherald/smart_cache/__init__.py`, provides an abstract base class for implementing various caching mechanisms within the project. This module is part of the `dataherald` package and is designed to be extended by concrete cache classes that implement the specified abstract methods.

## Dependencies

- `abc`: The module uses the `ABC` class and the `abstractmethod` decorator from the `abc` module to define the `SmartCache` as an abstract base class.
- `typing`: The `Any` and `Union` types from the `typing` module are used for type hinting.
- `dataherald.config`: The `Component` class is imported from the `dataherald.config` module, which `SmartCache` inherits from.
- `dataherald.types`: The `Response` type is imported from the `dataherald.types` module and is used in the type hinting of the `add` method.

## SmartCache Class

### Description

The `SmartCache` class serves as a base class for all cache implementations within the project. It inherits from both `Component` and `ABC`, indicating that it is a configurable component that must be subclassed to create a usable cache object. The class defines the structure and expected behavior of cache objects through abstract methods that must be implemented by subclasses.

### Methods

#### `add`

python
@abstractmethod
def add(self, key: str, value: Response) -> dict[str, Any]:
    """Adds a key-value pair to the cache."""


- **Parameters**:
  - `key` (`str`): The key under which the value should be stored in the cache.
  - `value` (`Response`): The value to be stored in the cache, where `Response` is a type defined in the `dataherald.types` module.
- **Returns**: A dictionary (`dict[str, Any]`) that may contain metadata or status information about the operation.
- **Description**: This method is an abstract method that must be implemented by subclasses. It is intended to add a key-value pair to the cache. The actual implementation will depend on the specific caching strategy used by the subclass.

#### `lookup`

python
@abstractmethod
def lookup(self, key: str) -> str:
    """Looks up a key in the cache."""


- **Parameters**:
  - `key` (`str`): The key to look up in the cache.
- **Returns**: A string (`str`) representing the cached value associated with the provided key.
- **Description**: This method is an abstract method that must be implemented by subclasses. It is intended to retrieve a value from the cache based on the provided key. The actual implementation will depend on the specific caching strategy used by the subclass.

## Usage

The `SmartCache` class is not intended to be instantiated directly. Instead, it provides a template for creating concrete cache classes that implement the `add` and `lookup` methods. These concrete classes will provide the actual caching functionality, such as storing data in memory, on disk, or in a distributed cache system.

Subclasses must override the abstract methods with concrete implementations that handle the addition and retrieval of data from the cache. Once implemented, these cache classes can be used throughout the project to improve performance by reducing redundant data retrieval operations.

## Example

Below is a hypothetical example of a subclass that implements the `SmartCache` abstract methods:

python
class MemoryCache(SmartCache):
    def __init__(self):
        self._cache = {}

    def add(self, key: str, value: Response) -> dict[str, Any]:
        self._cache[key] = value
        return {"status": "success"}

    def lookup(self, key: str) -> str:
        return self._cache.get(key, "Not Found")


In this example, `MemoryCache` is a simple in-memory cache that stores key-value pairs in a Python dictionary. The `add` method adds the key-value pair to the dictionary, and the `lookup` method retrieves the value associated with the key, returning "Not Found" if the key does not exist in the cache.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/eval/eval_agent.md

# EvaluationAgent

## Overview
`EvaluationAgent` is a subclass of `Evaluator` designed to evaluate the correctness of SQL queries in relation to a given user prompt. It leverages a language model (LLM) to generate a score that reflects how accurately the SQL query answers the question posed by the user.

## Attributes
- `sample_rows` (int): The number of sample rows to retrieve from the database when providing context to the LLM.
- `llm` (Any): The language model used for generating the evaluation.

## Methods

### `__init__(self, system: System)`
Constructor for the `EvaluationAgent` class.
- Parameters:
  - `system` (System): An instance of the `System` configuration class.

### `answer_parser(self, answer: str) -> int`
Parses the LLM's response to extract the score.
- Parameters:
  - `answer` (str): The raw string output from the LLM.
- Returns:
  - An integer score extracted from the LLM's response.

### `create_evaluation_agent(...) -> AgentExecutor`
Creates an `AgentExecutor` configured for evaluating SQL queries.
- Parameters:
  - `toolkit` (SQLEvaluationToolkit): An instance of `SQLEvaluationToolkit` containing the tools for interacting with the SQL database.
  - `database_connection` (DatabaseConnection): The connection details for the SQL database.
  - `prefix` (str): A string template used to generate the initial part of the prompt for the LLM.
  - `suffix` (str): A string template used to generate the final part of the prompt for the LLM.
  - `callback_manager` (BaseCallbackManager | None): A callback manager for handling tool execution callbacks.
  - `format_instructions` (str): Instructions on how the LLM should format its response.
  - `input_variables` (List[str] | None): A list of variables to be included in the prompt.
  - `max_iterations` (int | None): The maximum number of iterations the agent is allowed to perform.
  - `max_execution_time` (float | None): The maximum time allowed for the agent to execute.
  - `early_stopping_method` (str): The method used to determine when to stop the agent early.
  - `verbose` (bool): Whether to output verbose logging information.
  - `agent_executor_kwargs` (Dict[str, Any] | None): Additional keyword arguments for the `AgentExecutor`.
  - `**kwargs` (Dict[str, Any]): Additional keyword arguments for the `ZeroShotAgent`.
- Returns:
  - An instance of `AgentExecutor` configured with the provided parameters.

### `evaluate(self, user_prompt: Prompt, sql_generation: SQLGeneration, database_connection: DatabaseConnection) -> Evaluation`
Evaluates the given SQL query against the user prompt and returns an `Evaluation` object.
- Parameters:
  - `user_prompt` (Prompt): The user's question prompt.
  - `sql_generation` (SQLGeneration): The generated SQL query to be evaluated.
  - `database_connection` (DatabaseConnection): The connection details for the SQL database.
- Returns:
  - An `Evaluation` object containing the question ID, answer ID, and the score.

## Usage
The `EvaluationAgent` is used within a project to evaluate SQL queries generated in response to user prompts. It is instantiated with a `System` configuration, and the `evaluate` method is called with a `Prompt`, `SQLGeneration`, and `DatabaseConnection`. The agent uses the provided `SQLEvaluationToolkit` to interact with the database and leverages a language model to generate a score that reflects the accuracy of the SQL query in answering the user's question.

## Dependencies
- `Evaluator`: The base class from which `EvaluationAgent` inherits.
- `SQLEvaluationToolkit`: A toolkit class that provides tools for interacting with SQL databases.
- `AgentExecutor`: A class used to execute the evaluation agent.
- `ZeroShotAgent`: A class representing an agent that can evaluate SQL queries without prior training.
- `LLMChain`: A class representing a chain of language model operations.
- `SQLDatabase`: A class for interacting with SQL databases.
- `DatabaseConnection`: A class representing the connection details for a SQL database.
- `Evaluation`: A class representing the result of an evaluation, including the score.

## Example
python
system_config = System(...)
evaluation_agent = EvaluationAgent(system=system_config)
prompt = Prompt(id="1", text="What is the total revenue?")
sql_generation = SQLGeneration(sql="SELECT SUM(revenue) FROM sales;")
database_connection = DatabaseConnection(...)

evaluation = evaluation_agent.evaluate(
    user_prompt=prompt,
    sql_generation=sql_generation,
    database_connection=database_connection
)
print(evaluation.score)  # Outputs the score as a float between 0 and 1.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/eval/simple_evaluator.md

# SimpleEvaluator Class

## Overview

`SimpleEvaluator` is a subclass of `Evaluator` that provides functionality to evaluate the correctness of SQL queries generated in response to user questions. It leverages a language model chain (`LLMChain`) to analyze SQL queries and assign a score based on their accuracy and adherence to best practices.

## Attributes

- `llm`: An instance of a language model chain used for evaluating SQL queries.

## Methods

### `__init__(self, system: System)`

Constructor for the `SimpleEvaluator` class.

#### Parameters

- `system`: An instance of `System` containing the configuration and components of the project.

#### Behavior

- Initializes the `SimpleEvaluator` instance by calling the superclass constructor and setting the `system` attribute.

### `answer_parser(self, answer: str) -> int`

Parses the evaluator's textual answer to extract a numerical score.

#### Parameters

- `answer`: A string containing the evaluator's response.

#### Returns

- An integer score between 0 and 100.

#### Behavior

- Searches for a pattern "Score: <number>" in the answer.
- If the pattern is found, returns the number as an integer.
- If the pattern is not found, searches for the last number in the answer that is between 0 and 100.
- If no number is found, returns 0.

### `evaluate(self, user_prompt: Prompt, sql_generation: SQLGeneration, database_connection: DatabaseConnection) -> Evaluation`

Evaluates the correctness of a SQL query generated in response to a user prompt.

#### Parameters

- `user_prompt`: An instance of `Prompt` representing the user's question.
- `sql_generation`: An instance of `SQLGeneration` containing the generated SQL query.
- `database_connection`: An instance of `DatabaseConnection` representing the database connection details.

#### Returns

- An instance of `Evaluation` containing the question ID, answer ID, and the calculated score.

#### Behavior

- Retrieves the SQL engine for the given database connection.
- Logs the start of the evaluation process.
- Retrieves the table descriptions from the database using `TableDescriptionRepository`.
- Initializes the language model chain with the appropriate configuration.
- Parses the SQL query to extract table names.
- Constructs the schema description for the tables involved in the SQL query.
- Checks if the SQL query is marked as "INVALID" and returns a score of 0 if so.
- Executes the SQL query against the database and fetches the results.
- Converts the query results into a format suitable for the language model evaluation.
- Invokes the language model chain with the constructed prompt, including the dialect, question, SQL query, and results.
- Parses the language model's textual response to extract the score.
- Logs the score and the time taken for the evaluation.
- Returns the `Evaluation` instance with the calculated score.

## Usage

The `SimpleEvaluator` class is used within the project to evaluate the accuracy of SQL queries generated by the system. It is instantiated with the system configuration and then called upon to evaluate SQL queries using the `evaluate` method. The evaluation process involves parsing the SQL query, executing it against the database, and using a language model to analyze the query and results. The evaluator assigns a score based on the analysis and returns it as part of an `Evaluation` object.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/eval/__init__.md

# `dataherald/eval/__init__.py` Module

## Overview

This module defines the abstract base class `Evaluator` and the `Evaluation` data model used within the `dataherald` project. The `Evaluator` class is designed to assess the quality of SQL queries generated in response to user prompts. It is part of a larger system that involves natural language processing and SQL generation.

## Classes

### `Evaluation`

The `Evaluation` class is a Pydantic model that represents the result of evaluating a generated SQL query against a user prompt. It includes the following fields:

- `id`: An optional string that serves as a unique identifier for the evaluation instance. It is aliased to `_id` in the underlying data.
- `question_id`: An optional string that represents the identifier of the user's question. It is aliased to `q_id`.
- `answer_id`: An optional string that represents the identifier of the generated answer. It is aliased to `a_id`.
- `score`: A floating-point number constrained between 0 and 1 (inclusive) that represents the confidence score of the evaluation. The default value is set to 0.5.

### `Evaluator`

The `Evaluator` class is an abstract base class that inherits from both `Component` and `ABC` (Abstract Base Class). It is designed to evaluate SQL queries generated in response to user prompts. The class contains the following attributes and methods:

#### Attributes

- `database`: An instance of `SQLDatabase` that represents the database where the SQL queries will be executed.
- `acceptance_threshold`: A floating-point number constrained between 0 and 1 (inclusive) that defines the threshold for accepting a generated SQL query as valid. The default value is set to 0.8.
- `llm_config`: An instance of `LLMConfig` that holds the configuration for the language learning model.
- `llm`: An optional instance of `ChatModel` that represents the language learning model used for generating SQL queries. It is initialized to `None`.

#### Constructor

- `__init__(self, system: System)`: The constructor initializes the `Evaluator` with a reference to the `System` object and creates an instance of `ChatModel` using the system configuration.

#### Methods

- `get_confidence_score(self, user_prompt: Prompt, sql_generation: SQLGeneration, database_connection: DatabaseConnection) -> confloat`: This method calculates the confidence score of a generated SQL query by calling the `evaluate` method. It returns a floating-point number representing the confidence score.

- `evaluate(self, user_prompt: Prompt, sql_generation: SQLGeneration, database_connection: DatabaseConnection) -> Evaluation`: This is an abstract method that must be implemented by subclasses. It evaluates the generated SQL query against the user prompt and returns an `Evaluation` object.

## Usage

The `Evaluator` class is intended to be subclassed by concrete evaluator implementations that define the `evaluate` method. These implementations will use the `evaluate` method to assess the quality of SQL queries generated in response to user prompts. The `get_confidence_score` method can be used to retrieve the confidence score of the evaluation, which can then be compared against the `acceptance_threshold` to determine if the generated SQL query is acceptable.

The `Evaluation` class is used to encapsulate the results of the evaluation process, including the unique identifiers for the question and answer, as well as the confidence score of the evaluation.

## Integration

The `Evaluator` class is part of a larger system that involves components for natural language processing, SQL generation, and database interaction. It is designed to work within the `dataherald` project's infrastructure, which includes configuration management (`LLMConfig`), database models (`SQLDatabase`, `DatabaseConnection`), and a chat model (`ChatModel`).

The module is located at `/workspaces/documentation-generator/target_code/dataherald/eval/__init__.py` within the project's directory structure.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_generator/adaptive_agent_executor.md

# AdaptiveAgentExecutor Class

## Overview

`AdaptiveAgentExecutor` is a subclass of `AgentExecutor` that is designed to execute a sequence of actions determined by an agent. It is capable of handling single and multi-action agents, managing tools, and adapting the execution based on the context size and token count.

## Attributes

- `agent`: An instance of either `BaseSingleActionAgent` or `BaseMultiActionAgent` that defines the agent to be executed.
- `tools`: A sequence of `BaseTool` instances that the agent can use to perform actions.
- `return_intermediate_steps`: A boolean indicating whether to return intermediate steps of execution.
- `max_iterations`: An optional integer specifying the maximum number of iterations to execute.
- `max_execution_time`: An optional float specifying the maximum execution time in seconds.
- `early_stopping_method`: A string indicating the method for early stopping, defaulting to "force".
- `handle_parsing_errors`: A union type that can be a boolean, a string, or a callable function to handle parsing errors.
- `trim_intermediate_steps`: A union type that can be an integer or a callable function to trim intermediate steps.
- `llm_list`: A dictionary containing different language model instances.
- `switch_to_larger_model_threshold`: An integer specifying the token count threshold to switch to a larger language model.
- `enc`: An instance of `Encoding` used for token counting.
- `tokens`: An integer representing the initial token count based on the agent's prompt template.

## Methods

### from_agent_and_tools

A class method that creates an instance of `AdaptiveAgentExecutor` from the given agent, tools, and additional parameters.

#### Parameters

- `agent`: The agent to be executed.
- `tools`: The tools available for the agent to use.
- `llm_list`: A dictionary of language model instances.
- `switch_to_larger_model_threshold`: The token count threshold for switching language models.
- `encoding`: The encoding instance for token counting.
- `callbacks`: Optional `Callbacks` instance for managing callbacks during execution.
- `**kwargs`: Additional keyword arguments.

#### Returns

- An instance of `AgentExecutor`.

### token_counter

Calculates the total token count including the tokens from intermediate steps.

#### Parameters

- `intermediate_steps`: A list of tuples containing `AgentAction` and the corresponding output string.

#### Returns

- An integer representing the updated token count.

### _take_next_step

An overridden method that executes the next step in the agent's plan.

#### Parameters

- `name_to_tool_map`: A dictionary mapping tool names to `BaseTool` instances.
- `color_mapping`: A dictionary mapping tool names to their corresponding color for output.
- `inputs`: A dictionary of input values for the agent.
- `intermediate_steps`: A list of tuples containing `AgentAction` and the corresponding output string.
- `run_manager`: An optional `CallbackManagerForChainRun` instance for managing callbacks.

#### Returns

- Either an `AgentFinish` instance if the execution is complete or a list of tuples containing `AgentAction` and the corresponding output string.

#### Behavior

1. Prepares intermediate steps.
2. Checks if the token count exceeds the threshold and switches to a larger language model if necessary.
3. Calls the agent's `plan` method to determine the next action(s).
4. Handles `OutputParserException` errors based on the `handle_parsing_errors` attribute.
5. Executes the chosen tool's `run` method with the tool input to obtain an observation.
6. Appends the `AgentAction` and observation to the result list.
7. Returns the result list or an `AgentFinish` instance.

## Usage

`AdaptiveAgentExecutor` is used within a project to execute an agent that can perform a sequence of actions using various tools. It adapts to the context size by switching between language models and manages token counts to ensure efficient execution. It is typically instantiated with the `from_agent_and_tools` class method and then used to execute the agent's plan step by step with the `_take_next_step` method.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_generator/create_sql_query_status.md

# `create_sql_query_status.py` Module

## Overview

The `create_sql_query_status.py` module is part of the `dataherald` project and is responsible for validating SQL queries and updating the status of SQL generation objects. It includes functionality to execute SQL queries against a database with a timeout, handle potential SQL injection attempts, and format error messages.

## Dependencies

- `os`: Standard library module to interact with the operating system.
- `dataherald.sql_database.base`: Custom module providing `SQLDatabase` class and `SQLInjectionError` exception.
- `dataherald.types`: Custom module defining `SQLGeneration` type.
- `dataherald.utils.timeout_utils`: Custom module providing `run_with_timeout` function.

## Functions

### `format_error_message(sql_generation: SQLGeneration, error_message: str) -> SQLGeneration`

#### Description

This function takes an `SQLGeneration` object and an error message string, formats the error message by removing the complete SQL query between square brackets, updates the `SQLGeneration` object's status to "INVALID", and sets the error message.

#### Parameters

- `sql_generation`: An instance of `SQLGeneration` that holds the status and error message of the SQL generation process.
- `error_message`: A string containing the error message that may include the SQL query.

#### Returns

- An updated `SQLGeneration` object with the formatted error message and status set to "INVALID".

### `create_sql_query_status(db: SQLDatabase, query: str, sql_generation: SQLGeneration) -> SQLGeneration`

#### Description

This function determines the status of an SQL query by attempting to execute it against a database. It populates the `sql_generation` object with the result of the execution, the status of the SQL generation, and any error messages encountered during the process.

#### Parameters

- `db`: An instance of `SQLDatabase` that provides methods to interact with the database and parse/filter SQL commands.
- `query`: A string containing the SQL query to be executed.
- `sql_generation`: An instance of `SQLGeneration` that will be updated with the status and error message of the SQL generation process.

#### Returns

- An updated `SQLGeneration` object with the status set to either "VALID" or "INVALID" and the error message populated if applicable.

#### Behavior

1. Checks if the `query` string is empty. If it is, sets the `sql_generation` status to "INVALID" and sets the error message to indicate that SQL could not be generated from the prompt.
2. If the `query` is not empty, it proceeds to:
   - Parse and filter the query using `db.parser_to_filter_commands`.
   - Execute the query with a timeout using `run_with_timeout`, with the timeout duration fetched from the environment variable `SQL_EXECUTION_TIMEOUT` or defaulting to 60 seconds.
   - If the query executes successfully within the timeout, sets the `sql_generation` status to "VALID" and clears any error message.
3. Handles exceptions:
   - `TimeoutError`: Calls `format_error_message` to set the status to "INVALID" and sets the error message to indicate a timeout.
   - `SQLInjectionError`: Reraises the exception with a message indicating a sensitive SQL keyword was detected.
   - Any other `Exception`: Calls `format_error_message` with the exception message to set the status to "INVALID" and populate the error message.

#### Usage

This function is used within the `dataherald` project to validate SQL queries generated from user prompts or other sources. It ensures that the queries are safe to execute and provides feedback on any issues encountered during the validation process.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_generator/dataherald_sqlagent.md

# Dataherald SQL Agent (`dataherald_sqlagent.py`)

## Overview

The `dataherald_sqlagent.py` module is part of the Dataherald project and is responsible for generating SQL queries based on user prompts. It leverages a combination of machine learning models, specifically language models from OpenAI, and a set of custom tools to interpret user questions and generate corresponding SQL queries that can be executed against a database.

## Dependencies

- `datetime`: For handling date and time operations.
- `difflib`: For finding differences between sequences.
- `logging`: For logging messages.
- `os`: For interacting with the operating system.
- `queue`: For queue data structure to handle streaming data.
- `threading`: For running operations in separate threads.
- `typing`: For type annotations.
- `numpy`: For numerical operations, especially for calculating cosine similarity.
- `openai`: For interacting with OpenAI's language models.
- `pandas`: For data manipulation and analysis.
- `sqlalchemy`: For SQL database interaction.
- `google.api_core.exceptions`: For handling Google API errors.
- `langchain`: For chaining language models and tools.
- `overrides`: For method overriding.
- `pydantic`: For data validation and settings management through Python data classes.
- `dataherald`: For accessing the project's internal modules and utilities.

## Main Components

### Decorators

- `catch_exceptions`: A decorator to catch and handle exceptions from various sources, including OpenAI API errors, Google API errors, and SQLAlchemy errors.

### Helper Functions

- `replace_unprocessable_characters`: Replaces unprocessable characters in a string with a space.

### Classes

#### BaseSQLDatabaseTool

- Base class for tools interacting with the SQL database and context information.

#### SystemTime

- Tool for retrieving the current date and time.

#### QuerySQLDataBaseTool

- Tool for executing SQL queries against a database.

#### GetUserInstructions

- Tool for retrieving database admin instructions.

#### TablesSQLDatabaseTool

- Tool for identifying relevant tables based on a user question.

#### ColumnEntityChecker

- Tool for checking the existence of an entity within a column.

#### SchemaSQLDatabaseTool

- Tool for retrieving the schema of specified tables.

#### InfoRelevantColumns

- Tool for gathering details about potentially relevant columns.

#### GetFewShotExamples

- Tool for fetching few-shot examples to aid in SQL query generation.

#### SQLDatabaseToolkit

- Toolkit that aggregates various tools for SQL database interaction.

### DataheraldSQLAgent

- The main agent responsible for generating SQL queries based on user prompts. It orchestrates the interaction between the language model, the toolkit, and the database.

## Methods

### DataheraldSQLAgent Methods

#### `remove_duplicate_examples`

- Removes duplicate examples from a list of few-shot examples.

#### `create_sql_agent`

- Constructs an SQL agent from a language model and a set of tools.

#### `generate_response`

- Generates an SQL query in response to a user prompt.

#### `stream_response`

- Streams the response of the SQL query generation process.

## Usage

The `DataheraldSQLAgent` class is instantiated and used to generate SQL queries. It requires a user prompt and a database connection to function. The agent uses a combination of few-shot examples, admin instructions, and a set of custom tools to generate a query that matches the user's intent. The process can be streamed, allowing for real-time updates and interaction.

## Error Handling

The module includes comprehensive error handling to manage various exceptions that may occur during the query generation process, such as authentication errors, rate limit errors, and SQL execution errors.

## Logging

The module uses the `logging` library to log information, warnings, and errors throughout the execution of the agent.

## Environment Variables

The module relies on environment variables for configuration, such as `SQL_EXECUTION_TIMEOUT`, `AGENT_MAX_ITERATIONS`, and `DH_ENGINE_TIMEOUT`, which control various timeouts and limits within the agent's execution.

## Threading

The `stream_response` method uses the `threading` module to run the streaming process in a separate thread, allowing the main program to continue execution without blocking.

## Streaming

The agent supports streaming the SQL generation process, which involves sending intermediate steps and results to a queue that can be consumed by other parts of the application or by the end-user.

## Database Interaction

The module interacts with SQL databases using SQLAlchemy for executing queries and retrieving schema information. It also uses custom database models and repositories from the `dataherald` package for managing database-related operations.

## Machine Learning Models

The agent leverages OpenAI's language models to interpret user prompts and generate SQL queries. It uses embeddings to calculate relevance scores for tables and employs few-shot learning techniques to improve the quality of the generated queries.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_generator/generates_nl_answer.md

# GeneratesNlAnswer Class

## Overview

The `GeneratesNlAnswer` class is responsible for generating a natural language (NL) answer based on a given SQL query and its result. It utilizes a language model chain to process the input and produce a human-like response.

## Attributes

- `system`: An instance or identifier of the system that is used to interact with the language model.
- `storage`: A storage system where the prompts and database connection information are stored.
- `llm_config`: An instance of `LLMConfig` containing configuration details for the language model, such as the model name and API base URL.
- `model`: An instance of `ChatModel` initialized with the `system` attribute.

## Methods

### `__init__(self, system, storage, llm_config: LLMConfig)`

The constructor initializes the `GeneratesNlAnswer` class with the provided system, storage, and language model configuration.

### `execute(self, sql_generation: SQLGeneration, top_k: int = 100) -> NLGeneration`

The `execute` method is the core function of the class. It takes an `SQLGeneration` object, which contains the SQL query and associated metadata, and an optional `top_k` parameter that limits the number of SQL query results processed.

#### Steps:

1. Retrieve the prompt associated with the SQL query using `PromptRepository` and the `storage` attribute.
2. Fetch the database connection details using `DatabaseConnectionRepository` and the `storage` attribute.
3. Initialize the language model (`self.llm`) with the database connection details and the `llm_config`.
4. Create a SQL engine instance using `SQLDatabase.get_sql_engine` with the database connection details.
5. If the `sql_generation` status is "INVALID", return an `NLGeneration` object with a message indicating the SQL query is invalid.
6. Execute the SQL query using the SQL engine:
   - Parse the SQL query to filter out commands that could lead to SQL injection.
   - Connect to the database and execute the query, fetching up to `top_k` results.
   - Process each row of the result to convert `date`, `datetime`, and `Decimal` types to string or float, respectively.
7. If a `SQLInjectionError` is raised during query execution, propagate the error with an additional message.
8. Prepare the language model prompt using `HumanMessagePromptTemplate` and `ChatPromptTemplate` with the human-readable template defined in `HUMAN_TEMPLATE`.
9. Invoke the language model chain (`LLMChain`) with the prompt and the processed SQL query and results.
10. Return an `NLGeneration` object containing the generated natural language response and metadata such as the `sql_generation` ID and the current timestamp.

## Usage

The `GeneratesNlAnswer` class is used within a project to convert SQL query results into a natural language format that is easily understandable by humans. It is particularly useful in applications that require interaction with users in natural language, such as chatbots or virtual assistants that provide data insights based on SQL queries.

## Error Handling

The class includes error handling for SQL injection attempts by raising a `SQLInjectionError` if sensitive SQL keywords are detected in the query.

## Dependencies

- `datetime`: For handling date and time objects.
- `decimal`: For handling decimal numbers.
- `langchain.chains`: For the language model chain.
- `langchain.prompts.chat`: For creating chat prompts.
- `sqlalchemy`: For executing SQL queries.
- `dataherald.model.chat_model`: For the chat model.
- `dataherald.repositories.database_connections`: For fetching database connection details.
- `dataherald.repositories.prompts`: For fetching prompts.
- `dataherald.sql_database.base`: For SQL database operations.
- `dataherald.types`: For type definitions used in the class.

## Constants

- `HUMAN_TEMPLATE`: A template string used to format the prompt for the language model, which includes placeholders for the question, SQL query, and SQL query result.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_generator/dataherald_finetuning_agent.md

# DataheraldFinetuningAgent Technical Documentation

## Overview
`DataheraldFinetuningAgent` is a class within the `dataherald_finetuning_agent.py` module that extends the `SQLGenerator` class. It is designed to generate SQL queries using a fine-tuning model. The agent leverages the OpenAI API to generate responses to user prompts based on the context of a given database.

## Dependencies
- `datetime`
- `logging`
- `os`
- `functools.wraps`
- `queue.Queue`
- `threading.Thread`
- `typing` (Any, Callable, Dict, List, Type)
- `numpy` (np)
- `openai`
- `pandas` (pd)
- `google.api_core.exceptions.GoogleAPIError`
- `langchain.agents.agent.AgentExecutor`
- `langchain.agents.agent_toolkits.base.BaseToolkit`
- `langchain.agents.mrkl.base.ZeroShotAgent`
- `langchain.callbacks.base.BaseCallbackManager`
- `langchain.callbacks.manager` (AsyncCallbackManagerForToolRun, CallbackManagerForToolRun)
- `langchain.chains.llm.LLMChain`
- `langchain.tools.base.BaseTool`
- `langchain_community.callbacks.get_openai_callback`
- `langchain_openai.OpenAIEmbeddings`
- `openai.OpenAI`
- `overrides.override`
- `pydantic` (BaseModel, Field)
- `sqlalchemy.exc.SQLAlchemyError`
- `dataherald.context_store.ContextStore`
- `dataherald.db.DB`
- `dataherald.db_scanner.models.types` (TableDescription, TableDescriptionStatus)
- `dataherald.db_scanner.repository.base.TableDescriptionRepository`
- `dataherald.finetuning.openai_finetuning.OpenAIFineTuning`
- `dataherald.repositories.finetunings.FinetuningsRepository`
- `dataherald.repositories.sql_generations.SQLGenerationRepository`
- `dataherald.sql_database.base.SQLDatabase`
- `dataherald.sql_database.models.types.DatabaseConnection`
- `dataherald.sql_generator` (EngineTimeOutORItemLimitError, SQLGenerator)
- `dataherald.types` (FineTuningStatus, Prompt, SQLGeneration)
- `dataherald.utils.agent_prompts` (ERROR_PARSING_MESSAGE, FINETUNING_AGENT_PREFIX, FINETUNING_AGENT_PREFIX_FINETUNING_ONLY, FINETUNING_AGENT_SUFFIX, FINETUNING_SYSTEM_INFORMATION, FORMAT_INSTRUCTIONS)
- `dataherald.utils.models_context_window.OPENAI_FINETUNING_MODELS_WINDOW_SIZES`
- `dataherald.utils.timeout_utils.run_with_timeout`

## Constants
- `TOP_K`: Upper bound limit for SQL queries, retrieved from `SQLGenerator.get_upper_bound_limit()`.
- `EMBEDDING_MODEL`: The embedding model used for relevance scoring, set to `"text-embedding-3-large"`.
- `TOP_TABLES`: The number of top tables to consider for relevance scoring, set to `20`.

## Exceptions
- `FinetuningNotAvailableError`: Custom exception raised when finetuning is not available.

## Helper Functions
- `replace_unprocessable_characters(text: str) -> str`: Replaces unprocessable characters with a space.
- `catch_exceptions()`: Decorator function to catch and handle various exceptions from OpenAI API, Google API, and SQLAlchemy.

## Models
- `SQLInput`: Pydantic model for SQL query input.
- `QuestionInput`: Pydantic model for user question input.
- `BaseSQLDatabaseTool`: Base tool for interacting with the SQL database and context information.
- `SystemTime`: Tool for finding the current date and time.
- `TablesSQLDatabaseTool`: Tool for returning a list of tables with their relevance scores to a given question.
- `QuerySQLDataBaseTool`: Tool for querying a SQL database.
- `GenerateSQL`: Tool for generating SQL queries.
- `SchemaSQLDatabaseTool`: Tool for getting the schema of relevant tables.
- `SQLDatabaseToolkit`: Toolkit containing various tools for interacting with the SQL database.

## DataheraldFinetuningAgent Class
### Attributes
- `llm`: Language model instance.
- `finetuning_id`: Identifier for the finetuning model.
- `use_fintuned_model_only`: Boolean flag to indicate whether to use only the finetuned model.

### Methods
- `create_sql_agent(...) -> AgentExecutor`: Creates an `AgentExecutor` instance with the provided toolkit and callback manager.
- `generate_response(...) -> SQLGeneration`: Generates a response to a user question using a finetuning model.
- `stream_response(...)`: Streams the response to a user question using a finetuning model.

### Usage
1. An instance of `DataheraldFinetuningAgent` is created with the necessary configuration.
2. The `generate_response` method is called with a user prompt and database connection to generate an SQL query.
3. The `stream_response` method can be used to stream the response to a queue for asynchronous processing.

## Notes
- The agent uses OpenAI's fine-tuning capabilities to generate SQL queries that are contextually relevant to the user's question and the database schema.
- The agent can handle exceptions and errors gracefully, providing meaningful error messages.
- The agent supports both synchronous and asynchronous execution of SQL queries.
- The agent's behavior can be customized with various parameters such as `max_iterations`, `max_execution_time`, and `early_stopping_method`.
- The agent leverages embeddings to score the relevance of database tables to the user's question.
- The agent can generate SQL queries, execute them, and return results or error messages.
- The agent can also provide the schema of specified tables to assist users in constructing or editing SQL queries.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/sql_generator/__init__.md

# SQLGenerator Class Documentation

## Overview

The `SQLGenerator` class is an abstract base class designed to be inherited by classes that generate SQL queries in response to user prompts. It is part of a larger project that involves interacting with a language model to generate SQL queries, which are then executed against a database. The class is defined within the `dataherald/sql_generator` module.

## Dependencies

- `datetime`: Used for timestamping when a SQL generation is completed.
- `logging`: Used for logging messages.
- `os`: Used to access environment variables.
- `re`: Used for regular expression operations.
- `abc.ABC`: Used to create an abstract base class.
- `abc.abstractmethod`: Used to define abstract methods that must be implemented by subclasses.
- `queue.Queue`: Used for queue operations.
- `typing`: Used for type hinting.
- `sqlparse`: Used for parsing and formatting SQL queries.
- `langchain.agents.agent.AgentExecutor`: Used to execute agents in the language model.
- `langchain.callbacks.base.BaseCallbackHandler`: Used for callback handling.
- `langchain.schema`: Used for defining schema elements like `AgentAction` and `LLMResult`.
- `langchain.schema.messages.BaseMessage`: Used for message handling.
- `langchain_community.callbacks.get_openai_callback`: Used to get OpenAI callbacks.
- `dataherald.config.Component`: Used as a base class for configuration components.
- `dataherald.config.System`: Used to represent the system configuration.
- `dataherald.model.chat_model.ChatModel`: Used to interact with the chat model.
- `dataherald.repositories.sql_generations.SQLGenerationRepository`: Used to interact with the SQL generation repository.
- `dataherald.sql_database.base.SQLDatabase`: Used to interact with the SQL database.
- `dataherald.sql_database.base.SQLInjectionError`: Used to handle SQL injection errors.
- `dataherald.sql_database.models.types.DatabaseConnection`: Used to represent database connections.
- `dataherald.sql_generator.create_sql_query_status`: Used to create SQL query status.
- `dataherald.types.LLMConfig`: Used to represent language model configuration.
- `dataherald.types.Prompt`: Used to represent user prompts.
- `dataherald.types.SQLGeneration`: Used to represent SQL generation data.
- `dataherald.utils.strings.contains_line_breaks`: Used to check for line breaks in strings.

## Class Definition

### `EngineTimeOutORItemLimitError`

A custom exception class that is raised when the language model engine times out or reaches the tool limit.

### `replace_unprocessable_characters(text: str) -> str`

A static method that replaces unprocessable characters with a space.

### `SQLGenerator`

An abstract base class that defines the structure and behavior of SQL generation classes.

#### Attributes

- `metadata`: Any additional metadata associated with the SQL generator.
- `llm`: An optional `ChatModel` instance used for language model interactions.

#### Methods

- `__init__(self, system: System, llm_config: LLMConfig)`: Initializes the SQL generator with system configuration and language model configuration.
- `check_for_time_out_or_tool_limit(self, response: dict) -> dict`: Checks if the language model engine has timed out or reached the tool limit.
- `remove_markdown(self, query: str) -> str`: Removes markdown formatting from the SQL query.
- `get_upper_bound_limit() -> int`: Retrieves the upper limit for the number of rows returned by a query.
- `create_sql_query_status(self, db: SQLDatabase, query: str, sql_generation: SQLGeneration) -> SQLGeneration`: Creates a status for the SQL query.
- `format_intermediate_representations(self, intermediate_representation: List[Tuple[AgentAction, str]]) -> List[str]`: Formats the intermediate representation into a string.
- `format_sql_query(self, sql_query: str) -> str`: Formats the SQL query for readability.
- `extract_query_from_intermediate_steps(self, intermediate_steps: List[Tuple[AgentAction, str]]) -> str`: Extracts the SQL query from the intermediate steps.
- `generate_response(self, user_prompt: Prompt, database_connection: DatabaseConnection, context: List[dict] = None) -> SQLGeneration`: Abstract method to generate a response to a user question.
- `stream_agent_steps(self, question: str, agent_executor: AgentExecutor, response: SQLGeneration, sql_generation_repository: SQLGenerationRepository, queue: Queue)`: Streams the steps of the agent execution to a queue and updates the SQL generation response.
- `stream_response(self, user_prompt: Prompt, database_connection: DatabaseConnection, response: SQLGeneration, queue: Queue)`: Abstract method to stream a response to a user question.

## Usage

Subclasses of `SQLGenerator` must implement the abstract methods `generate_response` and `stream_response` to provide functionality for generating and streaming SQL query responses. The class provides utility methods for formatting SQL queries, handling intermediate representations, and managing the execution of language model agents.

Instances of subclasses are typically used within a larger system that handles user prompts, interacts with a language model, and executes SQL queries against a database. The `SQLGenerator` class provides a common interface and shared functionality for these operations.

## Error Handling

The class includes error handling for SQL injection errors and engine timeouts or tool limits. Custom exceptions are raised to indicate these errors, which can be caught and handled by the calling code.

## Environment Variables

The class uses the `UPPER_LIMIT_QUERY_RETURN_ROWS` environment variable to determine the upper limit for the number of rows returned by a query. If not set, a default value of 50 is used.

## Streaming

The `stream_agent_steps` method is used to stream the steps of the agent execution to a queue. It captures the intermediate steps, observations, and final output of the agent. It also updates the SQL generation response with the final SQL query, tokens used, completion timestamp, and any errors encountered during execution.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/api/fastapi.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/api/__init__.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/api/types/responses.md

# Responses Module Documentation

## Overview
The `responses.py` module within the `dataherald/api/types` directory defines a set of response classes that are used to structure the data returned by the API endpoints of the DataHerald project. These classes are built using Pydantic's `BaseModel` to ensure type validation and serialization. The module also includes custom validators to handle specific data formatting.

## Dependencies
- `datetime`: Provides classes for manipulating dates and times.
- `pytz`: Brings support for the Olson timezone database, allowing accurate and cross-platform timezone calculations.
- `pydantic`: A data validation and settings management library using Python type annotations.
- `dataherald.db_scanner.models.types`: Contains the `TableDescription` class definition.
- `dataherald.sql_database.models.types`: Contains the `DatabaseConnection` class definition.
- `dataherald.types`: Contains the `GoldenSQL` and `LLMConfig` class definitions.

## Classes

### BaseResponse
The `BaseResponse` class is a foundational response class that includes common attributes for all response types.

#### Attributes:
- `id`: A `str` representing a unique identifier for the response.
- `metadata`: An optional `dict` that can store additional information related to the response.
- `created_at`: An optional `str` representing the creation time of the response.

#### Validators:
- `created_at_as_string`: Ensures that the `created_at` attribute, if present, is serialized as a string in ISO 8601 format with UTC timezone.

### PromptResponse
The `PromptResponse` class extends `BaseResponse` and is used to represent responses related to prompts.

#### Attributes:
- `text`: A `str` containing the prompt text.
- `db_connection_id`: A `str` representing the identifier of the database connection associated with the prompt.

### SQLGenerationResponse
The `SQLGenerationResponse` class extends `BaseResponse` and is used to represent responses related to SQL generation tasks.

#### Attributes:
- `prompt_id`: A `str` representing the identifier of the associated prompt.
- `finetuning_id`: An optional `str` representing the identifier of the finetuning process.
- `status`: A `str` indicating the status of the SQL generation task.
- `completed_at`: An optional `str` representing the completion time of the task.
- `llm_config`: An optional `LLMConfig` instance containing configuration for the language model.
- `sql`: An optional `str` containing the generated SQL query.
- `tokens_used`: An optional `int` indicating the number of tokens used by the language model.
- `confidence_score`: An optional `float` representing the confidence score of the generated SQL.
- `error`: An optional `str` containing error information if the task failed.

#### Validators:
- `completed_at_as_string`: Ensures that the `completed_at` attribute, if present, is serialized as a string in ISO 8601 format with UTC timezone.

### NLGenerationResponse
The `NLGenerationResponse` class extends `BaseResponse` and is used to represent responses related to natural language generation tasks.

#### Attributes:
- `llm_config`: An optional `LLMConfig` instance containing configuration for the language model.
- `sql_generation_id`: A `str` representing the identifier of the associated SQL generation task.
- `text`: An optional `str` containing the generated natural language text.

### InstructionResponse
The `InstructionResponse` class extends `BaseResponse` and is used to represent responses related to instructions.

#### Attributes:
- `instruction`: A `str` containing the instruction text.
- `db_connection_id`: A `str` representing the identifier of the database connection associated with the instruction.

### DatabaseConnectionResponse
The `DatabaseConnectionResponse` class extends `BaseResponse` and `DatabaseConnection` and is used to represent responses related to database connections.

### TableDescriptionResponse
The `TableDescriptionResponse` class extends `BaseResponse` and `TableDescription` and is used to represent responses related to table descriptions.

#### Attributes:
- `id`: An optional `str` representing a unique identifier for the table description.

### GoldenSQLResponse
The `GoldenSQLResponse` class extends `BaseResponse` and `GoldenSQL` and is used to represent responses related to golden SQL queries.

## Usage
These response classes are typically instantiated with data retrieved from the database or generated by the application's logic. They are then serialized to JSON format and sent as HTTP responses to API clients. The validators ensure that timestamps are consistently formatted, and the inheritance from `BaseModel` ensures that all other data types are correctly validated and serialized.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/api/types/requests.md

# `requests.py` Module Documentation

## Overview

The `requests.py` module, located in the `/workspaces/documentation-generator/target_code/dataherald/api/types/` directory, defines a set of classes that represent different types of requests that can be made to the DataHerald API. These classes are built using Pydantic, which is a data validation and settings management library using Python type annotations.

The module imports the `BaseModel` class from Pydantic, which is used as the base class for all request models, providing automatic validation and serialization/deserialization. It also imports `LLMConfig` from the `dataherald.types` module, which is a configuration class for language model settings.

## Classes

### `PromptRequest`

- **Description**: Represents a request for generating a prompt.
- **Attributes**:
  - `text`: A `str` representing the text of the prompt.
  - `db_connection_id`: A `str` representing the identifier for the database connection.
  - `metadata`: An optional `dict` that can store additional metadata related to the prompt.

### `SQLGenerationRequest`

- **Description**: Represents a request for generating SQL queries.
- **Attributes**:
  - `finetuning_id`: An optional `str` representing the identifier for the finetuning process.
  - `low_latency_mode`: A `bool` indicating whether low latency mode is enabled, defaulting to `False`.
  - `llm_config`: An optional `LLMConfig` instance containing configuration for the language model.
  - `evaluate`: A `bool` indicating whether the SQL should be evaluated, defaulting to `False`.
  - `sql`: An optional `str` representing the SQL query to be generated or processed.
  - `metadata`: An optional `dict` that can store additional metadata related to the SQL generation.

### `StreamSQLGenerationRequest`

- **Description**: Represents a request for generating SQL queries in a streaming context.
- **Attributes**:
  - Inherits all attributes from `SQLGenerationRequest` except for `sql` and `evaluate`, which are not included.

### `PromptSQLGenerationRequest`

- **Description**: Represents a combined request for generating a prompt followed by SQL generation.
- **Attributes**:
  - Inherits all attributes from `SQLGenerationRequest`.
  - `prompt`: A `PromptRequest` instance representing the initial prompt part of the request.

### `StreamPromptSQLGenerationRequest`

- **Description**: Represents a combined request for generating a prompt followed by SQL generation in a streaming context.
- **Attributes**:
  - Inherits all attributes from `StreamSQLGenerationRequest`.
  - `prompt`: A `PromptRequest` instance representing the initial prompt part of the request.

### `NLGenerationRequest`

- **Description**: Represents a request for generating natural language text.
- **Attributes**:
  - `llm_config`: An optional `LLMConfig` instance containing configuration for the language model.
  - `max_rows`: An `int` representing the maximum number of rows to generate, defaulting to `100`.
  - `metadata`: An optional `dict` that can store additional metadata related to the natural language generation.

### `NLGenerationsSQLGenerationRequest`

- **Description**: Represents a request for generating natural language text based on SQL generation.
- **Attributes**:
  - Inherits all attributes from `NLGenerationRequest`.
  - `sql_generation`: A `SQLGenerationRequest` instance representing the SQL generation part of the request.

### `PromptSQLGenerationNLGenerationRequest`

- **Description**: Represents a request for generating natural language text based on a prompt followed by SQL generation.
- **Attributes**:
  - Inherits all attributes from `NLGenerationRequest`.
  - `sql_generation`: A `PromptSQLGenerationRequest` instance representing the combined prompt and SQL generation part of the request.

### `UpdateMetadataRequest`

- **Description**: Represents a request to update metadata.
- **Attributes**:
  - `metadata`: An optional `dict` that can store the metadata to be updated.

## Usage

Each class in this module is used to create instances that represent specific API requests with their respective parameters and settings. These instances can be serialized to JSON for HTTP requests or deserialized from incoming JSON payloads. The use of Pydantic models ensures that the data conforms to the expected structure and types, and provides clear error messages when validation fails.

The classes that inherit from other request classes are used to create more complex requests that combine the functionality of their parent classes. This allows for a modular approach to request handling, where different aspects of a request can be encapsulated in separate classes and then combined as needed.

The optional fields in the request classes allow for flexibility in specifying only the necessary parameters for a given request, while providing sensible defaults for others. The use of type annotations and Pydantic's validation features ensures that the API receives well-formed requests and that the developers have a clear contract for the data expected by each endpoint.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/api/types/query.md

# Query Class

## Overview

The `Query` class is a Python class that inherits from `BaseModel`, which is provided by the `pydantic` library. This class is designed to represent a query with specific attributes that can be used within the `dataherald` API. The `pydantic` library is used for data validation and settings management using Python type annotations.

## Attributes

The `Query` class defines the following attributes:

- `max_rows`: An integer that specifies the maximum number of rows to be returned by the query. It has a default value of 100, which means if the `max_rows` is not explicitly provided, the query will return up to 100 rows.
- `metadata`: A dictionary that can hold additional metadata related to the query. This attribute is optional and can be `None`. The `|` symbol is a type union operator introduced in Python 3.10, which indicates that `metadata` can be either a `dict` or `None`.

## Usage

The `Query` class is typically used to create query objects that can be passed around within the `dataherald` project. These objects encapsulate the query parameters and ensure that they adhere to the defined schema and validation rules set by `pydantic`.

### Instantiation

To create an instance of the `Query` class, you can simply instantiate it with the desired attributes:

python
query_instance = Query(max_rows=50, metadata={'user': 'admin', 'priority': 'high'})


If you do not provide the `max_rows` argument, it will default to 100:

python
query_instance = Query(metadata={'user': 'admin', 'priority': 'high'})


### Validation

When an instance of the `Query` class is created, `pydantic` performs validation on the provided data:

- It checks that `max_rows` is an integer.
- It ensures that `metadata`, if provided, is a dictionary.

If the validation fails, `pydantic` raises a `ValidationError` with details about what went wrong.

### Accessing Attributes

Once a `Query` object is instantiated, you can access its attributes using the dot notation:

python
print(query_instance.max_rows)  # Outputs the value of max_rows
print(query_instance.metadata)  # Outputs the metadata dictionary or None if not provided


### Serialization

`Query` objects can be serialized to JSON or other formats supported by `pydantic`. This is useful when you need to send the query data over HTTP or store it in a file:

python
json_representation = query_instance.json()


### Integration with API Endpoints

In the context of the `dataherald` API, `Query` objects can be used as request models for API endpoints that require query parameters. For example, an endpoint that retrieves data based on a query could accept a `Query` object as input, ensuring that all incoming query data is valid and conforms to the expected structure.

## File Location

The `Query` class is defined in the file located at `/workspaces/documentation-generator/target_code/dataherald/api/types/query.py` within the project's directory structure. This location suggests that the class is part of the API's type definitions, specifically related to querying functionality in the `dataherald` project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/api/types/__init__.md

# `__init__.py` in `dataherald/api/types`

## Overview

The `__init__.py` file within the `dataherald/api/types` directory serves as an initializer for the `types` module within the `dataherald` application's API. This file can be used to expose specific classes, functions, or variables defined in the module to make them easily accessible when the module is imported elsewhere in the project.

## Usage

When the `types` module is imported, Python will execute the `__init__.py` file. The contents of this file determine which objects from the module are available to the importer. This can include type definitions, constants, and utility functions relevant to the API.

## Structure

The structure of the `__init__.py` file can vary depending on the needs of the project. Below is a hypothetical structure of what the file might contain:

python
# __init__.py in dataherald/api/types

# Import specific types from submodule files for easier access
from .user_type import UserType
from .data_type import DataType

# Define constants that are used throughout the API
API_VERSION = '1.0'
DEFAULT_ENCODING = 'utf-8'

# Import utility functions that are relevant to type handling
from .type_utils import validate_type, convert_type

# Optionally, initialize any required state for the types module
initialize_types_database()

# Expose objects to be available when importing the module
__all__ = ['UserType', 'DataType', 'API_VERSION', 'DEFAULT_ENCODING', 'validate_type', 'convert_type']


## Details

### Importing Submodule Types

The `__init__.py` file often imports classes or functions from other files within the same module. For example, `UserType` and `DataType` might be classes defined in `user_type.py` and `data_type.py` respectively. By importing them in `__init__.py`, they can be accessed directly from `dataherald.api.types` without needing to reference the submodules.

### Constants

Constants such as `API_VERSION` and `DEFAULT_ENCODING` are defined at the module level for easy access and to avoid magic numbers or strings throughout the codebase. These constants can be used by other parts of the application to maintain consistency.

### Utility Functions

Utility functions like `validate_type` and `convert_type` are helper functions that may be used across multiple types within the API. By importing them here, they are made available as part of the `types` module's public interface.

### Initialization

The `initialize_types_database()` function is a hypothetical function that might be used to set up any necessary state or database connections required by the types module. This is an optional step and depends on the module's responsibilities.

### `__all__` Variable

The `__all__` variable is a list of strings defining what symbols the module will export when `from module import *` is used. It is a way to control which objects are considered part of the public API of the module.

## Conclusion

The `__init__.py` file in the `dataherald/api/types` directory is a crucial part of the module, as it defines the public interface and initializes any necessary components for the types used within the `dataherald` API. It simplifies the import statements required in other parts of the project and can help organize and encapsulate the module's functionality.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db/__init__.md

# DB Class

The `DB` class is an abstract base class (ABC) that defines a common interface for database operations within the `dataherald` project. It inherits from the `Component` class and the `ABC` class from the `abc` module. The `DB` class is designed to be subclassed by concrete database implementations that provide specific functionality for different types of databases.

## Attributes

- `system` (System): An instance of the `System` class from the `dataherald.config` module. This attribute is intended to hold system-wide configurations and dependencies.

## Methods

### `__init__(self, system: System)`

The constructor method for the `DB` class. It initializes a new instance of a database component with the provided system configuration.

#### Parameters

- `system` (System): The system configuration object.

### `insert_one(self, collection: str, obj: dict) -> int`

An abstract method that must be implemented by subclasses to insert a single document into a specified collection.

#### Parameters

- `collection` (str): The name of the collection where the document will be inserted.
- `obj` (dict): The document to be inserted as a dictionary.

#### Returns

- `int`: The number of documents inserted.

### `rename(self, old_collection_name: str, new_collection_name: str) -> None`

An abstract method that must be implemented by subclasses to rename an existing collection.

#### Parameters

- `old_collection_name` (str): The current name of the collection.
- `new_collection_name` (str): The new name for the collection.

### `rename_field(self, collection_name: str, old_field_name: str, new_field_name: str) -> None`

An abstract method that must be implemented by subclasses to rename a field within a collection.

#### Parameters

- `collection_name` (str): The name of the collection containing the field to be renamed.
- `old_field_name` (str): The current name of the field.
- `new_field_name` (str): The new name for the field.

### `update_or_create(self, collection: str, query: dict, obj: dict) -> int`

An abstract method that must be implemented by subclasses to update an existing document or create a new one if it does not exist.

#### Parameters

- `collection` (str): The name of the collection to update or insert the document into.
- `query` (dict): The query criteria to locate the document to be updated.
- `obj` (dict): The document to be updated or inserted.

#### Returns

- `int`: The number of documents updated or inserted.

### `find_one(self, collection: str, query: dict) -> dict`

An abstract method that must be implemented by subclasses to find a single document in a collection that matches the query.

#### Parameters

- `collection` (str): The name of the collection to search.
- `query` (dict): The query criteria to locate the document.

#### Returns

- `dict`: The found document or `None` if no document matches the query.

### `find_by_id(self, collection: str, id: str) -> dict`

An abstract method that must be implemented by subclasses to find a single document by its identifier.

#### Parameters

- `collection` (str): The name of the collection to search.
- `id` (str): The identifier of the document to find.

#### Returns

- `dict`: The found document or `None` if no document matches the identifier.

### `find(self, collection: str, query: dict, sort: list = None, page: int = 0, limit: int = 0) -> list`

An abstract method that must be implemented by subclasses to find documents in a collection that match the query, with optional sorting and pagination.

#### Parameters

- `collection` (str): The name of the collection to search.
- `query` (dict): The query criteria to locate the documents.
- `sort` (list, optional): A list of tuples specifying the field(s) and direction to sort the results.
- `page` (int, optional): The page number for pagination (starting from 0).
- `limit` (int, optional): The maximum number of documents to return.

#### Returns

- `list`: A list of found documents.

### `find_all(self, collection: str, page: int = 0, limit: int = 0) -> list`

An abstract method that must be implemented by subclasses to find all documents in a collection, with optional pagination.

#### Parameters

- `collection` (str): The name of the collection to search.
- `page` (int, optional): The page number for pagination (starting from 0).
- `limit` (int, optional): The maximum number of documents to return.

#### Returns

- `list`: A list of all found documents.

### `delete_by_id(self, collection: str, id: str) -> int`

An abstract method that must be implemented by subclasses to delete a single document by its identifier.

#### Parameters

- `collection` (str): The name of the collection from which the document will be deleted.
- `id` (str): The identifier of the document to delete.

#### Returns

- `int`: The number of documents deleted.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/db/mongo.md

# MongoDB Class

## Overview
The `MongoDB` class is a subclass of the `DB` class and provides an interface for interacting with a MongoDB database. It encapsulates the logic for connecting to the database and performing CRUD operations on collections within the database.

## Attributes
- `client`: An instance of `MongoClient` that represents the connection to the MongoDB server.

## Constructor
- `__init__(self, system: System)`: Initializes a new instance of the `MongoDB` class.
  - `system`: An instance of the `System` class from the `dataherald.config` module, which contains the application's configuration settings.
  - The constructor retrieves the MongoDB URI (`db_uri`) and database name (`db_name`) from the system settings and establishes a connection to the specified database, which is timezone-aware.

## Methods

### find_one
- `find_one(self, collection: str, query: dict) -> dict`: Retrieves a single document from the specified collection that matches the given query.
  - `collection`: The name of the collection to query.
  - `query`: A dictionary representing the query to be executed.
  - Returns a dictionary representing the found document or `None` if no document matches the query.

### insert_one
- `insert_one(self, collection: str, obj: dict) -> int`: Inserts a new document into the specified collection.
  - `collection`: The name of the collection where the document will be inserted.
  - `obj`: A dictionary representing the document to be inserted.
  - Returns the `ObjectId` of the inserted document.

### rename
- `rename(self, old_collection_name: str, new_collection_name) -> None`: Renames an existing collection.
  - `old_collection_name`: The current name of the collection.
  - `new_collection_name`: The new name for the collection.
  - This method does not return any value.

### rename_field
- `rename_field(self, collection_name: str, old_field_name: str, new_field_name: str) -> None`: Renames a field within all documents in the specified collection.
  - `collection_name`: The name of the collection containing the documents.
  - `old_field_name`: The current name of the field to be renamed.
  - `new_field_name`: The new name for the field.
  - This method does not return any value.

### update_or_create
- `update_or_create(self, collection: str, query: dict, obj: dict) -> int`: Updates an existing document or creates a new one if it does not exist.
  - `collection`: The name of the collection to be updated.
  - `query`: A dictionary representing the query to find the document.
  - `obj`: A dictionary representing the updated fields or the new document to be inserted.
  - If the document exists, it is updated with the provided fields (excluding `created_at` if present), and the method returns the `ObjectId` of the updated document.
  - If the document does not exist, a new document is inserted, and the method returns the `ObjectId` of the new document.

### find_by_id
- `find_by_id(self, collection: str, id: str) -> dict`: Retrieves a document by its `ObjectId`.
  - `collection`: The name of the collection to query.
  - `id`: The string representation of the document's `ObjectId`.
  - Returns a dictionary representing the found document or `None` if no document matches the `ObjectId`.

### find
- `find(self, collection: str, query: dict, sort: list = None, page: int = 0, limit: int = 0) -> list`: Retrieves a list of documents that match the given query, with optional sorting and pagination.
  - `collection`: The name of the collection to query.
  - `query`: A dictionary representing the query to be executed.
  - `sort`: An optional list of sorting tuples (field, direction).
  - `page`: The page number for pagination (1-indexed).
  - `limit`: The number of documents per page.
  - Returns a list of dictionaries representing the found documents.

### find_all
- `find_all(self, collection: str, page: int = 0, limit: int = 0) -> list`: Retrieves all documents from the specified collection, with optional pagination.
  - `collection`: The name of the collection to query.
  - `page`: The page number for pagination (1-indexed).
  - `limit`: The number of documents per page.
  - Returns a list of dictionaries representing the found documents.

### delete_by_id
- `delete_by_id(self, collection: str, id: str) -> int`: Deletes a document from the specified collection by its `ObjectId`.
  - `collection`: The name of the collection from which the document will be deleted.
  - `id`: The string representation of the document's `ObjectId`.
  - Returns the count of deleted documents (0 or 1).

## Usage
The `MongoDB` class is used within the project to interact with MongoDB collections. It provides a consistent interface for database operations, abstracting the details of the MongoDB API. This class is typically instantiated with the system configuration and then used to perform database operations throughout the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/model/chat_model.md

# ChatModel Class

## Overview

The `ChatModel` class is a subclass of `LLMModel` and is responsible for creating instances of chat models from various providers such as OpenAI, Anthropic, Google, and Cohere. It is designed to be used within a project that requires interaction with language models for chat or conversational purposes.

## Attributes

The `ChatModel` class does not define any additional attributes beyond those inherited from its superclass `LLMModel`.

## Methods

### `__init__(self, system)`

The constructor method initializes a new instance of the `ChatModel` class.

#### Parameters

- `system`: The system configuration or context in which the model will be used.

#### Behavior

- Calls the constructor of the superclass `LLMModel` with the provided `system` argument.

### `get_model(self, database_connection, model_family="openai", model_name="gpt-4-turbo-preview", api_base=None, **kwargs) -> Any`

The `get_model` method is responsible for creating and returning an instance of a chat model based on the specified `model_family`.

#### Parameters

- `database_connection` (`DatabaseConnection`): An object representing the database connection, which is used to decrypt the API key required to authenticate with the model provider's API.
- `model_family` (`str`, optional): A string indicating the family of the chat model to be used. Defaults to `"openai"`.
- `model_name` (`str`, optional): The name of the specific model to be instantiated. Defaults to `"gpt-4-turbo-preview"`.
- `api_base` (`str | None`, optional): The base URL for the API of the model provider. Defaults to `None`.
- `**kwargs` (`Any`): Additional keyword arguments that may be required for initializing the chat model.

#### Behavior

- Decrypts the API key using the `decrypt_api_key` method of the `database_connection` object.
- Depending on the value of `model_family`, it creates an instance of the corresponding chat model class:
  - `ChatOpenAI`: If `model_family` is `"openai"`.
  - `ChatAnthropic`: If `model_family` is `"anthropic"`.
  - `ChatGooglePalm`: If `model_family` is `"google"`.
  - `ChatCohere`: If `model_family` is `"cohere"`.
- Each chat model class is initialized with the `model_name`, the decrypted API key, and any additional keyword arguments provided in `**kwargs`.
- If the `api_base` is provided, it is passed to the `ChatOpenAI` class constructor.
- If the `model_family` does not match any of the expected values, a `ValueError` is raised with the message "No valid API key environment variable found".

#### Returns

- An instance of the chat model corresponding to the specified `model_family`.

## Usage

The `ChatModel` class is used in a project where a chat or conversational model is needed. It abstracts the details of creating instances of different chat models and handles the decryption of API keys securely. The class is designed to be flexible, allowing the user to specify the model family, model name, and any additional parameters required for the chat model initialization.

## Example

python
# Assuming `database_connection` is an instance of `DatabaseConnection`
chat_model_instance = ChatModel(system)
chat_model = chat_model_instance.get_model(
    database_connection=database_connection,
    model_family="openai",
    model_name="gpt-3.5-turbo",
    temperature=0.7
)


In the above example, a `ChatModel` instance is created, and the `get_model` method is called to create an instance of `ChatOpenAI` with the model name `"gpt-3.5-turbo"` and a temperature setting of `0.7`.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/model/base_model.md

# BaseModel Class

## Overview

The `BaseModel` class is a subclass of `LLMModel` and is responsible for initializing and retrieving instances of language models from various providers such as OpenAI, Aleph Alpha, Anthropic, and Cohere. It is designed to work within a project that interacts with language models and requires secure storage and retrieval of API keys for these services.

## Attributes

- `openai_api_key`: Stores the API key for OpenAI services, retrieved from the environment variable `OPENAI_API_KEY`.
- `aleph_alpha_api_key`: Stores the API key for Aleph Alpha services, retrieved from the environment variable `ALEPH_ALPHA_API_KEY`.
- `anthropic_api_key`: Stores the API key for Anthropic services, retrieved from the environment variable `ANTHROPIC_API_KEY`.
- `cohere_api_key`: Stores the API key for Cohere services, retrieved from the environment variable `COHERE_API_KEY`.

## Methods

### `__init__(self, system)`

The constructor method initializes the `BaseModel` instance by calling the superclass constructor with the `system` parameter and setting up the API keys for the various language model providers by reading from the respective environment variables.

#### Parameters

- `system`: The system configuration or context required by the superclass `LLMModel`.

### `get_model(self, database_connection, model_family="openai", model_name="davinci-003", api_base=None, **kwargs) -> Any`

The `get_model` method is responsible for retrieving an instance of a language model based on the provided parameters. It optionally decrypts an API key stored in a `DatabaseConnection` object and initializes the appropriate language model client.

#### Parameters

- `database_connection` (`DatabaseConnection`): An object containing database connection information, including an optionally encrypted API key for a language model service.
- `model_family` (`str`, optional): The family of the language model to be used. Defaults to `"openai"`.
- `model_name` (`str`, optional): The name of the specific language model to be initialized. Defaults to `"davinci-003"`.
- `api_base` (`str | None`, optional): The base URL for the API, if different from the default. Defaults to `None`.
- `**kwargs` (`Any`): Additional keyword arguments that may be required for initializing the language model.

#### Returns

- Returns an instance of the language model client.

#### Raises

- `ValueError`: If no valid API key is found in either the `database_connection` object or the environment variables.

#### Behavior

1. If an API key is provided in the `database_connection` object, it is decrypted using `FernetEncrypt` and used to set the appropriate API key attribute based on the `model_family`.
2. Depending on the `model_family` specified and the availability of the corresponding API key, an instance of the language model client is created using the `model_name` and any additional keyword arguments.
3. If no API key is available for the specified `model_family`, a `ValueError` is raised.

#### Usage

The `get_model` method is typically used within the project to instantiate a language model client that can be used to perform various natural language processing tasks. The method abstracts away the details of API key management and client initialization, providing a simple interface for the rest of the project to access language model services.

## Dependencies

- `os`: Used to access environment variables.
- `typing`: Provides type annotations.
- `langchain.llms`: Contains classes for different language model providers.
- `overrides`: Used to indicate that the `get_model` method overrides a superclass method.
- `dataherald.model`: Contains the `LLMModel` superclass.
- `dataherald.sql_database.models.types`: Contains the `DatabaseConnection` type.
- `dataherald.utils.encrypt`: Contains the `FernetEncrypt` class for encryption and decryption.

## Notes

- The `api_base` parameter is marked with `# noqa: ARG002` to ignore a specific linting rule, indicating that the parameter is intentionally optional and may not be used.
- The `**kwargs` parameter allows for flexibility in passing additional arguments required by specific language model clients.
- The `get_model` method uses the `override` decorator to ensure that it correctly overrides a method in the superclass.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/model/__init__.md

# LLMModel Class

## Overview

The `LLMModel` class is an abstract base class that defines the interface for language model components within the `dataherald` project. It inherits from the `Component` class, which is likely a part of the project's configuration management, and from the abstract base class `ABC` from Python's `abc` module, which is used to create abstract classes.

## Attributes

- `model`: This attribute is intended to store the actual language model instance. Its type is not specified and is represented by the `Any` type hint, indicating that it can be any type of object.

## Methods

### `__init__(self, system: System)`

The constructor method is abstract and must be implemented by subclasses. It initializes the `LLMModel` instance with a `system` object, which is an instance of the `System` class from the `dataherald.config` module. The `system` object likely contains configuration or state information relevant to the system in which the model operates.

#### Parameters

- `system`: An instance of the `System` class, representing the system configuration or state.

### `get_model(self, database_connection: DatabaseConnection, model_family="openai", model_name="gpt-4-turbo-preview", api_base: str | None = None, **kwargs: Any) -> Any`

This abstract method is intended to be implemented by subclasses to provide a mechanism for retrieving or initializing the language model. The method signature suggests that the model may be fetched or created based on parameters such as a database connection, model family, model name, and an optional API base URL.

#### Parameters

- `database_connection`: An instance of `DatabaseConnection` from the `dataherald.sql_database.models.types` module, which likely encapsulates the details required to connect to a database where model-related data might be stored or retrieved.
- `model_family`: A string defaulting to `"openai"`, which specifies the family or type of language model to be used.
- `model_name`: A string defaulting to `"gpt-4-turbo-preview"`, which specifies the particular model within the model family.
- `api_base`: An optional string or `None` that specifies the base URL of the API that might be used to interact with the language model. This parameter is optional and defaults to `None`.
- `**kwargs`: A variable number of keyword arguments that allow for additional parameters to be passed to the method, providing flexibility for subclasses to require more specific configuration options.

#### Returns

- The method returns an instance of the language model, the type of which is unspecified and represented by the `Any` type hint.

## Usage

As an abstract class, `LLMModel` cannot be instantiated directly. Instead, it serves as a template for subclasses that must implement the abstract methods defined in `LLMModel`. These subclasses will provide concrete implementations for initializing the model and retrieving it, potentially involving interactions with a database and/or an external API.

Subclasses of `LLMModel` are likely to be components within the `dataherald` project that are responsible for managing different types of language models, such as those provided by OpenAI or other providers. The `LLMModel` interface ensures that all such components adhere to a consistent API, making it easier to integrate and swap different language model implementations within the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/migrate_v002_to_v003.md

# Migration Script: migrate_v002_to_v003.py

## Overview
The `migrate_v002_to_v003.py` script is a migration utility designed to update the schema or data format in a database from version 002 to version 003 within the DataHerald project. This script is specifically focused on updating the `status` field of all documents in the `table_descriptions` collection to the value "SYNCHRONIZED".

## Dependencies
- `dataherald.config`: A module that provides access to the configuration settings of the DataHerald project.
- `dataherald.config.System`: A class that represents the system configuration and is responsible for initializing and managing system components.
- `dataherald.db.DB`: A class that provides an interface for interacting with the database.

## Execution Flow

### Entry Point
The script is executed as a standalone Python program. The entry point is the standard `if __name__ == "__main__":` block, which ensures that the code is only executed when the script is run directly, not when imported as a module.

### Configuration and System Initialization
1. An instance of `Settings` is created from the `dataherald.config` module, which loads the necessary configuration for the migration.
2. A `System` object is instantiated with the loaded settings.
3. The `start` method of the `System` object is called to initialize the system components required for the migration.

### Database Connection
1. An instance of the `DB` class is retrieved from the `System` object, which provides the interface to interact with the database.

### Data Migration
1. The script retrieves all documents from the `table_descriptions` collection using the `find_all` method of the `storage` object (an instance of `DB`).
2. It iterates over each document (referred to as `collection_row`) in the `table_descriptions` collection.
3. For each document, the `status` field is set to the string "SYNCHRONIZED".
4. The updated document is then saved back to the database using the `update_or_create` method of the `storage` object. This method takes three arguments:
   - The name of the collection (`"table_descriptions"`).
   - A filter dictionary to identify the document to update (using the `_id` field from the current `collection_row`).
   - The updated document (`collection_row` with the modified `status` field).

## Usage
This script is intended to be run as part of a migration process when upgrading the DataHerald project from version 002 to version 003. It should be executed by a system administrator or a deployment process with the necessary permissions to modify the database.

## Notes
- The script assumes that the `table_descriptions` collection and its schema are already present in the database.
- The script does not provide rollback functionality in case of failure. It is recommended to have a database backup before running the migration.
- The script does not include error handling, so any issues during the database update process will need to be addressed manually.
- The script is specific to the DataHerald project and may not be applicable to other projects without modification.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/migrate_v004_to_v005.md

# Migration Script: migrate_v004_to_v005.py

## Overview
The `migrate_v004_to_v005.py` script is a migration utility designed to update the structure of database connection records within a project that uses the `dataherald` framework. This script is specifically tailored to transition from version 0.0.4 to version 0.0.5 of the data model.

## Dependencies
- `dataherald.config`: Module that provides access to the configuration settings of the `dataherald` framework.
- `dataherald.db`: Module that provides database interaction capabilities.

## Execution Context
This script is intended to be executed as a standalone Python script. It is designed to be run manually by a system administrator or automatically by a migration system when upgrading the `dataherald` framework from an older version to a newer one.

## Process Flow

### Configuration and System Initialization
1. The script starts by importing necessary modules and classes from the `dataherald` framework.
2. It then initializes the `Settings` object from the `dataherald.config` module, which loads the configuration settings for the current environment.
3. A `System` object is instantiated with the loaded settings, which acts as a central point for managing different components of the `dataherald` framework.
4. The `System` object is started, which likely involves initializing connections and preparing the environment for operation.

### Database Connection and Migration
5. The script retrieves an instance of the `DB` class from the `System` object. This `DB` instance is responsible for database operations.
6. It then iterates over all records in the "database_connections" collection (or equivalent storage) using the `find_all` method of the `DB` instance.
7. For each database connection record found:
   - The script checks if the record contains the "llm_credentials" key and if it is not empty.
   - If the condition is met, it extracts the "api_key" from the "llm_credentials" sub-document and assigns it to a new key in the record called "llm_api_key".
   - The "llm_credentials" key is then set to `None`, effectively removing the credentials from the original location in the record.
   - The updated record is then saved back to the "database_connections" collection using the `update_or_create` method of the `DB` instance. This method ensures that the record is updated if it exists or created if it does not.

### Usage
- The script is executed from the command line by navigating to the directory containing the script and running `python migrate_v004_to_v005.py`.
- It does not take any command-line arguments and operates on the database connections as per the logic defined in the script.

## Post-Migration
After the script has been executed, all database connection records in the "database_connections" collection should have their "llm_credentials" migrated to a new "llm_api_key" field, with the original "llm_credentials" field being cleared. This change reflects a structural update in the data model between versions 0.0.4 and 0.0.5 of the `dataherald` framework.

## Error Handling
The script does not explicitly include error handling. It is assumed that the `dataherald` framework's underlying methods (`start`, `instance`, `find_all`, `update_or_create`) include their own error handling mechanisms. In a production environment, additional error handling and logging should be implemented to ensure smooth migration and to capture any issues that may arise during the process.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/migrate_v006_to_v100.md

# Migration Script: migrate_v006_to_v100.py

## Overview
The `migrate_v006_to_v100.py` script is designed to perform data migration from version 0.0.6 to version 1.0.0 of the DataHerald application. It updates the database schema, migrates data to new collections, and ensures compatibility with the new version.

## Dependencies
- `os`: Provides a way to use operating system dependent functionality.
- `datetime.timedelta`: Used for date and time manipulation.
- `bson.objectid.ObjectId`: Represents BSON Object IDs.
- `pymongo`: Python driver for MongoDB.
- `pymongo.ASCENDING`: Sort order specifier for MongoDB queries.
- `pymongo.errors.DuplicateKeyError`: Exception for handling duplicate key errors in MongoDB operations.
- `dataherald.config`: Module containing application configuration settings.
- `dataherald.config.System`: Class representing the system configuration.
- `dataherald.db.DB`: Class for database operations.
- `dataherald.db_scanner.models.types.TableDescriptionStatus`: Enum for table description status.
- `dataherald.types.GoldenSQL`: Class representing a golden SQL record.
- `dataherald.vector_store.VectorStore`: Class for vector store operations.

## Functions

### update_object_id_fields
Converts `ObjectId` fields to string representation in the specified collection.

#### Parameters
- `field_name: str`: The name of the field to update.
- `collection_name: str`: The name of the collection where the field is located.

#### Process
1. Iterates over all documents in the specified collection.
2. Checks if the field exists, is not empty, and is an instance of `ObjectId`.
3. Converts the `ObjectId` to a string and updates the document in the collection.

## Main Execution

### Initialization
1. Loads settings from `dataherald.config.Settings`.
2. Initializes the `System` with the loaded settings and starts it.
3. Creates an instance of `DB` for database operations.
4. Retrieves the name of the golden SQL collection from the environment variable `GOLDEN_RECORD_COLLECTION` or defaults to "dataherald-staging".
5. Creates an instance of `VectorStore` for vector store operations.

### Golden SQL Records Migration
1. Finds all documents in the "golden_records" collection.
2. For each golden record, attempts to insert a new document into the "golden_sqls" collection with the necessary fields.
3. Ignores documents that cause a `DuplicateKeyError`.

### Data Type Conversion
1. Calls `update_object_id_fields` for various fields across multiple collections to convert `ObjectId` fields to strings.

### Vector Store Operations
1. Attempts to delete the existing vector store collection.
2. Finds all documents in the "golden_sqls" collection.
3. Converts each document to a `GoldenSQL` object and appends it to a list.
4. Adds the list of `GoldenSQL` objects to the vector store.

### Table Descriptions Status Update
1. Finds all documents in the "table_descriptions" collection.
2. Updates the status field based on the current status, changing "SYNCHRONIZED" to `TableDescriptionStatus.SCANNED` and "NOT_SYNCHRONIZED" to `TableDescriptionStatus.NOT_SCANNED`.
3. Updates or creates the document in the "table_descriptions" collection.

### Prompts and Responses Migration
1. Finds all documents in the "questions" collection.
2. For each question, finds associated responses and attempts to insert a new document into the "prompts" collection.
3. Ignores documents that cause a `DuplicateKeyError`.
4. For each response, attempts to create documents in the "sql_generations" and "nl_generations" collections with the necessary fields.
5. Ignores documents that cause a `DuplicateKeyError`.

## Notes
- The script uses exception handling to ignore `DuplicateKeyError` exceptions, allowing the migration to continue even if some records already exist in the target collections.
- The script prints status messages to the console to indicate the progress of the migration.
- The script uses environment variables to allow configuration of collection names.
- The script assumes that the MongoDB connection and authentication are handled by the `DB` class instance.
- The script does not provide rollback functionality in case of failure, so it is assumed that the migration is run in a controlled environment where backups are available if needed.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/delete_and_populate_golden_records.md

# delete_and_populate_golden_records.py

## Overview
The `delete_and_populate_golden_records.py` script is designed to manage the lifecycle of "golden records" within a data management system. It performs two primary functions: deleting an existing collection of golden records and repopulating it with fresh data. This script is part of the `dataherald` project and interacts with the project's configuration, database, and vector store components.

## Dependencies
- `os`: Standard Python module to interact with the operating system.
- `dataherald.config`: Module containing configuration settings for the `dataherald` project.
- `dataherald.db`: Module providing database access functionality.
- `dataherald.types`: Module defining custom data types used within the `dataherald` project.
- `dataherald.vector_store`: Module responsible for managing vector storage within the `dataherald` project.

## Execution Flow

### Configuration and System Initialization
1. The script initializes by loading settings from the `dataherald.config.Settings` class.
2. It then creates an instance of the `System` class, passing the settings object to it.
3. The `System` instance is started, which likely initializes various components of the `dataherald` system.

### Database Connection
4. The script obtains an instance of the `DB` class from the `System` instance, which provides database access methods.

### Environment Variable Handling
5. The script retrieves the environment variable `GOLDEN_SQL_COLLECTION` or defaults to `"dataherald-staging"` if the environment variable is not set. This variable determines the name of the collection where golden records are stored.

### Golden Records Retrieval
6. The script uses the `storage.find_all("golden_sqls")` method to retrieve all golden SQL records from the database.

### Vector Store Initialization
7. An instance of `VectorStore` is obtained from the `System` instance, which is responsible for managing collections of records.

### Collection Deletion
8. The script attempts to delete the existing collection of golden records from the vector store using `vector_store.delete_collection(golden_sql_collection)`.
9. If an exception occurs during deletion, it is silently ignored (as indicated by `# noqa: S110` which suppresses linting warnings for the broad exception clause).

### Golden Records Preparation
10. The script initializes an empty list `stored_golden_sqls` to hold the golden SQL objects.
11. It iterates over each dictionary of golden SQL data retrieved from the database.
12. For each dictionary, it creates an instance of `GoldenSQL`, passing the dictionary unpacked as keyword arguments and explicitly setting the `id` attribute to the string representation of the dictionary's `_id` field.
13. Each `GoldenSQL` instance is appended to the `stored_golden_sqls` list.

### Collection Population
14. The script calls `vector_store.add_records(stored_golden_sqls, golden_sql_collection)` to add the list of `GoldenSQL` instances to the vector store under the collection name specified by `golden_sql_collection`.

## Usage
This script is intended to be run as a standalone Python script, typically as part of a data pipeline or maintenance task. It is executed by running `python delete_and_populate_golden_records.py` from the command line within the appropriate environment where the `dataherald` project and its dependencies are installed.

## Notes
- The script assumes that the necessary environment variables and system configurations are correctly set for the `dataherald` project.
- The script does not provide detailed error handling or logging for the deletion process, which may be a consideration for production environments.
- The script's functionality is tightly coupled with the `dataherald` project's internal modules and data structures, such as `GoldenSQL` and `VectorStore`.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/migrate_v100_to_v101.md

# Migration Script: migrate_v100_to_v101.py

## Overview
The `migrate_v100_to_v101.py` script is designed to perform a data migration on a collection named `database_connections` within a database managed by the `dataherald` system. The script updates the schema of the `database_connections` collection from version 1.0.0 to 1.0.1 by renaming a field and re-encrypting connection URIs for entries that use SSH.

## Dependencies
- `dataherald.config`: Provides access to the configuration settings of the `dataherald` system.
- `dataherald.db`: Contains the `DB` class responsible for database operations.
- `dataherald.utils.encrypt`: Contains the `FernetEncrypt` class used for encryption and decryption of sensitive data.

## Execution Flow

### System Initialization
1. The script initializes by loading the settings from `dataherald.config.Settings`.
2. It then creates a `System` instance using the loaded settings.
3. The `System` instance is started, which likely initializes the necessary components for the migration.

### Database Connection
4. The script retrieves an instance of the `DB` class from the `System` instance, which is used to interact with the database.

### Field Renaming
5. The `rename_field` method of the `storage` object (an instance of `DB`) is called to rename the field `uri` to `connection_uri` in the `database_connections` collection.

### Data Encryption and Update
6. The script creates an instance of `FernetEncrypt` to handle encryption tasks.
7. It then queries the `database_connections` collection for documents where the `use_ssh` field is `True`.
8. For each database connection retrieved:
   - The script checks if the `db_driver` field is missing in the `ssh_settings` sub-document and if the `connection_uri` is not empty or `None`.
   - If the above condition is met, the script continues to the next iteration without making changes.
   - Otherwise, it constructs a new URI using the decrypted `remote_db_password` from the `ssh_settings` and other SSH-related fields.
   - The new URI is then encrypted using `FernetEncrypt` and assigned to the `connection_uri` field of the database connection document.
   - The `ssh_settings` sub-document is updated with only the necessary fields: `host`, `username`, `password`, and `private_key_password`.

### Database Update
9. The script updates the existing document in the `database_connections` collection with the new `connection_uri` and modified `ssh_settings` using the `update_or_create` method of the `storage` object. The document is identified by its `_id`.

## Usage
This script is intended to be run as a standalone Python script during the migration process from version 1.0.0 to 1.0.1 of the `dataherald` system. It should be executed by a system administrator or a migration tool that handles version upgrades. The script is executed without any command-line arguments and assumes that the `dataherald` system is properly configured and operational.

## Important Notes
- The script assumes that the `dataherald` system's configuration is set up correctly and that the database is accessible.
- The script does not handle exceptions explicitly, so any issues during the migration process (e.g., database connectivity problems, encryption errors) will result in an unhandled exception.
- The script should be used with caution, as it modifies the database schema and data. It is recommended to perform a backup of the `database_connections` collection before running the script.
- The script does not provide rollback functionality in case the migration needs to be reversed.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/migrate_v003_to_v004.md

# Migration Script: migrate_v003_to_v004.py

## Overview
The `migrate_v003_to_v004.py` script is designed to perform data migration operations on a MongoDB database to transition from version 003 to version 004 of the data schema. The script includes operations such as renaming collections, renaming fields within documents, adding new fields to documents, and changing the datatype of specific fields.

## Dependencies
- `datetime` module for timestamping new fields.
- `bson.objectid` module for converting string representations of MongoDB ObjectIds to actual ObjectId instances.
- `dataherald.config` for accessing the project's configuration settings.
- `dataherald.db` for database operations.

## Functions

### update_object_id_fields
This function is responsible for converting string representations of MongoDB ObjectIds to actual ObjectId instances within specified fields of documents in a given collection.

#### Parameters
- `field_name` (str): The name of the field within the documents that needs to be updated.
- `collection_name` (str): The name of the collection containing the documents to be updated.

#### Process
1. Iterates over all documents in the specified collection.
2. Checks if the specified field exists and is not an empty string.
3. Converts the field value to a MongoDB ObjectId instance.
4. Updates the document in the database with the new ObjectId.

## Main Execution

### Initialization
1. A `Settings` object is created from the `dataherald.config` module.
2. A `System` object is instantiated using the settings.
3. The system is started to initialize all components.
4. An instance of the `DB` class is retrieved from the system for database operations.

### Rename Collections
1. The script attempts to rename the "nl_questions" collection to "questions".
2. The script attempts to rename the "nl_query_responses" collection to "responses".
3. If any exception occurs during the renaming process, it is silently ignored.

### Rename Fields
1. The "nl_question_id" field in the "responses" collection is renamed to "question_id".
2. The "nl_response" field in the "responses" collection is renamed to "response".

### Add Field
1. Iterates over all documents in the "responses" collection.
2. Checks if the "created_at" field does not exist in the document.
3. If the field does not exist, it is added with the current datetime as its value.
4. The document is updated in the database with the new "created_at" field.

### Change Datatype
1. The `update_object_id_fields` function is called with the appropriate field and collection names to convert string representations of ObjectIds to ObjectId instances for the following collections and fields:
   - "db_connection_id" field in the "table_descriptions" collection.
   - "db_connection_id" field in the "golden_records" collection.
   - "db_connection_id" field in the "questions" collection.
   - "db_connection_id" field in the "instructions" collection.
   - "question_id" field in the "responses" collection.

## Usage
This script is intended to be run as a standalone Python script during the migration process. It should be executed when upgrading the data schema from version 003 to version 004. The script should be run with appropriate database access permissions and environment configurations set to ensure it can perform the necessary database operations.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/__init__.md

# `__init__.py` in `dataherald/scripts`

## Overview

The `__init__.py` file is a part of the `dataherald` Python project, specifically within the `scripts` subpackage. This file serves as an initializer for the `scripts` package, allowing the package's modules to be imported from other parts of the project. It can also be used to define package-level variables, functions, or classes, although in many cases it may be left empty.

## Usage

### Package Initialization

When Python encounters a directory with an `__init__.py` file, it treats that directory as a package. This means that the directory's name can be used in import statements to access modules and subpackages contained within it.

For example, if there is a module named `example.py` within the `dataherald/scripts` directory, it can be imported from elsewhere in the project using:

python
from dataherald.scripts import example


### Import Control

The `__init__.py` file can also control which modules and symbols are exposed to the outside when `import *` is used. This is done by defining a list named `__all__` within `__init__.py`. For instance:

python
__all__ = ['module1', 'module2']


This would mean that when a user writes `from dataherald.scripts import *`, only `module1` and `module2` will be imported.

### Package-Level Variables, Functions, and Classes

The `__init__.py` file can define variables, functions, and classes that are meant to be available at the package level. For example:

python
# Define a package-level variable
package_variable = 'This is a package-level variable'

# Define a package-level function
def package_function():
    print("This is a package-level function")

# Define a package-level class
class PackageClass:
    pass


These can then be imported directly from the package:

python
from dataherald.scripts import package_variable, package_function, PackageClass


### Relative Imports

Within the `dataherald/scripts` package, the `__init__.py` file can facilitate relative imports between modules in the same package. For example, if there are two modules, `module_a.py` and `module_b.py`, and `module_a` needs to import something from `module_b`, it can be done as follows:

python
from .module_b import some_function


The dot (`.`) indicates a relative import from the current package.

## Project Structure

The presence of `__init__.py` in the `dataherald/scripts` directory indicates that `scripts` is a package and potentially contains multiple modules or subpackages that contribute to the functionality of the `dataherald` project. The `dataherald` project likely follows a modular structure, with different components encapsulated within their respective subpackages.

## Conclusion

The `__init__.py` file in the `dataherald/scripts` directory is a key component for package initialization, import control, and defining package-level constructs. It is essential for the proper organization and modularization of the Python project, allowing for a clean and maintainable codebase.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/scripts/migrate_v001_to_v002.md

# Migration Script: migrate_v001_to_v002.py

## Overview
The `migrate_v001_to_v002.py` script is designed to perform data migration tasks within the DataHerald project. It updates the schema of certain collections, adds new fields to documents, and refreshes vector stores with updated information.

## Dependencies
- `os`: Standard Python module to interact with the operating system.
- `sql_metadata`: Third-party library used to parse SQL queries and extract metadata.
- `dataherald.config`: Module from the DataHerald project containing configuration settings.
- `dataherald.db`: Module from the DataHerald project for database interactions.
- `dataherald.vector_store`: Module from the DataHerald project for managing vector stores.

## Functions

### add_db_connection_id
This function adds a new field `db_connection_id` to documents in a specified collection.

#### Parameters
- `collection_name` (str): The name of the collection to update.
- `storage`: An instance of the `DB` class from `dataherald.db` module, used to interact with the database.

#### Process
1. Retrieves all documents from the specified collection.
2. Iterates over each document (referred to as `collection_row`).
3. Checks if the `db_alias` field exists in the document; if not, continues to the next document.
4. Finds the corresponding database connection document using the `db_alias` value.
5. If a database connection document is found, adds a new field `db_connection_id` to the `collection_row` with the value of the `_id` field from the database connection document.
6. Updates the document in the collection with the new `db_connection_id` field.

## Main Execution Flow

### Configuration and System Initialization
1. Instantiates a `Settings` object from `dataherald.config`.
2. Creates a `System` instance using the settings.
3. Calls the `start` method on the `System` instance to initialize the system.

### Database Instance
1. Retrieves an instance of the `DB` class from the `System` instance, which is used to interact with the database.

### Update Relations
1. Calls the `add_db_connection_id` function for the following collections:
   - `table_schema_detail`
   - `golden_records`
   - `nl_question`

### Refresh Vector Stores
1. Retrieves the name of the golden record collection from the environment variable `GOLDEN_SQL_COLLECTION`, defaulting to `"dataherald-staging"` if not set.
2. Retrieves an instance of the `VectorStore` class from the `System` instance.
3. Attempts to delete the existing collection from the vector store. If an exception occurs, it is silently ignored.

### Upload Golden Records
1. Retrieves all documents from the `golden_records` collection.
2. Iterates over each golden record document.
3. Parses the SQL query from the golden record using `sql_metadata.Parser` to extract the tables involved.
4. If no tables are found, defaults to an empty string.
5. Retrieves the question associated with the golden record.
6. Adds a new record to the vector store with the following information:
   - The question text as documents.
   - The `db_connection_id` from the golden record.
   - The name of the golden record collection.
   - Metadata containing the first table used in the SQL query and the `db_connection_id`.
   - The `_id` of the golden record as an identifier.

### Rename Collections
1. Attempts to rename the following collections:
   - `nl_query_response` to `nl_query_responses`
   - `nl_question` to `nl_questions`
   - `database_connection` to `database_connections`
   - `table_schema_detail` to `table_descriptions`
2. If an exception occurs during the renaming process, it is silently ignored.

## Usage
This script is executed as a standalone Python script, typically during a migration or upgrade process to transition from version 001 to version 002 of the DataHerald project. It is assumed to be run by a system administrator or automated deployment process with the necessary environment variables and permissions set up.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/conftest.md

# `conftest.py` Technical Documentation

## Overview

The `conftest.py` file is a configuration script utilized by the pytest framework to define fixtures, hooks, and plugins that are applicable to multiple test files. This particular `conftest.py` file is located within the `tests` directory of the `dataherald` module, indicating that it is used to configure the testing environment for this module.

## Fixture: `execute_before_any_test`

### Purpose

The fixture `execute_before_any_test` is designed to set up the database environment before any tests are executed within the session. It ensures that a specific table, `numbers`, is created in an SQLite database named `mydb2.db`. This table is intended to be used by the tests to interact with persistent data.

### Scope

The scope of this fixture is set to `"session"`, which means the fixture will be executed only once per test session. This is an efficient way to handle setup tasks that are common to all tests and do not need to be repeated before each individual test.

### Autouse

The `autouse=True` parameter indicates that this fixture is automatically used by tests. It does not need to be explicitly referenced in test functions; pytest will execute it before any test within the session without any further configuration.

### Implementation Details

1. **Database Engine Creation**:
   The fixture begins by creating a SQLAlchemy `engine` object. This engine is responsible for interfacing with the database and is created using the `create_engine` function from the `sqlalchemy` package. The database URL provided is `"sqlite:///mydb2.db"`, which specifies that a SQLite database named `mydb2.db` should be used. This database file is expected to be located in the same directory as the `conftest.py` file.

2. **Table Creation**:
   Using the `engine` object, the fixture attempts to execute a SQL statement to create a new table named `numbers`. The SQL statement is a `CREATE TABLE` command that defines the structure of the table with two columns:
   - `number`: A text column intended to store number-related data.
   - `existing`: A boolean column indicating some state or condition of the `number` entries.

3. **Exception Handling**:
   The table creation is wrapped in a `try` block to handle any exceptions that may occur during the execution of the SQL statement. If an exception is raised (for example, if the table already exists), the `except` block will catch the exception and pass it, allowing the test session to continue without interruption. This ensures that the presence of an existing `numbers` table does not cause the test setup to fail.

### Usage in Tests

Since the fixture is set to `autouse`, it does not require explicit invocation in test functions. When a test session starts, pytest will automatically execute this fixture, setting up the database environment before any tests are run. Test functions can then assume that the `numbers` table is available for database interactions.

### Dependencies

- `pytest`: The fixture uses the pytest framework for its definition and execution.
- `sqlalchemy`: The fixture relies on SQLAlchemy for database engine creation and SQL execution.

## File Location

- Path: `/workspaces/documentation-generator/target_code/dataherald/tests/conftest.py`
  This path indicates that the `conftest.py` file is part of the `dataherald` project, specifically within the `tests` directory, which is used for storing test-related files.

## Conclusion

The `conftest.py` file in the `dataherald` project provides a session-scoped fixture that automatically sets up a database table before any tests are run, ensuring a consistent testing environment across the test suite.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/test_api.md

# Test API Module

## Overview

The `test_api.py` module is part of the test suite for the `dataherald` project. It is designed to test the API endpoints provided by the FastAPI application defined in `dataherald.app`. The tests are executed using the `TestClient` from FastAPI's `testclient` module, which allows for the simulation of sending HTTP requests to the API without running a server.

## Dependencies

- `fastapi.testclient.TestClient`: A class that allows for testing FastAPI applications with a mock client that can simulate HTTP requests.
- `dataherald.app.app`: The FastAPI application instance that defines the API endpoints to be tested.

## Constants

- `HTTP_200_CODE`: The HTTP status code for a successful request.
- `HTTP_201_CODE`: The HTTP status code for a request that resulted in the creation of a new resource.
- `HTTP_404_CODE`: The HTTP status code for a request to a resource that does not exist.

## TestClient Setup

A `TestClient` instance is created by passing the FastAPI application (`app`) to it. This client is used to make requests to the API endpoints and assert the responses in the test functions.

python
client = TestClient(app)


## Test Functions

### `test_heartbeat()`

This test function verifies that the `/api/v1/heartbeat` endpoint is functioning correctly. It sends a `GET` request to the endpoint and asserts that the response status code is `200`, indicating success.

python
def test_heartbeat():
    response = client.get("/api/v1/heartbeat")
    assert response.status_code == HTTP_200_CODE


### `test_scan_all_tables()`

This test function checks the functionality of the `/api/v1/table-descriptions/sync-schemas` endpoint for synchronizing all table schemas. It sends a `POST` request with a JSON payload containing a `db_connection_id`. The test asserts that the response status code is `201`, indicating that the resource was created successfully.

python
def test_scan_all_tables():
    response = client.post(
        "/api/v1/table-descriptions/sync-schemas",
        json={"db_connection_id": "64dfa0e103f5134086f7090c"},
    )
    assert response.status_code == HTTP_201_CODE


### `test_scan_one_table()`

This test function is designed to test the synchronization of a single table schema. It attempts to send a `POST` request to the `/api/v1/table-descriptions/sync-schemas` endpoint with a JSON payload that includes a `db_connection_id` and a list of `table_names`. The test is wrapped in a `try` block to catch a `ValueError` exception, which is expected to be raised if no table is found. The test asserts that the exception message matches "No table found".

python
def test_scan_one_table():
    try:
        client.post(
            "/api/v1/table-descriptions/sync-schemas",
            json={
                "db_connection_id": "64dfa0e103f5134086f7090c",
                "table_names": ["foo"],
            },
        )
    except ValueError as e:
        assert str(e) == "No table found"


## Usage

The test functions in this module are typically executed as part of an automated test suite. They can be run using a test runner that is compatible with the testing framework used in the `dataherald` project (e.g., `pytest`). The tests validate that the API endpoints behave as expected when accessed through the `TestClient`.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/__init__.md

# `__init__.py` in `dataherald/tests` Module

## Overview

The `__init__.py` file within the `dataherald/tests` directory serves as an initialization script for the `tests` package in the `dataherald` project. This file is part of the project's testing framework and is used to define the `tests` directory as a Python package, allowing the test modules contained within to be imported elsewhere in the project.

## Usage

The presence of the `__init__.py` file in the `tests` directory indicates to the Python interpreter that the directory should be treated as a package. This is a conventional approach in Python projects to organize tests, and it allows for the following:

- Grouping of test modules: Test cases are typically organized into different modules based on the functionality they are testing. The `__init__.py` file allows these modules to be grouped together under the `tests` package.
- Importing test modules: With the `tests` directory being recognized as a package, individual test modules or specific test cases can be imported into other parts of the project or for test discovery by test runners.
- Test discovery: Automated test runners like `unittest` or `pytest` can discover and run tests from the `tests` package. The presence of the `__init__.py` file allows these tools to recognize the directory as a package and search for test modules recursively.

## Technical Details

- File Path: `/workspaces/documentation-generator/target_code/dataherald/tests/__init__.py`
- Package Name: `tests`
- Parent Module: `dataherald`

### Contents

Typically, the `__init__.py` file can be empty or contain minimal code necessary for initializing the package. However, it can also include:

- Package-level variables or constants.
- Import statements to expose certain classes, functions, or modules at the package level.
- Initialization code that needs to run when the package is imported.

### Example Usage

Assuming there is a test module named `test_module.py` within the `tests` package, it can be imported as follows:

python
from dataherald.tests import test_module


Or, to import a specific test case or function:

python
from dataherald.tests.test_module import TestCaseName


### Interaction with Test Runners

When using a test runner like `pytest`, running the command `pytest` within the project directory will cause the test runner to look for any files matching the pattern `test_*.py` or `*_test.py` within the `tests` package and execute the test cases found.

### Best Practices

- Keep the `__init__.py` file as simple as possible, avoiding complex package initialization that could affect test performance or cause side effects.
- Use relative imports within the `tests` package to maintain modularity and ease of refactoring.

## Conclusion

The `__init__.py` file in the `dataherald/tests` directory is a key component for organizing and running tests within the `dataherald` project. It defines the directory as a Python package and facilitates test discovery and modular import of test cases.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/db_scanner/test_sqlalchemy.md

# `test_sqlalchemy.py` Module

## Overview

The `test_sqlalchemy.py` module is part of the test suite for the `dataherald` project, specifically focusing on testing the functionality related to SQLAlchemy database interactions. This module contains a collection of test cases that verify the correct behavior of the database scanning features provided by the `dataherald` application.

## Dependencies

- `pytest`: A framework used for writing and running tests.
- `sqlalchemy`: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- `dataherald`: The main project package that this test module is designed to test.

## Test Cases

### `test_connect_database()`

#### Description

This test case verifies that the application can successfully connect to a database using SQLAlchemy. It checks if the connection object is valid and if the connection can be established without any exceptions.

#### Steps

1. Set up a test database URI.
2. Attempt to connect to the database using the `dataherald` connection method.
3. Assert that the connection is successful and the connection object is not `None`.

### `test_scan_tables()`

#### Description

This test case ensures that the application can correctly scan and retrieve a list of tables from the connected database. It checks if all expected tables are present and if their names match the expected values.

#### Steps

1. Connect to the test database.
2. Invoke the table scanning method from the `dataherald` application.
3. Assert that the returned list of tables matches the expected list of table names.

### `test_scan_columns()`

#### Description

This test case checks whether the application can accurately scan and list the columns of a specific table in the database. It verifies the column names, types, and other properties.

#### Steps

1. Connect to the test database and select a target table.
2. Invoke the column scanning method for the target table.
3. Assert that the returned list of columns contains the correct column names and types as expected.

### `test_scan_primary_keys()`

#### Description

This test case is designed to verify that the application can identify and list the primary keys of a given table. It ensures that primary key constraints are correctly recognized.

#### Steps

1. Connect to the test database and select a target table with known primary keys.
2. Invoke the primary key scanning method for the target table.
3. Assert that the returned list of primary keys matches the expected primary key columns.

### `test_scan_foreign_keys()`

#### Description

This test case tests the application's ability to detect and list foreign key relationships between tables in the database. It checks for the correct identification of foreign key columns and their referenced tables and columns.

#### Steps

1. Connect to the test database and select a target table with known foreign key relationships.
2. Invoke the foreign key scanning method for the target table.
3. Assert that the returned foreign key mappings are correct, including the local and referenced column names.

### `test_scan_indexes()`

#### Description

This test case ensures that the application can correctly identify and list the indexes on a table, including unique and composite indexes.

#### Steps

1. Connect to the test database and select a target table with known indexes.
2. Invoke the index scanning method for the target table.
3. Assert that the returned list of indexes matches the expected index definitions, including the index names and associated columns.

## Usage

The `test_sqlalchemy.py` module is executed as part of the automated test suite for the `dataherald` project. It is typically run using a test runner such as `pytest` that collects and runs all the test cases defined within the module. The tests can be executed in isolation or as part of a larger test suite to ensure the stability and correctness of the database scanning functionality within the `dataherald` application.

To run the tests in this module, navigate to the project's root directory and execute the following command:

bash
pytest /workspaces/documentation-generator/target_code/dataherald/tests/db_scanner/test_sqlalchemy.py


This will trigger the test runner to execute each test case in `test_sqlalchemy.py`, reporting success or failure for each one and providing a summary of the test results upon completion.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/db_scanner/__init__.md

# `__init__.py` in `db_scanner` Test Module

## Overview

The `__init__.py` file within the `db_scanner` directory under the `tests` sub-module of the `dataherald` project serves as an initialization script for the `db_scanner` test module. This file is part of the project's testing framework and is used to define the `db_scanner` package, allowing for the organization and discovery of test cases related to database scanning functionality within the `dataherald` application.

## Purpose

The presence of an `__init__.py` file in a Python directory indicates to the Python interpreter that the directory should be treated as a package. In the context of testing, this allows test runners like `unittest`, `pytest`, or `nose` to recognize the directory as containing tests and to collect them accordingly.

## Usage

### Test Discovery

When a test runner is invoked, it recursively searches for test files within the specified directory. The presence of the `__init__.py` file ensures that the `db_scanner` directory is searchable and that any test modules within it are importable.

For example, running `pytest` from the command line in the project root directory would include the `db_scanner` tests in its discovery process:

bash
pytest /workspaces/documentation-generator/target_code/dataherald/tests/


### Test Organization

The `db_scanner` test module may contain multiple test files, each with a set of test cases. These files are typically named with a `test_` prefix, e.g., `test_database_connection.py`, `test_query_execution.py`, etc. The `__init__.py` file does not directly contain test cases but enables the grouping of these related test files under a common namespace.

### Importing Test Cases

Within the `db_scanner` test module, individual test cases or entire test classes can be imported from other test files. The `__init__.py` file allows for these imports to be done using relative paths, which simplifies the import statements and maintains a clean project structure.

For example, a test case from `test_database_connection.py` could be imported in another test file within the `db_scanner` module as follows:

python
from .test_database_connection import TestDatabaseConnection


## File Content

Typically, the `__init__.py` file in a test module may be empty or contain minimal code. However, it can also include common fixtures, setup code, or utility functions that are shared across multiple test files within the `db_scanner` module.

## Best Practices

- Keep the `__init__.py` file as simple as possible, avoiding complex logic or dependencies that could affect the test discovery process.
- Use the `__init__.py` file to share common test fixtures or helper functions if needed, but ensure they are clearly documented and maintained.
- Regularly check that the `__init__.py` file does not inadvertently exclude tests from being discovered due to misconfiguration or syntax errors.

## Conclusion

The `__init__.py` file in the `db_scanner` test module plays a crucial role in the organization and execution of tests within the `dataherald` project. It ensures that test cases are properly grouped, discoverable, and importable, contributing to the maintainability and scalability of the test suite.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/db_scanner/repository/__init__.md

# `__init__.py` in `dataherald/tests/db_scanner/repository`

## Overview

The `__init__.py` file within the `dataherald/tests/db_scanner/repository` directory serves as an initialization script for the `repository` package under the `db_scanner` testing module of the `dataherald` project. This file is responsible for setting up the package namespace and can also be used to perform any necessary setup for the package's test suite, such as importing test modules or initializing test fixtures.

## Usage

The presence of an `__init__.py` file in a directory indicates to Python that the directory should be treated as a package. This allows the test modules within the `repository` package to be imported elsewhere in the project. For example, one could import a test class from this package using the following syntax:

python
from dataherald.tests.db_scanner.repository import TestRepositoryClass


This file can also be used to aggregate test cases from different modules within the `repository` package, making it easier to run all related tests together.

## Structure

The `__init__.py` file can be structured in several ways, depending on the needs of the test suite. Below are some common patterns that might be found in this file:

### Importing Test Modules

The file may import test modules to expose them at the package level:

python
from .test_module1 import TestModule1
from .test_module2 import TestModule2


### Defining Test Suites

The file may define a test suite that aggregates tests from various modules:

python
import unittest

def repository_test_suite():
    suite = unittest.TestSuite()
    suite.addTest('test_module1.TestModule1')
    suite.addTest('test_module2.TestModule2')
    return suite


### Package Initialization

The file may include package-level initialization code that is required before running the tests:

python
# Package-level initialization code
def setup_package():
    # Code to set up the test environment for the repository package
    pass

setup_package()


### Conditional Imports

The file may conditionally import test modules based on certain criteria, such as environment variables or configuration settings:

python
import os

if os.getenv('RUN_INTEGRATION_TESTS'):
    from .integration import IntegrationTestModule


## Best Practices

- The `__init__.py` file should be kept minimal to avoid complex package initialization that could introduce side effects or make the test suite harder to understand.
- If the file contains initialization code, it should be idempotent to ensure that repeated imports do not cause unexpected behavior.
- Any shared fixtures or utilities that are used across multiple test modules within the `repository` package should be defined here to promote code reuse and maintainability.

## Conclusion

The `__init__.py` file in the `dataherald/tests/db_scanner/repository` directory is a key component for organizing and running the test suite for the `repository` package. It provides a mechanism for package initialization, test module imports, and test suite aggregation, ensuring that the tests for the `repository` package are easily accessible and maintainable.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/db_scanner/repository/test_base.md

# TestBase Module

## Overview

The `test_base.py` module is part of the `dataherald` project, specifically within the `tests/db_scanner/repository` directory. This module provides a base class for database repository tests, offering common setup and teardown procedures, as well as utility methods that can be used by test cases that inherit from it.

## Usage

The `TestBase` class is designed to be subclassed by other test modules that require a standardized testing environment for database interactions. It is not intended to be instantiated directly in test cases but serves as a foundation for other test classes.

## Class: TestBase

### Description

The `TestBase` class is an abstract base class that sets up a testing framework for database repository tests. It includes setup and teardown methods that handle the creation and cleanup of a temporary database environment, ensuring that each test runs in isolation.

### Methods

#### `setUpClass(cls)`

- **Description**: A class method that is called before any tests are run. It is responsible for setting up any class-level fixtures that are shared across all test cases. Typically, this might involve establishing a connection to a test database or creating shared resources.
- **Parameters**: `cls` - A reference to the class.
- **Returns**: None.

#### `tearDownClass(cls)`

- **Description**: A class method that is called after all tests in the class have been run. It is responsible for cleaning up any resources that were set up in the `setUpClass` method. This might involve closing database connections or deleting temporary data.
- **Parameters**: `cls` - A reference to the class.
- **Returns**: None.

#### `setUp(self)`

- **Description**: An instance method called before each test method is executed. It sets up the test environment for the specific test, such as initializing database transactions or resetting the state of the database to a known state.
- **Parameters**: None.
- **Returns**: None.

#### `tearDown(self)`

- **Description**: An instance method called after each test method has been executed. It is responsible for cleaning up after the test, such as rolling back database transactions or removing test data.
- **Parameters**: None.
- **Returns**: None.

### Attributes

The `TestBase` class may also define a set of attributes that are used to configure the test environment. These could include:

- `db_connection_string`: A string that specifies the connection details for the test database.
- `test_data`: A collection of data that is used to populate the database for testing purposes.

## Test Cases

Test cases that inherit from `TestBase` should implement their own test methods. These methods will typically follow this structure:

1. Call the `setUp` method to prepare the test environment.
2. Execute the code that is being tested, such as database queries or repository methods.
3. Assert the expected outcomes of the code execution.
4. Call the `tearDown` method to clean up the test environment.

## Example

Below is an example of how a test case might inherit from `TestBase`:

python
from dataherald.tests.db_scanner.repository.test_base import TestBase

class TestExampleRepository(TestBase):

    def test_some_database_functionality(self):
        # Arrange
        self.setUp()
        # Act
        result = self.some_repository_method()
        # Assert
        self.assertEqual(expected_result, result)
        # Cleanup
        self.tearDown()


In this example, `TestExampleRepository` inherits from `TestBase`, and the test method `test_some_database_functionality` uses the setup and teardown methods to ensure a consistent test environment.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/sql_generator/test_generator.md

# TestGenerator Class

## Overview

The `TestGenerator` class is a subclass of `SQLGenerator` and is designed for testing purposes within the `dataherald` project. It provides a mock implementation of the `generate_response` method, which is used to simulate the generation of SQL queries based on user prompts and database connections.

## Attributes

The `TestGenerator` class does not define any additional attributes beyond those inherited from its parent class, `SQLGenerator`.

## Constructor

### `__init__(self, system: System)`

The constructor takes a single argument:

- `system`: An instance of the `System` class from the `dataherald.config` module. This argument is not used in the current implementation of the `TestGenerator` class.

The constructor does not perform any actions and is effectively a placeholder.

## Methods

### `generate_response(self, user_prompt: Prompt, database_connection: DatabaseConnection, context: List[dict] = None) -> SQLGeneration`

This method overrides the `generate_response` method from the `SQLGenerator` class and is responsible for generating a mock SQL response.

#### Parameters

- `user_prompt`: An instance of the `Prompt` class, representing the user's input or query for which SQL code needs to be generated.
- `database_connection`: An instance of the `DatabaseConnection` class, representing the connection details to the database against which the SQL query will be executed.
- `context` (optional): A list of dictionaries that provide additional context for generating the SQL response. This parameter is not used in the current implementation and is marked with `# noqa: ARG002` to ignore a specific linting rule.

#### Returns

- `SQLGeneration`: An instance of the `SQLGeneration` class, which contains the following mock data:
  - `question_id`: A hardcoded string `"651f2d76275132d5b65175eb"`, representing a mock identifier for the user's prompt.
  - `sql`: A hardcoded string `"Foo response"`, representing a mock SQL query.
  - `status`: A hardcoded string `"bar"`, representing a mock status of the SQL generation process.

## Usage

The `TestGenerator` class is used in test cases within the `dataherald` project to verify the behavior of components that interact with instances of `SQLGenerator`. Since it provides a predictable and controlled output, it is useful for testing without the need for an actual database connection or complex SQL generation logic.

## Example

To use the `TestGenerator` class in a test case, one would instantiate it and call the `generate_response` method with mock `Prompt` and `DatabaseConnection` objects. The returned `SQLGeneration` object would then be used to assert that the correct behavior occurs in the component under test.

python
# Example usage in a test case
test_system = System()
test_generator = TestGenerator(system=test_system)
mock_prompt = Prompt(...)
mock_database_connection = DatabaseConnection(...)

# Generate the mock SQL response
sql_generation = test_generator.generate_response(
    user_prompt=mock_prompt,
    database_connection=mock_database_connection
)

# Assertions can be made here to verify the expected behavior
assert sql_generation.question_id == "651f2d76275132d5b65175eb"
assert sql_generation.sql == "Foo response"
assert sql_generation.status == "bar"


The `TestGenerator` class simplifies the testing process by providing a consistent and simple output that can be easily checked against expected values.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/sql_generator/__init__.md

# `__init__.py` in `sql_generator` Module

## Overview

The `__init__.py` file within the `sql_generator` directory of the `dataherald` project's `tests` sub-module serves as an initializer for the `sql_generator` test module. This file is part of the project's testing framework and is used to define the `sql_generator` module namespace, making it a Python package. It may also be used to perform any initialization required for the test suite contained within this module.

## Usage

The presence of an `__init__.py` file in a directory tells Python that the directory should be treated as a package. This means that when the testing framework or other parts of the project import from `dataherald.tests.sql_generator`, Python knows to look in this directory for the relevant code.

When the test suite is executed, either as part of a continuous integration pipeline or manually by a developer, Python will recognize the `sql_generator` directory as a package because of this file. This allows for the organization of tests into logical groups and for the use of relative imports within the test suite.

## Structure

The `__init__.py` file can be empty or may contain code. Here are some common uses:

- **Defining `__all__`**: A list named `__all__` can be defined, which explicitly states which modules should be imported when `from sql_generator import *` is used.
- **Initialization Code**: Any code that needs to be run once when the module is first imported can be placed here. This could include setting up test fixtures, initializing logging, or other preparatory tasks.
- **Subpackage Imports**: The file can be used to import submodules or classes from submodules into the package namespace for easier access.

## Example Content

Below is an example of what the `__init__.py` file might contain for the `sql_generator` test module:

python
# __init__.py for sql_generator tests

# Define what is available to import from the sql_generator package
__all__ = ['test_query_builder', 'test_sql_execution']

# Import specific classes or functions from submodules for convenience
from .test_query_builder import TestQueryBuilder
from .test_sql_execution import TestSQLExecution

# Perform any necessary initialization for the test suite
def _initialize_test_environment():
    # Code to initialize the test environment, e.g., setting up a test database
    pass

_initialize_test_environment()


## Notes

- The `__init__.py` file is not mandatory in Python 3.3 and above for a directory to be recognized as a package, but it is still commonly used for compatibility and to define package behavior.
- The actual content of the `__init__.py` file in the `dataherald` project's `sql_generator` test module may vary based on the specific needs of the test suite and the conventions of the project.
- The file should be kept as lightweight as possible to avoid unnecessary overhead when the package is imported.
- Any heavy initialization should be deferred if possible, to avoid slowing down the import process of the module, especially if it's part of a larger test suite or application.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/evaluator/test_eval.md

# TestEvaluator Class

## Overview

The `TestEvaluator` class is a subclass of the `Evaluator` class, designed for testing purposes within the `dataherald` project. It provides a mock implementation of the methods required by the `Evaluator` interface, specifically tailored for use in test scenarios where interactions with real evaluation logic are not necessary or desired.

## Usage

The `TestEvaluator` class is used in the context of unit tests for the `dataherald` project. It allows developers to test the functionality of components that depend on an `Evaluator` without requiring a fully implemented evaluation system.

## Initialization

### `__init__(self, system: System)`

The constructor of the `TestEvaluator` class takes a single argument:

- `system`: An instance of the `System` class from the `dataherald.config` module. In this mock implementation, the `system` parameter is not used, and the constructor body is empty.

## Methods

### `get_confidence_score(self, user_prompt: Prompt, sql_generation: SQLGeneration, database_connection: DatabaseConnection) -> confloat`

This method is an override of the `get_confidence_score` method from the `Evaluator` base class. It calculates a confidence score indicating the likelihood that the generated SQL query (`sql_generation`) correctly represents the user's intent as expressed in the `user_prompt`.

#### Parameters

- `user_prompt`: An instance of the `Prompt` class, representing the user's input.
- `sql_generation`: An instance of the `SQLGeneration` class, representing the generated SQL query.
- `database_connection`: An instance of the `DatabaseConnection` class, representing the database connection details.

#### Returns

- A `confloat` type representing the confidence score, which is a float constrained between 0 and 1 (inclusive). In this mock implementation, the method always returns a fixed score of `1.0`, indicating full confidence.

### `evaluate(self, user_prompt: Prompt, sql_generation: SQLGeneration, database_connection: DatabaseConnection) -> Evaluation`

This method is an override of the `evaluate` method from the `Evaluator` base class. It evaluates the generated SQL query (`sql_generation`) against the user's prompt (`user_prompt`) and returns an `Evaluation` object.

#### Parameters

- `user_prompt`: An instance of the `Prompt` class, representing the user's input.
- `sql_generation`: An instance of the `SQLGeneration` class, representing the generated SQL query.
- `database_connection`: An instance of the `DatabaseConnection` class, representing the database connection details.

#### Returns

- An `Evaluation` object with the following attributes:
  - `question_id`: A string representing the identifier of the user's prompt. In this mock implementation, it is set to `"0"`.
  - `answer_id`: A string representing the identifier of the generated SQL query. In this mock implementation, it is set to `"0"`.
  - `score`: A `confloat` representing the evaluation score. In this mock implementation, it is set to `0.8`.

## Dependencies

- `overrides`: A Python package used to indicate that a method overrides a method from the superclass.
- `pydantic`: A data validation and settings management library used for defining the `confloat` type.
- `dataherald.config`: A module containing the `System` class, which holds configuration details for the `dataherald` project.
- `dataherald.eval`: A module containing the `Evaluation` and `Evaluator` classes, which define the evaluation interface and data structures.
- `dataherald.sql_database.models.types`: A module containing the `DatabaseConnection` class, which defines the structure for database connection details.
- `dataherald.types`: A module containing the `Prompt` and `SQLGeneration` classes, which define the structure for user prompts and SQL query generations.

## File Location

The `TestEvaluator` class is defined in the file located at `/workspaces/documentation-generator/target_code/dataherald/tests/evaluator/test_eval.py` within the `dataherald` project. This file is part of the test suite for the evaluation component of the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/evaluator/__init__.md

# `__init__.py` in `dataherald/tests/evaluator`

## Overview

The `__init__.py` file within the `dataherald/tests/evaluator` directory serves as an initialization script for the `evaluator` test package in the `dataherald` project. This file is part of the project's testing framework and is used to define the `evaluator` subpackage within the larger test suite. The presence of an `__init__.py` file in a directory indicates to Python that the directory should be treated as a package, allowing its modules to be imported elsewhere in the project.

## Usage

The `__init__.py` file is automatically executed when the `evaluator` package is imported. This can occur in several contexts:

1. When running tests for the `evaluator` module using a test runner such as `unittest`, `pytest`, or a custom test runner integrated into the `dataherald` project.
2. When importing the `evaluator` test package or specific test modules within it from other test modules or scripts within the `dataherald` project.

## Structure and Content

The `__init__.py` file can contain several types of content:

1. **Package Initialization Code**: Any code that is needed to initialize the `evaluator` test package. This could include setting up test environments, initializing global variables, or configuring logging for the tests.

2. **Import Statements**: The file may include import statements to bring in necessary modules or specific classes and functions from those modules into the package namespace. This allows for easier access to these components when writing tests.

3. **Subpackage Declarations**: If the `evaluator` test package contains subpackages, the `__init__.py` file may declare these subpackages to ensure they are recognized by Python as part of the package hierarchy.

4. **Test Suite Definitions**: The file may define a test suite that aggregates various test cases and modules within the `evaluator` package. This suite can then be used by test runners to execute all the tests in the package.

5. **Utility Functions**: It may contain utility functions that are used across multiple test modules within the `evaluator` package.

6. **Constants**: Any constants that are relevant to the tests in the `evaluator` package could be defined here.

## Example Content

Below is an example of what the `__init__.py` file might contain:

python
# Import necessary modules for testing
from .test_evaluator import TestEvaluator
from .test_helpers import TestHelpers

# Define a test suite for easy execution of all evaluator tests
import unittest

def evaluator_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEvaluator))
    suite.addTest(unittest.makeSuite(TestHelpers))
    return suite

# Initialize any global variables or configurations for the tests
TEST_CONFIG = {
    'logging_level': 'DEBUG',
    'test_data_path': '/path/to/test/data'
}

# Utility function example
def load_test_data(file_name):
    with open(TEST_CONFIG['test_data_path'] + file_name, 'r') as file:
        return file.read()


## Integration with Test Runners

Test runners that are configured to work with the `dataherald` project will recognize the `evaluator` package as containing tests due to the presence of the `__init__.py` file. They will typically look for test cases and suites defined within this file or within other modules in the package to execute as part of the testing process.

## Conclusion

The `__init__.py` file in the `dataherald/tests/evaluator` directory is a crucial component of the testing infrastructure, providing package initialization, test suite aggregation, and utility functions for the `evaluator` tests. It ensures that the test modules are properly recognized and can be executed by the project's test runners.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/db/test_db.md

# TestDB Class

## Overview
The `TestDB` class is a subclass of the `DB` class, designed to simulate a database for testing purposes. It overrides methods from the `DB` class to perform operations in-memory rather than on an actual database. This class is part of the `dataherald` project, specifically within the `tests/db` directory, indicating its use for testing database interactions.

## Attributes
- `memory`: A dictionary that acts as the in-memory storage for the simulated database.

## Constructor
- `__init__(self, system: System)`: Initializes the `TestDB` instance.
  - Parameters:
    - `system`: An instance of the `System` class from the `dataherald.config` module.
  - Behavior:
    - Calls the superclass constructor with the `system` parameter.
    - Initializes the `memory` attribute as an empty dictionary.
    - Populates `memory` with predefined "database_connections" and "instructions" collections.

## Methods

### insert_one
- `insert_one(self, collection: str, obj: dict) -> int`:
  - Inserts a single document into the specified collection in memory.
  - Parameters:
    - `collection`: The name of the collection to insert the document into.
    - `obj`: The document to be inserted.
  - Returns:
    - The ObjectId of the inserted document.
  - Behavior:
    - Assigns a fixed ObjectId to the document.
    - Appends the document to the specified collection in memory.
    - If the collection does not exist, it is created.

### find_one
- `find_one(self, collection: str, query: dict) -> dict`:
  - Retrieves the first document from the specified collection in memory.
  - Parameters:
    - `collection`: The name of the collection to search.
    - `query`: The query criteria to match documents.
  - Returns:
    - The first document in the collection if it exists, otherwise an empty dictionary.

### find_by_id
- `find_by_id(self, collection: str, id: str) -> dict`:
  - Retrieves a document by its ObjectId from the specified collection in memory.
  - Parameters:
    - `collection`: The name of the collection to search.
    - `id`: The string representation of the ObjectId to search for.
  - Returns:
    - The document with the matching ObjectId if found, otherwise `None`.

### find
- `find(self, collection: str, query: dict, sort: list = None, page: int = 0, limit: int = 0) -> list`:
  - Retrieves a list of documents from the specified collection in memory.
  - Parameters:
    - `collection`: The name of the collection to search.
    - `query`: The query criteria to match documents.
    - `sort`: A list of sorting criteria.
    - `page`: The page number for pagination.
    - `limit`: The number of documents per page.
  - Returns:
    - An empty list (method not implemented).

### update_or_create
- `update_or_create(self, collection: str, query: dict, obj: dict) -> int`:
  - Updates an existing document or creates a new one in the specified collection in memory.
  - Parameters:
    - `collection`: The name of the collection to update or create the document in.
    - `query`: The query criteria to match documents.
    - `obj`: The document to be updated or created.
  - Returns:
    - The ObjectId of the updated or created document.
  - Behavior:
    - Delegates to the `insert_one` method, effectively always creating a new document.

### find_all
- `find_all(self, collection: str, page: int = 0, limit: int = 0) -> list`:
  - Retrieves all documents from the specified collection in memory.
  - Parameters:
    - `collection`: The name of the collection to search.
    - `page`: The page number for pagination.
    - `limit`: The number of documents per page.
  - Returns:
    - A list of all documents in the collection.

### delete_by_id
- `delete_by_id(self, collection: str, id: str) -> int`:
  - Deletes a document by its ObjectId from the specified collection in memory.
  - Parameters:
    - `collection`: The name of the collection to delete the document from.
    - `id`: The string representation of the ObjectId to delete.
  - Returns:
    - `1` if the document was deleted, `0` otherwise.

### rename
- `rename(self, old_collection_name: str, new_collection_name) -> None`:
  - Renames a collection in memory.
  - Parameters:
    - `old_collection_name`: The current name of the collection.
    - `new_collection_name`: The new name for the collection.
  - Behavior:
    - Method not implemented (no operation).

### rename_field
- `rename_field(self, collection_name: str, old_field_name: str, new_field_name: str) -> None`:
  - Renames a field within all documents in the specified collection in memory.
  - Parameters:
    - `collection_name`: The name of the collection containing the documents.
    - `old_field_name`: The current name of the field to rename.
    - `new_field_name`: The new name for the field.
  - Behavior:
    - Method not implemented (no operation).

## Usage
The `TestDB` class is used for testing purposes within the `dataherald` project. It allows developers to write tests that interact with a database without the need for an actual database connection. This can speed up test execution and avoid side effects on real data.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/db/__init__.md

# `__init__.py` in `dataherald/tests/db`

## Overview

The `__init__.py` file within the `dataherald/tests/db` directory serves as a package initializer for the `db` subpackage under the `tests` package in the `dataherald` project. This file is part of the testing framework and is used to group database-related test modules, making them discoverable and executable as part of the project's test suite.

## Usage

The presence of the `__init__.py` file in the `dataherald/tests/db` directory indicates to the Python interpreter that the directory should be treated as a Python package. This allows for the following:

- **Test Discovery**: Test runners like `unittest`, `pytest`, or `nose` can automatically discover test modules within this package. This is essential for automated testing environments and continuous integration (CI) workflows.
- **Namespace Package**: It establishes the `dataherald.tests.db` namespace, enabling the import of modules within this package using dot notation (e.g., `from dataherald.tests.db import test_module`).
- **Shared Fixtures and Utilities**: If the `__init__.py` file contains any common fixtures, helper functions, or base classes, they can be shared across multiple test modules within the `db` subpackage. This promotes code reuse and maintainability.

## Structure

The `__init__.py` file can be empty or contain code. An empty `__init__.py` file simply serves the purpose of package recognition. If it contains code, it might include the following:

- **Common Imports**: Import statements for commonly used modules or objects in the test suite.
- **Fixtures**: Setup and teardown code that is used by multiple test modules within the `db` subpackage.
- **Utility Functions**: Helper functions that assist in creating mock objects, asserting conditions, or performing repetitive tasks.
- **Constants**: Definitions of constants that are relevant to the database tests, such as connection strings, test database names, or configuration parameters.

## Example Content

Below is an example of what the `__init__.py` file might contain:

python
# __init__.py for dataherald/tests/db

# Common imports for database tests
from .common import create_test_database, destroy_test_database

# Define a fixture for setting up a test database
def setup_module(module):
    """Setup test database before running database tests."""
    create_test_database()

# Define a teardown fixture for cleaning up after tests
def teardown_module(module):
    """Destroy test database after running database tests."""
    destroy_test_database()


In this example, the `__init__.py` file defines setup and teardown methods that are executed before and after the test modules in the `db` subpackage are run. It also imports common utilities from a hypothetical `common` module within the same package.

## Integration with Test Frameworks

When integrated with a test framework, the `__init__.py` file's fixtures and utilities can be invoked automatically. For instance, `pytest` can use fixtures defined in the `__init__.py` file for setup and teardown at the module, class, or session level.

## Conclusion

The `__init__.py` file in the `dataherald/tests/db` directory is a crucial component for organizing and executing database-related tests within the `dataherald` project. It provides a mechanism for test discovery, shared resources, and namespace management, contributing to a structured and maintainable test suite.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/vector_store/test_vector_store.md

# TestVectorStore Class

## Overview

The `TestVectorStore` class is a subclass of `VectorStore` that is designed for testing purposes within the `dataherald` project. It provides a mock implementation of the `VectorStore` interface, allowing for the simulation of vector storage operations without the need for a live database connection or actual data persistence.

## Class Definition

### Constructor

python
def __init__(self, system: System):
    super().__init__(system)


#### Parameters

- `system`: An instance of the `System` class from the `dataherald.config` module, which contains configuration settings for the system.

#### Description

The constructor initializes the `TestVectorStore` instance by calling the constructor of the parent `VectorStore` class with the provided `system` configuration.

### Methods

#### query

python
@override
def query(
    self,
    query_texts: List[str],
    db_connection_id: str,
    collection: str,
    num_results: int,
) -> list:
    return [{"id": "64ade8ed3445882cedc06ab6", "score": 0.1}]


##### Parameters

- `query_texts`: A list of strings representing the query texts to be used for retrieving vectors.
- `db_connection_id`: A string identifier for the database connection.
- `collection`: The name of the collection from which to retrieve vectors.
- `num_results`: The number of results to return.

##### Returns

- A list of dictionaries, each representing a mock vector record. In this mock implementation, it always returns a single record with a fixed `id` and `score`.

##### Description

The `query` method is a mock implementation that simulates the retrieval of vector records from a vector store. It ignores the input parameters and returns a predefined list of results.

#### add_record

python
@override
def add_record(
    self,
    documents: str,
    db_connection_id: str,
    collection: str,
    metadata: Any,
    ids: List,
):
    pass


##### Parameters

- `documents`: A string representing the documents to be added to the vector store.
- `db_connection_id`: A string identifier for the database connection.
- `collection`: The name of the collection to which the documents will be added.
- `metadata`: Additional metadata associated with the documents.
- `ids`: A list of identifiers for the documents.

##### Description

The `add_record` method is a mock implementation that simulates the addition of vector records to a vector store. It performs no operation and is used for testing purposes.

#### delete_record

python
@override
def delete_record(self, collection: str, id: str):
    pass


##### Parameters

- `collection`: The name of the collection from which the record will be deleted.
- `id`: The identifier of the record to be deleted.

##### Description

The `delete_record` method is a mock implementation that simulates the deletion of a vector record from a vector store. It performs no operation and is used for testing purposes.

#### delete_collection

python
@override
def delete_collection(self, collection: str):
    pass


##### Parameters

- `collection`: The name of the collection to be deleted.

##### Description

The `delete_collection` method is a mock implementation that simulates the deletion of an entire collection from a vector store. It performs no operation and is used for testing purposes.

#### create_collection

python
@override
def create_collection(self, collection: str):
    pass


##### Parameters

- `collection`: The name of the collection to be created.

##### Description

The `create_collection` method is a mock implementation that simulates the creation of a new collection in a vector store. It performs no operation and is used for testing purposes.

## Usage

The `TestVectorStore` class is used in test cases to simulate interactions with a `VectorStore` without the need for an actual database. It allows developers to test the behavior of their code in a controlled environment where the outcomes of vector store operations are predictable and do not have side effects on a real database.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/tests/vector_store/__init__.md

# `__init__.py` in `vector_store` Module

## Overview

The `__init__.py` file within the `vector_store` directory of the `dataherald` project's `tests` sub-module serves as an initializer for the `vector_store` test module. This file is part of the project's testing framework and is used to define the `vector_store` package, allowing for the organization of test cases specific to the vector store functionality.

## Usage

The presence of the `__init__.py` file in the `vector_store` directory indicates to the Python interpreter that the directory should be treated as a package. This allows for the importation of the `vector_store` module or its contents in other parts of the test suite or the main application.

When the test suite is executed, the testing framework (e.g., `unittest`, `pytest`) will recognize the `vector_store` directory as a package containing test cases. This modular approach enables developers to run tests specific to the vector store functionality in isolation or as part of the entire test suite.

## Structure

The `__init__.py` file can be empty or contain code that initializes the test environment for the `vector_store` tests. This may include setting up mock data, configuring test fixtures, or importing necessary modules for the tests.

### Example Structure

python
# __init__.py within vector_store test module

# Import statements for test dependencies
from .test_vector_operations import TestVectorOperations
from .test_vector_storage import TestVectorStorage

# Any initialization code for the test module
# For example, setting up a mock database or configuring environment variables


## Test Discovery

During test discovery, the testing framework will traverse directories looking for test files. The presence of `__init__.py` ensures that the `vector_store` directory is searchable and that any test files within it are discoverable. Test files typically follow a naming convention such as `test_*.py` or `*_test.py`.

## Integration with Test Frameworks

The `__init__.py` file can also be used to integrate with specific test frameworks by including relevant decorators or configuration settings that apply to all tests within the `vector_store` module.

### Example Integration with `pytest`

python
# __init__.py within vector_store test module

# Pytest specific imports
import pytest

# Pytest configuration or fixtures that apply to all tests in the vector_store module
@pytest.fixture(scope="module")
def vector_store_fixture():
    # Setup code for the fixture
    pass
    yield
    # Teardown code for the fixture


## Conclusion

The `__init__.py` file in the `vector_store` test module is a crucial part of the project's testing infrastructure. It defines the module's scope, facilitates test discovery, and can provide module-level setup and integration with testing frameworks. This file ensures that the `vector_store` tests are well-organized and maintainable as part of the larger `dataherald` project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/vector_store/astra.md

# Astra Vector Store

The `Astra` class is a subclass of `VectorStore` and provides an interface for storing and querying vectorized representations of text data within an AstraDB database. It is designed to work with the DataHerald project and integrates with the OpenAI API for generating embeddings.

## Initialization

- `__init__(self, system: System)`: The constructor initializes the AstraDB connection using environment variables for the API endpoint and application token. It raises a `ValueError` if these are not set. The `namespace` is hardcoded to `"default_keyspace"`.

## Collection Name Formatting

- `collection_name_formatter(self, collection: str) -> str`: A helper method that formats collection names by replacing hyphens with underscores.

## Querying

- `query(self, query_texts: List[str], db_connection_id: str, collection: str, num_results: int) -> list`: This method queries the AstraDB for similar vectors to the provided `query_texts`. It checks if the collection exists, retrieves the database connection, generates embeddings for the query text using OpenAI API, and performs a vector similarity search in the specified collection. It returns the results converted to a Pinecone-compatible object model.

## Adding Records

- `add_records(self, golden_sqls: List[GoldenSQL], collection: str)`: This method adds multiple records to the specified collection. It checks if the collection exists and creates it if not. It retrieves the database connection, generates embeddings for the `prompt_text` of each `GoldenSQL` object, and inserts the records into the collection in chunks.

- `add_record(self, documents: str, db_connection_id: str, collection: str, metadata: Any, ids: List)`: Similar to `add_records`, but for a single document. It generates an embedding for the document and inserts it into the collection with the provided metadata and ID.

## Deleting Records and Collections

- `delete_record(self, collection: str, id: str)`: This method deletes a single record from the specified collection by its ID.

- `delete_collection(self, collection: str)`: This method deletes an entire collection from the AstraDB.

## Collection Creation

- `create_collection(self, collection: str)`: This method creates a new collection in the AstraDB with a specified dimension (1536) and metric ("cosine") for vector storage.

## Conversion to Pinecone Object Model

- `convert_to_pinecone_object_model(self, astra_results: dict) -> List`: A helper method that converts the results from AstraDB format to a list of dictionaries with `id` and `score` keys, compatible with Pinecone's object model.

## Error Handling

- The class includes error handling for API request errors and checks for the existence of collections before performing operations.

## Dependencies

- The class relies on the `astrapy` library for interacting with AstraDB, `langchain_openai` for generating embeddings using OpenAI's API, and `sql_metadata` for parsing SQL queries.

## Environment Variables

- The class requires the following environment variables to be set:
  - `ASTRA_DB_API_ENDPOINT`: The endpoint URL for the AstraDB API.
  - `ASTRA_DB_APPLICATION_TOKEN`: The application token for authenticating with the AstraDB API.

## Embedding Model

- The embedding model used for generating text embeddings is specified by the `EMBEDDING_MODEL` constant, set to `"text-embedding-3-small"`.

## Usage

- The `Astra` class is used within the DataHerald project to store and retrieve vectorized representations of SQL queries and other text data, facilitating similarity searches and other vector-based operations in the context of a database management system.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/vector_store/pinecone.md

# Pinecone Vector Store Module

## Overview

The `Pinecone` class is a subclass of `VectorStore` and provides an interface for interacting with Pinecone, a vector database for building search, recommendation, and AI applications. It is designed to store, query, and manage embeddings of SQL queries and their metadata.

## Initialization

### `__init__(self, system: System)`

The constructor initializes the Pinecone client with the necessary API key and environment variables. It requires a `System` object to access the application's configuration and database.

- **Parameters:**
  - `system`: An instance of the `System` class containing configuration and database access.

- **Environment Variables:**
  - `PINECONE_API_KEY`: The API key for authenticating with the Pinecone service.
  - `PINECONE_ENVIRONMENT`: The environment setting for Pinecone.

- **Exceptions:**
  - Raises `ValueError` if either `PINECONE_API_KEY` or `PINECONE_ENVIRONMENT` is not set.

## Methods

### `query(self, query_texts: List[str], db_connection_id: str, collection: str, num_results: int) -> list`

Queries the Pinecone index for similar vectors to the provided query text and returns a list of matches.

- **Parameters:**
  - `query_texts`: A list of strings containing the query text.
  - `db_connection_id`: The database connection ID to filter results.
  - `collection`: The name of the Pinecone collection to query.
  - `num_results`: The number of results to return.

- **Returns:**
  - A list of query results with metadata.

### `add_records(self, golden_sqls: List[GoldenSQL], collection: str)`

Adds multiple records to the Pinecone index.

- **Parameters:**
  - `golden_sqls`: A list of `GoldenSQL` objects containing the SQL queries and associated metadata.
  - `collection`: The name of the Pinecone collection to add records to.

### `add_record(self, documents: str, db_connection_id: str, collection: str, metadata: Any, ids: List)`

Adds a single record to the Pinecone index.

- **Parameters:**
  - `documents`: The document text to be embedded and stored.
  - `db_connection_id`: The database connection ID associated with the document.
  - `collection`: The name of the Pinecone collection to add the record to.
  - `metadata`: Additional metadata to store with the record.
  - `ids`: A list containing the ID of the record.

### `delete_record(self, collection: str, id: str)`

Deletes a record from the Pinecone index.

- **Parameters:**
  - `collection`: The name of the Pinecone collection to delete the record from.
  - `id`: The ID of the record to delete.

### `delete_collection(self, collection: str)`

Deletes an entire Pinecone collection.

- **Parameters:**
  - `collection`: The name of the Pinecone collection to delete.

### `create_collection(self, collection: str)`

Creates a new Pinecone collection with the specified name.

- **Parameters:**
  - `collection`: The name of the Pinecone collection to create.

## Usage

The `Pinecone` class is used within the project to manage the storage and retrieval of SQL query embeddings. It interacts with the Pinecone service to perform operations such as querying for similar embeddings, adding new embeddings, and managing collections and records within the Pinecone index.

The embeddings are generated using the `OpenAIEmbeddings` class, which utilizes the OpenAI API to convert text into vector representations. These embeddings are then stored in Pinecone along with metadata such as the tables used in the SQL query and the database connection ID.

The class methods are decorated with `@override` to indicate that they are overriding methods from the `VectorStore` base class. This ensures that the `Pinecone` class provides a consistent interface for vector storage operations within the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/vector_store/__init__.md

# VectorStore Module

## Overview

The `VectorStore` module is part of the `dataherald` package, specifically within the `vector_store` subpackage. It defines an abstract base class `VectorStore` that outlines the interface for various vector storage implementations. This module is designed to interact with collections of vectors, which are typically used in machine learning and data processing applications.

## Classes

### VectorStore

The `VectorStore` class is an abstract base class that inherits from `Component` and `ABC` (Abstract Base Class) from the `abc` module. It provides a template for creating concrete vector store implementations that can be integrated into the `dataherald` system.

#### Attributes

- `collections`: A list of strings representing the names of the collections managed by the vector store.

#### Methods

##### `__init__(self, system: System)`

The constructor initializes the vector store with a reference to the `System` object. This method is abstract and must be implemented by subclasses.

Parameters:
- `system`: An instance of the `System` class from the `dataherald.config` module.

##### `query(self, query_texts: List[str], db_connection_id: str, collection: str, num_results: int) -> list`

Abstract method for querying the vector store. It retrieves a list of results based on the provided query texts.

Parameters:
- `query_texts`: A list of strings containing the query texts.
- `db_connection_id`: A string representing the database connection identifier.
- `collection`: The name of the collection to query.
- `num_results`: The number of results to return.

Returns:
- A list of query results.

##### `create_collection(self, collection: str)`

Abstract method for creating a new collection within the vector store.

Parameters:
- `collection`: The name of the collection to create.

##### `add_records(self, golden_sqls: List[GoldenSQL], collection: str)`

Abstract method for adding multiple records to a specified collection.

Parameters:
- `golden_sqls`: A list of `GoldenSQL` objects to be added to the collection.
- `collection`: The name of the collection where the records will be added.

##### `add_record(self, documents: str, db_connection_id: str, collection: str, metadata: Any, ids: List = None)`

Abstract method for adding a single record to a specified collection.

Parameters:
- `documents`: A string representing the documents to be added.
- `db_connection_id`: A string representing the database connection identifier.
- `collection`: The name of the collection where the record will be added.
- `metadata`: Additional metadata associated with the record.
- `ids`: An optional list of identifiers for the record.

##### `delete_record(self, collection: str, id: str)`

Abstract method for deleting a record from a specified collection.

Parameters:
- `collection`: The name of the collection from which the record will be deleted.
- `id`: The identifier of the record to be deleted.

##### `delete_collection(self, collection: str)`

Abstract method for deleting an entire collection from the vector store.

Parameters:
- `collection`: The name of the collection to be deleted.

## Usage

The `VectorStore` class is not intended to be instantiated directly. Instead, it serves as a blueprint for creating concrete subclasses that implement the abstract methods defined in the class. These implementations are responsible for managing the storage and retrieval of vector data in various backends, such as databases or file systems.

Concrete subclasses of `VectorStore` must implement all abstract methods to provide functionality for querying, adding, and deleting records and collections. Once implemented, these subclasses can be integrated into the `dataherald` system and used to manage vector data as part of the project's data processing and machine learning workflows.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/vector_store/chroma.md

# Chroma Class

## Overview

The `Chroma` class is a subclass of `VectorStore` and provides an interface for interacting with a vector database using the `chromadb` library. It is designed to store, query, and manage collections of vectors, which are typically used for similarity search or other vector-based operations. The class includes methods for querying the database, adding records, deleting records, and managing collections.

## Initialization

### `__init__(self, system: System, persist_directory: str = "/app/chroma")`

The constructor initializes the `Chroma` class with the following parameters:

- `system`: An instance of the `System` class from the `dataherald.config` module, which contains configuration settings for the system.
- `persist_directory`: A string representing the file path to the directory where the `chromadb` persistent client will store its data. The default value is `/app/chroma`.

The constructor creates a `PersistentClient` from the `chromadb` library, which is used to interact with the vector database. The client is initialized with the specified `persist_directory`.

## Methods

### `query(self, query_texts: List[str], db_connection_id: str, collection: str, num_results: int) -> list`

Queries the specified collection for vectors similar to the provided `query_texts`. It takes the following parameters:

- `query_texts`: A list of strings representing the query vectors.
- `db_connection_id`: A string representing the database connection identifier.
- `collection`: A string representing the name of the collection to query.
- `num_results`: An integer specifying the maximum number of results to return.

The method attempts to retrieve the target collection from the `chromadb` client. If the collection does not exist, it returns an empty list. Otherwise, it performs the query and returns the results converted to the Pinecone object model using the `convert_to_pinecone_object_model` method.

### `add_records(self, golden_sqls: List[GoldenSQL], collection: str)`

Adds multiple records to the specified collection. It takes the following parameters:

- `golden_sqls`: A list of `GoldenSQL` objects, which contain the SQL queries and associated metadata.
- `collection`: A string representing the name of the collection where the records will be added.

The method iterates over the `golden_sqls` list, extracting the necessary information and adding each record to the collection using the `add_record` method.

### `add_record(self, documents: str, db_connection_id: str, collection: str, metadata: Any, ids: List)`

Adds a single record to the specified collection. It takes the following parameters:

- `documents`: A string representing the document to be added.
- `db_connection_id`: A string representing the database connection identifier.
- `collection`: A string representing the name of the collection where the record will be added.
- `metadata`: Any additional metadata associated with the document.
- `ids`: A list of identifiers for the document.

The method retrieves or creates the target collection and checks if the document already exists. If not, it adds the document along with its metadata and identifier to the collection.

### `delete_record(self, collection: str, id: str)`

Deletes a record from the specified collection. It takes the following parameters:

- `collection`: A string representing the name of the collection.
- `id`: A string representing the identifier of the record to be deleted.

The method retrieves or creates the target collection and deletes the record with the specified identifier.

### `delete_collection(self, collection: str)`

Deletes the specified collection. It takes the following parameter:

- `collection`: A string representing the name of the collection to be deleted.

This method overrides the `delete_collection` method from the `VectorStore` class.

### `create_collection(self, collection: str)`

Creates a new collection. It takes the following parameter:

- `collection`: A string representing the name of the collection to be created.

This method overrides the `create_collection` method from the `VectorStore` class.

### `convert_to_pinecone_object_model(self, chroma_results: dict) -> List`

Converts the results from a `chromadb` query to the Pinecone object model. It takes the following parameter:

- `chroma_results`: A dictionary containing the results from a `chromadb` query.

The method iterates over the results and constructs a list of dictionaries, each containing an identifier and a score, which are compatible with the Pinecone object model.

## Usage

The `Chroma` class is used within a project to interact with a vector database for storing and retrieving vector data. It provides a high-level API for performing operations such as querying for similar vectors, adding new vectors, and managing collections within the database. The class is designed to be used with the `chromadb` library and integrates with the Pinecone object model for compatibility with other components of the system.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/nl_generations.md

# NLGenerationRepository Class

## Overview

The `NLGenerationRepository` class provides an abstraction layer for interacting with a database collection named `nl_generations`. It is designed to handle the creation, retrieval, and updating of `NLGeneration` objects within the database. The class requires a `storage` object that is responsible for the actual database operations.

## Attributes

- `storage`: An instance of a storage class that provides methods for interacting with the database.

## Methods

### `__init__(self, storage)`

The constructor initializes the `NLGenerationRepository` with a given storage object.

#### Parameters

- `storage`: The storage object that provides the database operations.

### `insert(self, nl_generation: NLGeneration) -> NLGeneration`

Inserts a new `NLGeneration` object into the database.

#### Parameters

- `nl_generation`: An instance of `NLGeneration` to be inserted into the database.

#### Returns

- The `NLGeneration` object with its `id` attribute set to the newly created database entry's ID.

#### Process

1. Converts the `NLGeneration` object to a dictionary, excluding the `id` field.
2. Converts the `sql_generation_id` to a string and adds it to the dictionary.
3. Inserts the dictionary into the `nl_generations` collection in the database.
4. Sets the `id` attribute of the `NLGeneration` object to the string representation of the newly inserted document's ID.
5. Returns the updated `NLGeneration` object.

### `update(self, nl_generation: NLGeneration) -> NLGeneration`

Updates an existing `NLGeneration` object in the database.

#### Parameters

- `nl_generation`: An instance of `NLGeneration` to be updated in the database.

#### Returns

- The `NLGeneration` object after the update operation.

#### Process

1. Converts the `NLGeneration` object to a dictionary, excluding the `id` field.
2. Converts the `sql_generation_id` to a string and adds it to the dictionary.
3. Updates the document in the `nl_generations` collection that matches the `id` of the `NLGeneration` object, or creates it if it does not exist.
4. Returns the `NLGeneration` object.

### `find_one(self, query: dict) -> NLGeneration | None`

Finds a single `NLGeneration` object in the database that matches the given query.

#### Parameters

- `query`: A dictionary representing the query to find the document.

#### Returns

- An instance of `NLGeneration` if a matching document is found, otherwise `None`.

#### Process

1. Executes a query to find a single document in the `nl_generations` collection.
2. If a document is found, converts the `_id` field to a string and assigns it to the `id` field.
3. Returns an `NLGeneration` object created from the document data.

### `find_by_id(self, id: str) -> NLGeneration | None`

Finds a single `NLGeneration` object in the database by its ID.

#### Parameters

- `id`: A string representing the ID of the document to find.

#### Returns

- An instance of `NLGeneration` if a matching document is found, otherwise `None`.

#### Process

1. Executes a query to find a single document in the `nl_generations` collection by its `_id`.
2. If a document is found, converts the `_id` field to a string and assigns it to the `id` field.
3. Returns an `NLGeneration` object created from the document data.

### `find_by(self, query: dict, page: int = 0, limit: int = 0) -> list[NLGeneration]`

Finds a list of `NLGeneration` objects in the database that match the given query, with optional pagination.

#### Parameters

- `query`: A dictionary representing the query to find the documents.
- `page`: An integer representing the page number for pagination (optional).
- `limit`: An integer representing the number of documents per page for pagination (optional).

#### Returns

- A list of `NLGeneration` objects that match the query.

#### Process

1. Executes a query to find documents in the `nl_generations` collection based on the given query, with optional pagination.
2. For each document found, converts the `_id` field to a string and assigns it to the `id` field.
3. Creates an `NLGeneration` object from the document data and adds it to the result list.
4. Returns the list of `NLGeneration` objects.

## Exceptions

### `NLGenerationNotFoundError`

A custom exception class that is raised when an `NLGeneration` object is not found in the database.

## Constants

- `DB_COLLECTION`: A string representing the name of the database collection (`"nl_generations"`) used by the repository.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/finetunings.md

# FinetuningsRepository Class

## Overview

The `FinetuningsRepository` class provides an abstraction layer for performing CRUD (Create, Read, Update, Delete) operations on a database collection named `finetunings`. It uses a storage object passed to it during initialization to interact with the database. The class is designed to work with `Finetuning` objects, which are presumably a custom data type defined in the `dataherald.types` module.

## Attributes

- `storage`: An instance of a storage class that provides methods for interacting with the database.

## Methods

### `__init__(self, storage)`
The constructor takes a `storage` parameter, which is expected to be an instance of a storage class that provides the necessary database operations.

### `insert(self, model: Finetuning) -> Finetuning`
Inserts a new `Finetuning` object into the `finetunings` collection. It excludes the `id` field from the model when inserting and assigns a new `id` to the `model` after insertion. The new `id` is the string representation of the `_id` field generated by the database. It returns the `Finetuning` object with the new `id` set.

### `find_one(self, query: dict) -> Finetuning | None`
Retrieves a single `Finetuning` object from the `finetunings` collection that matches the given `query`. If no matching document is found, it returns `None`. If a document is found, it creates a `Finetuning` object with the data and sets its `id` to the string representation of the `_id` field from the database.

### `update(self, model: Finetuning) -> Finetuning`
Updates an existing `Finetuning` object in the `finetunings` collection. It uses the `id` of the `model` to locate the document in the database and updates it with the rest of the `model`'s data, excluding the `id`. It returns the updated `Finetuning` object.

### `find_by_id(self, id: str) -> Finetuning | None`
Retrieves a `Finetuning` object from the `finetunings` collection by its `id`. If no document with the given `id` is found, it returns `None`. If found, it creates a `Finetuning` object with the data and sets its `id` to the string representation of the `_id` field from the database.

### `find_by(self, query: dict, page: int = 0, limit: int = 0) -> list[Finetuning]`
Retrieves a list of `Finetuning` objects that match the given `query`. It supports pagination through the `page` and `limit` parameters. If `page` and `limit` are greater than 0, it retrieves a subset of the results based on these values. It returns a list of `Finetuning` objects with their `id` fields set to the string representation of their `_id` fields from the database.

### `find_all(self, page: int = 0, limit: int = 0) -> list[Finetuning]`
Retrieves all `Finetuning` objects from the `finetunings` collection. It supports pagination through the `page` and `limit` parameters. It returns a list of `Finetuning` objects with their `id` fields set to the string representation of their `_id` fields from the database.

### `delete_by_id(self, id: str) -> int`
Deletes a `Finetuning` object from the `finetunings` collection by its `id`. It returns the number of documents deleted (which should be 1 if the deletion was successful, or 0 if no document with the given `id` was found).

## Usage

The `FinetuningsRepository` class is used to interact with the `finetunings` collection in the database. It provides a high-level API for performing database operations on `Finetuning` objects, abstracting away the details of the database access. This class is typically used by other parts of the project that require data persistence for `Finetuning` objects, such as web service endpoints, background processing jobs, or other data management scripts.

## Dependencies

- `bson.objectid.ObjectId`: Used to convert string representations of MongoDB `_id` fields to ObjectId instances for querying.
- `dataherald.types.Finetuning`: The custom data type that this repository handles. It is assumed to be a Pydantic model or similar, with a `dict` method for serialization and an `id` attribute.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the database collection this repository manages, which is `"finetunings"`.

## Notes

- The `storage` object is expected to have the following methods: `insert_one`, `find_one`, `update_or_create`, `find`, `find_all`, and `delete_by_id`, which correspond to the database operations used in the repository methods.
- The `Finetuning` type is expected to have a constructor that accepts keyword arguments corresponding to the fields of the `Finetuning` documents in the database.
- The `id` field of `Finetuning` objects is managed as a string within the application, even though it is stored as an ObjectId in the database.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/instructions.md

# InstructionRepository Class

## Overview
The `InstructionRepository` class provides an abstraction layer for performing CRUD (Create, Read, Update, Delete) operations on a collection named `instructions` within a database. It is designed to work with `Instruction` objects, which are presumably a custom data type defined in the `dataherald.types` module.

## Attributes
- `storage`: An instance of a storage class that provides methods for interacting with the database.

## Methods

### `__init__(self, storage)`
Constructor for the `InstructionRepository` class.
- **Parameters**:
  - `storage`: An instance of a storage class.

### `insert(self, instruction: Instruction) -> Instruction`
Inserts a new `Instruction` object into the database.
- **Parameters**:
  - `instruction`: An `Instruction` object to be inserted into the database.
- **Returns**: The `Instruction` object with its `id` attribute set to the newly created database entry's ID.
- **Process**:
  1. Converts the `Instruction` object to a dictionary, excluding the `id` field.
  2. Converts the `db_connection_id` to a string and adds it to the dictionary.
  3. Inserts the dictionary into the database using the `storage` instance's `insert_one` method.
  4. Sets the `id` attribute of the `Instruction` object to the string representation of the newly inserted document's ID.
  5. Returns the updated `Instruction` object.

### `find_one(self, query: dict) -> Instruction | None`
Finds a single `Instruction` object in the database that matches the given query.
- **Parameters**:
  - `query`: A dictionary representing the query to find the document.
- **Returns**: An `Instruction` object if found, otherwise `None`.
- **Process**:
  1. Uses the `storage` instance's `find_one` method to search for a document in the database.
  2. If a document is found, converts the `_id` and `db_connection_id` fields to strings.
  3. Returns an `Instruction` object initialized with the document's data.

### `update(self, instruction: Instruction) -> Instruction`
Updates an existing `Instruction` object in the database.
- **Parameters**:
  - `instruction`: An `Instruction` object with updated fields.
- **Returns**: The `Instruction` object.
- **Process**:
  1. Converts the `Instruction` object to a dictionary, excluding the `id` field.
  2. Converts the `db_connection_id` to a string and adds it to the dictionary.
  3. Updates the corresponding document in the database using the `storage` instance's `update_or_create` method, matching by the `Instruction` object's `id`.
  4. Returns the `Instruction` object.

### `find_by_id(self, id: str) -> Instruction | None`
Finds an `Instruction` object by its ID.
- **Parameters**:
  - `id`: A string representing the `Instruction` object's ID.
- **Returns**: An `Instruction` object if found, otherwise `None`.
- **Process**:
  1. Uses the `storage` instance's `find_one` method to search for a document by its `_id`.
  2. If a document is found, converts the `_id` and `db_connection_id` fields to strings.
  3. Returns an `Instruction` object initialized with the document's data.

### `find_by(self, query: dict, page: int = 1, limit: int = 10) -> list[Instruction]`
Finds `Instruction` objects that match a given query, with pagination.
- **Parameters**:
  - `query`: A dictionary representing the query to find documents.
  - `page`: An integer representing the page number for pagination (default is 1).
  - `limit`: An integer representing the number of documents per page (default is 10).
- **Returns**: A list of `Instruction` objects.
- **Process**:
  1. Uses the `storage` instance's `find` method to search for documents with pagination.
  2. Converts the `_id` and `db_connection_id` fields of each document to strings.
  3. Initializes `Instruction` objects with the documents' data and appends them to a list.
  4. Returns the list of `Instruction` objects.

### `find_all(self, page: int = 0, limit: int = 0) -> list[Instruction]`
Finds all `Instruction` objects in the database, with optional pagination.
- **Parameters**:
  - `page`: An integer representing the page number for pagination (default is 0, which means no pagination).
  - `limit`: An integer representing the number of documents per page (default is 0, which means no limit).
- **Returns**: A list of `Instruction` objects.
- **Process**:
  1. Uses the `storage` instance's `find_all` method to retrieve all documents with optional pagination.
  2. Converts the `_id` and `db_connection_id` fields of each document to strings.
  3. Initializes `Instruction` objects with the documents' data and appends them to a list.
  4. Returns the list of `Instruction` objects.

### `delete_by_id(self, id: str) -> int`
Deletes an `Instruction` object by its ID.
- **Parameters**:
  - `id`: A string representing the `Instruction` object's ID.
- **Returns**: An integer indicating the number of documents deleted (should be 1 or 0).
- **Process**:
  1. Uses the `storage` instance's `delete_by_id` method to delete a document by its ID.
  2. Returns the result of the deletion operation.

## Usage
The `InstructionRepository` class is used to interact with the `instructions` collection in the database. It provides a high-level API for managing `Instruction` objects, abstracting away the details of the database operations. This class is typically used by other parts of the project that require data persistence for `Instruction` entities.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/database_connections.md

# DatabaseConnectionRepository Class

## Overview

The `DatabaseConnectionRepository` class is responsible for managing the persistence of `DatabaseConnection` objects within a MongoDB collection. It provides an abstraction layer over the direct database access, offering methods to insert, find, update, and list `DatabaseConnection` instances. The class ensures that the `DatabaseConnection` objects are properly serialized and deserialized when stored and retrieved from the database.

## Attributes

- `storage`: An instance of a storage class that provides methods for interacting with the MongoDB database.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the MongoDB collection where `DatabaseConnection` objects are stored.

## Methods

### `__init__(self, storage)`

The constructor initializes a new instance of the `DatabaseConnectionRepository` class.

#### Parameters

- `storage`: An instance of a storage class that provides methods for interacting with the MongoDB database.

### `insert(self, database_connection: DatabaseConnection) -> DatabaseConnection`

Inserts a new `DatabaseConnection` object into the MongoDB collection.

#### Parameters

- `database_connection`: An instance of `DatabaseConnection` to be inserted into the database.

#### Returns

- The `DatabaseConnection` object with its `id` attribute set to the MongoDB-generated `_id`.

### `find_one(self, query: dict) -> DatabaseConnection | None`

Finds a single `DatabaseConnection` object in the MongoDB collection that matches the given query.

#### Parameters

- `query`: A dictionary representing the MongoDB query used to find the object.

#### Returns

- A `DatabaseConnection` object if found, otherwise `None`.

### `update(self, database_connection: DatabaseConnection) -> DatabaseConnection`

Updates an existing `DatabaseConnection` object in the MongoDB collection or creates it if it does not exist.

#### Parameters

- `database_connection`: An instance of `DatabaseConnection` to be updated or created in the database.

#### Returns

- The `DatabaseConnection` object after the update.

### `find_by_id(self, id: str) -> DatabaseConnection | None`

Finds a `DatabaseConnection` object in the MongoDB collection by its `_id`.

#### Parameters

- `id`: A string representing the MongoDB `_id` of the `DatabaseConnection` object.

#### Returns

- A `DatabaseConnection` object if found, otherwise `None`.

### `find_all(self) -> list[DatabaseConnection]`

Retrieves all `DatabaseConnection` objects from the MongoDB collection.

#### Returns

- A list of `DatabaseConnection` objects.

## Exceptions

### `DatabaseConnectionNotFoundError`

A custom exception class that is raised when a `DatabaseConnection` object is not found in the database.

## Usage

The `DatabaseConnectionRepository` class is typically used by other components of the project that require access to `DatabaseConnection` objects stored in the database. It is instantiated with a storage object that knows how to interact with MongoDB. The repository methods are then used to perform CRUD operations on `DatabaseConnection` objects within the MongoDB collection named `database_connections`.

## Integration with MongoDB

The `DatabaseConnectionRepository` class interacts with MongoDB using the `storage` object's methods such as `insert_one`, `find_one`, `update_or_create`, and `find_all`. These methods abstract the actual MongoDB operations, allowing the repository to focus on the business logic related to `DatabaseConnection` objects.

## Serialization and Deserialization

When storing `DatabaseConnection` objects, the `dict` method is used to convert the object into a dictionary, excluding the `id` field, which is managed by MongoDB. When retrieving objects from the database, the class reconstructs `DatabaseConnection` instances from the dictionaries returned by the `storage` object, ensuring the `_id` field is converted to a string and assigned to the `id` attribute of the `DatabaseConnection` instance.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/sql_generations.md

# SQLGenerationRepository Class

## Overview

The `SQLGenerationRepository` class is a data access layer designed to interact with a database collection named `sql_generations`. It provides methods to insert, update, and retrieve `SQLGeneration` objects from the database. The class requires a `storage` object that handles the actual database operations.

## Attributes

- `storage`: An instance of a storage class that provides methods for interacting with the database.

## Methods

### `__init__(self, storage)`

The constructor initializes the `SQLGenerationRepository` with a given `storage` object.

#### Parameters

- `storage`: An object that provides the interface for database operations.

### `insert(self, sql_generation: SQLGeneration) -> SQLGeneration`

Inserts a new `SQLGeneration` object into the database.

#### Parameters

- `sql_generation`: An instance of `SQLGeneration` to be inserted into the database.

#### Returns

- The `SQLGeneration` object with its `id` attribute set to the newly created database entry's ID.

#### Process

1. Converts the `SQLGeneration` object to a dictionary, excluding the `id` field.
2. Converts the `prompt_id` attribute to a string.
3. Inserts the dictionary into the database using the `storage` object's `insert_one` method.
4. Sets the `id` attribute of the `SQLGeneration` object to the string representation of the inserted ID.
5. Returns the updated `SQLGeneration` object.

### `update(self, sql_generation: SQLGeneration) -> SQLGeneration`

Updates an existing `SQLGeneration` object in the database.

#### Parameters

- `sql_generation`: An instance of `SQLGeneration` to be updated in the database.

#### Returns

- The `SQLGeneration` object after the update operation.

#### Process

1. Converts the `SQLGeneration` object to a dictionary, excluding the `id` field.
2. Converts the `prompt_id` attribute to a string.
3. Updates the database entry identified by the `id` of the `SQLGeneration` object using the `storage` object's `update_or_create` method.
4. Returns the `SQLGeneration` object.

### `find_one(self, query: dict) -> SQLGeneration | None`

Finds a single `SQLGeneration` object in the database that matches the given query.

#### Parameters

- `query`: A dictionary representing the query to be used for finding the object.

#### Returns

- An instance of `SQLGeneration` if found, otherwise `None`.

#### Process

1. Uses the `storage` object's `find_one` method to retrieve a single document from the database that matches the query.
2. If a document is found, converts the `_id` field to a string and assigns it to the `id` attribute.
3. Returns an instance of `SQLGeneration` created from the retrieved document.

### `find_by_id(self, id: str) -> SQLGeneration | None`

Finds a `SQLGeneration` object in the database by its ID.

#### Parameters

- `id`: A string representing the ID of the `SQLGeneration` object to be retrieved.

#### Returns

- An instance of `SQLGeneration` if found, otherwise `None`.

#### Process

1. Uses the `storage` object's `find_one` method to retrieve a document from the database by its `_id`.
2. If a document is found, converts the `_id` field to a string and assigns it to the `id` attribute.
3. Returns an instance of `SQLGeneration` created from the retrieved document.

### `find_by(self, query: dict, page: int = 0, limit: int = 0) -> list[SQLGeneration]`

Finds a list of `SQLGeneration` objects in the database that match the given query, with optional pagination.

#### Parameters

- `query`: A dictionary representing the query to be used for finding the objects.
- `page`: An integer representing the page number for pagination (optional).
- `limit`: An integer representing the number of items per page for pagination (optional).

#### Returns

- A list of `SQLGeneration` instances that match the query.

#### Process

1. If both `page` and `limit` are greater than 0, uses the `storage` object's `find` method with pagination to retrieve documents from the database.
2. If pagination is not used, retrieves all documents that match the query.
3. Iterates over the retrieved documents, converts the `_id` field to a string, and assigns it to the `id` attribute.
4. Creates instances of `SQLGeneration` from the retrieved documents and appends them to a result list.
5. Returns the list of `SQLGeneration` instances.

## Exceptions

### `SQLGenerationNotFoundError`

A custom exception class that is raised when a `SQLGeneration` object is not found in the database.

## Constants

- `DB_COLLECTION`: A string representing the name of the database collection used by the repository (`"sql_generations"`).

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/golden_sqls.md

# GoldenSQLRepository Class

## Overview

The `GoldenSQLRepository` class provides an abstraction layer for interacting with a database collection named `golden_sqls`. It defines methods for inserting, finding, updating, and deleting `GoldenSQL` objects within the collection. The class is designed to work with a storage backend that is passed to it during initialization.

## Attributes

- `storage`: An instance of a storage class that provides methods for database operations such as `insert_one`, `find_one`, `update_or_create`, `find`, `find_all`, and `delete_by_id`.

## Methods

### `__init__(self, storage)`
Constructor for the `GoldenSQLRepository` class.

- **Parameters:**
  - `storage`: An instance of a storage class that will be used for database operations.

### `insert(self, golden_sql: GoldenSQL) -> GoldenSQL`
Inserts a new `GoldenSQL` object into the `golden_sqls` collection.

- **Parameters:**
  - `golden_sql`: An instance of `GoldenSQL` to be inserted into the database.
- **Returns:**
  - The `GoldenSQL` instance with its `id` attribute set to the newly created document's ID in the database.
- **Behavior:**
  - Converts the `GoldenSQL` instance to a dictionary, excluding the `id` field.
  - Inserts the dictionary into the `golden_sqls` collection.
  - Sets the `id` attribute of the `GoldenSQL` instance to the ID of the inserted document.

### `find_one(self, query: dict) -> GoldenSQL | None`
Finds a single `GoldenSQL` object in the `golden_sqls` collection that matches the given query.

- **Parameters:**
  - `query`: A dictionary representing the query to find the document.
- **Returns:**
  - A `GoldenSQL` instance if a matching document is found; otherwise, `None`.
- **Behavior:**
  - Uses the `storage.find_one` method to retrieve a single document from the `golden_sqls` collection.
  - Converts the document to a `GoldenSQL` instance if found.

### `update(self, golden_sql: GoldenSQL) -> GoldenSQL`
Updates an existing `GoldenSQL` object in the `golden_sqls` collection.

- **Parameters:**
  - `golden_sql`: An instance of `GoldenSQL` with updated values.
- **Returns:**
  - The updated `GoldenSQL` instance.
- **Behavior:**
  - Converts the `GoldenSQL` instance to a dictionary, excluding the `id` field.
  - Updates the corresponding document in the `golden_sqls` collection using the `storage.update_or_create` method.

### `find_by_id(self, id: str) -> GoldenSQL | None`
Finds a `GoldenSQL` object by its ID in the `golden_sqls` collection.

- **Parameters:**
  - `id`: The string representation of the document's ID.
- **Returns:**
  - A `GoldenSQL` instance if a document with the given ID is found; otherwise, `None`.
- **Behavior:**
  - Uses the `storage.find_one` method to retrieve the document by its ID.
  - Converts the document to a `GoldenSQL` instance if found.

### `find_by(self, query: dict, page: int = 1, limit: int = 10) -> list[GoldenSQL]`
Finds `GoldenSQL` objects that match a given query, with pagination support.

- **Parameters:**
  - `query`: A dictionary representing the query to find documents.
  - `page`: The page number for pagination (default is 1).
  - `limit`: The number of documents per page (default is 10).
- **Returns:**
  - A list of `GoldenSQL` instances that match the query.
- **Behavior:**
  - Uses the `storage.find` method to retrieve documents from the `golden_sqls` collection with pagination.
  - Converts each document to a `GoldenSQL` instance.

### `find_all(self, page: int = 0, limit: int = 0) -> list[GoldenSQL]`
Retrieves all `GoldenSQL` objects from the `golden_sqls` collection, with optional pagination.

- **Parameters:**
  - `page`: The page number for pagination (default is 0, which means no pagination).
  - `limit`: The number of documents per page (default is 0, which means no limit).
- **Returns:**
  - A list of all `GoldenSQL` instances in the collection.
- **Behavior:**
  - Uses the `storage.find_all` method to retrieve all documents from the `golden_sqls` collection with optional pagination.
  - Converts each document to a `GoldenSQL` instance.

### `delete_by_id(self, id: str) -> int`
Deletes a `GoldenSQL` object by its ID from the `golden_sqls` collection.

- **Parameters:**
  - `id`: The string representation of the document's ID.
- **Returns:**
  - The number of documents deleted (should be 1 or 0).
- **Behavior:**
  - Uses the `storage.delete_by_id` method to delete the document by its ID from the `golden_sqls` collection.

## Exceptions

### `GoldenSQLNotFoundError`
A custom exception class that can be raised when a `GoldenSQL` object is not found in the database.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the database collection (`"golden_sqls"`).

## Usage

The `GoldenSQLRepository` class is used to perform CRUD operations on `GoldenSQL` objects within a MongoDB collection. It is typically instantiated with a storage backend that conforms to the expected interface for database operations. The class methods allow for easy manipulation of `GoldenSQL` objects, abstracting away the direct database access and providing a clean API for the rest of the project to use.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/__init__.md

# `__init__.py` in `dataherald/repositories`

## Overview

The `__init__.py` file within the `dataherald/repositories` directory serves as an initialization script for the `repositories` package in the `dataherald` project. This file can be used to expose specific classes, functions, or variables from the package, making them directly accessible when the package is imported elsewhere in the project.

## Usage

When the `dataherald/repositories` package is imported, Python will execute the `__init__.py` file. The contents of this file determine which modules or symbols are available at the package level. For example, if the package contains multiple modules with repository classes, the `__init__.py` file could import these classes and assign them to variables that are then accessible directly from the `repositories` namespace.

## Structure

The `__init__.py` file can contain several types of statements:

- Import statements: These are used to import classes, functions, or other elements from modules within the `repositories` package. This allows users to access these elements directly from the `repositories` namespace without having to import them from their respective modules.

- `__all__` list: This is an optional list of strings defining which symbols will be exported when `from dataherald.repositories import *` is used. It is a way to control which symbols are made available to the importer.

- Initialization code: Any code that needs to be run during the package initialization can be placed here. This could include setting up logging, initializing connections, or other startup tasks.

- Package-level variables: Variables that are meant to be constants or configuration settings for the entire package can be defined here.

## Example

Below is a hypothetical example of what the `__init__.py` file might contain:

python
# Import specific repository classes from their respective modules
from .user_repository import UserRepository
from .product_repository import ProductRepository

# Define an __all__ list to control what is exported
__all__ = ['UserRepository', 'ProductRepository']

# Initialize package-level variables or settings
DEFAULT_PAGE_SIZE = 20

# Any initialization code that needs to run when the package is imported
def _initialize_logging():
    # Set up package-specific logging configuration
    pass

_initialize_logging()


In this example, when a user imports the `repositories` package with `from dataherald.repositories import *`, they will have access to `UserRepository` and `ProductRepository` without needing to know the specific modules they come from. The `DEFAULT_PAGE_SIZE` variable is also available at the package level, and the `_initialize_logging` function is called to set up logging for the package.

## Conventions

- The `__init__.py` file is often kept minimal to avoid complex package initialization that can lead to circular dependencies or other import issues.

- If the package is large with many modules, it is common to only import the most essential elements in the `__init__.py` file to keep the package namespace clean and avoid unnecessary imports.

- The use of the `__all__` list is optional and should be used judiciously to ensure that the namespace is not cluttered with symbols that are not meant to be public.

## Conclusion

The `__init__.py` file in the `dataherald/repositories` directory is a crucial component for package initialization and namespace management within the `dataherald` project. It dictates how the package is presented to the rest of the project and what components are readily available for use when the package is imported.

---



File Path: /workspaces/documentation-generator/generated_documentation/dataherald/repositories/prompts.md

# `prompts.py` Module Documentation

## Overview

The `prompts.py` module defines a `PromptRepository` class that provides an abstraction layer for interacting with a database collection named `prompts`. This class is responsible for performing CRUD (Create, Read, Update, Delete) operations on `Prompt` objects within the database. The module also defines a custom exception `PromptNotFoundError` for handling cases where a prompt is not found in the database.

## Dependencies

- `bson.objectid`: Used for handling MongoDB ObjectIds.
- `dataherald.types`: Contains the `Prompt` class definition which is a data type used throughout this module.

## Constants

- `DB_COLLECTION`: A string constant representing the name of the database collection used by the `PromptRepository` class.

## Classes

### `PromptNotFoundError`

A custom exception class that inherits from Python's base `Exception` class. This exception is raised when a prompt cannot be found in the database.

### `PromptRepository`

A repository class that provides methods to interact with the `prompts` collection in the database.

#### Attributes

- `storage`: An instance of a storage class that provides low-level database operations. It is expected to have methods like `insert_one`, `find_one`, `find`, and `update_or_create`.

#### Methods

##### `__init__(self, storage)`

The constructor for the `PromptRepository` class.

- Parameters:
  - `storage`: An instance of a storage class that will be used to perform database operations.

##### `insert(self, prompt: Prompt) -> Prompt`

Inserts a new `Prompt` object into the database.

- Parameters:
  - `prompt`: An instance of the `Prompt` class to be inserted into the database.
- Returns:
  - The `Prompt` instance with its `id` attribute set to the newly created ObjectId in string format.

##### `find_one(self, query: dict) -> Prompt | None`

Finds a single `Prompt` object in the database that matches the given query.

- Parameters:
  - `query`: A dictionary representing the query to be used for finding a prompt.
- Returns:
  - A `Prompt` instance if a matching document is found, otherwise `None`.

##### `find_by_id(self, id: str) -> Prompt | None`

Finds a single `Prompt` object in the database by its ObjectId.

- Parameters:
  - `id`: A string representation of the ObjectId of the prompt to be found.
- Returns:
  - A `Prompt` instance if a matching document is found, otherwise `None`.

##### `find_by(self, query: dict, page: int = 0, limit: int = 0) -> list[Prompt]`

Finds all `Prompt` objects that match the given query, with optional pagination.

- Parameters:
  - `query`: A dictionary representing the query to be used for finding prompts.
  - `page`: An integer representing the page number for pagination (optional).
  - `limit`: An integer representing the number of items per page for pagination (optional).
- Returns:
  - A list of `Prompt` instances that match the query.

##### `update(self, prompt: Prompt) -> Prompt`

Updates an existing `Prompt` object in the database.

- Parameters:
  - `prompt`: An instance of the `Prompt` class with updated values.
- Returns:
  - The `Prompt` instance that was updated.

## Usage

The `PromptRepository` class is used to manage `Prompt` objects in a MongoDB database. It provides a high-level interface for other parts of the project to perform database operations without needing to directly interact with the database or write raw queries. The class methods handle the conversion between `Prompt` instances and their dictionary representations suitable for database storage, as well as the translation of MongoDB ObjectIds to and from string format.

---



