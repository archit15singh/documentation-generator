```markdown
## WeaviateExperiment Class

### Description
The `WeaviateExperiment` class is designed to facilitate experiments with Weaviate, a vector search engine. It allows for testing different vectorizers or querying functions by querying from an existing class or creating and populating a new class within Weaviate. The class provides functionality to insert data objects, define classes with specific properties and vector index configurations, and execute text-based queries using various query builders.

### Initialization Parameters
- `client`: A `weaviate.Client` instance for interacting with the Weaviate server.
- `class_name`: A string representing the name of the Weaviate class to be used or created.
- `use_existing_data`: A boolean indicating whether to use existing data (`True`) or to insert new data objects (`False`).
- `property_names`: A list of strings specifying the property names in the Weaviate class for the experiment.
- `text_queries`: A list of strings containing text queries for retrieval.
- `query_builders`: An optional dictionary mapping string names to Callable functions that construct Weaviate query objects. Defaults to a built-in query function.
- `vectorizers_and_moduleConfigs`: An optional list of tuples, each containing a vectorizer name and its corresponding moduleConfig as a dictionary, used during data insertion.
- `property_definitions`: An optional list of dictionaries defining properties for the Weaviate class, used during data insertion.
- `data_objects`: An optional list of dictionaries representing data objects to be inserted into Weaviate.
- `distance_metrics`: An optional list of strings specifying distance metrics for generating vectorIndexConfig.
- `vectorIndexConfigs`: An optional list of dictionaries specifying vectorIndexConfig for defining the class object.

### Methods
- `initialize`: A class method that sets up the experiment with given test and frozen parameters.
- `prepare`: Prepares argument combinations for the experiment by taking the cartesian product of all inputs.
- `run`: Executes the experiment, performing queries and optionally creating and populating a Weaviate class.
- `_construct_result_dfs`: Constructs DataFrames containing input arguments, results, and evaluation metrics.

### Usage Notes
- If `use_existing_data` is `False`, the class will be created and populated with `data_objects`.
- Either `distance_metrics` or `vectorIndexConfigs` should be provided, not both.
- Custom `query_builder` functions should accept the same parameters as the default one.

### Internal Functions
- `_generate_vectorIndexConfigs`: Generates a vectorIndexConfig dictionary based on a given distance metric.
- `weaviate_completion_fn`: Helper function to make a query request to Weaviate.
- `_extract_responses`: Extracts relevant objects from the Weaviate response.

### Exceptions
- Raises `ModuleNotFoundError` if the `weaviate` package is not installed.
- Raises `RuntimeError` for invalid parameter combinations or missing required parameters.

### Example
```python
# Assuming `weaviate_client` is a weaviate.Client instance and other required parameters are defined
experiment = WeaviateExperiment(
    client=weaviate_client,
    class_name="MyClass",
    use_existing_data=False,
    property_names=["name", "description"],
    text_queries=["search term"],
    query_builders={"default": default_query_builder},
    vectorizers_and_moduleConfigs=[("text2vec-contextionary", {})],
    property_definitions=[{"name": "name", "dataType": ["string"]}, {"name": "description", "dataType": ["text"]}],
    data_objects=[{"name": "Object1", "description": "A description of object 1"}],
    distance_metrics=["cosine"]
)
experiment.run(runs=3)
```
```