```markdown
# MindsDBExperiment Class

## Overview
`MindsDBExperiment` is a subclass of `Experiment` designed to conduct experiments with MindsDB, a predictive database layer for existing databases. It is used to test different combinations of SQL queries and parameters to evaluate the performance and responses of MindsDB.

## Attributes
- `cursor`: A database cursor object obtained from the `db_connector` to execute SQL queries.
- `completion_fn`: A function reference that points to `mindsdb_completion_fn` by default or `mock_mindsdb_completion_fn` if debugging.
- `call_params`: A dictionary containing the `prompt` parameter extracted from `kwargs`.
- `model_params`: A dictionary containing all parameters from `kwargs` except for `prompt`.
- `all_args`: A dictionary that merges `model_params` and `call_params`.
- `model_argument_combos`: A list of dictionaries representing all possible combinations of model parameters.
- `call_argument_combos`: A list of dictionaries representing all possible combinations of call parameters.

## Methods

### `__init__(db_connector: "CMySQLConnection", **kwargs: Dict[str, object])`
Constructor for the `MindsDBExperiment` class.
- Initializes the database cursor.
- Sets the completion function based on the `DEBUG` environment variable.
- Separates `kwargs` into `call_params` and `model_params`.
- Calls the superclass constructor.

### `prepare() -> None`
Prepares the experiment by creating cartesian products of model and call parameters to form `model_argument_combos` and `call_argument_combos`.

### `mindsdb_completion_fn(**params: Dict[str, Any]) -> List[Any]`
A helper function that executes a SQL query using the provided `prompt` parameter and returns the results as a list.
- Executes the SQL query using the cursor.
- Returns the results of the query.

### `run(runs: int = 1) -> None`
Executes the experiment by running each combination of arguments for a specified number of `runs`.
- Prepares argument combinations if not already done.
- Iterates over each combination of model and call arguments.
- Formats the `prompt` with the current model arguments.
- Executes the completion function for the number of specified `runs`.
- Measures the latency for each call.
- Appends the results and argument combinations to the respective lists.
- Constructs result dataframes with the collected data.
- Raises `PromptExperimentException` if no results are obtained.

### `_extract_responses(output: List[Dict[str, object]]) -> Tuple[str]`
A static method to extract responses from the output list.
- Returns the first element of the output list.

## Usage
The `MindsDBExperiment` class is instantiated with a `CMySQLConnection` object and keyword arguments representing the parameters for the MindsDB model and SQL prompts. The `run` method is then called to execute the experiment, which will generate and test various combinations of SQL queries and parameters, collecting performance metrics and responses for analysis.

## Exceptions
- `PromptExperimentException`: Raised if no results are obtained during the `run` method execution.

## Dependencies
- `os`: To access environment variables.
- `typing`: For type annotations.
- `itertools`: To create cartesian products of parameters.
- `time`: To measure execution latency.
- `logging`: For logging information and errors.
- `mysql.connector.connection_cext`: To import `CMySQLConnection` for database connectivity.
- `prompttools.mock.mock`: To import `mock_mindsdb_completion_fn` for debugging purposes.
- `experiment`: To inherit from the `Experiment` class.
- `error`: To raise `PromptExperimentException`.

## Notes
- The `TODO` comment suggests that the execution of combinations could be improved by using an asynchronous queue.
- The `run` method currently executes synchronously and could be a bottleneck if the number of combinations or runs is large.
- The `mindsdb_completion_fn` is designed to work with SQL queries, and the output is expected to be a list of database rows.
```