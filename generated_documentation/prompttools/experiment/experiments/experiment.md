```markdown
## Experiment Class

### Overview

The `Experiment` class serves as a base class for conducting experiments with various parameters and models. It is designed to be subclassed for specific types of experiments, such as those involving language models or image processing. The class provides methods for initializing experiments, preparing argument combinations, running the experiments, constructing result dataframes, visualizing results, evaluating metrics, and exporting results.

### Initialization

- `__init__`: Initializes the `Experiment` object, setting up a `RequestQueue` for managing requests and initializing various instance variables. Optionally sends a message to Sentry if not opted out.
- `initialize`: Class method to initialize an experiment with specified test and frozen parameters, allowing for easy setup without wrapping parameters in lists.

### Experiment Setup

- `prepare`: Creates argument combinations by taking the cartesian product of all input arguments.
- `_is_chat`: Static method that returns `False`, indicating the default experiment type is not a chat-based experiment.

### Running Experiments

- `run`: Executes the experiment for every combination of arguments, a specified number of times. It constructs result dataframes for further analysis.
- `_construct_result_dfs`: Constructs DataFrames containing input arguments, results, latencies, and other metrics from the experiment's run.

### Result Visualization and Retrieval

- `get_table`: Retrieves a DataFrame containing either a subset of columns for visualization or all columns for full results.
- `visualize`: Visualizes the experiment results in a notebook or logs them, depending on the environment. Supports image visualization if `image_experiment` is `True`.
- `cv2_image_to_base64`: Converts an OpenCV image to a base64-encoded string.
- `display_image_html`: Returns an HTML string for displaying an image in a notebook.

### Evaluation and Feedback

- `evaluate`: Computes a new metric column using an evaluation function and updates the result DataFrames.
- `_update_score`: Updates the score DataFrame with new metric results.
- `pivot_table`: Returns a pivoted DataFrame based on specified pivot columns and response value name.
- `aggregate`: Aggregates a metric for a given column and displays the results to the user.
- `rank`: Groups data by a specified column to get scores and sorts them in descending order.

### Data Export

- `to_csv`: Exports the results to a CSV file.
- `to_pandas_df`: Returns the results as a pandas DataFrame.
- `to_json`: Exports the results to a JSON file.
- `to_lora_json`: Exports the results to a LoRA-format JSON file for fine-tuning.
- `to_mongo_db`: Inserts the results into a MongoDB collection for persistence.
- `to_markdown`: Converts the results DataFrame to a markdown table format.

### Utility Methods

- `_extract_responses`: Abstract static method that should be implemented by subclasses to extract responses from model outputs.
- `_get_model_names`: Placeholder method to be implemented by subclasses.
- `_get_prompts`: Placeholder method to be implemented by subclasses.
- `_get_state`: Abstract method that should be implemented by subclasses to retrieve the state of the experiment.
- `_load_state`: Abstract class method that should be implemented by subclasses to load the state of an experiment.

### Notes

- The class contains several commented-out sections related to feedback and comparison widgets, which are not active in the current implementation.
- The class relies on external libraries such as `pandas`, `itertools`, `logging`, `IPython`, `tabulate`, `sentry_sdk`, `cv2`, and `pymongo`, some of which are optional and must be installed separately.
- The class is designed to be used in an interactive environment, such as Jupyter notebooks, but also supports non-interactive usage.
- The class handles image experiments differently, with additional methods for image conversion and display.
- The class provides methods for exporting results in various formats, including CSV, JSON, LoRA JSON, MongoDB, and markdown, to accommodate different use cases and persistence needs.
- The class is not intended to be used directly but should be subclassed for specific experiment types, with certain methods implemented or overridden as needed.
```