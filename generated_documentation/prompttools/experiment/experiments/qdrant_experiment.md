```markdown
# QdrantExperiment Class

## Overview

The `QdrantExperiment` class is a subclass of `Experiment` designed to facilitate the testing and benchmarking of vector search queries using the Qdrant vector database. It provides methods to prepare a collection of documents, vectorize them, run queries, and collect performance metrics.

## Dependencies

- `itertools`: Used for creating combinations of parameters.
- `json`: Used for handling JSON data structures.
- `logging`: Used for logging information during the experiment.
- `os`: Used for environment variable access.
- `time`: Used for adding delays during indexing.
- `warnings`: Used for issuing warnings about potential issues.
- `collections.defaultdict`: Used for creating nested dictionaries.
- `typing`: Provides type hints for function signatures and variables.
- `prompttools.experiment.experiments.error.PromptExperimentException`: Custom exception class for experiment errors.
- `prompttools.mock.mock.mock_qdrant_fn`: Mock function for Qdrant completion.
- `qdrant_client`: Optional dependency for Qdrant client functionality.

## Class Attributes

- `DEFAULT_DISTANCE`: A class-level attribute that sets the default distance metric for vector comparisons to "Cosine".

## Initialization

The `__init__` method initializes the experiment with the following parameters:

- `client`: An instance of `qdrant_client.QdrantClient` used to interact with the Qdrant service.
- `collection_name`: The name of the collection to be used in Qdrant.
- `embedding_fn`: A function that converts a document into a vector embedding.
- `vector_size`: The size of the vector embeddings.
- `documents`: An iterable of documents to be indexed and searched.
- `queries`: An iterable of query strings to be used in the search.
- `collection_params`: Optional dictionary of parameters for collection configuration.
- `query_params`: Optional dictionary of parameters for query configuration.

The method checks for the presence of the `qdrant_client` module and raises a `ModuleNotFoundError` if it is not installed. It also sets up the collection parameters, ensuring the vector size is correctly configured and the distance metric is set if not provided by the user. If the `DEBUG` environment variable is set, a mock Qdrant function is used instead of the actual Qdrant client.

## Class Methods

- `initialize`: A class method that takes `test_parameters` and `frozen_parameters` dictionaries to create an instance of `QdrantExperiment`. It ensures that required parameters are frozen and not included in the test parameters.

## Instance Methods

- `qdrant_completion_fn`: Executes a search query against the Qdrant collection and returns the results.
- `prepare`: Vectorizes the documents and queries, and prepares combinations of collection and query parameters for testing.
- `run`: Executes the experiment by creating a collection, uploading documents, waiting for indexing, running queries, and collecting results. It also handles cleanup by deleting the collection after the experiment.
- `run` also uses the `_create_nested_object` method to transform flat dictionaries into nested objects based on keys containing double underscores, which is necessary for Qdrant's configuration format.
- `_extract_responses`: Static method that extracts document payloads from the search results.
- `_create_nested_object`: Static method that converts a flat dictionary with double underscore-separated keys into a nested dictionary structure suitable for Qdrant's API.

## Usage

The `QdrantExperiment` class is used to conduct experiments on vector search performance using the Qdrant vector database. It requires a Qdrant client instance and an embedding function to convert text documents into vector embeddings. The class handles the creation and deletion of collections, indexing of documents, running of search queries, and collection of performance metrics.

## Example

To use the `QdrantExperiment` class, one would typically:

1. Instantiate the class with the required parameters, including a Qdrant client, collection name, embedding function, vector size, documents, and queries.
2. Call the `prepare` method to vectorize documents and prepare parameter combinations.
3. Call the `run` method with the desired number of runs to execute the experiment and collect results.

```python
# Example usage
client = qdrant_client.QdrantClient(...)
embedding_fn = lambda text: [0.0] * 128  # Dummy embedding function
documents = ["doc1", "doc2", "doc3"]
queries = ["query1", "query2"]

experiment = QdrantExperiment(
    client=client,
    collection_name="my_collection",
    embedding_fn=embedding_fn,
    vector_size=128,
    documents=documents,
    queries=queries
)

experiment.prepare()
experiment.run(runs=5)
```

This example would create a Qdrant collection, index the provided documents, run the queries five times each, and then delete the collection.
```