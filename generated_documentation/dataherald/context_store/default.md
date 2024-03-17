```markdown
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
```
