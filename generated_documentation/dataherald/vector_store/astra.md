```markdown
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
```