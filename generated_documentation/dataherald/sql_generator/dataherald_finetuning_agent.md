```markdown
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
```