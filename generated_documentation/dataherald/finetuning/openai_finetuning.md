```markdown
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
```