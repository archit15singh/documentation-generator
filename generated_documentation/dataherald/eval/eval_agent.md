```markdown
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
```python
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
```
```