```markdown
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
```