```markdown
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
```
