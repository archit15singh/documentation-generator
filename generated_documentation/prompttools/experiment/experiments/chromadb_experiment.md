```markdown
## ChromaDBExperiment Class

### Description
`ChromaDBExperiment` is a class that extends the `Experiment` class, designed to perform experiments with `ChromaDB`. It allows testing different embedding functions or retrieval arguments by querying from an existing collection or creating and inserting documents into a new one during the experiment. The class handles the setup, execution, and cleanup of the experiment, including the creation and deletion of collections if necessary.

### Initialization
The `__init__` method initializes the `ChromaDBExperiment` instance with the following parameters:

- `chroma_client`: An instance of `chromadb.Client` used to interact with the ChromaDB database.
- `collection_name`: A string representing the name of the collection to query or create.
- `use_existing_collection`: A boolean indicating whether to use an existing collection or create a new one.
- `query_collection_params`: A dictionary where each key is a string representing a query parameter and each value is a list of possible values for that parameter.
- `embedding_fns`: A list of callables representing embedding functions to test in the experiment. Defaults to the default embedding function in ChromaDB if available.
- `embedding_fn_names`: A list of strings representing the names of the embedding functions.
- `add_to_collection_params`: An optional dictionary containing documents or embeddings to add to a newly created collection.

### Methods

#### `initialize`
A class method that sets up the experiment with test and frozen parameters. It ensures that required parameters are frozen and not included in the test parameters.

#### `chromadb_completion_fn`
A helper function that makes a query request to a `chromadb.api.Collection` instance using the provided query parameters.

#### `prepare`
Prepares the argument combinations for the experiment by taking the cartesian product of all input parameters.

#### `run`
Executes the experiment with the prepared argument combinations. It performs the following steps:
1. Constructs a DataFrame table for input arguments.
2. Iterates over the embedding functions and argument combinations.
3. Creates or retrieves a collection based on `use_existing_collection`.
4. Adds documents to the collection if a new one is created.
5. Executes queries using the `chromadb_completion_fn`.
6. Measures the latency of each query.
7. Constructs result DataFrames after all queries are executed.
8. Cleans up by deleting the collection if it was created during the experiment.

#### `_construct_result_dfs`
Constructs several pandas DataFrames containing all relevant data, such as input arguments, results, and evaluation metrics. It extracts the most relevant objects returned by ChromaDB and organizes them into DataFrames for analysis.

#### `_extract_top_doc_ids`
A static helper function to extract the top document IDs from the ChromaDB query output.

#### `_extract_chromadb_dists`
A static helper function to extract the distances between the query prompt and documents from the ChromaDB query output.

#### `_extract_chromadb_docs`
A static helper function to extract the top documents from the ChromaDB query output.

### Usage
The `ChromaDBExperiment` class is used to conduct experiments with ChromaDB by testing different embedding functions and retrieval parameters. It is instantiated with the necessary parameters and then the `run` method is called to execute the experiment. The results are stored in DataFrames for further analysis.

### Error Handling
The class includes error handling to ensure that:
- The `chromadb` package is installed.
- The lengths of `embedding_fns` and `embedding_fn_names` are aligned.
- The user does not attempt to use an existing collection and create a new one simultaneously.
- If a new collection is created, documents are added to it.

### Environment Variables
The class checks for the `DEBUG` environment variable to determine whether to use the actual `chromadb_completion_fn` or a mock function for testing purposes.

### Cleanup
If a new collection is created during the experiment, it is automatically deleted at the end of the `run` method to clean up resources.
```