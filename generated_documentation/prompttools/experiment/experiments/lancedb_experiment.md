```markdown
## LanceDBExperiment Class

### Overview
The `LanceDBExperiment` class is designed to perform experiments using `LanceDB`, a database system that supports embedding-based search. It allows testing different embedding functions or retrieval arguments by querying from an existing table or creating a new one and inserting documents into it during the experiment.

### Initialization
The class is initialized with the following parameters:

- `embedding_fns`: A dictionary mapping names to embedding functions to be tested in the experiment.
- `query_args`: A dictionary where each key is a parameter name and each value is a list of values for that parameter. All possible combinations of these parameters will be used to query the table.
- `uri`: The URI to interact with the LanceDB database. Defaults to `"lancedb"`.
- `table_name`: The name of the table to get or create. Defaults to `"table"`.
- `use_existing_table`: A boolean indicating whether to use an existing table or create a new one. Defaults to `False`.
- `data`: An optional list of dictionaries representing documents or embeddings to be added to a newly created table.
- `text_col_name`: The name of the text column in the table. Defaults to `"text"`.
- `clean_up`: A boolean indicating whether to drop the table after the experiment ends. Defaults to `False`.

### Methods

#### `prepare`
Prepares the experiment by generating all possible combinations of query arguments.

#### `run`
Executes the experiment with the specified number of runs. It performs the following steps:
1. Constructs a DataFrame to hold input arguments.
2. Iterates over each embedding function and query argument combination.
3. If `use_existing_table` is `True`, opens the existing table; otherwise, creates a new table and inserts data.
4. Queries the table using the `lancedb_completion_fn` method.
5. Measures the latency of each query.
6. Optionally drops the table if `clean_up` is `True`.
7. Constructs result DataFrames using the `_construct_result_dfs` method.

#### `lancedb_completion_fn`
A wrapper function that calls the `query_builder` function with the provided table, embedding function, and additional keyword arguments.

#### `_construct_result_dfs`
Constructs several DataFrames containing all relevant data, such as input arguments, results, and evaluation metrics. It creates the following DataFrames:
- `input_arg_df`: Contains all input arguments.
- `dynamic_input_arg_df`: Contains input arguments with more than one unique value.
- `response_df`: Contains the extracted response, including top document IDs, distances, and documents.
- `result_df`: Contains everything returned by the completion function.
- `score_df`: Contains computed metrics, such as latency.
- `partial_df`: Contains some input arguments, extracted responses, and scores.
- `full_df`: Contains all input arguments, responses, and scores.

#### Helper Functions
- `_extract_top_doc_ids`: Extracts the top document IDs from the LanceDB output.
- `_extract_lancedb_dists`: Extracts the distances between documents from the LanceDB output.
- `_extract_lancedb_docs`: Extracts the documents from the LanceDB output.

### Usage
The `LanceDBExperiment` class is used to conduct experiments with LanceDB. It requires the `lancedb` package to be installed. The class can be used to evaluate the performance of different embedding functions and query parameters by measuring latency and analyzing the results of embedding-based searches.

### Exceptions
- Raises `ModuleNotFoundError` if the `lancedb` package is not installed.
- Raises `RuntimeError` if there is a conflict between `use_existing_table` and `data` parameters or if the specified table does not exist when expected to.

### Query Builder Function
The `query_builder` function is used to construct a query for LanceDB. It takes the following parameters:
- `table`: The LanceDB table to query.
- `embed_fn`: The embedding function to use for the query.
- `text`: The text to query.
- `metric`: The distance metric to use. Defaults to `"cosine"`.
- `limit`: The number of results to return. Defaults to `3`.
- `filter`: An optional filter to apply to the query.
- `nprobes`: An optional parameter for the number of probes to use (not used by default).
- `refine_factor`: An optional parameter for the refine factor (not used by default).

It constructs a query using the provided parameters and returns the results as a DataFrame.

### Notes
- The `VALID_TASKS` list is currently empty and not used in the provided code.
- The `query_builder` function warns if `nprobes` or `refine_factor` are provided since they are not used by default.
```