```markdown
# PineconeExperiment Class

## Overview

`PineconeExperiment` is a class derived from `Experiment` that facilitates the execution of experiments using the Pinecone service. Pinecone is a vector database used for similarity search and machine learning applications. This class allows users to test different embedding functions or retrieval arguments by querying an existing Pinecone collection or creating a new one. If a new collection is created, it is automatically cleaned up at the end of the experiment.

## Initialization

The `__init__` method initializes the `PineconeExperiment` instance with the following parameters:

- `index_name` (str): The name of the Pinecone index to use or create.
- `use_existing_index` (bool): A flag indicating whether to use an existing index or create a new one.
- `query_index_params` (dict[str, list]): A dictionary where each key is a parameter name and each value is a list of parameter values. These are used to query the Pinecone index with all possible combinations of parameters.
- `create_index_params` (Optional[dict]): Configuration for creating a new index, such as the number of dimensions and the distance function.
- `data` (Optional[list]): A list of documents or embeddings to add to the newly created index.

The constructor checks for the presence of the `pinecone` module and initializes the Pinecone client with the API key and environment variables. It also validates the input parameters to ensure that they are consistent with the intended use of the class.

## Methods

### pinecone_completion_fn

This method is a helper function that sends a query to the Pinecone index and returns the result.

### prepare

The `prepare` method generates all possible combinations of query parameters by taking the Cartesian product of the values provided in `query_index_params`.

### _batch_upsert

A static method that performs batch upsert operations on the Pinecone index. It inserts documents in batches of 100 to optimize the insertion process.

### _wait_for_eventual_consistency

A static method that waits for Pinecone's eventual consistency after inserting data. It checks the total vector count and waits until it matches the expected number of samples.

### run

The `run` method executes the experiment by performing the following steps:

1. Prepares the argument combinations if not already done.
2. Inserts data into the Pinecone index if a new index is being created.
3. Waits for eventual consistency if a new index is created.
4. Queries the Pinecone index with each combination of arguments.
5. Measures the latency of each query.
6. Deletes the Pinecone index if a new index was created.
7. Constructs result DataFrames with input arguments, results, and latencies.

### _construct_result_dfs

This method constructs several pandas DataFrames that contain all relevant data from the experiment, including input arguments, results, and evaluation metrics. It extracts the most relevant objects returned by Pinecone and organizes them into DataFrames for analysis.

### _extract_top_doc_ids

A static helper function that extracts the top document IDs from the Pinecone query response.

### _extract_pinecone_scores

A static helper function that extracts the scores of documents from the Pinecone query response.

### _extract_pinecone_docs

A static helper function that extracts the top documents from the Pinecone query response.

## Usage

To use the `PineconeExperiment` class, one must instantiate it with the appropriate parameters and then call the `run` method to execute the experiment. The class handles the creation and deletion of the Pinecone index, insertion of data, querying, and result aggregation.

## Error Handling

The class includes error handling to ensure that the Pinecone client is properly initialized and that the input parameters are valid. It raises exceptions if the `pinecone` module is not installed, if both an existing index is specified and new index parameters are provided, or if a new index is to be created without providing data.

## Dependencies

The class depends on the `pinecone-client` package, which must be installed separately. It also uses the `pandas` library for data manipulation and the `itertools` and `logging` modules from the Python standard library.
```