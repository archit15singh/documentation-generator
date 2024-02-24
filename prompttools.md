File Path: /workspaces/documentation-generator/generated_documentation/prompttools/sentry.md

# Sentry Integration Module (`sentry.py`)

## Overview

The `sentry.py` module is responsible for integrating Sentry, an error tracking and performance monitoring tool, into the project. Sentry helps developers monitor and fix crashes in real time. The module is designed to be configurable via environment variables and includes mechanisms to protect user privacy by filtering out personal information from the reports.

## Dependencies

- `sentry_sdk`: The official Sentry SDK for Python.
- `os`: Standard Python module to interact with the operating system.
- `platform`: Standard Python module to retrieve as much platform-identifying data as possible.
- `uuid`: Standard Python module to generate unique identifiers.
- `hashlib`: Standard Python module that implements a common interface to many different secure hash and message digest algorithms.

## Constants

- `SENTRY_DSN`: A string containing the Data Source Name (DSN) that uniquely identifies the Sentry project to which events and performance data should be sent.

## Functions

### `find_certifi_path()`

Locates the path to the `cacert.pem` file provided by the `certifi` package. This is used to ensure that the Sentry SDK can securely communicate with the Sentry server over HTTPS, especially on macOS systems where there may be issues with CA certificates.

#### Returns

- The path to the `cacert.pem` file as a string, or `None` if the `certifi` package is not found or an error occurs.

### `filter_info(event, _hint)`

A callback function used by the Sentry SDK to filter out personal information from events before they are sent to Sentry.

#### Parameters

- `event`: A dictionary containing the event data that will be sent to Sentry.
- `hint`: Additional information provided by the Sentry SDK about the event.

#### Returns

- The modified `event` dictionary with personal information fields set to `None`.

### `init_sentry()`

Initializes the Sentry SDK with the project's DSN and various configuration options. It also writes a `.token` file containing a hashed machine identifier to the user's home directory or a temporary directory. This function checks for the `SENTRY_OPT_OUT` environment variable, and if it is not set, proceeds with the initialization.

#### Sentry SDK Initialization Options

- `dsn`: The Sentry DSN to which events and performance data will be sent.
- `release`: The version of the application, obtained from the `version` module.
- `traces_sample_rate`: The rate at which transaction and performance data is sampled. Set to `0.01`.
- `include_local_variables`: Whether to include local variables in stack traces. Set to `False`.
- `send_default_pii`: Whether to send personally identifiable information. Set to `False`.
- `attach_stacktrace`: Whether to attach stack traces to messages. Set to `False`.
- `before_send`: A callback function that filters out personal information from events.
- `include_source_context`: Whether to include source code context in stack traces. Set to `False`.
- `profiles_sample_rate`: The rate at which profiling data is sampled. Set to `0.0`.

#### Side Effects

- Sets the `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` environment variables on macOS systems to the path of the `cacert.pem` file if they are not already set.
- Writes a `.token` file to the user's home directory or a temporary directory, containing a hashed machine identifier.

#### Sentry Message Capture

After initialization, the function captures a message with the level "info" indicating that the "prompttools" are being initialized.

## Usage

To use this module in a project, it should be imported and the `init_sentry()` function should be called during the application's startup sequence. The module will automatically configure Sentry based on the environment and the provided DSN, and will start capturing errors and performance data according to the specified sample rates.

## Privacy Considerations

The module includes a mechanism to opt-out of data collection by setting the `SENTRY_OPT_OUT` environment variable. Additionally, the `filter_info` function ensures that no personal information is sent to Sentry by clearing potentially sensitive fields from the event data.

## Platform-Specific Behavior

The module contains specific code paths for macOS and Windows systems to handle platform-specific issues, such as CA certificate configuration on macOS and file path handling on Windows.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/version.md

# `version.py` Module

## Overview

The `version.py` module is a part of the `prompttools` package located within the `documentation-generator` project. This module defines the version information for the `prompttools` package, which includes both the semantic version and the Git commit hash that corresponds to the source code state at the time of the version's release.

## Details

### Variables

- `__version__`: A string that represents the semantic version of the `prompttools` package. The semantic version follows the [Semantic Versioning 2.0.0](https://semver.org/) specification. The version string is composed of three numerical components separated by dots (`major.minor.patch`), followed by an optional pre-release identifier and build metadata.

  - `major`: The first digit in the version string, indicating the major version. Changes in the major version typically indicate backward-incompatible API changes.
  - `minor`: The second digit, representing the minor version. This is incremented when new, backward-compatible functionality is introduced.
  - `patch`: The third digit, indicating the patch version. This is incremented with backward-compatible bug fixes.
  - `pre-release identifier`: An optional alphanumeric identifier that follows the patch version, starting with a hyphen (e.g., `alpha`, `beta`, `rc` for release candidate). In this case, `45a0` indicates a pre-release version.
  - `build metadata`: Optional metadata following a plus sign, which can include information like the build number or a commit hash. Here, `6151062` is likely a reference to the build or commit hash.

- `git_version`: A string containing the full Git commit hash that the source code corresponds to. This hash can be used to identify the exact state of the source code in the version control system (Git) at the time the version was released.

### Usage

The `version.py` module is typically used in the following ways:

1. **Package Metadata**: The `__version__` variable is used as the version number in the package's metadata, which is often defined in `setup.py` or `pyproject.toml` for Python projects. This metadata is used by package managers like `pip` to manage the installation and dependencies of the package.

2. **Version Display**: The `__version__` variable can be used to display the current version of the `prompttools` package to the user, often through a command-line interface (CLI) or a graphical user interface (GUI).

3. **Release Management**: The `__version__` and `git_version` variables are used during the release process to tag the repository with the current version number and to ensure that the source code matches the distributed package.

4. **Dependency Resolution**: When other packages or projects list `prompttools` as a dependency, they may specify a particular version or range of versions using the `__version__` string. This ensures compatibility and predictable behavior.

5. **Debugging and Support**: The `git_version` variable is particularly useful for debugging purposes. If an issue arises, developers can use the commit hash to check out the exact state of the codebase that corresponds to the version in use.

6. **Continuous Integration/Continuous Deployment (CI/CD)**: In automated build and deployment pipelines, the `__version__` and `git_version` variables can be used to tag Docker images, create release notes, and track which version of the code is deployed to different environments.

## File Location

The `version.py` file is located at the following path within the project's directory structure:


/workspaces/documentation-generator/target_code/prompttools/version.py


This path indicates that the file is part of the `target_code` directory under the `prompttools` package within the `documentation-generator` workspace.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/common.md

# Common Configuration Module

## Overview

The `common.py` module is part of the `prompttools` package within the `documentation-generator` project. It serves as a configuration utility that sets up environment-specific variables for the rest of the project. This module is responsible for loading environment variables from a `.env` file and defining the `HEGEL_BACKEND_URL` based on the current environment.

## Dependencies

- `os`: A standard Python module that provides a portable way of using operating system-dependent functionality.
- `os.path`: A submodule of `os` that provides a way of manipulating file paths.
- `dotenv`: An optional third-party package that loads environment variables from a `.env` file into `os.environ`.

## Environment Variable Loading

The module attempts to import `load_dotenv` from the `dotenv` package. If the import fails (e.g., if `dotenv` is not installed), `load_dotenv` is set to `None`.

If `load_dotenv` is available, the module constructs a path to the `.env` file by joining the directory name two levels up from the current file (`__file__`) with the `.env` filename. This path is then used to load the environment variables from the `.env` file into the system environment variables.

## Environment Configuration

The module defines a variable `ENV` that fetches the value of the environment variable `ENV` from the system environment variables, defaulting to `"prod"` if it is not set.

Based on the value of `ENV`, the module sets the `HEGEL_BACKEND_URL` variable:

- If `ENV` is equal to `"development"`, `HEGEL_BACKEND_URL` is set to the local development server URL `http://127.0.0.1:5000`.
- If `ENV` is not `"development"`, `HEGEL_BACKEND_URL` is set to the production server URL `https://api.hegel-ai.com`.

## Usage

Other modules within the `documentation-generator` project can import `common.py` to access the `HEGEL_BACKEND_URL` variable. This allows for consistent access to the backend URL that is appropriate for the current environment (development or production).

## File Structure

- The module is located at `/workspaces/documentation-generator/target_code/prompttools/common.py` within the project directory structure.

## License

The source code's license information is indicated to be in the `LICENSE` file located in the root directory of the source tree. The copyright notice at the beginning of the file states that the code is owned by "Hegel AI, Inc." and that all rights are reserved.

## Example

Here is an example of how another module within the project might use `common.py`:

python
from prompttools.common import HEGEL_BACKEND_URL

def fetch_data():
    response = requests.get(HEGEL_BACKEND_URL + '/data-endpoint')
    return response.json()


In this example, the `fetch_data` function uses the `HEGEL_BACKEND_URL` to construct the full URL to a hypothetical data endpoint and fetches data from it.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/__init__.md

# `prompttools` Package

The `prompttools` package is a Python module designed to provide utilities for testing and monitoring prompts within a larger project. It is part of the `documentation-generator` project located at `/workspaces/documentation-generator/`. The package is initialized by the `__init__.py` file within the `prompttools` directory at `/workspaces/documentation-generator/target_code/prompttools/`.

## File Description: `__init__.py`

The `__init__.py` file serves as the initializer for the `prompttools` package. It performs the following actions:

1. **Import Statements**:
   - The file imports specific functions from its submodules. In this case, it imports:
     - `prompttest` from the `.prompttest` submodule, which likely contains functionality for testing prompts.
     - `init_sentry` from the `.sentry` submodule, which is presumably used for initializing Sentry, an error tracking and monitoring tool.

2. **Sentry Initialization**:
   - Upon importing, the `init_sentry` function is immediately called. This suggests that Sentry is a critical component for error tracking in the project, and it needs to be initialized as soon as the `prompttools` package is loaded.

3. **Export Control**:
   - The `__all__` variable is defined as a list containing the string `"prompttest"`. This controls what is exported when `import *` is used on the package. It explicitly states that only the `prompttest` function should be publicly available to users who perform a wildcard import from the `prompttools` package.

## Usage in the Project

The `prompttools` package is likely used by other parts of the `documentation-generator` project to test and monitor the behavior of prompts. The specific usage can be outlined as follows:

1. **Testing Prompts**:
   - The `prompttest` function is made available for import by other modules. Developers can use this function to test the prompts that are generated or used within the project, ensuring they meet certain criteria or behave as expected.

2. **Error Monitoring**:
   - By initializing Sentry at the package level, any module that imports from `prompttools` will have error tracking enabled. This allows for automatic capture of exceptions and issues that occur during the execution of prompt-related code, facilitating debugging and improving reliability.

3. **Integration with Other Modules**:
   - Other modules within the `documentation-generator` project can import `prompttools` to leverage its testing and monitoring capabilities. The package's functions can be used in unit tests, integration tests, or even during runtime to ensure the quality and stability of the prompts.

## File Metadata

- **Copyright Notice**: The file includes a copyright notice for Hegel AI, Inc., indicating the proprietary nature of the code.
- **License Information**: It refers to a `LICENSE` file located in the root directory of the source tree, which contains the terms under which the source code can be used.

## Conclusion

The `__init__.py` file in the `prompttools` package is a crucial component that sets up testing and monitoring utilities for prompt management within the `documentation-generator` project. It ensures that only the necessary functions are exposed and that error tracking is consistently enabled across the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/playground/data_loader.md

# `data_loader.py` Module Documentation

## Overview

The `data_loader.py` module is part of the `prompttools` package within the `playground` subpackage. It provides functionality to load and process data for use in various machine learning experiments, particularly those involving language models. The module includes functions to render prompts using Jinja2 templates, load data for individual experiments, and run multiple experiments across different model types.

## Dependencies

- `os`: Standard library module to interact with the operating system.
- `jinja2`: Templating engine for Python.
- `streamlit`: An open-source app framework for Machine Learning and Data Science projects.
- `prompttools.selector.prompt_selector`: A custom module providing the `PromptSelector` class used to pair instructions with user inputs.
- `prompttools.playground.constants`: A module containing constants such as `ENVIRONMENT_VARIABLE` and `EXPERIMENTS`.

## Functions

### `render_prompts(templates, vars)`

Renders a list of prompts based on provided Jinja2 templates and variables.

#### Parameters

- `templates`: A list of Jinja2 template strings.
- `vars`: A list of dictionaries, where each dictionary contains variables to be rendered in the templates.

#### Returns

- `prompts`: A list of strings, where each string is a rendered prompt.

#### Process

1. Initialize an empty list `prompts`.
2. Iterate over each template in `templates`.
3. For each template, iterate over each variable set in `vars`.
4. Create a new Jinja2 `Environment`.
5. Convert the current template string into a `jinja_template`.
6. Render the `jinja_template` with the current variable set and append the result to `prompts`.
7. Return the list of rendered prompts.

### `load_data(model_type, model, instructions, user_inputs, temperature, top_p, max_tokens, frequency_penalty, presence_penalty, api_key)`

Loads data for a single experiment based on the specified parameters.

#### Parameters

- `model_type`: A string indicating the type of model to be used.
- `model`: The specific model to be used for the experiment.
- `instructions`: A list of instruction strings.
- `user_inputs`: A list of user input strings.
- `temperature`: A float representing the sampling temperature.
- `top_p`: A float representing the nucleus sampling parameter.
- `max_tokens`: An integer representing the maximum number of tokens to generate.
- `frequency_penalty`: A float representing the frequency penalty parameter.
- `presence_penalty`: A float representing the presence penalty parameter.
- `api_key`: An optional string representing the API key for the model's service.

#### Returns

- A pandas DataFrame containing the results of the experiment.

#### Process

1. If an `api_key` is provided, set the corresponding environment variable for the `model_type`.
2. Create a list of `PromptSelector` objects by pairing each instruction with each user input.
3. Depending on the `model_type`, initialize the appropriate experiment with the relevant parameters.
4. Convert the experiment results to a pandas DataFrame and return it.

### `run_multiple(model_types, models, instructions, prompts, openai_api_key, anthropic_api_key, google_api_key, hf_api_key, replicate_api_key)`

Runs multiple experiments across different model types and aggregates the results.

#### Parameters

- `model_types`: A list of strings indicating the types of models to be used.
- `models`: A list of models to be used for the experiments.
- `instructions`: A dictionary mapping instruction indices to instruction strings.
- `prompts`: A list of prompt strings.
- `openai_api_key`: An optional string representing the OpenAI API key.
- `anthropic_api_key`: An optional string representing the Anthropic API key.
- `google_api_key`: An optional string representing the Google PaLM API key.
- `hf_api_key`: An optional string representing the HuggingFace Hub API token.
- `replicate_api_key`: An optional string representing the Replicate API token.

#### Returns

- A list of pandas DataFrames, each containing the results of an experiment.

#### Process

1. Set the environment variables for each provided API key.
2. Initialize an empty list `dfs` to store the DataFrames.
3. Iterate over the `models` list.
4. For each model, check if there are corresponding instructions and create `PromptSelector` objects or use the provided `prompts`.
5. Depending on the `model_type`, initialize the appropriate experiment with the relevant parameters.
6. Convert the experiment results to a pandas DataFrame and append it to `dfs`.
7. Return the list of DataFrames.

## Decorators

- `@st.cache_data`: A decorator provided by Streamlit to cache the output of the decorated function, preventing unnecessary recomputation.

## Usage

The functions in this module are typically used within a Streamlit application to interactively run experiments with language models. Users can input different parameters and API keys to test various models and compare their outputs.

## Notes

- The module contains a `TODO` comment indicating that support for additional parameters such as temperature should be considered for the `run_multiple` function.
- The module assumes the existence of a `to_pandas_df` method on the experiment objects, which is used to convert the experiment results into pandas DataFrames.
- The module sets environment variables for API keys, which implies that the experiments are likely making calls to external services requiring authentication.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/playground/playground.md

# playground.py

## Overview
`playground.py` is a Python script that utilizes the Streamlit library to create an interactive web application for experimenting with different AI models and prompt configurations. It allows users to select models, input prompts, and view the generated responses. The application supports various modes of operation, including single model interaction, prompt templating, and model comparison.

## Dependencies
- `streamlit`: Provides the web application framework.
- `pyperclip`: Allows copying text to the clipboard.
- `urllib.parse`: Used for encoding and decoding URL parameters.
- `os`, `pathlib.Path`: Used for file and directory manipulation.
- `dotenv`: Loads environment variables from a `.env` file.

## Constants
- `MODES`, `MODEL_TYPES`, `OPENAI_CHAT_MODELS`, `OPENAI_COMPLETION_MODELS`: Defined in `constants.py`, these constants represent the available modes of operation, model types, and specific models for OpenAI's Chat and Completion APIs.

## Data Handling
- `render_prompts`, `load_data`, `run_multiple`: Functions imported from `data_loader.py` that handle the rendering of prompts, loading of data from models, and running multiple models for comparison.

## Query Parameters
- `params`: Retrieves the current query parameters from the URL.
- `st.experimental_set_query_params()`: Resets the query parameters.

## Streamlit Components
- `st.header`, `st.write`: Display the application title and a link to the GitHub repository.
- `st.sidebar`: Contains the controls for selecting the mode, model type, and other configurations.
- `st.radio`, `st.selectbox`, `st.text_input`, `st.number_input`, `st.slider`, `st.text_area`, `st.button`, `st.columns`, `st.empty`, `st.divider`: Various Streamlit components used to create the user interface.

## Session State Management
- `st.session_state`: A state management system to preserve user input across reruns of the application.

## Modes of Operation
- `Instruction`: Allows users to input instructions and prompts for a single model and view the generated responses.
- `Prompt Template`: Enables users to create prompt templates with variables and generate responses based on user input.
- `Model Comparison`: Facilitates the comparison of responses from multiple models for the same prompts.

## Model Configuration
Depending on the selected mode and model type, users can configure:
- Local model paths for LlamaCpp models.
- Repository IDs for models hosted on HuggingFace Hub.
- Model names for Google PaLM.
- API keys for various services (OpenAI, Anthropic, Google PaLM, HuggingFace Hub, Replicate).

## Input Configuration
Users can specify the number of instructions, prompts, and variables, as well as fine-tune parameters like temperature, presence penalty, and frequency penalty.

## Running the Models
- `run`: A button that triggers the generation of responses based on the current configuration.
- `clear`: A button that clears the session state.
- `share`: A button that copies a shareable link with the current configuration to the clipboard.

## Output Display
- `placeholders`: Empty Streamlit components that are later filled with the generated responses from the models.

## Error Handling
- The script includes a try-except block to handle the loading of environment variables and gracefully pass if an exception occurs.

## Clipboard Interaction
- The application attempts to copy the shareable link to the clipboard using `pyperclip`. If this fails, it provides the link as text for manual copying.

## Clearing Session State
- If the clear button is pressed, the script removes all keys from the session state to reset the application.

## Sharing Functionality
- The share button constructs a URL with the current configuration encoded as query parameters and attempts to copy it to the clipboard.

## Usage
To use the application, the user interacts with the sidebar to select the desired mode and model configurations, inputs prompts or templates, and then runs the model to see the generated responses. The application can be accessed through a web browser, typically hosted on a platform that supports Streamlit applications.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/playground/__init__.md

# `__init__.py` in `prompttools/playground` Module

## Overview

The `__init__.py` file is a Python initializer file that is required to make the `prompttools/playground` directory be treated as a Python package. This allows the modules within the package to be imported from other parts of the project. The presence of an `__init__.py` file in a directory indicates to the Python interpreter that the directory should be treated as a package.

## Usage

When the `prompttools/playground` package is imported, the `__init__.py` file is automatically executed. The primary purpose of this file is to initialize the Python package. It can be used to set up the package environment, import necessary modules, define variables, or execute any startup code that is required for the package.

## Details

The `__init__.py` file can contain any valid Python code. In this specific instance, the file does not contain any executable code or definitions. It is an empty file, which is a common practice when no package initialization is needed. However, it still serves the purpose of declaring the `prompttools/playground` directory as a Python package.

## Project Structure

The `prompttools/playground` package is part of a larger project located in the `/workspaces/documentation-generator` directory. The structure of the project is as follows:


/workspaces/documentation-generator/
├── target_code/
│   ├── prompttools/
│   │   ├── playground/
│   │   │   ├── __init__.py
│   │   │   └── (other modules or sub-packages)
│   │   └── (other modules or sub-packages)
│   └── (other packages or modules)
└── LICENSE


## Licensing

The file header indicates that the source code is copyrighted by Hegel AI, Inc. and that all rights are reserved. The license for the source code can be found in the `LICENSE` file located in the root directory of the source tree. It is important for users and contributors to review the `LICENSE` file to understand the terms under which the code can be used or modified.

## Conclusion

While the `__init__.py` file in the `prompttools/playground` package does not contain any code, it is essential for the Python interpreter to recognize the directory as a package. This allows for the modular organization of the project and the ability to import the package's modules elsewhere in the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/playground/constants.md

# Constants Module Documentation

## Overview

The `constants.py` module is part of the `/workspaces/documentation-generator/target_code/prompttools/playground` package. It defines several constants used throughout the project, particularly for managing experiments with different AI models and their associated environment variables.

## Imports

The module imports various experiment classes from the `prompttools.experiment` package:

- `LlamaCppExperiment`
- `OpenAIChatExperiment`
- `OpenAICompletionExperiment`
- `AnthropicCompletionExperiment`
- `GooglePaLMCompletionExperiment`
- `HuggingFaceHubExperiment`
- `ReplicateExperiment`

These classes are likely to represent different types of experiments that can be conducted with various AI models.

## Constants

### ENVIRONMENT_VARIABLE

A dictionary mapping the name of the experiment to the corresponding environment variable that stores the API token or key required to access the service.

- `"Replicate"` maps to `"REPLICATE_API_TOKEN"`
- `"OpenAI Chat"` maps to `"OPENAI_API_KEY"`
- `"OpenAI Completion"` maps to `"OPENAI_API_KEY"`
- `"Anthropic"` maps to `"ANTHROPIC_API_KEY"`
- `"Google PaLM"` maps to `"GOOGLE_PALM_API_KEY"`
- `"HuggingFace Hub"` maps to `"HUGGINGFACEHUB_API_TOKEN"`

This dictionary is used to dynamically fetch the correct API token based on the experiment being run.

### EXPERIMENTS

A dictionary mapping the name of the experiment to the experiment class that should be instantiated when running that experiment.

- `"LlamaCpp Chat"` maps to `LlamaCppExperiment`
- `"OpenAI Chat"` maps to `OpenAIChatExperiment`
- `"OpenAI Completion"` maps to `OpenAICompletionExperiment`
- `"Anthropic"` maps to `AnthropicCompletionExperiment`
- `"Google PaLM"` maps to `GooglePaLMCompletionExperiment`
- `"HuggingFace Hub"` maps to `HuggingFaceHubExperiment`
- `"Replicate"` maps to `ReplicateExperiment`

This dictionary is used to instantiate the correct experiment class based on the user's selection.

### MODES

A tuple containing different modes of operation for the experiments:

- `"Instruction"`
- `"Prompt Template"`
- `"Model Comparison"`

These modes likely correspond to different ways the experiments can be configured or the type of input they accept.

### MODEL_TYPES

A tuple listing all the model types that can be used in the experiments:

- `"OpenAI Chat"`
- `"OpenAI Completion"`
- `"Anthropic"`
- `"Google PaLM"`
- `"LlamaCpp Chat"`
- `"LlamaCpp Completion"`
- `"HuggingFace Hub"`
- `"Replicate"`

This tuple is used to validate or display the available model types to the user.

### OPENAI_CHAT_MODELS

A tuple containing the identifiers for different configurations of the OpenAI Chat models:

- `"gpt-3.5-turbo"`
- `"gpt-3.5-turbo-16k"`
- `"gpt-3.5-turbo-0613"`
- `"gpt-3.5-turbo-16k-0613"`
- `"gpt-3.5-turbo-0301"`
- `"gpt-4"`
- `"gpt-4-0613"`
- `"gpt-4-32k"`
- `"gpt-4-32k-0613"`
- `"gpt-4-0314"`
- `"gpt-4-32k-0314"`

These identifiers are used to specify which OpenAI Chat model to use during an experiment.

### OPENAI_COMPLETION_MODELS

A tuple containing the identifiers for different configurations of the OpenAI Completion models:

- `"text-davinci-003"`
- `"text-davinci-002"`
- `"code-davinci-002"`

These identifiers are used to specify which OpenAI Completion model to use during an experiment.

## Usage

The constants defined in this module are used throughout the project to:

- Dynamically fetch API tokens based on the experiment being run.
- Instantiate the correct experiment class based on user selection.
- Validate or display the available model types to the user.
- Specify the model configuration for OpenAI Chat and Completion experiments.

The module serves as a central repository for configuration options that are likely to be referenced in multiple places within the project, ensuring consistency and ease of maintenance.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/ranking_correlation.md

# `ranking_correlation.py` Module

## Overview

The `ranking_correlation.py` module is part of the `prompttools/utils` package within the `documentation-generator` project. It provides a utility function to compute the Spearman's rank correlation coefficient between an expected ranking and an actual ranking produced by a model. This function is typically used to evaluate the performance of ranking models in information retrieval, recommendation systems, or any other domain where items are ranked according to their relevance or importance.

## Dependencies

- `scipy.stats`: This module from the SciPy library provides functions for statistical calculations, including the Spearman's rank correlation. It is a required dependency for the `ranking_correlation` function to work. If `scipy.stats` is not installed, the function will raise a `ModuleNotFoundError`.
- `pandas`: The function expects input in the form of a `pandas.core.series.Series` object, which is a one-dimensional array with axis labels from the pandas library.

## Function: `ranking_correlation`

### Description

The `ranking_correlation` function compares an expected ranking list with an actual ranking produced by a model to determine how well the model's ranking aligns with the expected outcome. It calculates the Spearman's rank correlation coefficient, which assesses how well the relationship between two rankings can be described using a monotonic function.

### Parameters

- `row` (`pandas.core.series.Series`): A single row of data from a pandas DataFrame. This row should include the actual ranking produced by the model, along with other relevant data such as input features and model responses.
- `expected_ranking` (`list`): A list representing the expected ranking of items. Each element in the list is an identifier (such as a document ID) that corresponds to the ranked items.
- `ranking_column_name` (`str`, optional): The name of the column in `row` that contains the actual ranking produced by the model. The default value for this parameter is `"top doc ids"`.

### Returns

- `float`: The Spearman's rank correlation coefficient between the expected ranking and the actual ranking. The value ranges from -1 to 1, where 1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no correlation.

### Usage Example

python
EXPECTED_RANKING_LIST = [
    ["id1", "id3", "id2"],
    ["id2", "id3", "id1"],
    ["id1", "id3", "id2"],
    ["id2", "id3", "id1"],
]
experiment.evaluate("ranking_correlation", ranking_correlation, expected_ranking=EXPECTED_RANKING_LIST)


In the example above, `EXPECTED_RANKING_LIST` is a list of expected rankings, and `experiment.evaluate` is a hypothetical method that evaluates the ranking correlation for each row in a dataset.

### Error Handling

If the `scipy.stats` module is not available, the function will raise a `ModuleNotFoundError` with instructions to install the SciPy package.

### Special Cases

- If both the expected ranking and the actual ranking contain only one item each, the function will return 1.0 if they match, or -1.0 if they do not match, without performing a correlation calculation.

### Implementation Details

The function first checks if the `scipy.stats` module is available. If not, it raises an error. It then retrieves the actual ranking from the specified column in the input `row`. If there is only one item in both the expected and actual rankings, it returns 1.0 or -1.0 based on a direct comparison. Otherwise, it calculates the Spearman's rank correlation coefficient using the `spearmanr` function from `scipy.stats` and returns the correlation value.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/autoeval_from_expected.md

# autoeval_from_expected.py

This Python module is part of a larger project and is responsible for automatically evaluating responses to prompts based on expected answers. It leverages the OpenAI GPT-4 model to perform this evaluation. The module contains several functions that work together to achieve this functionality.

## Dependencies

- `os`: Standard Python module to interact with the operating system.
- `openai`: Python client library for the OpenAI API.
- `jinja2`: A modern and designer-friendly templating language for Python.
- `pandas`: An open-source data analysis and manipulation tool.

## Constants

- `EVALUATION_SYSTEM_PROMPT`: A string that defines the instructions for the GPT-4 model to evaluate responses. It tells the model to grade the response as either RIGHT or WRONG based on whether the ACTUAL answer matches the EXPECTED answer.

- `EVALUATION_USER_TEMPLATE`: A Jinja2 template string that formats the prompt, expected answer, and actual answer for evaluation by the model.

## Functions

### `_get_messages`

This private function uses the Jinja2 template to create a formatted message that includes the prompt, expected answer, and actual response. It returns a list of dictionaries, each representing a message with a role (either "system" or "user") and content.

#### Parameters

- `prompt (str)`: The original prompt given to the model.
- `expected (str)`: The expected correct answer to the prompt.
- `response (str)`: The actual response from the model that needs to be evaluated.

#### Returns

- `List[Dict[str, str]]`: A list of message dictionaries ready to be used by the OpenAI API.

### `compute`

This function calls the OpenAI API to evaluate a response using the GPT-4 model. It returns a score of 1.0 if the response is correct (RIGHT) or 0.0 if it is incorrect (WRONG).

#### Parameters

- `prompt (str)`: The input prompt.
- `expected (str)`: The expected correct answer.
- `response (str)`: The actual response from the model.
- `model (str)`: The identifier for the OpenAI chat model to use. Defaults to "gpt-4".

#### Returns

- `float`: The evaluation score, either 1.0 or 0.0.

#### Raises

- `PromptToolsUtilityError`: If the `OPENAI_API_KEY` environment variable is not set.

### `evaluate`

This function is a wrapper around the `compute` function, providing a consistent interface for auto-evaluation.

#### Parameters

- `prompt (str)`: The input prompt.
- `response (str)`: The actual response from the model.
- `metadata (dict)`: A dictionary containing metadata for the evaluation. (Unused in the current implementation)
- `expected (str)`: The expected correct answer.

#### Returns

- `float`: The evaluation score from the `compute` function.

### `autoeval_from_expected_response`

This function is designed to be applied to a pandas DataFrame. It evaluates the response in each row of the DataFrame against an expected answer.

#### Parameters

- `row (pandas.core.series.Series)`: A row from a pandas DataFrame.
- `expected (str)`: The expected correct answer.
- `prompt_column_name (str)`: The name of the column in the DataFrame that contains the prompts. Defaults to the column name provided.
- `response_column_name (str)`: The name of the column in the DataFrame that contains the responses. Defaults to "response".

#### Returns

- `float`: The evaluation score for the response in the given row.

## Usage

The module is used to automatically evaluate responses to prompts by comparing them with expected answers. It is particularly useful in scenarios where responses from a language model like GPT-4 need to be graded or validated at scale. The module can be integrated into a larger system that processes and evaluates large datasets, such as student responses to math questions or automated testing of chatbot outputs.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/validate_python.md

# `validate_python.py` Module

## Overview

The `validate_python.py` module is part of the `prompttools` package and provides functionality to validate whether a given text string is syntactically correct Python code. It is designed to be used within a larger project that generates or manipulates Python code, ensuring that the output is valid Python before it is executed or further processed.

## Dependencies

- `os`: Standard Python module to interact with the operating system.
- `typing.Dict`: Type hinting for dictionaries.
- `pandas.core.series`: Used to handle data in a series format, typically obtained from a DataFrame.
- `error.PromptToolsUtilityError`: Custom exception class defined within the `prompttools` package for error handling.
- `pylint.epylint`: External library used for linting Python code. It is an optional dependency and must be installed separately.

## Temporary File

- `PROMPTTOOLS_TMP`: A constant string that defines the name of a temporary file (`"prompttools_tmp.py"`) used during the validation process.

## Functions

### `validate(text: str) -> float`

Validates that the provided text is syntactically correct Python code.

#### Arguments

- `text (str)`: The generated text which is expected to be valid Python code.

#### Behavior

1. Checks if `pylint` is available. If not, raises a `RuntimeError` indicating that `pylint` is required.
2. Checks if the temporary file defined by `PROMPTTOOLS_TMP` already exists. If it does, raises a `PromptToolsUtilityError`.
3. Writes the input text to the temporary file.
4. Runs `pylint` on the temporary file and captures the standard output.
5. Deletes the temporary file.
6. Returns `0.0` if the word "error" is found in the `pylint` output, indicating invalid Python code. Otherwise, returns `1.0`, indicating valid Python code.

### `validate_python_response(row: pandas.core.series.Series, response_column_name: str = "response") -> float`

Validates whether the `response` string in a given row follows Python's syntax.

#### Arguments

- `row (pandas.core.series.Series)`: A row of data from a DataFrame, which includes various columns such as input, model response, and other metrics.
- `response_column_name (str)`: The name of the column that contains the model's response. Defaults to `"response"`.

#### Behavior

1. Calls the `validate` function, passing the value from the `response_column_name` of the given row.
2. Returns the result of the `validate` function.

### `evaluate(prompt: str, response: str, metadata: Dict) -> float`

Validates whether the `response` string follows Python's syntax. This function is designed to conform to a common evaluation interface.

#### Arguments

- `prompt (str)`: The input prompt string. Not used in the function.
- `response (str)`: The string that will be validated as Python code.
- `metadata (Dict)`: Additional metadata. Not used in the function.

#### Behavior

1. Calls the `validate` function, passing the `response` string.
2. Returns the result of the `validate` function.

## Usage

This module is used to ensure that text generated by a model or entered by a user is valid Python code. It can be integrated into a larger system that requires validation of Python syntax, such as code generation tools, automated testing frameworks, or educational platforms that evaluate Python exercises.

## Error Handling

- If `pylint` is not installed, a `RuntimeError` is raised.
- If the temporary file already exists, a `PromptToolsUtilityError` is raised to prevent overwriting or data corruption.

## Notes

- The module assumes that `pylint` is installed and is less than version 3.0.
- The temporary file is used to avoid in-memory linting and to work around limitations of `pylint`'s API.
- The module does not handle the case where the temporary file cannot be deleted due to permissions or other file system issues.
- The module does not provide detailed error messages or locations of syntax errors in the code; it only indicates whether an error was detected by `pylint`.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/validate_json.md

# `validate_json.py` Module Documentation

## Overview

The `validate_json.py` module provides utility functions for validating JSON strings within a Python project. It includes functions to preprocess text, validate JSON format, validate JSON keys, and integrate with data structures such as pandas Series. The module is designed to be used in projects where JSON validation is required, particularly when dealing with responses from language model APIs or other sources that output JSON strings.

## Functions

### `strip_outer_brackets`

python
def strip_outer_brackets(text: str) -> str


#### Description

Removes all characters outside the first opening curly brace `{` and the last closing curly brace `}` in a given string. This function is intended to be used as a preprocessing step before attempting to parse a string as JSON.

#### Parameters

- `text (str)`: The text to process.

#### Returns

- `str`: The processed text with outer characters removed.

---

### `sample_pre_process_fn`

python
def sample_pre_process_fn(text: str)


#### Description

Provides an example of a preprocessing function that can be used before attempting to parse a string as JSON. It first calls `strip_outer_brackets` to remove outer characters and then removes newline escape sequences `"\n"`.

#### Parameters

- `text (str)`: The text to process.

#### Returns

- `str`: The preprocessed text ready for JSON parsing.

---

### `validate`

python
def validate(text: str, pre_process_fn: Optional[Callable] = None)


#### Description

Validates whether the provided text is a valid JSON string. Optionally, a preprocessing function can be applied to the text before validation.

#### Parameters

- `text (str)`: The generated text that should be valid JSON.
- `pre_process_fn (Callable[str, str], optional)`: A function to preprocess the text response before attempting to parse the string as JSON.

#### Returns

- `float`: A score of `1.0` if the text is valid JSON, otherwise `0.0`.

---

### `validate_keys`

python
def validate_keys(text: str, valid_keys: List[str])


#### Description

Ensures that all keys present in the generated JSON are within a specified list of valid keys.

#### Parameters

- `text (str)`: The generated text that should be valid JSON.
- `valid_keys (List[str])`: A list of strings representing valid keys that may appear in the JSON.

#### Returns

- `float`: A score of `1.0` if all keys are valid, otherwise `0.0`.

---

### `validate_json_response`

python
def validate_json_response(row: pandas.core.series.Series, response_column_name: str = "response") -> float


#### Description

Validates whether the `response` string in a pandas Series is in a valid JSON format.

#### Parameters

- `row (pandas.core.series.Series)`: A row of data from a pandas DataFrame.
- `response_column_name (str)`: The name of the column that contains the model's response. Defaults to `"response"`.

#### Returns

- `float`: A score of `1.0` if the response is valid JSON, otherwise `0.0`.

---

### `evaluate`

python
def evaluate(prompt: str, response: str, metadata: Dict) -> float


#### Description

Validates whether the `response` string is in a valid JSON format. This function is designed to be used in evaluation scripts where the prompt and metadata are not used but are part of the function signature for consistency.

#### Parameters

- `prompt (str)`: The prompt string, not used in this function.
- `response (str)`: The string that will be validated as JSON.
- `metadata (Dict)`: A dictionary of metadata, not used in this function.

#### Returns

- `float`: A score of `1.0` if the response is valid JSON, otherwise `0.0`.

## Usage

The functions in this module can be used to validate JSON strings, particularly in scenarios where JSON responses are received from language models or other APIs. The validation process can be customized with preprocessing functions as needed. The module can be integrated into data processing pipelines, especially when working with pandas DataFrames.

## Dependencies

- `typing`: Provides type hints for function signatures.
- `pandas.core.series`: Used for handling pandas Series objects.
- `json`: Used for loading and parsing JSON strings.
- `re`: Used for regular expression matching to validate JSON keys.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/expected.md

# `expected.py` Module Documentation

## Overview

The `expected.py` module is part of the `prompttools` package and provides functionality to interact with OpenAI's language models, specifically GPT-4, to generate expected responses to prompts and evaluate the similarity of given responses to these expected results. It is designed to be used in projects that require automated testing or evaluation of text generated by language models.

## Functions

### `compute`

python
def compute(prompt: str, model: str = "gpt-4") -> str:


#### Description

Generates an expected response to a given prompt using a specified language model from OpenAI, defaulting to GPT-4.

#### Parameters

- `prompt (str)`: The input text prompt for which the expected response is to be generated.
- `model (str)`: The identifier for the OpenAI language model to use. Defaults to "gpt-4".

#### Returns

- `(str)`: The content of the message from the first choice of the model's response.

#### Raises

- `PromptToolsUtilityError`: If the `OPENAI_API_KEY` environment variable is not set.

#### Usage

This function is typically used to obtain a baseline response from a high-quality language model to compare against other responses.

### `evaluate`

python
def evaluate(prompt: str, response: str, model: str = "gpt-4") -> str:


#### Description

Evaluates the similarity between a given response and the expected result generated by the same prompt using a specified language model.

#### Parameters

- `prompt (str)`: The input text prompt.
- `response (str)`: The response text to be evaluated against the expected result.
- `model (str)`: The identifier for the OpenAI language model to use for generating the expected response. Defaults to "gpt-4".

#### Returns

- `(str)`: A similarity score between the given response and the expected response.

#### Usage

This function is used to compute how closely a response matches the expected result from a language model, which can be useful for testing or quality assurance purposes.

### `compute_similarity_against_model`

python
def compute_similarity_against_model(
    row: pandas.core.series.Series,
    prompt_column_name: str,
    model: str = "gpt-4",
    response_column_name: str = "response",
) -> str:


#### Description

Computes the similarity of a response contained within a DataFrame row to the expected result generated by a language model using the corresponding prompt from the same row.

#### Parameters

- `row (pandas.core.series.Series)`: A single row from a pandas DataFrame, which includes the prompt and response data among other possible metrics.
- `prompt_column_name (str)`: The column name in the DataFrame that contains the input prompt.
- `model (str)`: The identifier for the OpenAI language model to use for generating the expected response. Defaults to "gpt-4".
- `response_column_name (str)`: The column name in the DataFrame that contains the response to be evaluated. Defaults to "response".

#### Returns

- `(str)`: A similarity score between the response in the row and the expected response generated by the model.

#### Usage

This function is particularly useful for batch processing of a DataFrame where each row contains a prompt-response pair. It allows for the automated evaluation of responses in the context of a larger dataset.

## Dependencies

- `os`: To access environment variables.
- `openai`: To interact with OpenAI's API for generating responses.
- `pandas.core.series`: To handle individual rows of a DataFrame as Series objects.
- `.error`: To raise custom errors defined within the `prompttools` package.
- `.similarity`: To compute similarity scores between text responses.

## Error Handling

The module includes error handling to ensure that the `OPENAI_API_KEY` is set in the environment before attempting to generate responses with OpenAI's API. If the key is not set, a `PromptToolsUtilityError` is raised.

## Integration

The module is designed to be integrated into larger projects that require automated interaction with language models for tasks such as testing, evaluation, or data analysis. It can be used as a standalone utility or as part of a suite of tools within the `prompttools` package.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/autoeval.md

# autoeval.py Module

## Overview

The `autoeval.py` module is part of the `prompttools` package and provides functionality for automatically evaluating the quality of responses generated by a language model, such as GPT-4, based on a given prompt. It determines if the response is following the directions provided in the prompt.

## Functions

### `_get_messages`

python
def _get_messages(prompt: str, response: str):


#### Description

This private function generates a list of messages formatted for evaluation by the OpenAI chat model. It uses the Jinja2 templating engine to create a user message that combines the prompt and response.

#### Parameters

- `prompt (str)`: The input prompt.
- `response (str)`: The model response.

#### Returns

- `List[Dict[str, str]]`: A list of dictionaries with two key-value pairs, where the keys are `role` and `content`. The `role` can be either `"system"` or `"user"`, and `content` contains the respective messages.

### `compute`

python
def compute(prompt: str, response: str, model: str = "gpt-4") -> float:


#### Description

This function uses an OpenAI chat model, such as GPT-4, to automatically evaluate a given prompt/response pair. It returns a binary score indicating whether the response is correct (1.0) or incorrect (0.0) based on the model's judgment.

#### Parameters

- `prompt (str)`: The input prompt.
- `response (str)`: The model response.
- `model (str)`: The OpenAI chat model to use for generating an expected response. Defaults to GPT-4.

#### Returns

- `float`: A binary score, either 1.0 if the response is judged as "RIGHT" or 0.0 if judged as "WRONG".

#### Exceptions

- `PromptToolsUtilityError`: Raised if the `OPENAI_API_KEY` environment variable is not set.

### `evaluate`

python
def evaluate(prompt: str, response: str, _metadata: Dict) -> float:


#### Description

This function is a wrapper around the `compute` function. It uses auto-evaluation to score the model response with "gpt-4" as the judge, returning a binary score.

#### Parameters

- `prompt (str)`: The input prompt.
- `response (str)`: The model response.
- `_metadata (Dict)`: A dictionary of metadata, currently not used in the function.

#### Returns

- `float`: A binary score, either 1.0 if the response is judged as "RIGHT" or 0.0 if judged as "WRONG".

### `autoeval_binary_scoring`

python
def autoeval_binary_scoring(
    row: pandas.core.series.Series,
    prompt_column_name: str,
    response_column_name: str = "response",
) -> float:


#### Description

This function applies the auto-evaluation scoring to a row from a pandas DataFrame. It is designed to be used with the `apply` method of a DataFrame to score each row.

#### Parameters

- `row (pandas.core.series.Series)`: A row of data from the full DataFrame, which includes input, model response, and other metrics.
- `prompt_column_name (str)`: The name of the column that contains the input prompt.
- `response_column_name (str)`: The name of the column that contains the model's response. Defaults to `"response"`.

#### Returns

- `float`: A binary score, either 1.0 if the response is judged as "RIGHT" or 0.0 if judged as "WRONG".

## Constants

### `EVALUATION_SYSTEM_PROMPT`

A constant string that contains the system prompt used to instruct the OpenAI chat model on how to evaluate the responses.

### `EVALUATION_USER_TEMPLATE`

A constant string that serves as a Jinja2 template for formatting the user message that will be evaluated by the OpenAI chat model.

## Dependencies

- `os`: Standard library module to interact with the operating system.
- `typing.Dict`: Type hinting for dictionaries.
- `openai`: The OpenAI Python client library for accessing the OpenAI API.
- `pandas.core.series`: Data structure for a single column of a DataFrame.
- `jinja2`: Templating engine for Python.
- `error.PromptToolsUtilityError`: Custom exception class defined within the `prompttools` package.

## Usage

The module is used within a larger project to automatically score the quality of responses generated by a language model. It is typically used in scenarios where a large number of responses need to be evaluated quickly and consistently, such as in the development and testing of language models.

## License

The source code's license can be found in the `LICENSE` file in the root directory of this source tree.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/similarity.md

# similarity.py

This Python module provides functionality to compute the similarity between two documents or images. It includes methods for semantic similarity using text embeddings and structural similarity using image processing.

## Dependencies

- `pandas`: Used for handling data in DataFrame format.
- `logging`: Used for logging warnings and errors.
- `cv2` (OpenCV): Required for image processing tasks.
- `skimage.metrics`: Provides the structural similarity index measure (SSIM) function.
- `sentence_transformers`: Used for computing semantic text embeddings and cosine similarity.

## Functions

### `_get_embedding_model`

This function lazily initializes and retrieves a singleton instance of the sentence embedding model from the `sentence_transformers` library.

- **Returns**: An instance of `SentenceTransformer`.

### `_get_chroma_client`

This function lazily initializes and retrieves a singleton instance of the ChromaDB client.

- **Returns**: An instance of `chromadb.Client`.

### `_from_huggingface`

This function computes the semantic similarity between two documents using the HuggingFace sentence_transformers library.

- **Parameters**:
  - `doc1` (str): The first document.
  - `doc2` (str): The second document.
- **Returns**: A float representing the cosine similarity between the embeddings of `doc1` and `doc2`.

### `_from_chroma`

This function computes the semantic similarity between two documents using ChromaDB.

- **Parameters**:
  - `doc1` (str): The first document.
  - `doc2` (str): The second document.
- **Returns**: A float representing the similarity score from ChromaDB.

### `compute`

This function computes the semantic similarity between two documents, using either ChromaDB or HuggingFace sentence_transformers based on the `use_chroma` flag.

- **Parameters**:
  - `doc1` (str): The first document.
  - `doc2` (str): The second document.
  - `use_chroma` (bool): Indicates whether to use ChromaDB or HuggingFace.
- **Returns**: A float representing the similarity score.

### `evaluate`

This function evaluates the semantic similarity between an expected response and the model's text response.

- **Parameters**:
  - `prompt` (str): Not used.
  - `response` (str): The response string to compare.
  - `metadata` (Dict): Not used.
  - `expected` (str): The expected response.
- **Returns**: A float representing the semantic similarity score.

### `structural_similarity`

This function computes the structural similarity index measure (SSIM) between two images.

- **Parameters**:
  - `row` (pandas.core.series.Series): A row from a DataFrame.
  - `expected` (str): The column name of the expected image responses.
  - `response_column_name` (str): The column name containing the model's response (default: `"response"`).
- **Returns**: A float representing the SSIM score.

### `semantic_similarity`

This function checks the semantic similarity between the expected text response and the model's text response.

- **Parameters**:
  - `row` (pandas.core.series.Series): A row from a DataFrame.
  - `expected` (str): The expected responses for each row in the column.
  - `response_column_name` (str): The column name containing the model's response (default: `"response"`).
- **Returns**: A float representing the semantic similarity score.

## Usage

The module is used to evaluate the similarity between documents or images, typically in a testing or validation context where the expected output is compared against the actual output from a model. The choice of similarity measure (semantic or structural) depends on the type of data being compared (text or images).

## Notes

- The module expects the `cv2` and `skimage` packages to be installed for image processing tasks.
- The `sentence_transformers` library is used for text embedding and similarity computation.
- The module handles lazy initialization of the embedding model and ChromaDB client to avoid unnecessary resource usage.
- The module includes error handling for missing dependencies and provides informative error messages.
- The `structural_similarity` function converts images to grayscale before computing SSIM.
- The `semantic_similarity` function uses the `compute` function to calculate similarity scores.
- The module includes logging to warn users about potential issues, such as passing a single string instead of a list of strings.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/autoeval_scoring.md

# autoeval_scoring.py

## Overview
The `autoeval_scoring.py` module is part of the `prompttools` utility package within the `documentation-generator` project. It provides functionality to automatically evaluate and score a model's response against a given fact using a high-quality chat model, such as `claude-2`. The module leverages the `anthropic` package to interact with the Anthropic API for generating scores.

## Dependencies
- `os`: Standard library module to interact with the operating system.
- `pandas.core.series`: Part of the `pandas` library, used for handling data in Series format.
- `jinja2`: Templating engine for Python, used to generate prompts dynamically.
- `anthropic`: A third-party package (optional) for interacting with the Anthropic API.

## Constants
- `AUTO_EVAL_PROMPT_TEMPLATE`: A Jinja2 template string that defines the structure of the prompt to be sent to the evaluation model. It includes placeholders for a human prompt, an AI prompt, a fact, and a model answer.

## Functions

### `_generate_auto_eval_prompt(fact: str, model_answer: str) -> str`
A private function that generates an auto-evaluation prompt using the `AUTO_EVAL_PROMPT_TEMPLATE`. It takes a fact and a model answer as input and returns a string with the rendered prompt.

#### Parameters
- `fact (str)`: The fact to be evaluated against.
- `model_answer (str)`: The answer provided by the model.

#### Returns
- `str`: The rendered auto-evaluation prompt.

### `compute(fact: str, model_answer: str, model: str = "claude-2") -> float`
This function uses a specified chat model to automatically score a given fact/response pair. The score is an integer ranging from 1 to 7.

#### Parameters
- `fact (str)`: The fact (truth) against which the response is evaluated.
- `model_answer (str)`: The model's response to be scored.
- `model (str)`: The name of the model used for evaluation, defaulting to "claude-2".

#### Returns
- `float`: The score as an integer from 1 to 7.

#### Raises
- `RuntimeError`: If the `ANTHROPIC_API_KEY` environment variable is not set.

### `autoeval_scoring(row: pandas.core.series.Series, expected: str, response_column_name: str = "response") -> float`
This function scores a model's response using auto-evaluation.

#### Parameters
- `row (pandas.core.series.Series)`: A row from a DataFrame containing various data, including the model's response.
- `expected (str)`: The expected correct response.
- `response_column_name (str)`: The column name in the DataFrame that contains the model's response, defaulting to "response".

#### Returns
- `float`: The score as an integer from 1 to 7.

#### Raises
- `ModuleNotFoundError`: If the `anthropic` package is not installed.

## Usage
The `autoeval_scoring.py` module is used to automatically score the accuracy of a model's response to a prompt. It is typically used in the context of evaluating AI-generated text, where the correctness of the response is critical. The module requires an API key for the Anthropic API to be set in the environment and the `anthropic` package to be installed.

## Example
To use the `autoeval_scoring` function, one would typically have a DataFrame with a column containing model responses. The function can be applied to each row of the DataFrame to obtain a score for the response:

python
import pandas as pd
from prompttools.utils.autoeval_scoring import autoeval_scoring

# Assuming df is a DataFrame with a 'response' column
df['score'] = df.apply(autoeval_scoring, expected='The correct answer', axis=1)

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/moderation.md

# `moderation.py` Module Documentation

## Overview

The `moderation.py` module is part of the `prompttools.utils` package and is responsible for interfacing with OpenAI's moderation API. It provides a function `apply_moderation` that checks if a given text complies with OpenAI's usage policies by using a specified moderation model.

## Functions

### `apply_moderation`

#### Description

The `apply_moderation` function takes a row from a pandas DataFrame and a text column name to perform moderation on the specified text. It can optionally extract and return specific category flags and scores from the moderation response.

#### Parameters

- `row` (`pandas.core.series.Series`): A single row of data from a pandas DataFrame. This row should contain the text to be moderated along with any other relevant information.
- `text_col_name` (`str`): The name of the column within the row that contains the text to be moderated. Defaults to `"response"`.
- `moderation_model` (`str`): The identifier for the OpenAI moderation model to be used. Defaults to `"text-moderation-latest"`.
- `category_names` (`Optional[list[str]]`): A list of category names for which flags should be extracted from the moderation response and added to the result. This parameter is optional.
- `category_score_names` (`Optional[list[str]]`): A list of category names for which scores should be extracted from the moderation response and added to the result. This parameter is optional.

#### Returns

- `Union[bool, dict]`: The function returns a boolean flag indicating whether the text violates any of OpenAI's usage policies if neither `category_names` nor `category_score_names` are provided. If either of these parameters is provided, it returns a dictionary with keys corresponding to the specified categories and their respective flags or scores, as well as a `moderation_flag` key indicating the overall moderation result.

#### Behavior

1. The function extracts the text to be moderated from the specified column in the input row.
2. It calls the `openai.moderations.create` method with the moderation model and the text to be moderated.
3. The moderation response is parsed to determine if the text has been flagged as violating policies.
4. If `category_names` is provided, the function extracts flags for the specified categories from the moderation response and adds them to the result dictionary.
5. If `category_score_names` is provided, the function extracts scores for the specified categories from the moderation response and adds them to the result dictionary.
6. If either `category_names` or `category_score_names` is provided, the result dictionary also includes the overall moderation flag. Otherwise, only the boolean moderation flag is returned.

#### Example Usage

python
import pandas as pd
from prompttools.utils.moderation import apply_moderation

# Assuming df is a pandas DataFrame with a 'response' column that contains text to be moderated
row = df.iloc[0]  # Get the first row of the DataFrame
moderation_result = apply_moderation(
    row=row,
    text_col_name="response",
    category_names=["harassment", "violence"],
    category_score_names=["harassment", "violence"]
)

# moderation_result will be a dictionary with keys 'harassment', 'violence', 'harassment_score', 'violence_score', and 'moderation_flag'


## Dependencies

- `openai`: The OpenAI Python client library used to interact with the OpenAI API.
- `pandas`: A powerful data manipulation library used for handling the input data row.

## License

The source code is licensed under the license found in the LICENSE file in the root directory of this source tree, and the copyright belongs to Hegel AI, Inc.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/autoeval_with_docs.md

# autoeval_with_docs.py

## Overview

The `autoeval_with_docs.py` module is part of the `prompttools` package and provides functionality to automatically evaluate the accuracy of a response given a set of documents using a language model such as GPT-4. It is designed to be used within a larger project that requires the assessment of text responses against provided context.

## Functions

### `_get_messages`

python
def _get_messages(documents: list[str], response: str):


#### Description

This private function generates a formatted message for the evaluation system and the user's response using the Jinja2 templating engine.

#### Parameters

- `documents` (list[str]): A list of strings, each representing a document that provides context for the evaluation.
- `response` (str): The response text that needs to be evaluated for accuracy.

#### Returns

- A list of dictionaries, each containing a `role` key (either `"system"` or `"user"`) and a `content` key with the corresponding message content.

#### Usage

This function is used internally to prepare the input for the OpenAI chat model.

### `compute`

python
def compute(documents: list[str], response: str, model: str = "gpt-4") -> float:


#### Description

This function uses an OpenAI chat model, such as GPT-4, to evaluate the accuracy of a response given a set of documents. It returns an integer score representing the accuracy.

#### Parameters

- `documents` (list[str]): A list of documents providing context for the evaluation.
- `response` (str): The response text to be evaluated.
- `model` (str, optional): The identifier for the OpenAI chat model to use. Defaults to `"gpt-4"`.

#### Returns

- An integer score from 0 to 10, where 0 indicates extreme inaccuracy and 10 indicates perfect accuracy.

#### Exceptions

- Raises `PromptToolsUtilityError` if the `OPENAI_API_KEY` environment variable is not set.

#### Usage

This function is called to compute the accuracy score of a response based on the provided documents.

### `autoeval_with_documents`

python
def autoeval_with_documents(
    row: pandas.core.series.Series,
    documents: list[str],
    response_column_name: str = "response",
) -> float:


#### Description

This function scores the accuracy of a model's response given a list of documents, using GPT-4 as the evaluator. It is designed to be used with a pandas DataFrame where each row contains a model response and other data.

#### Parameters

- `row` (pandas.core.series.Series): A row from a pandas DataFrame, which includes the model response and potentially other data.
- `documents` (list[str]): A list of documents that provide context for the evaluation.
- `response_column_name` (str, optional): The name of the column in the DataFrame that contains the model's response. Defaults to `"response"`.

#### Returns

- An integer score from 0 to 10, representing the accuracy of the response.

#### Usage

This function is typically used within a DataFrame apply operation to score each row's response based on the provided documents.

## Dependencies

- `os`: To access environment variables.
- `openai`: To interact with the OpenAI API.
- `pandas.core.series`: To handle data in a pandas Series format.
- `jinja2`: To use templating for message formatting.
- `.error`: To raise custom errors defined within the `prompttools` package.

## Error Handling

- The module defines a custom error `PromptToolsUtilityError` which is raised when the required `OPENAI_API_KEY` environment variable is not set.

## Constants

- `EVALUATION_SYSTEM_PROMPT`: A string constant that defines the prompt for the evaluation system.
- `EVALUATION_USER_TEMPLATE`: A string constant that defines the template for the user's response using Jinja2 syntax.

## Usage Example

python
import pandas as pd
from prompttools.utils.autoeval_with_docs import autoeval_with_documents

# Example DataFrame with responses
df = pd.DataFrame({
    'response': ["This is a response to evaluate.", "Another response to check."]
})

# Documents providing context
documents = ["Document 1 text.", "Document 2 text."]

# Apply the autoeval_with_documents function to each row
df['accuracy_score'] = df.apply(autoeval_with_documents, axis=1, documents=documents)


In the example above, the `autoeval_with_documents` function is applied to each row of a DataFrame to score the accuracy of the responses based on the provided documents.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/error.md

# `error.py` Module Documentation

## Overview

The `error.py` module is part of the `prompttools` package within the `documentation-generator` project. It defines a custom exception class that is used throughout the `prompttools` utility to handle error scenarios specific to the utility's operations.

## Classes

### `PromptToolsUtilityError`

#### Description

`PromptToolsUtilityError` is a custom exception class that inherits from Python's built-in `Exception` class. This custom exception is designed to be raised when an error occurs within the `prompttools` utility that is not adequately described by Python's standard exceptions.

#### Usage

The `PromptToolsUtilityError` class is intended to be used in the following manner:

1. The class is imported into other modules within the `prompttools` utility where error handling is required.
2. When an error condition is encountered that is specific to the `prompttools` utility's functionality, an instance of `PromptToolsUtilityError` is raised with an appropriate error message.
3. The raised `PromptToolsUtilityError` can be caught and handled by the calling code, allowing for graceful degradation of the utility or user notification of the issue.

#### Example

python
from prompttools.utils.error import PromptToolsUtilityError

def some_function():
    try:
        # Code that may cause a specific error related to prompttools
        ...
    except SomeSpecificError as e:
        # Handle specific error and raise custom exception
        raise PromptToolsUtilityError("An error occurred in prompttools: " + str(e))


In this example, `some_function` is a hypothetical function within the `prompttools` utility. If a specific error occurs, it is caught, and a `PromptToolsUtilityError` is raised with additional context about the error.

## File Metadata

- **License**: The source code's license information is specified to be in the `LICENSE` file located in the root directory of the source tree. Users of this module should refer to that file for the full license text.
- **Copyright**: The copyright notice at the beginning of the file indicates that Hegel AI, Inc. holds the copyright for this code.

## Conclusion

The `error.py` module provides a mechanism for consistent error handling within the `prompttools` utility, allowing developers to raise and handle errors that are specific to the utility's domain.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/__init__.md

# `prompttools.utils` Module

## Overview

The `prompttools.utils` module is a collection of utility functions and submodules designed to support various operations such as automatic evaluation, validation, moderation, and similarity computation within the `documentation-generator` project. This module is part of the `prompttools` package, which is likely used for generating or processing documentation based on prompts.

## Submodules and Functions

### Submodules

- `autoeval`: Contains functions for automatic evaluation of responses.
- `expected`: Provides functionality to handle expected responses.
- `validate_json`: Includes functions to validate JSON responses.
- `validate_python`: Contains functions to validate Python code responses.
- `similarity`: Offers methods to compute semantic similarity.

### Functions

- `autoeval_binary_scoring`: A function that performs binary scoring for automatic evaluation.
- `autoeval_from_expected_response`: A function that automatically evaluates a response based on an expected response.
- `autoeval_scoring`: A function that calculates a score for automatic evaluation.
- `autoeval_with_documents`: A function that performs automatic evaluation in the context of documents.
- `chunk_text`: A utility function that breaks down text into manageable chunks.
- `compute_similarity_against_model`: A function that computes similarity against a model's output.
- `apply_moderation`: A function that applies moderation rules to content.
- `ranking_correlation`: A function that calculates the correlation between different rankings.
- `semantic_similarity`: A function that computes the semantic similarity between pieces of text.
- `validate_json_response`: A function that validates a JSON response for correctness.
- `validate_python_response`: A function that validates a Python code response for correctness.

## Usage

The functions and submodules within `prompttools.utils` are likely used throughout the `documentation-generator` project to perform tasks such as:

- Automatically scoring generated documentation against a set of criteria or expected outputs.
- Validating the structure and content of JSON and Python responses to ensure they meet project requirements.
- Moderating content to filter out inappropriate or unwanted material.
- Computing the similarity between different pieces of text, which can be useful for tasks like detecting plagiarism or ensuring content uniqueness.
- Chunking large texts into smaller parts for easier processing or analysis.

## Importing

The module exposes its submodules and functions through the `__init__.py` file, allowing for convenient importing within the project. For example, to use the `semantic_similarity` function, one would import it as follows:

python
from prompttools.utils import semantic_similarity


## `__all__` Variable

The `__all__` variable is defined to explicitly declare the exported names from the module. This list includes all the submodules and functions that are intended to be used when importing `prompttools.utils` using the `from prompttools.utils import *` syntax. This ensures that only the specified names are imported and prevents any unintended names from being exposed.

## Licensing

The module includes a header comment indicating that the source code is copyrighted by Hegel AI, Inc. and that the license for the source code can be found in the LICENSE file located in the root directory of the source tree. This suggests that the module is proprietary and its use is subject to the terms of the license.

## Conclusion

The `prompttools.utils` module is a central part of the `documentation-generator` project, providing essential tools for automatic evaluation, validation, moderation, and similarity computation. Its well-defined interface allows for easy integration within the project, facilitating the generation and processing of documentation based on prompts.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/utils/chunk_text.md

# `chunk_text.py` Module

## Overview

The `chunk_text.py` module contains a single function `chunk_text` which is designed to split a given string of text into smaller chunks. These chunks are constrained by a specified maximum length, ensuring that no individual chunk exceeds this length. The function is careful to avoid breaking words across chunks, preserving whole words within the boundaries of each chunk.

## Function: `chunk_text`

### Description

The `chunk_text` function takes a string of text and divides it into a list of smaller strings, or "chunks", based on a specified maximum length for each chunk. The function ensures that words are not split across chunks by only breaking the text at spaces.

### Usage

The function is used when there is a need to process or display long strings of text in smaller, more manageable parts. This can be particularly useful in scenarios where there are constraints on the amount of text that can be processed or displayed at once, such as in user interfaces, text processing pipelines, or when interfacing with APIs that have a limit on the size of text input.

### Arguments

- `text` (`str`): The source text that needs to be chunked. This argument takes a string that represents a paragraph or any long form of text.
- `max_chunk_length` (`int`): The maximum allowed length for each chunk. This integer value determines the upper limit on the size of each chunk of text.

### Returns

- `list[str]`: A list of strings, where each string is a chunk of the original text. Each chunk is guaranteed to be less than or equal to the specified `max_chunk_length`, and words are not split across chunks.

### Algorithm

1. The input text is split into words based on spaces using the `split()` method.
2. An empty list called `chunks` is initialized to store the resulting chunks of text.
3. A temporary string `current_chunk` is used to build each chunk.
4. The function iterates over each word in the split text:
   - If adding the next word to `current_chunk` (including a space if `current_chunk` is not empty) does not exceed `max_chunk_length`, the word is appended to `current_chunk`.
   - If adding the next word would exceed `max_chunk_length`, the current `current_chunk` is added to the `chunks` list, and `current_chunk` is reset to the current word.
5. After the loop, if `current_chunk` contains any text, it is appended to the `chunks` list to ensure the last chunk is not lost.
6. The `chunks` list is returned.

### Example

python
text_to_chunk = "This is an example of a long text that needs to be chunked into smaller parts."
max_length = 20
chunks = chunk_text(text_to_chunk, max_length)
print(chunks)
# Output: ['This is an example', 'of a long text that', 'needs to be chunked', 'into smaller parts.']


### Notes

- The function assumes that the input text does not contain words longer than `max_chunk_length`. If such a word exists, it will be placed in its own chunk, potentially exceeding the maximum length.
- The function does not account for punctuation or special characters when determining word boundaries; it simply uses spaces to identify words.
- The function is designed to be used with text data and may not be suitable for binary or non-text content.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/logger/logger.md

# Logger Module

## Overview

The `logger.py` module is part of the `prompttools` package, specifically within the `logger` subpackage. It provides functionality for logging and sending feedback data to a remote backend service. The module includes a `Logger` class that handles the queuing and asynchronous transmission of log data, as well as a logging wrapper function for the OpenAI API client.

## Dependencies

- `json`: Used for encoding data into JSON format.
- `uuid`: Generates unique identifiers for log entries.
- `requests`: Sends HTTP requests to the remote backend service.
- `threading`: Manages concurrent execution of the logging process.
- `queue`: Provides a thread-safe queue for storing log data.
- `functools.partial`: Used to create a partial function with pre-filled arguments.
- `openai`: The OpenAI API client library.
- `os`: Accesses environment variables.
- `dotenv`: Loads environment variables from a `.env` file.
- `os.path`: Handles file path operations.
- `time.perf_counter`: Measures execution time for performance monitoring.
- `prompttools.common`: Contains common utilities and configurations, such as the backend URL.

## Logger Class

### Attributes

- `backend_url`: The URL endpoint for sending log data to the remote backend service.
- `data_queue`: A thread-safe queue for storing log data before it is sent.
- `feedback_queue`: A thread-safe queue for storing feedback data before it is sent.
- `worker_thread`: A thread that processes and sends data from the queues to the backend.

### Methods

- `__init__`: Initializes the logger instance, starts the worker thread, and ensures the worker thread stops when the main thread ends.
- `add_feedback`: Adds feedback data to the `feedback_queue`.
- `add_to_queue`: Adds log data to the `data_queue`.
- `execute_and_add_to_queue`: Executes a callable function, measures its latency, and adds the result to the log queue.
- `wrap`: Wraps a callable function so that its execution is logged.
- `worker`: Continuously processes data from the `data_queue` and `feedback_queue`, sending it to the remote backend.
- `log_data_to_remote`: Sends log data to the remote backend service.
- `send_feedback_to_remote`: Sends feedback data to the remote backend service.

### Usage

- The `Logger` class is instantiated as a global `sender` object.
- The `worker` method runs in a separate thread to handle asynchronous logging.

## Logging Wrapper Function

- `logging_wrapper`: A decorator function that wraps the OpenAI API client's methods to log their execution and results.

### Usage

- The `logging_wrapper` is applied to the `openai.chat.completions.create` method to log calls to the OpenAI API.

## Monkey-Patching

- The module attempts to monkey-patch the `openai.chat.completions.create` method and the `openai.resources.chat.completions.Completions.create` method of the OpenAI API client with the logging functionality provided by the `Logger` class and the `logging_wrapper` function.

## Feedback Function

- `add_feedback`: A convenience function that allows external modules to add feedback data to the logger.

## Environment Variables

- The module loads the `OPENAI_API_KEY` environment variable from a `.env` file located relative to the module's file path.

## Error Handling

- The module includes error handling for issues that may arise during the monkey-patching process or when sending data to the remote backend service.

## Backend Service Communication

- The logger communicates with the backend service defined by `HEGEL_BACKEND_URL` using HTTP POST requests with appropriate headers, including authorization using the `HEGELAI_API_KEY` environment variable.

## Performance Monitoring

- The module measures the latency of function calls to provide performance metrics as part of the logged data.

## Shutdown Mechanism

- A shutdown mechanism is implemented by inserting `None` into the queues, signaling the worker thread to terminate when the main thread joins (i.e., when the program is exiting).

## Thread Safety

- The module ensures thread safety by using queues and threading mechanisms to manage concurrent access to shared resources.

## Extensibility

- The `Logger` class and the `logging_wrapper` function are designed to be easily applied to other callable functions or methods that require logging, making the module extensible for various use cases within the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/logger/__init__.md

# `logger` Module

## Overview

The `logger` module provides logging functionality for the project. It is designed to facilitate the creation of log messages and potentially collect user feedback. The module is contained within the `prompttools/logger` directory.

## Components

The module consists of the following components:

- `Logger`: A class that encapsulates the logging logic.
- `add_feedback`: A function that allows for the addition of user feedback to the logs.

## Usage

### Importing

To use the `logger` module in the project, the relevant classes and functions must be imported:

python
from prompttools.logger import Logger, add_feedback


### `Logger` Class

#### Description

The `Logger` class is responsible for creating log messages. It likely includes methods to log at different levels (e.g., info, warning, error) and to handle the formatting and output of log messages.

#### Methods

The class may include, but is not limited to, the following methods:

- `__init__`: Initializes a new instance of the `Logger` class.
- `info`: Logs an informational message.
- `warning`: Logs a warning message.
- `error`: Logs an error message.
- `debug`: Logs a debug message.

#### Example

python
logger = Logger()
logger.info("This is an informational message.")


### `add_feedback` Function

#### Description

The `add_feedback` function is used to collect and log user feedback. This function may be called when the application needs to record the user's input or reactions, possibly for analytics or improvement purposes.

#### Parameters

The function likely takes parameters that include the feedback message and any relevant metadata.

#### Example

python
add_feedback("User found the interface intuitive.", user_id=12345)


## `__all__` Declaration

The `__all__` list in the `__init__.py` file specifies the public API of the module, indicating which components should be available when the module is imported using the `from prompttools.logger import *` syntax.

## File Structure

The `__init__.py` file is located at:


/workspaces/documentation-generator/target_code/prompttools/logger/__init__.py


This file is part of the `prompttools` package and specifically within the `logger` subpackage.

## Licensing

The source code is copyrighted by Hegel AI, Inc. and is subject to the terms of the license found in the LICENSE file in the root directory of this source tree.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/__init__.md

# `__init__.py` Module in `experiment` Package

## Overview

The `__init__.py` file serves as the initialization module for the `experiment` package within the `prompttools` namespace of the `documentation-generator` project. This file imports various experiment classes from submodules and makes them available for use throughout the project. It also defines the `__all__` list, which explicitly specifies the symbols that are exported when `from experiment import *` is used.

## Imports

The module imports the following experiment classes from their respective submodules within the `experiments` package:

- `Experiment`: A base class for experiments, likely providing common interfaces or methods for derived experiment classes.
- `OpenAIChatExperiment`: A class for conducting experiments with OpenAI's chat models.
- `OpenAICompletionExperiment`: A class for running experiments using OpenAI's text completion models.
- `AnthropicCompletionExperiment`: A class for experiments involving Anthropic's completion models.
- `HuggingFaceHubExperiment`: A class for experiments that interact with models available on Hugging Face's model hub.
- `GoogleGeminiChatCompletionExperiment`: A class for experiments with Google's Gemini chat and completion models.
- `GooglePaLMCompletionExperiment`: A class for experiments using Google's PaLM completion models.
- `GoogleVertexChatCompletionExperiment`: A class for experiments with Google's Vertex chat models.
- `LlamaCppExperiment`: A class for experiments involving Llama C++ models.
- `ChromaDBExperiment`: A class for experiments with the ChromaDB database.
- `WeaviateExperiment`: A class for experiments using the Weaviate vector search engine.
- `LanceDBExperiment`: A class for experiments involving the LanceDB database.
- `MistralChatCompletionExperiment`: A class for experiments with Mistral's chat and completion models.
- `MindsDBExperiment`: A class for experiments with MindsDB, an open-source predictive database.
- `SequentialChainExperiment`: A class for experiments that involve sequential chaining of models or operations.
- `RouterChainExperiment`: A class for experiments that involve routing between different models or operations based on certain criteria.
- `StableDiffusionExperiment`: A class for experiments with the Stable Diffusion model, likely related to image generation.
- `ReplicateExperiment`: A class for experiments that involve replication of models or data.
- `QdrantExperiment`: A class for experiments with the Qdrant vector search engine.
- `PineconeExperiment`: A class for experiments using Pinecone, a vector database for machine learning applications.

## Exported Symbols

The `__all__` list defines the symbols that are exported when the `experiment` package is imported using the `from experiment import *` syntax. This list includes the names of all the imported experiment classes, ensuring that they are accessible to other modules within the project.

## Usage

Other modules within the `documentation-generator` project can import the `experiment` package and use the experiment classes directly. For example:

python
from prompttools.experiment import OpenAIChatExperiment

# Initialize an experiment with OpenAI's chat model
experiment = OpenAIChatExperiment(...)


This allows for a clean and organized structure where experiment-related classes are encapsulated within the `experiment` package and can be easily reused across the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/widgets/feedback.md

# FeedbackWidgetProvider Class

## Overview

The `FeedbackWidgetProvider` class is designed to provide interactive widgets for evaluating models within an IPython environment, such as Jupyter notebooks. It facilitates the display of evaluation widgets, collection of feedback, and aggregation of evaluation results.

## Attributes

- `completion_fn`: A callable that is executed upon completion of feedback collection.
- `agg_fn`: A callable that aggregates feedback data.
- `eval_listener_fn`: A callable that listens for evaluation events (e.g., when feedback is provided).
- `pivot_columns`: A list of strings representing the column names used for pivoting data in the feedback table.

## Methods

### `__init__(self, completion_fn, agg_fn, eval_listener_fn)`

Constructor for the `FeedbackWidgetProvider` class.

- `completion_fn`: A callable that is executed upon completion of feedback collection.
- `agg_fn`: A callable that aggregates feedback data.
- `eval_listener_fn`: A callable that listens for evaluation events (e.g., when feedback is provided).

### `_get_feedback_submission_listener(self, table: pd.DataFrame, pivot_columns: List[str]) -> Callable`

Private method that returns a callback function to be executed when the submit button is clicked.

- `table`: A pandas DataFrame containing the data to be evaluated.
- `pivot_columns`: A list of strings representing the column names used for pivoting data in the feedback table.

The callback function sorts the feedback scores using the `agg_fn`, creates a new DataFrame with the sorted scores, and displays it using IPython's `display` function.

### `set_pivot_columns(self, pivot_columns: List[str]) -> None`

Sets the pivot columns used for displaying and aggregating feedback data.

- `pivot_columns`: A list of strings representing the column names to be used.

### `get_header_widgets(self) -> List[object]`

Returns a list of `ipywidgets.Label` objects representing the header of the feedback table.

### `get_row_widgets(self, index, row)`

Creates and returns a list of widgets for a single row of the feedback table.

- `index`: The index of the row in the feedback table.
- `row`: A dictionary-like object representing the data in the row.

The method creates HTML widgets for displaying the content of the specified `pivot_columns` and the "response(s)" column. It also creates a dropdown widget for feedback input, which is set to observe evaluation events using the `eval_listener_fn`.

### `get_footer_widgets(self, table)`

Creates and returns a list of widgets for the footer of the feedback table.

- `table`: A pandas DataFrame containing the data to be evaluated.

The method creates a submit button that, when clicked, triggers the feedback submission listener.

### `display(self, items)`

Displays the provided list of widgets in a grid layout.

- `items`: A list of widget objects to be displayed.

The method uses `ipywidgets.GridBox` to create a grid layout and IPython's `display` function to render the grid.

## Usage

The `FeedbackWidgetProvider` class is used within an IPython environment to create an interactive feedback system for model evaluation. It is typically instantiated with the necessary callback functions and then used to generate and display a feedback form with headers, rows for each data point, and a submit button. Users can provide feedback through the interface, and upon submission, the feedback is aggregated and displayed as a DataFrame.

## Dependencies

- `typing`: Provides support for type hints.
- `pandas`: Used for handling data in DataFrame format.
- `IPython`: Provides the display functionality for rendering widgets.
- `ipywidgets`: Used for creating interactive UI elements like labels, dropdowns, and buttons.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/widgets/utility.md

# Utility Module Documentation

## Overview

The `utility.py` module is part of the `prompttools.experiment.widgets` package within the `documentation-generator` project. This module provides utility functions that are used across the experiment widgets subpackage. Currently, it contains a single function `is_interactive()`.

## Function: is_interactive

### Purpose

The `is_interactive` function is designed to check the environment in which the code is running to determine if it is an interactive environment, such as a Jupyter notebook. This is important for the project as it affects how visualizations and interactive widgets are presented to the user.

### Signature

python
def is_interactive() -> bool:


The function signature indicates that `is_interactive` takes no parameters and returns a boolean value.

### Implementation Details

#### Import Statement

python
import __main__ as main


At the beginning of the function, the `__main__` module is imported and aliased as `main`. This module represents the environment in which the top-level script is running.

#### Function Logic

python
return not hasattr(main, "__file__")


The function uses the built-in `hasattr` function to check if the `__main__` module has the attribute `__file__`. The `__file__` attribute is set by the Python interpreter when a script is run as a file. However, in interactive environments like Jupyter notebooks, this attribute is typically not set.

- If `__file__` is not present in the `__main__` module, it implies that the code is running in an interactive environment, and the function returns `True`.
- If `__file__` is present, it implies that the code is running as a script in a non-interactive environment, and the function returns `False`.

### Usage

The `is_interactive` function is used within the `prompttools.experiment.widgets` package to conditionally execute code that is specific to interactive environments. For example, it can be used to decide whether to display inline plots or to use interactive widgets that are only compatible with Jupyter notebooks.

### Example

python
from prompttools.experiment.widgets.utility import is_interactive

if is_interactive():
    # Code specific to Jupyter notebooks or other interactive environments
    pass
else:
    # Code for non-interactive environments
    pass


In the example above, the function is used in a conditional statement to execute different blocks of code based on the environment detected.

## License

The source code's license information for `utility.py` can be found in the `LICENSE` file located in the root directory of the source tree. The copyright notice at the beginning of the file indicates that the code is owned by Hegel AI, Inc. and that all rights are reserved.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/widgets/comparison.md

# ComparisonWidgetProvider Class

## Overview

The `ComparisonWidgetProvider` class is designed to facilitate the comparison of different models within an interactive Jupyter Notebook environment. It provides a user interface for displaying model outputs side by side and collecting user feedback on these outputs.

## Attributes

- `completion_fn`: A callable that is executed when the comparison is complete.
- `agg_fn`: A callable that aggregates the comparison data.
- `eval_listener_fn`: A callable that listens for evaluation events (e.g., user feedback).
- `models`: A list of strings representing the models being compared.
- `row_len`: An integer representing the number of columns in the widget grid, including the input, models, and feedback columns.

## Methods

### `__init__(self, completion_fn, agg_fn, eval_listener_fn)`

The constructor initializes the `ComparisonWidgetProvider` with the provided functions for completion, aggregation, and evaluation listening.

### `_get_comparison_submission_listener(self, table: pd.DataFrame, models: List[str]) -> Callable`

A private method that returns a callable to be used as an event listener for the submit button. When the submit button is clicked, it aggregates the scores using `agg_fn`, creates a DataFrame with the results, and displays it.

### `set_models(self, models: List[str]) -> None`

Sets the `models` attribute with a list of model names and calculates the `row_len` based on the number of models.

### `get_header_widgets(self) -> List[object]`

Returns a list of `ipywidgets.Label` objects to be used as headers in the comparison grid. The headers include "Input", one label for each model, and "Feedback".

### `get_row_widgets(self, index, row)`

Generates a list of widgets for a single row in the comparison grid. The row includes an HTML widget for the input, HTML widgets for each model's output, and a dropdown widget for user feedback.

### `get_footer_widgets(self, table)`

Creates the footer widgets for the comparison grid, which includes a submit button that triggers the comparison submission listener.

### `display(self, items)`

Displays the comparison grid using the provided list of items. It creates a `widgets.GridBox` with a layout that has a column for each element in the grid (input, models, feedback).

## Usage

The `ComparisonWidgetProvider` class is used within a Jupyter Notebook to create an interactive comparison interface. The user can view model outputs and provide feedback, which can then be aggregated and processed for model evaluation.

1. An instance of `ComparisonWidgetProvider` is created with the necessary completion, aggregation, and evaluation listener functions.
2. The `set_models` method is called with a list of model names to set up the comparison grid.
3. The `get_header_widgets`, `get_row_widgets`, and `get_footer_widgets` methods are used to generate the widgets for the comparison grid.
4. The `display` method is called with the list of widgets to render the grid in the notebook.
5. User interactions with the feedback dropdowns trigger the evaluation listener function.
6. Clicking the submit button triggers the aggregation of feedback and displays the results.

## Dependencies

- `typing`: Provides support for type hints.
- `pandas`: Used for handling data in DataFrame format.
- `IPython.display`: Used to display widgets in the Jupyter Notebook.
- `ipywidgets`: Provides interactive widgets for the Jupyter Notebook.

## File Metadata

- **Copyright**: Hegel AI, Inc.
- **License**: The license for the source code can be found in the LICENSE file in the root directory of this source tree.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/widgets/__init__.md

# `__init__.py` in `prompttools/experiment/widgets`

## Overview

The `__init__.py` file within the `prompttools/experiment/widgets` directory serves as an initializer for the `widgets` package, which is a submodule of the `experiment` module within the `prompttools` project. This file can be used to expose specific classes, functions, or variables from within the package, making them directly accessible when the package is imported elsewhere in the project.

## Usage

When the `widgets` package is imported, Python will execute the contents of the `__init__.py` file. The presence of this file makes the directory a Python package, and it can be used to perform package initialization tasks such as setting up package-level variables, importing necessary modules, or running any startup code required by the package.

### Importing the Package

To import the `widgets` package from another module within the `prompttools` project, you would use the following import statement:

python
from prompttools.experiment.widgets import SomeWidget


Assuming `SomeWidget` is a class or function defined within the `widgets` package and made available through the `__init__.py` file.

### Package Initialization

The `__init__.py` file can include initialization code. For example:

python
# __init__.py content
print("Initializing widgets package")

# Import a specific widget from a module within the package
from .cool_widget import CoolWidget

# Define a package-level variable
widget_count = 0


With this setup, when the `widgets` package is imported, it will print "Initializing widgets package" to the console, import the `CoolWidget` class for use elsewhere, and define a `widget_count` variable that can be accessed as `prompttools.experiment.widgets.widget_count`.

## Structure

The structure of the `__init__.py` file can vary depending on the needs of the package. It may simply consist of import statements to bring in components from submodules, or it may include more complex initialization code.

### Example Structure

python
# Import submodule classes/functions
from .widget_a import WidgetA
from .widget_b import WidgetB

# Package-level constants
DEFAULT_WIDGET_SIZE = (100, 100)

# Initialization code
def _init_widgets():
    # Perform any necessary setup for the widgets
    pass

# Execute initialization function
_init_widgets()


In this example, the `__init__.py` file imports `WidgetA` and `WidgetB` from their respective modules within the `widgets` package, defines a constant `DEFAULT_WIDGET_SIZE`, and includes a private function `_init_widgets` that is called to perform any necessary initialization tasks.

## Best Practices

- Keep the `__init__.py` file as simple as possible; it should primarily be used for import management and minimal package setup.
- Avoid complex logic in the `__init__.py` file to prevent side effects during the import process.
- Use relative imports (e.g., `.cool_widget`) to maintain package encapsulation and avoid dependency issues.

## Conclusion

The `__init__.py` file in the `prompttools/experiment/widgets` directory is a crucial component for package initialization and management within the Python project. It dictates how the package is presented to the rest of the project and can simplify the import process for package consumers.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/experiment.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/huggingface_endpoint_experiment.md

# Huggingface Endpoint Experiment Module

## Overview

The `huggingface_endpoint_experiment.py` module is designed to facilitate experiments with Hugging Face's machine learning models. It provides a structured way to interact with Hugging Face's API endpoints, allowing users to send requests to the models hosted on the Hugging Face platform and receive predictions or other outputs.

## Usage

This module is used within a larger project to conduct experiments on the performance, accuracy, and behavior of various Hugging Face models. It is typically imported and utilized by other scripts or modules that are responsible for orchestrating experiments, collecting data, and analyzing results.

## Functionality

As of the current version, the module's specific functionality has not been implemented, indicated by the `# TODO: Coming soon` comment. However, based on the module's name and typical use cases for Hugging Face models, we can infer the intended functionality:

1. **API Interaction**: The module will likely contain functions to handle the construction and sending of HTTP requests to Hugging Face's API endpoints.
2. **Authentication**: It may include methods for authenticating with the Hugging Face API, possibly using API tokens.
3. **Data Handling**: Functions to format input data into a structure that is compatible with the API's expected request format and to parse the response data will probably be part of the module.
4. **Experiment Configuration**: The module might allow users to specify parameters for the experiment, such as the model to be used, the dataset, and any hyperparameters.
5. **Result Analysis**: It could provide tools for analyzing the results of the experiment, such as calculating accuracy, generating confusion matrices, or other relevant metrics.
6. **Logging**: The module may include logging capabilities to track the progress of experiments and to record any errors or important information.

## Integration

The module is expected to be integrated into the `experiment` package within the `prompttools` namespace. This suggests that it is part of a collection of tools designed for conducting experiments with prompt-based models or tools.

## License

The module is proprietary software, as indicated by the copyright notice at the top of the file. The license details are available in the `LICENSE` file located in the root directory of the source tree, which must be reviewed to understand the terms under which the module can be used or modified.

## Future Development

The `# TODO: Coming soon` comment indicates that the module is under development and that its detailed implementation is pending. Future updates to the module will likely add the necessary classes, functions, and logic to perform the intended experiments with Hugging Face models.

## File Location

The file is located at `/workspaces/documentation-generator/target_code/prompttools/experiment/experiments/huggingface_endpoint_experiment.py` within the project's directory structure, suggesting that it is part of a larger documentation generator or a similar toolset aimed at facilitating machine learning experiments and analysis.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/openai_completion_experiment.md

## OpenAICompletionExperiment Class

### Overview
The `OpenAICompletionExperiment` class is designed to facilitate experiments with OpenAI's completion API. It allows users to pass lists of parameters to the API and performs a cartesian product of these parameters to test different combinations. The class is part of a larger project that includes a module for selecting prompts and a mock function for simulating OpenAI completions.

### Initialization
The `__init__` method initializes the `OpenAICompletionExperiment` class with a variety of parameters that correspond to the options available in the OpenAI API for text completions.

#### Parameters
- `model`: A list of strings representing the model IDs to be used for the completions.
- `prompt`: A list of strings or a list of `PromptSelector` objects representing the prompts for which completions will be generated.
- `suffix`: An optional list of strings representing the suffixes to append after the completion. Defaults to `[None]`.
- `max_tokens`: An optional list of integers specifying the maximum number of tokens to generate. Defaults to `[float("inf")]`.
- `temperature`: An optional list of floats that control the randomness of the output. Defaults to `[1.0]`.
- `top_p`: An optional list of floats for nucleus sampling. Defaults to `[1.0]`.
- `n`: An optional list of integers indicating the number of completions to generate for each input. Defaults to `[1]`.
- `stream`: An optional list of booleans indicating whether to stream partial completions. Defaults to `[False]`.
- `logprobs`: An optional list of integers specifying the number of log probabilities to include. Defaults to `[None]`.
- `echo`: An optional list of booleans indicating whether to echo the prompt with the completion. Defaults to `[False]`.
- `stop`: An optional list of lists of strings specifying sequences where the API should stop generating tokens. Defaults to `[None]`.
- `presence_penalty`: An optional list of floats for penalizing new tokens based on their presence. Defaults to `[0.0]`.
- `frequency_penalty`: An optional list of floats for penalizing new tokens based on their frequency. Defaults to `[0.0]`.
- `best_of`: An optional list of integers for generating multiple completions and returning the best. Defaults to `[1]`.
- `logit_bias`: An optional list of dictionaries for modifying the likelihood of specific tokens. Defaults to `[None]`.
- `azure_openai_service_configs`: An optional dictionary for configuring the use of Azure OpenAI Service. Defaults to `None`.

### Attributes
- `completion_fn`: The function used to create completions. Defaults to `openai.completions.create` but can be overridden with a mock function for testing.
- `prompt_keys`: A dictionary mapping prompts to their keys, used when `PromptSelector` objects are provided.
- `all_args`: A dictionary containing all the arguments that will be passed to the OpenAI API.

### Methods
- `_extract_responses`: A static method that extracts the text from the completion choices returned by the OpenAI API.
- `_get_model_names`: A method that retrieves the model names from the argument combinations generated for the experiment.

### Usage
To use the `OpenAICompletionExperiment` class, instantiate it with the desired parameters and then call its methods to perform the experiment. The class handles the creation of all possible combinations of parameters and interacts with the OpenAI API to generate completions based on these combinations.

### Notes
- The class assumes that all parameters are provided as lists, even if a single value is desired (e.g., `temperature=[1.0]`).
- If the `DEBUG` environment variable is set, the class will use a mock completion function instead of the actual OpenAI API.
- Certain parameters (`echo`, `logit_bias`, `best_of`) are removed from the `all_args` dictionary if they are set to their default values, as they are not supported by the `gpt-3.5-turbo` model.
- If `azure_openai_service_configs` is provided, the class will configure the OpenAI API to use Azure OpenAI Service instead of the standard OpenAI service.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/stablediffusion_experiment.md

# StableDiffusionExperiment Class

## Overview
`StableDiffusionExperiment` is a class that extends the `Experiment` class, designed to facilitate experimentation with the Stable Diffusion model. It allows for the generation of images based on textual prompts using the Stable Diffusion model and provides functionality to compare the generated images with a set of reference images.

## Dependencies
- `os`: Standard library module for interacting with the operating system.
- `typing`: Module for type hints.
- `itertools`: Module for creating iterators for efficient looping.
- `time.perf_counter`: Function for timing code execution.
- `logging`: Module for logging events.
- `cv2`: OpenCV module for image processing tasks.
- `diffusers`: Library that provides diffusion models including Stable Diffusion.
- `prompttools.mock.mock`: Module containing mock functions for testing.

## Class Attributes
- `MODEL_PARAMETERS`: A list of parameters specific to the model configuration.
- `CALL_PARAMETERS`: A list of parameters used when calling the model to generate images.

## Constructor
The constructor takes the following arguments:
- `hf_model_path`: A list of strings specifying the paths to the model on Hugging Face.
- `prompt`: A list of strings containing prompts for image generation.
- `compare_images_folder`: A string specifying the folder path where comparison images are stored.
- `use_auth_token`: A boolean indicating whether an Hugging Face authentication token is required (necessary when not using a GPU).
- `**kwargs`: A dictionary of additional keyword arguments to configure the model.

The constructor performs the following actions:
1. Checks if the required `diffusers` and `cv2` packages are installed, raising a `ModuleNotFoundError` if not.
2. Initializes instance variables for authentication, image comparison, and model parameters.
3. If in debug mode, sets the completion function to a mock function.
4. Combines model and call parameters into a single dictionary of all arguments.
5. Calls the superclass constructor.

## Methods

### prepare
Prepares combinations of model and call arguments for the experiment by creating Cartesian products of the parameter values.

### sd_completion_fn
A helper function that takes a dictionary of parameters, generates an image using the Stable Diffusion model, and resizes comparison images to match the generated image's size. It returns the main generated image.

### run
Executes the experiment for every combination of model and call arguments. It can run multiple times for each combination, as specified by the `runs` argument. The method performs the following steps:
1. Prepares argument combinations if not already done.
2. Initializes lists for storing results and latencies.
3. Iterates over all model and call argument combinations.
4. Initializes the Stable Diffusion model client with or without an authentication token.
5. Executes the image generation function, measures latency, and stores the results.
6. Constructs result dataframes from the experiment data.

### _extract_responses
A static method that converts the output image to grayscale. This method is used to process the generated images before storing or comparing them.

## Usage
To use the `StableDiffusionExperiment` class, one must instantiate it with the required parameters and then call the `run` method to start the experiment. The class handles the generation of images based on textual prompts and compares them with reference images in the specified folder.

## Exceptions
- `PromptExperimentException`: Custom exception raised if no results are generated during the experiment.

## Notes
- The class assumes that the necessary packages (`diffusers`, `cv2`, etc.) are installed.
- The class is designed to work with GPU acceleration; however, it can also use an authentication token for CPU-based execution.
- The `run` method includes a TODO comment suggesting the implementation of an asynchronous queue for handling the experiment runs.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/google_palm_experiment.md

# GooglePaLMCompletionExperiment Class

## Overview

The `GooglePaLMCompletionExperiment` class is designed to facilitate experiments with Google's PaLM (Pathways Language Model) text generation API. It allows users to pass lists of arguments to the API, creating a cartesian product of those arguments to test various combinations and analyze the generated text output.

## Requirements

- The `google.generativeai` package must be installed to interact with the PaLM API.
- An API key must be set in the environment variable `GOOGLE_PALM_API_KEY` to authenticate requests to the API.

## Attributes

- `completion_fn`: A function that calls the PaLM API to generate text. It points to `mock_palm_completion_fn` if the `DEBUG` environment variable is set, otherwise, it points to `palm_completion_fn`.
- `all_args`: A dictionary containing all the arguments that will be passed to the PaLM API. It includes model, prompt, temperature, candidate_count, max_output_tokens, top_p, top_k, safety_settings, and stop_sequences.

## Methods

### `__init__`

The constructor initializes the experiment with the provided arguments. It validates the presence of the `google.generativeai` package and sets up the completion function based on the debug mode. It also processes prompt selectors if provided.

#### Parameters

- `model`: A list of strings specifying which model to use.
- `prompt`: A list of strings or `PromptSelector` instances for the input text.
- `temperature`: A list of floats controlling the randomness of the output.
- `candidate_count`: A list of integers specifying the maximum number of responses to return.
- `max_output_tokens`: A list of integers defining the maximum number of tokens per candidate.
- `top_p`: A list of floats for nucleus sampling configuration.
- `top_k`: A list of floats for top-k sampling configuration.
- `safety_settings`: A list of `palm.types.SafetySettingDict` for blocking unsafe content.
- `stop_sequences`: A list of strings or iterables of strings that will stop output generation.

### `palm_completion_fn`

This method is a wrapper around the `palm.generate_text` function, which sends the request to the PaLM API with the provided input arguments.

#### Parameters

- `**input_args`: A variable number of keyword arguments that are passed to the PaLM API.

#### Returns

The response from the PaLM API.

### `_extract_responses`

A static method that extracts the generated text responses from the PaLM API's completion response.

#### Parameters

- `completion_response`: A `palm.text.text_types.Completion` object containing the API response.

#### Returns

A list of strings, each representing a generated text response.

### `_get_model_names`

Extracts the model names from the argument combinations prepared for the experiment.

#### Returns

A list of strings, each representing a model name used in the experiment.

### `_get_prompts`

Extracts the prompts from the argument combinations prepared for the experiment.

#### Returns

A list of strings, each representing a prompt used in the experiment.

## Usage

To use the `GooglePaLMCompletionExperiment` class, instantiate it with the desired argument lists and call the methods to perform the text generation experiment. Ensure that the required environment variable for the API key is set and that the `google.generativeai` package is installed and configured correctly.

## Notes

- The class is designed to handle multiple combinations of input arguments, allowing for extensive testing of the PaLM API's capabilities.
- The class assumes that all arguments are provided as lists, even if a single value is used (e.g., `temperature=[1.0]`).
- The class can be extended or modified to include additional methods for analyzing the generated text or for integrating with other components of a project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/mistral_experiment.md

# MistralChatCompletionExperiment Class

## Overview

The `MistralChatCompletionExperiment` class is a subclass of the `Experiment` class, designed to facilitate experiments with Mistral's chat completion API. It allows users to pass lists of arguments to the API, generating a cartesian product of these arguments to test various combinations and retrieve results for each.

## Requirements

- The `mistralai` Python package must be installed. If not present, the class initialization will fail with a `ModuleNotFoundError`.
- An API key for Mistral's API must be set as an environment variable (`MISTRAL_API_KEY`).

## Attributes

- `url`: A class-level attribute that stores the URL endpoint for the Mistral chat completion API.

## Initialization

The constructor of the `MistralChatCompletionExperiment` class takes the following parameters:

- `model`: A list of strings specifying the model(s) to use for prompt completion (e.g., "mistral-tiny").
- `messages`: A list of `ChatMessage` objects representing the input prompts. The first prompt role should be `user` or `system`.
- `temperature`: An optional list of floats that control the randomness of the response. Defaults to `[None]`.
- `top_p`: An optional list of floats for nucleus sampling. Defaults to `[None]`.
- `max_tokens`: A list of integers or `None` values indicating the maximum number of tokens to generate in the completion.
- `safe_prompt`: A list of booleans indicating whether to prepend a safety prompt before all conversations. Defaults to `[False]`.
- `random_seed`: An optional list of integers or `None` values for deterministic random sampling. Defaults to `[None]`.

During initialization, the constructor:

1. Checks if the `mistralai` package is installed and raises an error if it is not.
2. Initializes a `MistralClient` with the API key from the environment variable.
3. Sets the `completion_fn` attribute to the instance method `mistral_completion_fn`.
4. Stores all constructor arguments in the `all_args` dictionary.
5. Calls the superclass constructor to complete the initialization.

## Methods

### mistral_completion_fn

This instance method takes keyword arguments (`**input_args`) and passes them to the `chat` method of the `MistralClient` instance. It returns the response from the API call.

### _extract_responses

A static method that extracts the content of the messages from the API response. It takes a `response` object and returns a list of strings containing the message contents.

### _get_model_names

An instance method that retrieves the model names from the argument combinations generated for the experiment. It returns a list of model names.

### _get_prompts

An instance method that retrieves the prompts from the argument combinations generated for the experiment. It returns a list of prompts.

## Usage

To use the `MistralChatCompletionExperiment` class in a project:

1. Ensure the `mistralai` package is installed and the `MISTRAL_API_KEY` environment variable is set.
2. Instantiate the class with the desired parameters.
3. Call the `run` method inherited from the `Experiment` superclass to execute the experiment with all combinations of arguments.
4. Use the `_extract_responses` method to process the results from the experiment.

## Notes

- All constructor arguments except `model` and `messages` have default values, allowing them to be optional.
- The `temperature`, `top_p`, `max_tokens`, and `random_seed` parameters accept `None` to indicate the use of default behavior in the API.
- The `safe_prompt` parameter is a boolean that determines whether a safety prompt is used, which can be important for content moderation.
- The class is designed to work with the cartesian product of input arguments, meaning that it will try every possible combination of the provided lists.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/google_vertex_chat_experiment.md

# GoogleVertexChatCompletionExperiment Class

## Overview

The `GoogleVertexChatCompletionExperiment` class is designed to facilitate experiments with Google Vertex AI's chat API. It inherits from the `Experiment` base class and is used to test different configurations of chat model parameters by creating a cartesian product of the provided argument lists. The class then retrieves results for each combination of arguments.

## Requirements

- The `vertexai` package must be installed to use the Google Vertex AI API within this experiment.
- Google Vertex AI credentials must be set up properly before executing this experiment.

## Attributes

- `completion_fn`: A reference to the `vertex_chat_completion_fn` method, which is used to send messages to the chat model and receive responses.
- `all_args`: A dictionary containing all the arguments that will be passed to the chat model. These arguments include `model`, `message`, `context`, `examples`, `temperature`, `max_output_tokens`, `top_p`, `top_k`, and `stop_sequences`.

## Constructor Arguments

- `model`: A list of strings or `types.Model` objects specifying which chat model to use.
- `message`: A list of strings representing the messages for the chat model to respond to.
- `context`: An optional list of strings that shape how the model responds throughout the conversation.
- `examples`: An optional list of `InputOutputTextPair` lists that provide examples for the model to learn from.
- `temperature`: An optional list of floats controlling the randomness of the output.
- `max_output_tokens`: An optional list of integers specifying the maximum number of tokens in a candidate response.
- `top_p`: An optional list of floats configuring the nucleus sampling for the chat model.
- `top_k`: An optional list of integers setting the maximum number of tokens to sample from on each step.
- `stop_sequences`: An optional list of strings or iterables of strings that, when detected, will stop the generation of output.

## Methods

### `vertex_chat_completion_fn`

This method is responsible for creating a chat model instance using the provided `model` name, sending a `message` to the model, and returning the model's response. It takes care of copying the input arguments, excluding `model` and `message`, and passing them to the `start_chat` method of the `ChatModel`.

#### Parameters

- `**input_args`: A variable number of keyword arguments that are used to configure the chat model.

#### Returns

- The response from the chat model after sending the message.

### `_extract_responses`

A static method that extracts the top response from the chat model's output.

#### Parameters

- `response`: The response object from the chat model.

#### Returns

- A list of strings containing the top response from the chat model.

### `_get_model_names`

This method retrieves a list of model names from the argument combinations generated for the experiment.

#### Returns

- A list of strings representing the model names used in the experiment.

### `_get_prompts`

This method retrieves a list of prompts (messages) from the argument combinations generated for the experiment.

#### Returns

- A list of strings representing the prompts used in the experiment.

## Usage

To use the `GoogleVertexChatCompletionExperiment` class, instantiate it with the required lists of arguments, ensuring that each argument is provided as a list to allow for the creation of argument combinations. Once instantiated, the experiment can be run to test the chat model's responses across the different configurations.

## Notes

- The class assumes that all arguments are provided as lists, even if a single value is to be tested (e.g., `temperature=[1.0]`).
- The class will raise a `ModuleNotFoundError` if the `vertexai` package is not installed.
- The class does not handle the setup of Google Vertex AI credentials, which must be done prior to using the class.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/chromadb_experiment.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/mindsdb_experiment.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/google_gemini_chat_experiment.md

# GoogleGeminiChatCompletionExperiment Class

## Overview

The `GoogleGeminiChatCompletionExperiment` class is designed to facilitate experiments with Google's Generative AI chat API, specifically through the Vertex AI platform. It allows users to test various configurations of the chat model by creating a cartesian product of provided argument lists and obtaining results for each combination.

## Dependencies

- The class relies on the `google-generativeai` package, which must be installed prior to usage. If the package is not found, the class initialization will raise a `ModuleNotFoundError`.

## Attributes

- `completion_fn`: A reference to the instance method `google_text_completion_fn`, which is responsible for making API calls to the Google GenAI service.
- `all_args`: A dictionary holding all the arguments that will be used to create the cartesian product for the experiment. It includes `model`, `contents`, `generation_config`, and `safety_settings`.

## Methods

### `__init__(self, model, contents, generation_config, safety_settings)`

The constructor for the `GoogleGeminiChatCompletionExperiment` class.

#### Parameters

- `model`: A list of strings or `types.Model` instances specifying which models to call.
- `contents`: A list of `content_types.ContentsType` instances representing the messages for the chat model to respond to.
- `generation_config`: A list of `generation_types.GenerationConfigType` instances or `None` specifying configurations for the generation process.
- `safety_settings`: A list of `safety_types.SafetySettingOptions` instances or `None` specifying configurations for the safety features of the model.

#### Behavior

- Validates the presence of the `google-generativeai` package.
- Initializes the `completion_fn` attribute.
- Stores the provided arguments in the `all_args` attribute.
- Calls the superclass constructor.

### `google_text_completion_fn(self, **input_args)`

An instance method that performs the actual API call to Google GenAI's chat model.

#### Parameters

- `**input_args`: A dictionary of arguments to pass to the chat model.

#### Behavior

- Creates a deep copy of the input arguments to avoid mutating the original data.
- Extracts the model name from the arguments and initializes a `GenerativeModel` instance.
- Removes the model name from the parameters to avoid passing it as an argument to the `generate_content` method.
- Calls the `generate_content` method of the `GenerativeModel` instance with the remaining parameters.
- Returns the response from the API call.

### `_extract_responses(response)`

A static method to extract text responses from the API call result.

#### Parameters

- `response`: The response object returned by the `generate_content` method.

#### Returns

- A list of strings containing the top response from the chat model.

### `_get_model_names(self)`

An instance method to retrieve model names from the argument combinations.

#### Returns

- A list of model names used in the experiment.

### `_get_prompts(self)`

An instance method to retrieve prompts from the argument combinations.

#### Returns

- A list of prompts (messages) used in the experiment.

## Usage

To use the `GoogleGeminiChatCompletionExperiment` class, one must:

1. Ensure that the `google-generativeai` package is installed and Google Vertex AI credentials are properly set up.
2. Instantiate the class with the required arguments, all of which should be provided as lists.
3. Call the `run` method inherited from the `Experiment` superclass to execute the experiment with all combinations of arguments.
4. Use the `_extract_responses` method to parse the responses from the chat model.

## Note

- The class is part of a larger project structure and is expected to be used in conjunction with other modules and classes, particularly those related to experiment management and execution.
- The class assumes that the user has appropriate access to Google Cloud resources and has set up authentication credentials for Vertex AI.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/langchain_experiment.md

# SequentialChainExperiment Class

## Description
The `SequentialChainExperiment` class is a subclass of `Experiment` designed to test the functionality of LangChain's sequential chains. It allows for the execution of multiple language model (LLM) chains in sequence, each with its own prompt template and prompt.

## Attributes
- `MODEL_PARAMETERS`: A list of strings representing the parameters related to the model configuration.
- `CALL_PARAMETERS`: A list of strings representing the parameters used when calling the model.
- `completion_fn`: A function that is used to complete the prompts. It defaults to `lc_completion_fn` but can be overridden with `mock_lc_completion_fn` if the `DEBUG` environment variable is set.
- `model_params`: A dictionary containing the model parameters.
- `call_params`: A dictionary containing the call parameters.
- `all_args`: A dictionary that merges `model_params` and `call_params`.

## Methods

### `__init__(self, llm, prompt_template, prompt, **kwargs)`
The constructor initializes the experiment with the provided language models, prompt templates, and prompts. It also accepts additional keyword arguments that are added to the call parameters.

### `prepare(self)`
Prepares the experiment by building combinations of model and call arguments.

### `lc_completion_fn(self, **params)`
A helper function that sends a request to the provided client with the given prompt and returns the response.

### `run(self, runs=1)`
Executes the experiment for each combination of arguments, running each combination a specified number of times (default is 1). It measures the latency of each call and constructs result dataframes with the responses.

### `_extract_responses(output)`
A static method that extracts responses from the output dictionary.

# RouterChainExperiment Class

## Description
The `RouterChainExperiment` class is a subclass of `Experiment` designed to test the functionality of LangChain's router chains. It allows for the execution of a router chain that directs prompts to different destination chains based on the input.

## Attributes
- `MODEL_PARAMETERS`: A list of strings representing the parameters related to the model configuration.
- `CALL_PARAMETERS`: A list of strings representing the parameters used when calling the model.
- `completion_fn`: A function that is used to complete the prompts. It defaults to `lc_completion_fn` but can be overridden with `mock_lc_completion_fn` if the `DEBUG` environment variable is set.
- `model_params`: A dictionary containing the model parameters.
- `call_params`: A dictionary containing the call parameters.
- `all_args`: A dictionary that merges `model_params` and `call_params`.

## Methods

### `__init__(self, llm, prompt_infos, prompt, **kwargs)`
The constructor initializes the experiment with the provided language models, prompt information, and prompts. It also accepts additional keyword arguments that are added to the call parameters.

### `prepare(self)`
Prepares the experiment by building combinations of model and call arguments.

### `lc_completion_fn(self, **params)`
A helper function that sends a request to the provided client with the given prompt and returns the response.

### `run(self, runs=1)`
Executes the experiment for each combination of arguments, running each combination a specified number of times (default is 1). It measures the latency of each call and constructs result dataframes with the responses.

### `_extract_responses(output)`
A static method that returns the output dictionary as is.

## Usage
Both `SequentialChainExperiment` and `RouterChainExperiment` are used to conduct experiments with LangChain's sequential and router chains, respectively. They are instantiated with the necessary parameters and then the `run` method is called to execute the experiment. The results are used to analyze the performance and behavior of the chains under different conditions.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/lancedb_experiment.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/weaviate_experiment.md

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
python
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

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/llama_cpp_experiment.md

# LlamaCppExperiment Class

## Overview
`LlamaCppExperiment` is a class derived from the `Experiment` base class, designed to facilitate experimentation with different parameter combinations for a local model supported by LlamaCpp and GGML. It allows users to specify a range of parameters for both model initialization and model completion calls, and then runs the model with every possible combination of these parameters.

## Attributes
- `MODEL_PARAMETERS`: A tuple containing the names of all parameters that can be used to initialize the model.
- `CALL_PARAMETERS`: A tuple containing the names of all parameters that can be used when calling the model's completion function.
- `DEFAULT`: A dictionary providing default values for all parameters in `MODEL_PARAMETERS` and `CALL_PARAMETERS`.

## Constructor
The `__init__` method initializes the `LlamaCppExperiment` instance with the following arguments:
- `model_path`: A list of strings representing paths to the models to be run.
- `prompt`: A list of strings or `PromptSelector` instances representing the prompts to test.
- `model_params`: A dictionary where keys are parameter names and values are lists of objects representing the parameters for initializing the model.
- `call_params`: A dictionary where keys are parameter names and values are lists of objects representing the parameters for calling the model completion function.

The constructor checks for the presence of the `Llama` class from the `llama_cpp` module and raises an error if it is not found. It also sets default values for any parameters not explicitly provided.

## Methods
### `prepare`
The `prepare` method generates all possible combinations of model and call parameters by taking the cartesian product of the values provided in the `model_params` and `call_params` dictionaries.

### `llama_completion_fn`
The `llama_completion_fn` method is a helper function that takes a `client` (an instance of `Llama`) and additional call parameters, and then calls the client with those parameters to get a response.

### `run`
The `run` method takes an optional `runs` parameter (defaulting to 1) and executes the experiment for each combination of model and call parameters. It runs the model the specified number of times for each combination and records the results and latencies.

### `_extract_responses`
The `_extract_responses` static method takes the output dictionary from a model call and extracts the text responses.

### `_get_model_names`
The `_get_model_names` method returns a list of model names based on the `model_path` parameter from the argument combinations.

### `_get_prompts`
The `_get_prompts` method returns a list of prompts based on the `prompt` parameter from the argument combinations.

## Usage
To use the `LlamaCppExperiment` class, one must instantiate it with the required parameters and then call the `run` method to execute the experiment. The results can be analyzed to understand the impact of different parameter combinations on the model's performance.

## Exceptions
- Raises `ModuleNotFoundError` if the `llama_cpp` module is not installed.
- Raises `NotImplementedError` if the `initialize` class method is called, as it is not compatible with `LlamaCppExperiment`.
- Raises `PromptExperimentException` if no results are obtained after running the experiment.

## Dependencies
- `os`: For handling file paths.
- `itertools`: For creating cartesian products of parameter combinations.
- `logging`: For logging information and errors.
- `perf_counter` from `time`: For measuring latencies.
- `Llama` from `llama_cpp`: The local model client used for running experiments.
- `PromptSelector` from `prompttools.selector.prompt_selector`: For handling prompt selection if required.

## Notes
- The class assumes that all arguments provided in `model_params` and `call_params` are lists, even if they contain only a single value.
- The class is designed to work with local models and runs experiments in a single thread.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/openai_chat_experiment.md

## OpenAIChatExperiment Class

### Overview

The `OpenAIChatExperiment` class is designed to facilitate experiments with OpenAI's chat completion API. It allows users to specify various parameters as lists, and then it generates a cartesian product of these parameters to test different combinations. The class is capable of handling both standard and Azure OpenAI service configurations.

### Attributes

- `_experiment_type`: A string indicating the type of experiment, set to `"RawExperiment"`.

### Constructor

The `__init__` method initializes the `OpenAIChatExperiment` with the following parameters:

- `model`: A list of model IDs to be used for the experiment.
- `messages`: A list of dictionaries representing the conversation history, or a list of `PromptSelector` objects.
- `temperature`: A list of floats representing the sampling temperature.
- `top_p`: A list of floats for nucleus sampling.
- `n`: A list of integers indicating the number of chat completions to generate.
- `stream`: A list of booleans indicating whether to stream partial message deltas.
- `stop`: A list of lists containing stop sequences.
- `max_tokens`: A list of integers specifying the maximum number of tokens to generate.
- `presence_penalty`: A list of floats for presence penalty.
- `frequency_penalty`: A list of floats for frequency penalty.
- `logit_bias`: A list of dictionaries to modify token likelihoods.
- `response_format`: A list of dictionaries to enable JSON mode.
- `seed`: A list of integers for deterministic sampling.
- `functions`: A list of dictionaries defining functions for the model to generate JSON inputs.
- `function_call`: A list of dictionaries specifying a function call.
- `azure_openai_service_configs`: An optional dictionary for Azure OpenAI service configuration.

### Methods

#### `_extract_responses`

Static method that extracts the content from the chat completion output.

#### `_is_chat`

Static method that returns `True`, indicating that this is a chat experiment.

#### `_get_model_names`

Returns a list of model names from the argument combinations.

#### `_get_prompts`

Returns a list of prompts corresponding to the argument combinations.

#### `_get_state`

Captures the current state of the experiment, including DataFrame columns and parameters.

#### `save_experiment`

Saves the current state of the experiment to the backend.

#### `load_experiment`

Class method to load an experiment from the backend using an experiment ID.

#### `load_revision`

Class method to load a specific revision of an experiment from the backend using a revision ID.

#### `_load_state`

Class method to reconstruct an experiment from a saved state.

#### `_validate_arg_key`

Validates if a provided argument name matches known argument names.

#### `run_partial`

Runs the experiment with a single parameter, appending the result to existing DataFrames.

#### `run_one`

Executes a single configuration of the experiment and adds the result to the DataFrame.

#### `get_table`

Returns a DataFrame with the results of the experiment, optionally hiding certain columns.

### Usage

To use the `OpenAIChatExperiment` class, instantiate it with the desired parameters and call the `run_partial` or `run_one` methods to execute the experiment. Results can be saved and loaded using the `save_experiment`, `load_experiment`, and `load_revision` methods. The `get_table` method can be used to retrieve the results in a tabular format.

### Error Handling

The class includes a custom exception `PromptExperimentException` for handling errors specific to the experiment.

### Environment Variables

The class expects the following environment variables to be set:

- `AZURE_OPENAI_KEY`: The API key for Azure OpenAI service.
- `HEGELAI_API_KEY`: The API key for accessing the backend services.

### Dependencies

The class imports various modules such as `copy`, `os`, `json`, `pickle`, `typing`, `openai`, `requests`, `itertools`, `logging`, `pandas`, and custom modules from the `prompttools` package.

### Notes

- The class is designed to work with OpenAI's chat completion API and may require updates as the API evolves.
- The class assumes that all arguments are provided as lists to facilitate the cartesian product generation.
- The class handles both standard and Azure OpenAI service configurations, with the ability to mock responses for debugging purposes.
- The class is part of a larger project structure and interacts with backend services for saving and loading experiments.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/error.md

## `error.py` Module

### Overview

The `error.py` module is part of the `prompttools/experiment` package within the `documentation-generator` project. It defines a custom exception class that is intended to be used across the prompt experiment sub-system of the project.

### Custom Exception Class

#### `PromptExperimentException`

- **Inherits From**: `Exception`
- **Purpose**: This class provides a specific exception type that can be raised to indicate an error or unexpected behavior specifically within the context of prompt experiments. It is designed to signal issues related to the setup or execution of experiments involving prompts.
- **Usage**:
  - This exception should be raised when an error condition is encountered that is specific to the prompt experiment workflow. For example, if an experiment configuration is invalid or if there is a failure in initializing an experiment, this exception could be raised.
  - By using a custom exception, the codebase allows for more granular error handling. Catch blocks can be tailored to handle `PromptExperimentException` differently from other exceptions, providing more context-specific error handling.
- **Attributes**: The class does not define any additional attributes beyond those provided by its superclass, `Exception`.
- **Methods**: The class does not define any methods. It inherits the `__init__` and `__str__` methods from `Exception`, which are sufficient for creating an instance of the exception with an optional error message and converting the exception to a string, respectively.

### Example Usage

python
def initialize_experiment(config):
    if not validate_config(config):
        raise PromptExperimentException("Experiment configuration is invalid.")

try:
    initialize_experiment(experiment_config)
except PromptExperimentException as e:
    print(f"Failed to initialize experiment: {e}")


In the example above, `PromptExperimentException` is raised when the `initialize_experiment` function detects an invalid configuration. The exception is then caught and handled, with an error message being printed to the console.

### Integration with Project

The `error.py` module is expected to be imported and used by other modules within the `prompttools/experiment` package or by any other component of the `documentation-generator` project that deals with prompt experiments. The custom exception allows for consistent error handling and reporting throughout the experiment subsystem.

### File Location

- **Path**: `/workspaces/documentation-generator/target_code/prompttools/experiment/experiments/error.py`
- **Repository Root**: The root directory of the source tree, which contains the `LICENSE` file mentioned in the header comment.

### Licensing

- The source code is copyrighted by Hegel AI, Inc.
- The licensing details for the source code are available in the `LICENSE` file located in the root directory of the source tree.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/__init__.md

# `__init__.py` in `experiments` Module

## Overview

The `__init__.py` file within the `experiments` directory of the `prompttools/experiment` package serves as an initializer for the `experiments` module. This file can be used to set up the module environment, define what symbols the module exports, and run any necessary initialization code required for the module's components.

## Usage

When the `experiments` module is imported, Python will execute the `__init__.py` file. The contents of this file determine which objects and submodules are available to the user when they import the `experiments` module.

### Importing the Module

To import the `experiments` module, one would use the following Python code:

python
from prompttools.experiment import experiments


Upon execution of this import statement, Python will look for the `__init__.py` file in the `experiments` directory and execute it.

### Defining Exports

The `__init__.py` file can define a list of public symbols that the module exports. This is done using the `__all__` variable, which is a list of strings representing the names of objects that should be importable from the module.

For example:

python
__all__ = ['ExperimentA', 'ExperimentB', 'run_experiment']


With the above definition, when a user imports the `experiments` module, they can directly access `ExperimentA`, `ExperimentB`, and `run_experiment`.

### Initialization Code

The `__init__.py` file can also contain any initialization code that needs to run when the module is first imported. This could include setting up logging, initializing module-level data structures, or performing checks that are necessary before the module's functions and classes can be used.

Example:

python
print("Initializing the experiments module")

# Module-level initialization code
experiment_registry = {}

def register_experiment(name, experiment_class):
    experiment_registry[name] = experiment_class

# Register default experiments
register_experiment('default_experiment', DefaultExperiment)


### Submodule Importing

The `__init__.py` file can also be used to import submodules or specific classes and functions from submodules to make them available at the module level.

For instance:

python
from .experiment_a import ExperimentA
from .experiment_b import ExperimentB
from .utils import run_experiment


This allows users to access `ExperimentA`, `ExperimentB`, and `run_experiment` directly from the `experiments` module without having to navigate through the submodule structure.

## File Structure

The `__init__.py` file is typically located at the root of the module directory. In this case, the file structure would look like this:


/workspaces/
└── documentation-generator/
    └── target_code/
        └── prompttools/
            └── experiment/
                └── experiments/
                    ├── __init__.py
                    ├── experiment_a.py
                    ├── experiment_b.py
                    └── utils.py


## Conclusion

The `__init__.py` file in the `experiments` module is a crucial component for defining the module's interface, initializing its environment, and providing a user-friendly way to access its contents. It is executed when the module is imported and can be tailored to meet the specific needs of the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/pinecone_experiment.md

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

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/_utils.md

# `_utils.py` Module Documentation

## Overview

The `_utils.py` module is part of the `experiment` package within the `prompttools` namespace. It provides utility functions for handling and processing data within pandas DataFrames, specifically focusing on the uniqueness of column values.

## Functions

### `_check_column_uniqueness`

python
def _check_column_uniqueness(column: "pd.core.series.Series") -> bool:


#### Description

This function checks if all elements in a given pandas Series (column) are equal. It is used to determine if a column contains more than one unique value.

#### Arguments

- `column` (`pandas.core.series.Series`): The column to be checked for uniqueness.

#### Returns

- `bool`: Returns `True` if there is at least one element in the column that is different from the others, indicating that the column has multiple unique values. Returns `False` if all elements are the same.

#### Internal Logic

1. The function initializes by storing the first element of the column in `first_ele`.
2. It then iterates over each element in the column.
3. During iteration, if it finds an element that is not equal to `first_ele`, it immediately returns `True`.
4. If no such element is found by the end of the iteration, it returns `False`.

### `_get_dynamic_columns`

python
def _get_dynamic_columns(df: pd.DataFrame) -> pd.DataFrame:


#### Description

This function identifies and returns a new DataFrame containing only the columns from the input DataFrame that have more than one unique value. It is designed to filter out columns that are static (having the same value across all rows) and keep only dynamic columns.

#### Arguments

- `df` (`pd.DataFrame`): The DataFrame to be examined for dynamic columns.

#### Returns

- `pd.DataFrame`: A new DataFrame consisting of columns from the original DataFrame that have more than one unique value.

#### Internal Logic

1. Two lists, `hashable_columns` and `unhashable_columns`, are initialized to keep track of columns based on whether their first element can be hashed.
2. The function iterates over each column in the input DataFrame.
3. For each column, it attempts to hash the first element.
   - If successful, the column name is added to `hashable_columns`.
   - If a `TypeError` is raised (indicating the element is unhashable), the function calls `_check_column_uniqueness` to check if the column should be considered dynamic. If so, the column name is added to `unhashable_columns`.
4. The function calculates the number of unique values for each hashable column and identifies those with more than one unique value.
5. It prepares a list of DataFrames (`dfs_to_concat`) containing the dynamic columns identified in both hashable and unhashable categories.
6. The function checks if the special columns "prompt" or "messages" exist in the original DataFrame but are not already included in the dynamic columns. If found, they are appended to `dfs_to_concat`.
7. Finally, the function concatenates all DataFrames in `dfs_to_concat` along the columns (axis=1) and returns the resulting DataFrame.

## Usage

The functions in this module are likely used internally within the `experiment` package to preprocess and filter DataFrames before running experiments. The `_check_column_uniqueness` function serves as a helper to `_get_dynamic_columns`, which is the primary function intended for direct use.

## Notes

- The module is intended for internal use within the `experiment` package, as indicated by the underscore prefix in the module name.
- The functions are designed to work with pandas DataFrames and Series, which are common data structures for data analysis in Python.
- The module includes a copyright notice and a license reference, suggesting that it is proprietary software belonging to Hegel AI, Inc.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/huggingface_hub_experiment.md

# HuggingFaceHubExperiment Class

## Overview
`HuggingFaceHubExperiment` is a subclass of `Experiment` designed to interact with the Hugging Face Hub's API. It is used to perform experiments by sending prompts to various models hosted on the Hugging Face Hub and collecting the responses. The class supports running experiments with different combinations of model parameters and prompt inputs by creating a cartesian product of the provided arguments.

## Attributes
- `MODEL_PARAMETERS`: A list of parameter names related to the model configuration.
- `CALL_PARAMETERS`: A list of parameter names related to the API call configuration.
- `model_params`: A dictionary containing model-related parameters such as `repo_id` and `task`.
- `call_params`: A dictionary containing parameters for the API call, including `prompt` and any additional keyword arguments.
- `prompt_keys`: A dictionary mapping prompts to their corresponding keys, used when prompts are instances of `PromptSelector`.
- `all_args`: A dictionary containing all arguments, a combination of `model_params` and `call_params`.
- `model_argument_combos`: A list of dictionaries representing all possible combinations of model-related arguments.
- `call_argument_combos`: A list of dictionaries representing all possible combinations of call-related arguments.

## Methods

### `__init__(self, repo_id: List[str], prompt: Union[List[str], List[PromptSelector]], task: List[str] = ["text-generation"], **kwargs: Dict[str, list[object]])`
Constructor for the `HuggingFaceHubExperiment` class. It initializes the experiment with the provided repository IDs, prompts, tasks, and additional keyword arguments. If the `huggingface_hub` package is not installed, it raises a `ModuleNotFoundError`.

### `prepare(self) -> None`
Prepares the experiment by generating all possible combinations of model and call arguments using the cartesian product.

### `hf_completion_fn(self, **params: Dict[str, Any])`
A helper function that makes a request to the Hugging Face Hub API using the provided parameters. It extracts the necessary arguments from `params` and sends a request to the API client.

### `run(self, runs: int = 1) -> None`
Executes the experiment for each combination of arguments. It performs the experiment `runs` times for each combination (default is 1). The method initializes an `InferenceApi` client for each model configuration and sends the prompts to the API. It measures the latency for each call and collects the results. If no results are obtained, it logs an error and raises a `PromptExperimentException`.

### `_extract_responses(output: List[Dict[str, object]]) -> list[str]`
A static method that extracts the generated text from the API response. It is used to process the output of the API calls and retrieve the generated text from the list of choices.

## Usage
The `HuggingFaceHubExperiment` class is used to conduct experiments with models on the Hugging Face Hub. Users can specify different model repositories, tasks, and prompts, along with other parameters, to test the performance and output of the models. The class handles the complexity of making multiple API calls with different combinations of inputs and collecting the results for analysis.

## Exceptions
- Raises `ModuleNotFoundError` if the `huggingface_hub` package is not installed.
- Raises `PromptExperimentException` if no results are obtained during the experiment run.

## Dependencies
- `os`: To access environment variables and check for debug mode.
- `itertools`: To create cartesian products of input arguments.
- `huggingface_hub.inference_api`: To interact with the Hugging Face Hub API.
- `time.perf_counter`: To measure the latency of API calls.
- `logging`: To log information and errors.
- `prompttools.selector.prompt_selector`: To handle prompt selection if `PromptSelector` instances are used.
- `prompttools.mock.mock`: To provide a mock completion function for debugging purposes.
- `experiment`: To inherit from the `Experiment` base class.
- `error`: To handle custom exceptions specific to the experiment.

## Environment Variables
- `DEBUG`: Determines whether to use the mock completion function instead of the actual Hugging Face Hub API.
- `HUGGINGFACEHUB_API_TOKEN`: The API token used to authenticate with the Hugging Face Hub API.

## Notes
- The class assumes that all arguments provided to the constructor are lists, even if they contain a single element. This is necessary for the cartesian product generation.
- The class supports the use of `PromptSelector` instances to handle prompts that require rendering or mapping to other models.
- The `VALID_TASKS` constant defines the supported tasks for the experiment.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/replicate_experiment.md

# ReplicateExperiment Class

## Overview

The `ReplicateExperiment` class is a subclass of the `Experiment` class designed to perform experiments using the Replicate API. It supports both image models and language models (LLMs). The class requires the `replicate` Python package to be installed and an API token to be set in the environment variable `REPLICATE_API_TOKEN`.

## Initialization

### `__init__(self, models, input_kwargs, model_specific_kwargs={}, use_image_model=False)`

The constructor initializes the `ReplicateExperiment` with the following parameters:

- `models`: A list of strings representing the model identifiers to be used in the experiment (e.g., `"stability-ai/stable-diffusion:27b93a2413e"`).
- `input_kwargs`: A dictionary where keys are argument names and values are lists of argument values. These arguments are common across all models.
- `model_specific_kwargs`: A dictionary where keys are model identifiers and values are dictionaries with keys as argument names and values as lists of argument values. These arguments are specific to each model.
- `use_image_model`: A boolean flag indicating whether the experiment is for an image model. Defaults to `False`.

The constructor checks for the presence of the `replicate` package and the `REPLICATE_API_TOKEN` environment variable. It also handles the conversion of `PromptSelector` objects to prompts if they are used in `input_kwargs`.

## Methods

### `prepare(self)`

The `prepare` method generates all combinations of arguments for each model by combining `input_kwargs` and `model_specific_kwargs`. It populates the `self.argument_combos` list with dictionaries representing each combination of arguments, including the model version.

### `replicate_completion_fn(model_version: str, **kwargs)`

A static method that calls the `replicate.run` function with the specified `model_version` and additional keyword arguments (`kwargs`). It is used to execute the model and obtain the results.

### `_extract_responses(self, output) -> str`

A method to extract responses from the output of the `replicate.run` function. If `self.image_experiment` is `True`, it assumes the output is a list of image URIs. Otherwise, it concatenates text responses from a generator.

### `_image_tag(url, image_width)`

A static method that generates HTML code for rendering an image given its URL and a specified image width.

### `visualize(self, get_all_cols=False, pivot=False, pivot_columns=[], image_width=300)`

The `visualize` method displays the results of the experiment. If `self.image_experiment` is `False`, it calls the `visualize` method of the superclass. If `self.image_experiment` is `True`, it creates an HTML table with image tags to display the images. It supports pivoting the results table based on specified columns.

- `get_all_cols`: A boolean indicating whether to retrieve all columns in the visualization.
- `pivot`: A boolean indicating whether to pivot the table.
- `pivot_columns`: A list of columns to use for pivoting the table.
- `image_width`: An integer specifying the width of the images in the visualization.

## Usage

To use the `ReplicateExperiment` class, one must instantiate it with the required parameters, call the `prepare` method to generate argument combinations, and then call the `visualize` method to display the results. The class is designed to be used in an interactive environment, such as Jupyter notebooks, where the output can be rendered directly. In non-interactive environments, it logs the tabulated results using the `logging` module.

## Dependencies

- `replicate`: The Python package for interacting with the Replicate API.
- `logging`: Used for logging information in non-interactive environments.
- `itertools`: Utilized for generating combinations of arguments.
- `functools.partial`: Used to create partial functions.
- `IPython.display`: For displaying HTML content in interactive environments.
- `tabulate`: For tabulating results in a human-readable format.
- `prompttools.mock.mock`: Contains the `mock_replicate_stable_diffusion_completion_fn` for debugging purposes.
- `prompttools.selector.prompt_selector`: Contains the `PromptSelector` class for handling prompt selection.
- `..widgets.utility`: Contains the `is_interactive` function to check if the environment is interactive.
- `os`: For accessing environment variables.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/anthropic_completion_experiment.md

# AnthropicCompletionExperiment Class

## Overview

The `AnthropicCompletionExperiment` class is a Python class that extends the `Experiment` class, designed to interact with Anthropic's completion API. It is used to conduct experiments by generating a cartesian product of input arguments and obtaining results for each combination from the API.

## Dependencies

- The class requires the `anthropic` package to be installed. If not present, an `ImportError` will be raised.
- The `os` module is used to access environment variables.
- The `logging` module is used for logging errors and information.
- The `prompttools.selector.prompt_selector` and `prompttools.mock.mock` modules are used for prompt selection and mocking the API for testing purposes.

## Environment Variables

- `ANTHROPIC_API_KEY`: Must be set in the environment to authenticate with the Anthropic API.

## Initialization

The constructor of the `AnthropicCompletionExperiment` class takes the following parameters:

- `model`: A list of strings specifying the model(s) to use for completion.
- `prompt`: A list of strings or `PromptSelector` objects representing the input prompts.
- `metadata`: A list of objects describing metadata about the request. Defaults to `[NOT_GIVEN]`.
- `max_tokens_to_sample`: A list of integers indicating the maximum number of tokens to generate. Defaults to `[1000]`.
- `stop_sequences`: A list of lists of strings representing sequences that will stop the model from generating more text. Defaults to `[NOT_GIVEN]`.
- `stream`: A list of booleans indicating whether to stream the response. Defaults to `[False]`.
- `temperature`: A list of floats representing the randomness in the response. Defaults to `[NOT_GIVEN]`.
- `top_k`: A list of integers for sampling only from the top K options. Defaults to `[NOT_GIVEN]`.
- `top_p`: A list of floats for nucleus sampling. Defaults to `[NOT_GIVEN]`.
- `timeout`: A list of floats indicating the timeout for the request in seconds. Defaults to `[600.0]`.

The constructor checks for the presence of the `anthropic` package and initializes the API client with the provided API key. If the `DEBUG` environment variable is set, a mock completion function is used instead of the actual API call.

## Methods

### anthropic_completion_fn

This instance method makes a call to the Anthropic API with the provided input arguments and handles various exceptions that may occur during the API call, such as connection errors and rate limits.

### _extract_responses

A static method that extracts the completion text from the API response.

### _get_model_names

An instance method that retrieves the model names from the argument combinations.

### _get_prompts

An instance method that retrieves the prompts from the argument combinations.

## Usage

To use the `AnthropicCompletionExperiment` class, instantiate it with the required arguments and call its methods to perform the experiment. Ensure that the `ANTHROPIC_API_KEY` environment variable is set before creating an instance of the class.

## Error Handling

The class includes error handling for issues such as missing dependencies, API connection errors, rate limiting, and non-200 HTTP status codes.

## Notes

- All arguments to the constructor should be provided as lists, even if they are not intended to vary during the experiment.
- The class is designed to be used in a larger project where experiments are conducted using the Anthropic API.
- The class assumes that the `Experiment` base class and other required modules are available in the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/experiment/experiments/qdrant_experiment.md

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

python
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


This example would create a Qdrant collection, index the provided documents, run the queries five times each, and then delete the collection.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/benchmarks/benchmark.md

# Benchmark Class

## Overview
The `Benchmark` class is designed to evaluate models using predefined datasets and metrics. It is particularly tailored for benchmarking language models (LLMs) on multiple-choice tasks. The class provides methods to run experiments, calculate accuracy, and potentially other precision metrics (as indicated by the placeholder method `_get_precision`).

## Attributes
- `experiment`: An instance of an experiment class that contains the method `run` to execute the experiment and a DataFrame `full_df` with the results.
- `eval_method`: A callable that takes a row of data and an expected response to evaluate the similarity between model responses and expected responses.
- `prompts`: A list of strings representing queries, questions, or prompts for LLMs to generate responses.
- `response_options`: A list of possible responses for each prompt.
- `correct_response_indices`: An optional list of integers indicating the index of the correct response within `response_options`.

## Methods

### `__init__`
The constructor initializes the `Benchmark` object with the provided experiment, evaluation method, prompts, response options, and correct response indices.

### `_get_precision`
A placeholder method intended to calculate precision from a DataFrame. It is not implemented yet (`TODO: coming soon`).

### `multiple_choice_accuracy`
Calculates the accuracy of the LLM on multiple-choice tasks by comparing the model's choices with the correct answers.

#### Parameters
- `dataframe`: A pandas DataFrame containing the results of the experiment.
- `col1`: The name of the column in the DataFrame that contains the model's choices.
- `col2`: The name of the column in the DataFrame that contains the correct answers.

#### Returns
- A float representing the accuracy of the model's responses.

### `multiple_choice_benchmark`
Executes the experiment using the `experiment` attribute's `run` method and processes the results to measure the quality of the LLM's responses.

#### Steps
1. Runs the experiment using the `experiment` object.
2. Checks if the `prompt` column exists in the `experiment.full_df` DataFrame. If not, it creates the `prompt` column by mapping the `messages` column to strings and issues a warning.
3. Prepares a DataFrame `benchmark_df` with the `prompt` and `response` columns from `experiment.full_df`.
4. Associates each prompt with the list of `response_options`.
5. Explodes the `response_options` column to create a row for each option and resets the index.
6. Iterates over the rows of `benchmark_df` and applies the `eval_method` to calculate similarity scores between the LLM response and each response option.
7. Adds a `scores` column to `benchmark_df` with the calculated similarity scores.
8. Determines the maximum score for each prompt and filters the DataFrame to only include rows with the highest score.
9. Sorts `benchmark_df` by index to maintain the original order.
10. Extracts the model's choices based on the index of the response options and adds a `model_choice` column to `benchmark_df`.
11. Adds a `labels` column to `benchmark_df` with the correct response indices.
12. Calls `multiple_choice_accuracy` with `benchmark_df`, `model_choice`, and `labels` columns to calculate the accuracy.

#### Returns
- The accuracy of the LLM as determined by the `multiple_choice_accuracy` method.

## Usage
The `Benchmark` class is used to evaluate the performance of language models on multiple-choice tasks. An example of its usage can be found in the `benchmarks/examples/benchmarking.ipynb` notebook. The class requires an experiment object that can run a model and collect responses, an evaluation method to score the responses, a set of prompts, response options, and the indices of the correct responses. The main method to use is `multiple_choice_benchmark`, which orchestrates the benchmarking process and returns the accuracy of the model.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/benchmarks/__init__.md

# `__init__.py` in `prompttools/benchmarks` Module

## Overview

The `__init__.py` file serves as the initialization script for the `prompttools/benchmarks` package within the larger project. This file is executed when the `prompttools/benchmarks` package is imported in a Python script, and it is responsible for setting up the package namespace.

## Contents

The file contains an import statement and a special list named `__all__`.

### Import Statements

python
from .benchmark import Benchmark


This line imports the `Benchmark` class from the `benchmark.py` module located in the same directory as the `__init__.py` file. The `.` before `benchmark` indicates that it is a relative import, meaning that the module is part of the current package.

### `__all__` List

python
__all__ = [
    "Benchmark",
]


The `__all__` list is a mechanism for defining which symbols will be exported when `from prompttools.benchmarks import *` is used. It explicitly declares the public API of the package. In this case, only the `Benchmark` class is made available for import when using the wildcard `*`. This prevents other modules that may be present in the package directory from being imported unintentionally.

## Usage

When a user wants to use the `Benchmark` class in their code, they can import it directly from the `prompttools/benchmarks` package as follows:

python
from prompttools.benchmarks import Benchmark


This import is possible because the `__init__.py` file has explicitly made `Benchmark` available in the package's namespace. Without the import statement in `__init__.py`, the user would have to use a longer import path:

python
from prompttools.benchmarks.benchmark import Benchmark


By using the `__init__.py` file to manage imports, the package provides a cleaner and more convenient API to its users.

## Project Structure

The presence of the `__init__.py` file indicates that `prompttools/benchmarks` is a Python package. This file is part of the standard structure of a Python package and is required for Python to recognize the directory as a package and to allow imports from it.

## Licensing

The file header contains a copyright notice and a reference to the license under which the source code is provided:

plaintext
# Copyright (c) Hegel AI, Inc.
# All rights reserved.
#
# This source code's license can be found in the
# LICENSE file in the root directory of this source tree.


This notice informs users and contributors that the code is the property of "Hegel AI, Inc." and that all rights are reserved. It also directs users to the `LICENSE` file for the full license terms, which should be located in the root directory of the source tree.

## Conclusion

The `__init__.py` file in the `prompttools/benchmarks` package is a key component for managing the package's namespace and providing a clean API for importing its contents. It specifies the `Benchmark` class as part of the public interface of the package and adheres to the project's licensing terms.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/selector/prompt_selector.md

# PromptSelector Class

## Overview

The `PromptSelector` class is designed to facilitate the rendering of prompts for various language models. It provides a unified interface to generate prompts that are compatible with different models such as OpenAI's Chat models, Llama models, and others.

## Attributes

- `instruction`: A string representing the instruction or context to be provided to the model.
- `user_input`: An object representing the user's input that will be included in the prompt.

## Methods

### `for_openai_chat`

- **Description**: Generates a prompt formatted for OpenAI's Chat models.
- **Returns**: A list of dictionaries, each containing a "role" key (either "system" or "user") and a "content" key with the corresponding text.

### `for_openai_completion`

- **Description**: Generates a prompt formatted for OpenAI's text completion models.
- **Returns**: A string formatted using the `GENERIC_TEMPLATE`, which includes placeholders for the instruction and user input.

### `for_huggingface_hub`

- **Description**: Generates a prompt formatted for models hosted on Hugging Face's Model Hub.
- **Returns**: A string formatted using the `GENERIC_TEMPLATE`, similar to the `for_openai_completion` method.

### `for_llama`

- **Description**: Generates a prompt formatted for Llama models.
- **Returns**: A string formatted using the `LLAMA_TEMPLATE`, which includes special tokens and placeholders for the instruction and user input.

### `for_anthropic`

- **Description**: Generates a prompt formatted for Anthropic's models.
- **Returns**: A string formatted using the `ANTHROPIC_TEMPLATE`, which includes the `HUMAN_PROMPT` and `AI_PROMPT` tokens if available, along with placeholders for the instruction and user input.

### `for_palm`

- **Description**: Generates a prompt formatted for PALM models.
- **Returns**: A string formatted using the `PALM_TEMPLATE`, which includes placeholders for the instruction and user input.

## Templates

The class uses predefined templates for generating prompts for different models:

- `GENERIC_TEMPLATE`: A basic template that includes an "INSTRUCTION" section followed by a "PROMPT" section and a "RESPONSE" section.
- `PALM_TEMPLATE`: A template for PALM models that directly concatenates the instruction and user input.
- `LLAMA_TEMPLATE`: A template for Llama models that includes special tokens `[INST]`, `<<SYS>>`, and `[/INST]` to delineate the instruction from the user input.
- `ANTHROPIC_TEMPLATE`: A template for Anthropic models that includes `HUMAN_PROMPT` and `AI_PROMPT` tokens to frame the instruction and user input.

## Usage

The `PromptSelector` class is instantiated with an instruction and user input. The appropriate method is then called to generate a prompt for the desired model, which can be used to interact with the model's API or interface.

## Error Handling

The class attempts to import `HUMAN_PROMPT` and `AI_PROMPT` from the `anthropic` module. If the module is not found, it sets these variables to `None`. This allows the `for_anthropic` method to function without these tokens if they are not available.

## License

The source code's license can be found in the `LICENSE` file in the root directory of this source tree. The copyright notice at the beginning of the file indicates that the code is owned by Hegel AI, Inc. and that all rights are reserved.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/selector/__init__.md

# `selector` Module

## Overview

The `selector` module is a component of the `documentation-generator` project, located within the `prompttools` package. This module is designed to provide functionality for selecting specific elements or data based on certain criteria within the scope of the documentation generation process.

## File Structure

The file is located at the following path within the project:


/workspaces/documentation-generator/target_code/prompttools/selector/__init__.py


This indicates that the `selector` module is a package with its own `__init__.py` file, which may be used to initialize the package and define what is exposed to the outside when the package is imported.

## Licensing

The file begins with a copyright notice and a reference to the license under which the source code is released:

python
# Copyright (c) Hegel AI, Inc.
# All rights reserved.
#
# This source code's license can be found in the
# LICENSE file in the root directory of this source tree.


Users and contributors must refer to the `LICENSE` file in the root directory of the source tree to understand their rights and limitations under the license.

## Usage

As an `__init__.py` file, its primary use is to initialize the `selector` package. This can involve several tasks:

1. Importing necessary classes, functions, or submodules from within the package or from external packages.
2. Defining any package-level variables or constants.
3. Setting up any required state or configuration needed by the package.
4. Exposing a public API for the package by specifying which classes, functions, or objects will be available when the package is imported elsewhere in the project.

The `__init__.py` file may also contain package-level documentation strings (docstrings) that describe the purpose and usage of the package.

## Integration with the Project

The `selector` module would be used by other parts of the `documentation-generator` project that require selection logic. For example, it might be used to:

- Select specific code blocks for which documentation should be generated.
- Filter out elements that do not meet certain criteria from the documentation process.
- Choose templates or formats based on the type of code or documentation being generated.

Other modules or scripts within the `documentation-generator` project would import the `selector` package and utilize its exposed functions or classes to perform the necessary selection tasks.

## Extensibility

The structure of the `selector` module as a package allows for extensibility. Additional submodules, classes, or functions can be added to the package to extend its functionality. These can then be imported within the `__init__.py` file to make them part of the package's public API.

## Conclusion

This file serves as the entry point for the `selector` package within the `prompttools` namespace of the `documentation-generator` project. It is responsible for initializing the package and defining its public interface, which other parts of the project will use to perform selection-related tasks during the documentation generation process.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/requests/request_queue.md

# RequestQueue Class

## Overview

The `RequestQueue` class is a component of the `prompttools` library designed to manage and process asynchronous requests to large language models (LLMs) such as those provided by OpenAI. It utilizes a queue system to handle requests and measure their latencies.

## Attributes

- `data_queue`: An instance of `Queue` from the `queue` module, used to store tasks in the form of `(function, arguments)` tuples.
- `is_running`: A boolean flag indicating whether the queue processing thread should continue running.
- `worker_thread`: A `Thread` object from the `threading` module, responsible for processing tasks in the queue.
- `request_args`: A list of dictionaries containing the arguments for each request that has been processed.
- `request_results`: A list of dictionaries containing the results of each request that has been processed.
- `request_latencies`: A list of floats representing the time taken to process each request.

## Methods

### `__init__(self)`
Constructor that initializes the queue, starts the worker thread, and initializes lists to store request arguments, results, and latencies.

### `_process_queue(self) -> None`
A private method that runs in the worker thread. It continuously retrieves and processes tasks from the queue until `is_running` is set to `False`. It handles queue `Empty` exceptions by continuing the loop.

### `_do_task(self, fn: Callable, args: Dict[str, object]) -> None`
A private method that executes a given task. It sets the OpenAI API key if it's present in the environment variables, runs the task, and appends the arguments, results, and latencies to their respective lists. It handles `AuthenticationError` by logging an error message.

### `_run(self, fn: Callable, args: Dict[str, object]) -> Tuple[Dict[str, object], float]`
A private method decorated with `@retry_decorator` to handle retries. It measures the time taken to execute a given function with the provided arguments and returns the result along with the latency.

### `shutdown(self) -> None`
Public method to stop the worker thread. It waits for the queue to be empty, sets `is_running` to `False`, and joins the worker thread.

### `__del__(self) -> None`
Destructor that ensures the queue is properly shut down when the `RequestQueue` object is deleted.

### `enqueue(self, callable: Callable, args: Dict[str, object]) -> None`
Public method to add a new request to the queue. It accepts a callable and its arguments as a dictionary.

### `get_input_args(self) -> List[Dict[str, object]]`
Public method to retrieve the list of input arguments for all processed requests. It waits for the queue to be empty before returning the list.

### `get_results(self) -> List[Dict[str, object]]`
Public method to retrieve the list of results for all processed requests. It waits for the queue to be empty before returning the list.

### `get_latencies(self) -> List[float]`
Public method to retrieve the list of latencies for all processed requests. It waits for the queue to be empty before returning the list.

## Usage

The `RequestQueue` class is used to manage asynchronous requests to LLMs. Users can enqueue tasks, which are then processed by the worker thread. The class provides methods to retrieve the input arguments, results, and latencies of these tasks after they have been processed.

## Error Handling

The class includes TODO comments indicating areas for improvement, such as handling unexpected errors that could cause the queue to hang and addressing potential `TypeError` during shutdown if an interrupt occurs.

## Integration

This class is intended to be used within the `prompttools` library and can be integrated with other components that require asynchronous request handling, such as a Streamlit app or other interfaces that interact with LLMs.

## Dependencies

- `os`: To access environment variables.
- `typing`: For type annotations.
- `queue`: To create and manage the task queue.
- `time`: To measure request latencies.
- `threading`: To run the queue processing in a separate thread.
- `openai`: To make requests to OpenAI's API.
- `logging`: To log errors.
- `prompttools.requests.retries`: To use the `retry_decorator` for handling retries.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/requests/__init__.md

# `requests` Module

## Overview

The `requests` module, located at `/workspaces/documentation-generator/target_code/prompttools/requests/__init__.py`, is a Python package initializer for handling HTTP requests within the `prompttools` project. This module is designed to provide a simplified interface for sending HTTP/HTTPS requests and handling responses.

## Usage

The `requests` module is typically imported at the beginning of a Python script or module where HTTP communication is required. It is used to make GET, POST, PUT, DELETE, and other HTTP method calls to RESTful APIs or web services.

Example of importing the module:
python
from prompttools.requests import requests


## Functions and Classes

The `requests` module may define several functions and classes, which are not visible in the provided file path. However, it is common for such modules to include the following:

- `get(url, params=None, **kwargs)`: Sends a GET request to the specified URL with optional query parameters and additional keyword arguments.
- `post(url, data=None, json=None, **kwargs)`: Sends a POST request to the specified URL with optional form data, JSON payload, and additional keyword arguments.
- `put(url, data=None, **kwargs)`: Sends a PUT request to the specified URL with optional data and additional keyword arguments.
- `delete(url, **kwargs)`: Sends a DELETE request to the specified URL with additional keyword arguments.
- `head(url, **kwargs)`: Sends a HEAD request to the specified URL with additional keyword arguments.
- `options(url, **kwargs)`: Sends an OPTIONS request to the specified URL with additional keyword arguments.
- `Session()`: A class that allows for persistent settings across requests (cookies, headers, etc.).

## Parameters

Common parameters for the request functions include:

- `url`: The URL to which the request is to be sent.
- `params`: A dictionary or bytes to be sent in the query string for the `get` method.
- `data`: A dictionary, list of tuples, bytes, or file-like object to send in the body of the `post` and `put` methods.
- `json`: A JSON serializable Python object to send in the body of the `post` and `put` methods.
- `headers`: A dictionary of HTTP headers to send with the request.
- `cookies`: A dictionary of cookies to send with the request.
- `files`: A dictionary of `{filename: fileobject}` files to send in the body of the request.
- `auth`: An auth tuple or callable to enable Basic/Digest/Custom HTTP Auth.
- `timeout`: How many seconds to wait for the server to send data before giving up.
- `allow_redirects`: Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection.
- `proxies`: A dictionary of the scheme to proxy URL.
- `verify`: Either a boolean, in which case it controls whether to verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use.
- `stream`: if `False`, the response content will be immediately downloaded.
- `cert`: if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.

## Return Values

The functions typically return a `Response` object, which contains the server's response to the HTTP request. This object includes:

- `.status_code`: An integer code of the response HTTP status (e.g., 200, 404).
- `.text`: The content of the response in Unicode.
- `.content`: The content of the response in bytes.
- `.json()`: A method to decode the response content as JSON.
- `.headers`: A dictionary representation of the response headers.
- `.cookies`: A `RequestsCookieJar` of cookies the server sent back.
- `.url`: The URL of the obtained page.
- `.history`: A list of `Response` objects from the history of the request (in case of redirects).

## Error Handling

The module may also provide exception classes to manage errors that arise during the request process, such as `ConnectionError`, `HTTPError`, `Timeout`, `TooManyRedirects`, and `RequestException`.

## Integration with `prompttools` Project

Within the `prompttools` project, the `requests` module is used to interact with external services or APIs. It simplifies the process of sending and receiving HTTP requests, abstracting away the complexities of creating and managing network connections and sessions.

## Dependencies

The `requests` module typically depends on third-party libraries such as `urllib3`, `chardet`, `certifi`, and `idna`. These dependencies are required to handle various aspects of HTTP communication, such as SSL/TLS verification, character encoding detection, and internationalized domain names.

## Installation

The `requests` module is not part of the Python Standard Library, so it must be installed using a package manager like `pip` before it can be used in the `prompttools` project.

Example installation command:
bash
pip install requests


## Conclusion

The `requests` module is a critical component of the `prompttools` project, enabling it to communicate with web services and APIs in a straightforward and efficient manner. Its design follows the principle of simplicity, making HTTP requests as painless as possible for developers.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/requests/retries.md

# retries.py Module Documentation

## Overview

The `retries.py` module is part of the `prompttools.requests` package within the `documentation-generator` project. It provides a utility to create a retry decorator using the `tenacity` library, which is designed to handle transient errors in network requests by implementing a retry mechanism. This module is particularly useful when dealing with the OpenAI API, as it includes handling for specific OpenAI-related exceptions.

## Functions

### generate_retry_decorator

#### Description

The `generate_retry_decorator` function creates and returns a retry decorator configured with exponential backoff and specific exception handling. This decorator can be applied to functions that perform network requests to automatically retry them in case of certain types of failures, such as connection errors or rate limits.

#### Parameters

- `wait_lower_bound` (int, optional): The minimum amount of time, in seconds, to wait before the first retry attempt. Defaults to 3 seconds.
- `wait_upper_bound` (int, optional): The maximum amount of time, in seconds, that the wait time can reach through exponential backoff before a retry attempt. Defaults to 12 seconds.
- `max_retry_attempts` (int, optional): The maximum number of retry attempts before giving up and re-raising the exception. Defaults to 5 attempts.

#### Returns

A `retry` decorator configured with the specified parameters.

#### Behavior

- **Exponential Backoff**: The decorator uses an exponential backoff strategy for the wait times between retries. For the `i`th attempt, it waits for `2^i` seconds, with the wait time bounded between `wait_lower_bound` and `wait_upper_bound`.
- **Maximum Attempts**: The retry process stops after `max_retry_attempts` have been made without success.
- **Exception Handling**: The decorator is configured to retry on the following OpenAI exceptions:
  - `openai.APIConnectionError`
  - `openai.APIError`
  - `openai.RateLimitError`
  - `openai.APIStatusError`
  - `openai.APIResponseValidationError`
  - `openai.APITimeoutError`
- **Logging**: Before each sleep (wait before retry), a warning log is emitted using the `logging` module.

#### Usage

To use the `generate_retry_decorator`, call the function with the desired parameters to create a decorator. Then, apply this decorator to any function that makes network requests and should be retried upon encountering specific exceptions.

python
@generate_retry_decorator(wait_lower_bound=2, wait_upper_bound=10, max_retry_attempts=3)
def my_network_request_function():
    # Function code that makes a network request


## Module-Level Variables

### retry_decorator

#### Description

The `retry_decorator` variable is an instance of the retry decorator created by calling `generate_retry_decorator` with the default parameters. It is ready to be used throughout the project without needing to create a new instance.

#### Usage

Apply `retry_decorator` directly to functions that require a retry mechanism with the default configuration.

python
@retry_decorator
def another_network_request_function():
    # Function code that makes a network request


## Dependencies

- `tenacity`: Used for implementing the retry logic with exponential backoff and specific exception handling.
- `openai`: The OpenAI Python client library, from which specific exceptions are handled by the retry decorator.
- `logging`: Used to log warning messages before each retry attempt.

## License

The source code is licensed under the license found in the `LICENSE` file in the root directory of the source tree, and the copyright belongs to Hegel AI, Inc.

## Notes

- The module is designed to be robust against transient network issues and API-specific errors when interacting with the OpenAI API.
- The retry strategy is particularly useful in distributed systems where network reliability can be an issue.
- The module's functionality is critical for ensuring that the application can gracefully handle and recover from errors encountered during API requests.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/mock/mock.md

# Mock Functions for Testing and Demonstration

## Overview

The file `mock.py` contains a collection of mock functions designed to simulate the behavior of various APIs and libraries for testing and demonstration purposes. These functions are typically used in place of actual API calls during development, testing, or when showcasing features without the need for live data or services.

## Dependencies

- `json`: A built-in Python module used for encoding and decoding JSON data.
- `cv2`: An optional module for computer vision tasks, part of the OpenCV library. If not installed, `cv2` is set to `None`.

## Classes

### DotDict

A subclass of `dict` that allows attribute-style access to dictionary keys.

#### Methods

- `__getattr__(self, key)`: Attempts to retrieve the value associated with `key`. If the key does not exist or its value is `None`, it raises an `AttributeError`.

### _mock_Anthropic_Completion_Object

A simple class to represent a completion object from the Anthropic API.

#### Attributes

- `completion`: A string representing the completion text.
- `model`: A string indicating the model used for the completion.
- `stop_reason`: A string describing the reason the completion stopped.

### _mock_PaLM_Completion_Object

A class to represent a completion object from the PaLM API.

#### Attributes

- `candidates`: A list of dictionaries containing completion candidates and their safety ratings.
- `result`: A string representing the final selected completion.
- `filters`: A list of filters applied to the completion process (optional).
- `safety_feedback`: A list of safety feedback items (optional).

## Mock Functions

### mock_openai_chat_completion_fn

Simulates the response from OpenAI's chat completion API.

#### Returns

- A `DotDict` object with predefined chat completion data.

### mock_openai_chat_function_completion_fn

Simulates the response from OpenAI's chat function completion API, including a function call within the chat.

#### Returns

- A `DotDict` object with predefined chat function completion data.

### mock_openai_completion_fn

Simulates the response from OpenAI's text completion API.

#### Returns

- A `DotDict` object with predefined text completion data.

### mock_hf_completion_fn

Simulates the response from Hugging Face's text completion API.

#### Returns

- A list containing a dictionary with the key `generated_text` and a sample completion.

### mock_chromadb_fn

Simulates the response from a database query, such as ChromaDB.

#### Returns

- A dictionary with keys `ids`, `embeddings`, `documents`, `metadatas`, and `distances`, containing sample data.

### mock_anthropic_completion_fn

Simulates the response from Anthropic's text completion API.

#### Returns

- An instance of `_mock_Anthropic_Completion_Object` with predefined data.

### mock_palm_completion_fn

Simulates the response from Google's PaLM text completion API.

#### Returns

- An instance of `_mock_PaLM_Completion_Object` with predefined data.

### mock_mindsdb_completion_fn

Simulates the response from MindsDB's text completion API.

#### Returns

- A list containing a sample completion string.

### mock_lc_completion_fn

Simulates the response from an unspecified text completion API.

#### Returns

- A string containing a sample completion.

### mock_stable_diffusion

Simulates the generation of an image using the Stable Diffusion model.

#### Returns

- The result of `cv2.imread` with a predefined image path.

#### Exceptions

- Raises `ModuleNotFoundError` if `cv2` is not installed.

### mock_replicate_stable_diffusion_completion_fn

Simulates the response from the Stable Diffusion model hosted on Replicate.

#### Parameters

- `model_version`: A string indicating the version of the model used.

#### Returns

- A list containing a predefined image path.

### mock_qdrant_fn

Simulates the response from a Qdrant vector database query.

#### Returns

- A list containing an instance of `ScoredPoint` with predefined data.

## Usage

These mock functions are used in place of actual API calls to simulate responses for testing and demonstration. They can be called with any arguments, as they do not process input parameters and return static, predefined data.

## Notes

- The mock functions do not perform any real data processing or API communication.
- The `cv2` dependency is only required for the `mock_stable_diffusion` function.
- The `qdrant_client` module is assumed to be available for the `mock_qdrant_fn` function.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/mock/__init__.md

# `__init__.py` in `prompttools/mock` Module

## Overview

The `__init__.py` file in the `prompttools/mock` directory serves as an initializer for the `mock` Python package within the `prompttools` project. This file can contain package-level documentation, initialization code, or import management to expose the package's components to the users.

## Usage

When the `prompttools` package is imported, Python will execute the `__init__.py` file in the `mock` subpackage. This execution can perform several tasks:

- Initialize any global variables or state required by the subpackage.
- Import classes, functions, and variables from other modules within the `mock` subpackage to make them available at the package level.
- Set up any package-wide configurations or settings.
- Perform checks or preparations that are necessary before the subpackage can be used.

## Structure

The structure of the `__init__.py` file can vary depending on the needs of the `mock` subpackage. A typical structure might include:

1. **Module Docstring**: At the top of the file, a module docstring provides a high-level description of the subpackage's purpose and contents.

2. **Imports**: The file may include imports of submodules or individual classes, functions, or variables from within the subpackage. These imports make it easier for users to access commonly used components without needing to know the internal structure of the subpackage.

3. **Initialization Code**: Any code that needs to run when the subpackage is first imported would be placed here. This could include setting up logging, initializing configuration files, or preparing any necessary resources.

4. **Subpackage API Exposition**: The `__init__.py` file can also be used to define an API for the subpackage by explicitly specifying which components should be exposed to the user. This is done using the `__all__` variable, which is a list of strings representing the names of modules and attributes that should be imported when `from prompttools.mock import *` is used.

## Example

Below is a hypothetical example of what the `__init__.py` file might contain:

python
"""Mock subpackage for the prompttools project.

This subpackage provides mock implementations and testing utilities
for various components of the prompttools project.
"""

# Import key classes and functions from submodules for easier access
from .mock_generator import MockGenerator
from .mock_validator import MockValidator

# Initialize subpackage-level variables or state if necessary
_default_mock_config = {
    'use_defaults': True,
    'verbose': False
}

# Define the subpackage API for wildcard imports
__all__ = ['MockGenerator', 'MockValidator', 'setup_mock_environment']

def setup_mock_environment():
    """Set up the mock environment for testing."""
    # Implementation of environment setup
    pass


In this example, the `__init__.py` file provides a docstring explaining the purpose of the `mock` subpackage, imports two classes for easy access, initializes a default configuration dictionary, and defines a function to set up the mock environment. It also specifies an API for wildcard imports using the `__all__` variable.

## Conclusion

The `__init__.py` file in the `prompttools/mock` directory is a crucial component for initializing the `mock` subpackage, managing imports, and defining the subpackage's API. It is executed when the subpackage is imported and can contain any necessary setup or configuration code to ensure the subpackage is ready for use.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/prompttest/prompttest.md

# Technical Documentation for `prompttest.py`

## Overview

The `prompttest.py` module is part of the `documentation-generator` project and is located within the `prompttools/prompttest` subdirectory. It is designed to facilitate the creation and execution of a suite of prompt tests for evaluating the performance of AI models or functions against predefined prompts and expected outcomes.

## Dependencies

- `typing`: Provides support for type hints.
- `functools.wraps`: Used to preserve the metadata of the original function when it is decorated.
- `logging`: Utilized for logging warnings and other messages.
- `threshold_type`: A module that defines the `ThresholdType` enumeration.
- `error.failure`: Contains the `PromptTestSetupException` class for handling setup exceptions.
- `runner.runner`: Includes the `run_prompttest` function that executes the actual prompt test.

## Global Variables

- `TESTS_TO_RUN`: A list that stores all the test functions to be executed.

## Functions

### `prompttest`

#### Description

The `prompttest` function is a higher-order function that returns a decorator. This decorator can be applied to functions that generate completions for prompts. It is used to define a test by specifying various parameters such as the metric name, evaluation function, prompts, threshold, threshold type, and expected results.

#### Parameters

- `metric_name` (str): The name of the metric used for evaluation.
- `eval_fn` (Callable): The evaluation function that assesses the quality of the completions.
- `prompts` (List[str]): A list of prompt strings to be used for generating completions.
- `threshold` (float, optional): The threshold value for the metric to determine test success. Defaults to 1.0.
- `threshold_type` (ThresholdType, optional): An instance of `ThresholdType` that specifies whether the threshold is a minimum or maximum value. Defaults to `ThresholdType.MINIMUM`.
- `expected` (Optional[List[str]], optional): An optional list of expected completion strings corresponding to the prompts.

#### Returns

- A decorator function that can be used to annotate a completion-generating function.

### `prompttest_decorator`

#### Description

The `prompttest_decorator` is an inner function of `prompttest` that takes a completion function as an argument and wraps it to create a test function. This test function is then appended to the `TESTS_TO_RUN` list.

#### Parameters

- `completion_fn` (Callable): The function that generates completions for the given prompts.

#### Returns

- A wrapped function that, when called, executes the test.

### `main`

#### Description

The `main` function is the entry point of the script. It sets the logging level to `WARNING`, runs all the tests collected in `TESTS_TO_RUN`, and exits with a status code indicating success or failure of the tests.

#### Behavior

1. Sets the logging level to `WARNING`.
2. Prints the number of tests to run.
3. Executes each test function in `TESTS_TO_RUN` and counts the number of failures.
4. If all tests pass, prints a success message and exits with status code 0.
5. If any test fails, prints the number of failed tests and exits with status code 1.

## Usage

To use this module, a developer would:

1. Import the `prompttest` decorator.
2. Define a completion function that takes a prompt and returns a completion.
3. Annotate the completion function with the `prompttest` decorator, providing the necessary parameters.
4. Call the `main` function to execute all defined tests.

The `prompttest` decorator will automatically add the test to the `TESTS_TO_RUN` list. When the `main` function is called, it will iterate over this list and execute each test, reporting the results accordingly.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/prompttest/threshold_type.md

## `ThresholdType` Enum Class

### Overview

The `ThresholdType` class is an enumeration that defines constant values representing different types of thresholds that can be applied to test cases within the project. This class is part of the `prompttools` package, specifically within the `prompttest` module, and is located at `/workspaces/documentation-generator/target_code/prompttools/prompttest/threshold_type.py`.

### Usage

The `ThresholdType` enum is used to specify the kind of threshold that a user wants to apply to a test case. It helps in maintaining a clear and standardized way of referring to threshold types across the project. By using an enum, the code becomes more readable and less prone to errors that might occur due to the use of plain strings or integers.

### Enum Members

The `ThresholdType` enum defines the following members:

- `MINIMUM`: This member has an integer value of `1` and represents a minimum threshold. It is used when the user wants to specify a lower bound for a test case, ensuring that the test value does not fall below this threshold.

- `MAXIMUM`: This member has an integer value of `2` and represents a maximum threshold. It is used when the user wants to specify an upper bound for a test case, ensuring that the test value does not exceed this threshold.

### Importing and Referencing

To use the `ThresholdType` enum in other parts of the project, it must first be imported:

python
from prompttools.prompttest.threshold_type import ThresholdType


Once imported, the enum can be referenced in the code as follows:

python
def set_threshold(threshold_type: ThresholdType, value: float):
    if threshold_type == ThresholdType.MINIMUM:
        # Implement logic for minimum threshold
        pass
    elif threshold_type == ThresholdType.MAXIMUM:
        # Implement logic for maximum threshold
        pass


### File Metadata

- **License**: The source code is licensed under the terms found in the `LICENSE` file located in the root directory of the source tree. The copyright notice at the beginning of the file indicates that Hegel AI, Inc. holds all rights to the code.

### Conclusion

The `ThresholdType` enum is a simple yet crucial part of the `prompttools` package, providing a standardized way to handle threshold types in test cases. Its use ensures consistency and reduces the likelihood of errors in threshold-related logic throughout the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/prompttest/__init__.md

# `__init__.py` in `prompttest` Module

## Overview

The `__init__.py` file is a Python initializer file that is required for Python to recognize the directory `prompttest` as a Python package. This allows the directory to be imported as a module in other parts of the project.

## Usage

When the `prompttest` package is imported, the Python interpreter executes the contents of the `__init__.py` file. This file can be used to perform package initialization tasks such as setting up package-level variables, importing necessary submodules, or running initialization code that is required for the package to function properly.

## Contents

The `__init__.py` file can contain any valid Python code. Commonly, it includes:

- Package version number
- Import statements for submodules
- Initialization code for the package
- Definitions of `__all__` to restrict what is exported when `from prompttest import *` is used

## Example Structure

python
# __init__.py for prompttest package

# Define the version of the prompttest package
__version__ = '1.0.0'

# Import submodules for easier access
from . import submodule1
from . import submodule2

# Initialize package-level variables or constants
PACKAGE_CONSTANT = 'constant_value'

# Define an __all__ for import * control
__all__ = ['submodule1', 'submodule2', 'some_function']

# Any initialization code can go here
def some_function():
    pass

# Perform any necessary checks or setup on package import
def _initialize_package():
    # Code to initialize the package
    pass

_initialize_package()


## Interaction with Other Files

The `__init__.py` file can import other submodules within the `prompttest` package, which may themselves be directories with their own `__init__.py` files or Python files (`.py`). This creates a hierarchy of modules within the package.

## Best Practices

- Keep the `__init__.py` file as simple as possible.
- Use relative imports when importing submodules within the same package.
- Define an `__all__` list to explicitly declare the public API of the package.
- Avoid complex initialization code that can make imports slow or lead to circular dependencies.

## Impact on Project

The presence of the `__init__.py` file in `prompttest` makes it a package, allowing it to be included in other parts of the project using the `import` statement. Without this file, the Python interpreter would not recognize `prompttest` as a package, and it would not be importable.

## Conclusion

The `__init__.py` file in the `prompttest` package serves as an entry point for package initialization and configuration. It is a critical component for package recognition and structure within a Python project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/prompttest/runner/runner.md

# PromptTestRunner Class

## Description
`PromptTestRunner` is a base class designed to manage and run prompt-based tests for machine learning models, particularly in the context of natural language processing. It is intended to be subclassed for specific testing scenarios. The class provides methods to run experiments, evaluate results, visualize outcomes, and retrieve scores.

## Attributes
- `ran`: A `defaultdict` that tracks whether a test has been run, using a boolean flag.
- `experiments`: A dictionary that stores instances of `Experiment` objects, keyed by a string representation of the arguments used to create them.

## Methods

### `__init__(self)`
Constructor that initializes the `ran` and `experiments` attributes.

### `run(self, *args, **kwargs) -> str`
Executes the test if it has not been run previously. It creates a unique key based on the arguments, checks if the test with this key has been run, and if not, creates and runs a new `Experiment` object. It then marks the test as run and returns the key.

### `evaluate(self, key: str, metric_name: str, eval_fn: Callable, expected: Optional[str] = None) -> None`
Calls the `evaluate` method of the `Experiment` object associated with the given key. It passes the metric name, evaluation function, and an optional expected result to the experiment's evaluate method.

### `visualize(self, key: str) -> None`
Invokes the `visualize` method of the `Experiment` object associated with the given key to generate visual representations of the test results.

### `scores(self, key)`
Retrieves the scores from the `Experiment` object associated with the given key.

### `_get_experiment(experiment: Type[Experiment], model_name: str, prompts: List[str], model_args: Dict[str, object]) -> Experiment`
A static method that instantiates an `Experiment` object with the provided model name, prompts, and model arguments. It wraps the model arguments into lists to match the expected input format for `Experiment`.

## Usage
The `PromptTestRunner` class is used to manage the lifecycle of prompt-based tests. It ensures that each test is run only once and provides a structured way to evaluate and visualize the results. It is not intended to be used directly but rather to be subclassed for specific testing needs.

# run_prompttest Function

## Description
`run_prompttest` is a standalone function that performs the evaluation of prompt test results. It computes scores for each prompt-result pair using a provided evaluation function and compares them against a threshold to determine test success or failure.

## Parameters
- `metric_name`: The name of the metric used for evaluation.
- `eval_fn`: A callable that takes a prompt, result, optional metadata, and an optional expected result to compute a score.
- `threshold`: A numerical threshold that the scores must meet to pass the test.
- `threshold_type`: An instance of `ThresholdType` that specifies whether the threshold is a maximum or minimum value.
- `prompts`: A list of prompts used in the test.
- `results`: A list of results corresponding to the prompts.
- `expected`: An optional list of expected results for the prompts.

## Returns
- Returns `0` if all scores meet the threshold criteria, indicating success.
- Returns `1` if any score fails to meet the threshold criteria, indicating failure.

## Behavior
The function iterates over each prompt-result pair, computes a score using the `eval_fn`, and appends the score to a list. If the `expected` parameter is provided, it is passed to the `eval_fn` along with the prompt and result. If no scores are generated, an error is logged, and a `PromptTestSetupException` is raised. Each score is then compared against the threshold according to the `threshold_type`. If any score fails to meet the threshold, a failure is logged, and the function returns `1`. If all scores meet the threshold, the function returns `0`.

## Usage
`run_prompttest` is used to evaluate the performance of a model against a set of prompts and expected results. It is a utility function that can be called with the necessary parameters to perform a prompt test evaluation outside the context of the `PromptTestRunner` class.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/prompttest/runner/__init__.md

# `__init__.py` Module

## Overview

The `__init__.py` file is located in the `runner` subpackage of the `prompttest` module, which is part of the `prompttools` package within the `documentation-generator` project. This file serves as an initializer for the `runner` subpackage, allowing the Python interpreter to recognize it as a package and enabling the import of its modules and functions.

## Usage

The presence of the `__init__.py` file in the `runner` directory makes it possible for other Python scripts within the `documentation-generator` project to import the `runner` subpackage or its contents. For example:

python
from prompttools.prompttest.runner import some_module


or

python
from prompttools.prompttest.runner.some_module import some_function


## Contents

The `__init__.py` file can be empty or contain code that initializes the `runner` subpackage. This can include:

- Package-level variables
- Import statements to expose certain modules at the package level
- Initialization code that runs when the package is imported

## Example

If the `runner` subpackage contains modules `module_a.py` and `module_b.py`, the `__init__.py` file could be used to import specific functions or classes from these modules to make them available at the package level:

python
from .module_a import ClassA
from .module_b import function_b


Now, `ClassA` and `function_b` can be imported directly from the `runner` package:

python
from prompttools.prompttest.runner import ClassA, function_b


## Best Practices

- Keep the `__init__.py` file as simple as possible.
- Use relative imports when importing from within the same package.
- Avoid importing external dependencies in the `__init__.py` file to reduce the risk of circular import issues.
- Use `__all__` to explicitly define which modules or names are public and should be exposed when `import *` is used.

## `__all__` Variable

The `__all__` variable can be defined in the `__init__.py` file to control which symbols are exported when `from prompttools.prompttest.runner import *` is used:

python
__all__ = ['ClassA', 'function_b']


This ensures that only `ClassA` and `function_b` are imported in such a case, and not every name defined in the package.

## Conclusion

The `__init__.py` file in the `runner` subpackage is a crucial component for package management and namespace organization in the `documentation-generator` project. It dictates how the modules within the `runner` subpackage are exposed and imported throughout the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/prompttest/error/failure.md

# `failure.py` Module

## Overview

The `failure.py` module is part of the `prompttools` package, specifically within the `prompttest.error` subpackage. It is designed to handle failures in prompt testing by providing a custom exception class and a logging function to output failure details to the console.

## Contents

### Import Statements

python
from prompttools.prompttest.threshold_type import ThresholdType


This import statement brings in the `ThresholdType` enumeration from the `threshold_type` module, which is used to distinguish between minimum and maximum threshold types in the context of prompt testing.

### `PromptTestSetupException` Class

python
class PromptTestSetupException(Exception):
    """
    An exception to throw when something goes wrong with the prompt test setup.
    """
    pass


This class is a custom exception type that inherits from Python's built-in `Exception` class. It is intended to be raised when there is an issue with setting up a prompt test, such as invalid configuration or parameters.

### `log_failure` Function

python
def log_failure(metric_name, threshold, actual, threshold_type):
    """
    Prints the test results to the console.
    """
    # Function implementation...


#### Parameters

- `metric_name` (str): The name of the metric that failed the test.
- `threshold` (float/int): The threshold value that the actual result was expected to meet or exceed.
- `actual` (float/int): The actual value obtained from the test.
- `threshold_type` (ThresholdType): An instance of the `ThresholdType` enumeration indicating whether the threshold is a minimum or maximum value.

#### Functionality

The `log_failure` function is responsible for logging the details of a failed test to the console. It constructs a formatted message that includes the metric name, the expected threshold, the actual result, and the type of threshold (minimum or maximum). The message is printed with alignment to enhance readability.

#### Implementation Details

The function prints two messages:

1. The first message includes the following:
   - A header "Test failed: " followed by the `metric_name`.
   - The "Threshold: " label aligned with the header, followed by the `threshold` value.
   - The "Actual: " label aligned with the header, followed by the `actual` value.
   - The "Type: " label aligned with the header, followed by a string representation of the `threshold_type` ("Minimum" or "Maximum").

2. The second message prints a line of dashes ("-") that matches the length of the header plus the metric name, serving as a visual separator.

#### Example Usage

The `log_failure` function would typically be called within a testing framework when an assertion fails due to a metric not meeting the specified threshold. The function outputs the failure details to the console for the developer to review.

## File Metadata

- **License**: The source code's license information is specified to be in the `LICENSE` file located in the root directory of the source tree.
- **Copyright**: The copyright notice at the beginning of the file indicates that Hegel AI, Inc. holds all rights to the code.

## Integration

The `failure.py` module is likely integrated into a larger testing suite within the `prompttools` package. It would be used in conjunction with other modules that perform prompt testing, where it can provide error handling and failure logging capabilities.

## Conclusion

The `failure.py` module is a utility for logging test failures in a structured and readable format to the console, as well as defining a custom exception for prompt test setup issues.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/prompttest/error/__init__.md

# `__init__.py` in `prompttools/prompttest/error` Module

## Overview

The `__init__.py` file within the `prompttools/prompttest/error` directory is a Python initializer file that is used to treat the directory as a Python package. This allows the directory to be imported as a module in other parts of the project.

## Purpose

The primary purpose of the `__init__.py` file is to initialize the `error` package when it is imported. This can include setting up the package namespace, initializing package-level variables, and importing necessary classes or functions from submodules within the package.

## Usage

When the `error` package is imported in a Python script, the Python interpreter executes the `__init__.py` file. The contents of this file determine what symbols (functions, classes, variables, etc.) are available to the importer.

For example, if another module within the project needs to handle errors defined in the `error` package, it would start with an import statement like this:

python
from prompttools.prompttest.error import CustomError


This would import `CustomError` from the `error` package, assuming that `CustomError` is defined and made available in the `__init__.py` file or in one of its submodules.

## Contents

The `__init__.py` file can contain several types of statements and definitions:

1. **Package Documentation**: A docstring at the beginning of the file to describe the package's purpose and contents.

2. **Imports**: Import statements to bring in classes, functions, and variables from submodules, making them available when the package is imported.

3. **Package-level Variables**: Definitions of variables that are meant to be used across the package.

4. **Initialization Code**: Any code that needs to run to set up the package environment, such as configuring logging or setting up connections.

5. **Subpackage and Submodule Declarations**: If the package contains subpackages or submodules, they may be imported or initialized here to make them available as part of the package API.

## Example Structure

Below is a hypothetical example of what the `__init__.py` file might contain:

python
"""Error handling utilities for the prompttools.prompttest package."""

# Import necessary exceptions from submodules
from .custom_error import CustomError
from .validation_error import ValidationError

# Initialize package-level variables if necessary
default_error_message = "An unknown error has occurred."

# Define a package-level function
def handle_error(error):
    """Handle errors in a standardized way."""
    print(f"Error: {error}")

# Optionally, import subpackages if the package is structured hierarchically
from . import subpackage


## Interaction with Other Project Components

The `error` package defined by this `__init__.py` file can be used by other components of the project that need to handle errors. For instance, a command-line interface (CLI) module might catch exceptions and use the `handle_error` function defined in the package to display error messages to the user.

## Conclusion

The `__init__.py` file in the `prompttools/prompttest/error` directory serves as the entry point for the `error` package, defining its interface and initializing its environment. It is a critical component for package organization and modularity within the project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/function_call_harness.md

# Function Call Harness Module

## Overview

The `function_call_harness.py` module is part of the `prompttools` package within the `documentation-generator` project. It is designed to facilitate the testing and integration of functions by providing a standardized harness for function invocation. The module is expected to be used by developers to ensure that functions within the project are correctly called with the appropriate arguments and that they handle edge cases as expected.

## Usage

Currently, the module does not contain any implemented functionality, as indicated by the `TODO: Coming soon.` comment. When completed, the module would typically be used as follows:

1. **Importing the Harness**: Developers would import the `function_call_harness` module into their test suites or integration scripts.

2. **Configuring the Harness**: The harness would require configuration, likely involving specifying the function to be tested, along with any necessary arguments, expected outputs, and edge cases.

3. **Running the Harness**: Once configured, the harness could be executed, which would involve calling the specified function with the provided arguments and capturing the output.

4. **Validating Results**: The harness would then compare the actual output of the function call against the expected output to determine if the function behaves as intended.

5. **Handling Exceptions**: The harness would also be responsible for handling any exceptions thrown by the function, ensuring that they are either expected as part of the function's behavior or logged as errors.

6. **Reporting**: After execution, the harness would generate a report detailing the success or failure of the function calls, including any discrepancies between expected and actual results.

## Integration

The `function_call_harness.py` module would be integrated into the larger `documentation-generator` project as a utility for developers. It would be invoked during the development cycle, particularly in the testing phase, to ensure that all functions are well-tested and documented before deployment.

## File Structure

The file is located at `/workspaces/documentation-generator/target_code/prompttools/harness/`, indicating that it is part of a larger collection of harness tools within the `prompttools` namespace. The `target_code` directory suggests that this module is specifically designed to target the code for testing purposes.

## Licensing

The file header indicates that the source code is copyrighted by Hegel AI, Inc. and that all rights are reserved. The license for the source code can be found in the `LICENSE` file located in the root directory of the source tree. Users and contributors must adhere to the terms specified in the LICENSE file when using or modifying the `function_call_harness.py` module.

## Future Development

As the module is not yet implemented, future development will involve fleshing out the functionality as described in the "Usage" section. This will include writing the code necessary to configure, execute, and report on function calls within the project. The `TODO` comment serves as a placeholder and a reminder for developers to complete the module's implementation.

## Conclusion

In its current state, the `function_call_harness.py` module serves as a template for future development. Once completed, it will be a critical tool for ensuring the reliability and correctness of functions within the `documentation-generator` project.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/chat_model_comparison_harness.md

# ChatModelComparisonHarness Class

## Overview
`ChatModelComparisonHarness` is a class that extends `ExperimentationHarness` and is designed to facilitate the comparison of different chat models. It allows users to conduct experiments by providing chat histories to multiple models and comparing their outputs.

## Attributes
- `experiment_cls_constructor`: A reference to the `OpenAIChatExperiment` class, which is used to instantiate an experiment object.
- `model_names`: A list of strings representing the names of the models to be compared.
- `chat_histories`: A list of chat histories, where each chat history is a list of dictionaries with string keys and values. Each dictionary represents a message in the chat history.
- `runs`: An integer indicating the number of times the experiment should be executed. Defaults to `1`.
- `model_arguments`: An optional dictionary of additional arguments that can be passed to the model. Defaults to an empty dictionary if `None` is provided.
- `PIVOT_COLUMNS`: A class attribute that defines the columns used for pivoting the data during comparison. It is set to `["model", "messages"]`.

## Methods
### `__init__(self, model_names, chat_histories, runs=1, model_arguments=None)`
The constructor for the `ChatModelComparisonHarness` class. It initializes the class with the provided model names, chat histories, number of runs, and model arguments.

### `prepare(self)`
This method initializes and prepares the experiment by creating an instance of `OpenAIChatExperiment` with the provided model names, chat histories, and model arguments. It then calls the `prepare` method of the superclass.

### `run(self)`
This method runs the experiment. If the experiment has not been prepared, it calls the `prepare` method before running the experiment using the superclass's `run` method.

### `compare(self)`
This method compares the outputs of the different models. It calls the `compare` method of the `experiment` instance, passing the first model name in the `model_names` list and the `PIVOT_COLUMNS` as arguments.

## Usage
The `ChatModelComparisonHarness` class is used in a project to compare the performance of different chat models. Users can instantiate the class with the desired models and chat histories, and then call the `run` method to execute the experiment. After running the experiment, the `compare` method can be used to analyze and compare the results of the different models.

## Example
python
# Instantiate the harness with two models and a sample chat history
harness = ChatModelComparisonHarness(
    model_names=['model_1', 'model_2'],
    chat_histories=[
        [
            {'user': 'How are you?', 'model': 'I am fine, thank you.'},
            {'user': 'What's the weather like?', 'model': 'It's sunny today.'}
        ]
    ],
    runs=3
)

# Run the experiment
harness.run()

# Compare the results
harness.compare()


In this example, the `ChatModelComparisonHarness` is used to compare two models, `model_1` and `model_2`, over three runs using a predefined chat history. After running the experiment, the results are compared to evaluate the performance of each model.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/multi_experiment_harness.md

# MultiExperimentHarness Class

## Overview

`MultiExperimentHarness` is a class designed to facilitate the execution of experiments across multiple model providers with varying APIs. It aims to streamline the process of running experiments, evaluating results, and consolidating the data into a single table for comparison and analysis.

## Usage

The class is typically used in a project where multiple experiments need to be conducted using different machine learning models or APIs, such as comparing the performance of language models from different providers.

An example of its usage can be found in the Jupyter notebook located at `examples/notebooks/GPT4vsLlama2.ipynb`, which demonstrates how to test prompts across different models.

## Initialization

### `__init__(self, experiments: List[Experiment])`

The constructor takes a list of `Experiment` objects as an argument. Each `Experiment` object represents a specific experiment to be run using a particular model provider.

## Methods

### `prepare(self)`

This method iterates over each `Experiment` object in the `experiments` list and calls its `prepare` method. This is typically used to set up any necessary configurations or preconditions before running the experiments.

### `run(self)`

This method iterates over each `Experiment` object in the `experiments` list and calls its `run` method. This triggers the execution of the experiments, collecting results from the different model providers.

### `evaluate(self, metric_name: str, eval_fn: Callable) -> None`

This method iterates over each `Experiment` object in the `experiments` list and calls its `evaluate` method, passing a `metric_name` and an evaluation function `eval_fn`. This is used to apply a specific evaluation metric to the results of the experiments.

### `gather_feedback(self) -> None`

This method is a placeholder and does not perform any action. It is intended to be overridden or extended in subclasses to collect additional feedback from the experiments if necessary.

### `_get_argument_combos(self)`

This private method aggregates all argument combinations from each `Experiment` object's `argument_combos` attribute. It returns a list of these combinations.

### `_get_prompts(self)`

This private method aggregates all prompts from each `Experiment` object by calling their `_get_prompts` method. It returns a list of these prompts.

### `_get_results(self)`

This private method extracts and aggregates the responses from each `Experiment` object's `results` attribute by calling their `_extract_responses` method. It returns a list of these responses.

### `_get_scores(self)`

This private method aggregates the scores from each `Experiment` object's `scores` attribute. It returns a dictionary where each key is a metric name and the value is a list of scores for that metric.

### `_get_experiment_names(self)`

This private method aggregates the model names from each `Experiment` object by calling their `_get_model_names` method. It returns a list of these model names.

### `visualize(self, colname: str = None) -> None`

This method creates a visualization of the experiment results. It constructs a dictionary with keys such as "prompt", "response(s)", "latency", and "model", and populates them with data aggregated from the private methods `_get_prompts`, `_get_results`, `_get_scores`, and `_get_experiment_names`. It then creates a pandas DataFrame from this dictionary.

If a `colname` is provided, the method creates a pivot table from the DataFrame, with the `colname` values, indexed by "prompt" and with columns corresponding to "model". The aggregation function used is to take the first element.

### `rank(self, metric_name: str, is_average: bool = False) -> Dict[str, float]`

This method is a placeholder and does not perform any action. It is intended to be overridden or extended in subclasses to rank the models based on a specific metric.

## Dependencies

- `typing`: Provides type hints for function arguments and return types.
- `collections.defaultdict`: Used to create a dictionary with a default value for new keys.
- `prompttools.experiment.Experiment`: The base class for the experiments that are to be run.
- `pandas as pd`: Used for creating and manipulating data tables (DataFrames) for visualization and analysis.

## License

The source code's license information can be found in the `LICENSE` file in the root directory of the source tree.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/utility.md

# Utility Module Documentation

## Module: `utility.py`

Located at `/workspaces/documentation-generator/target_code/prompttools/harness/`, the `utility.py` module provides utility functions for the larger project. This module contains functions that are used across various parts of the project to perform common tasks.

### Function: `is_interactive`

#### Description

The `is_interactive` function is designed to check the environment in which the code is running to determine if it is being executed within an interactive environment, such as a Jupyter notebook.

#### Usage

This function is typically used to conditionally format or present output, such as visualizations, differently when the code is run in an interactive environment versus a non-interactive script or command-line interface.

#### Signature

python
def is_interactive() -> bool:


#### Returns

- `bool`: Returns `True` if the code is running in an interactive environment (like a Jupyter notebook), and `False` otherwise.

#### Implementation Details

- The function imports the `__main__` module, which is the top-level script environment.
- It checks for the presence of the `__file__` attribute within the `__main__` module.
- If the `__file__` attribute does not exist, it implies that the code is running in an interactive environment where the `__file__` attribute is typically not set, such as a Jupyter notebook.
- The function returns `True` if the `__file__` attribute is not found, indicating an interactive environment, and `False` otherwise.

#### Example

python
if is_interactive():
    # Code to display interactive visualizations
else:
    # Code for non-interactive presentation of results


### License

The source code in `utility.py` is proprietary and owned by Hegel AI, Inc. The license for this source code can be found in the `LICENSE` file located in the root directory of the source tree.

---

**Note:** This documentation is for the `utility.py` module as of the last update and may change as the project evolves.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/document_retrieval_harness.md

# Document Retrieval Harness Module

## Overview

The `document_retrieval_harness.py` module is part of the `prompttools` package within the `documentation-generator` project. It is designed to facilitate the retrieval of documents in a structured manner, likely for the purpose of generating documentation or processing text data. The module is currently a placeholder, as indicated by the "TODO: Coming soon" comment, and is expected to be implemented in the future.

## License

The module is copyrighted by Hegel AI, Inc. and is subject to the terms of the license found in the LICENSE file located in the root directory of the source tree. Users and developers must consult the LICENSE file to understand the usage rights and restrictions for this module.

## Usage

As the module is not yet implemented, there is no current usage or functionality provided. Once implemented, it is expected that the module will include functions or classes that can be imported and used in other parts of the `documentation-generator` project to retrieve documents from various sources.

## Expected Functionality

When completed, the `document_retrieval_harness.py` module may provide the following functionality:

- Connect to different document storage systems (e.g., databases, file systems, cloud storage).
- Query and retrieve documents based on specific criteria or identifiers.
- Parse and preprocess documents to a standardized format for further processing.
- Cache retrieved documents for efficient access in repeated operations.
- Handle authentication and authorization if required by the document storage system.
- Provide an interface for other modules to request and receive documents seamlessly.

## Integration

The module is expected to be integrated with other components of the `documentation-generator` project, such as parsers, analyzers, and generators, to form a complete documentation generation pipeline. It will likely be invoked by higher-level scripts or modules that coordinate the overall process of documentation generation.

## Development Status

As indicated by the "TODO" comment, the module is under development and not yet functional. Developers assigned to this module will need to implement the planned features and ensure that it meets the project's requirements for document retrieval.

## Future Considerations

- The module should be designed with extensibility in mind to support new document sources as they become relevant.
- Performance considerations, such as multi-threading or asynchronous I/O, may be important for handling large volumes of documents.
- Error handling and logging will be crucial for diagnosing issues during the retrieval process.
- Unit tests and integration tests should be written to ensure the module's reliability and correctness.

## Conclusion

The `document_retrieval_harness.py` module is a planned component of the `documentation-generator` project that will be responsible for retrieving documents. It is currently not implemented, and its design and functionality will be determined as the project progresses.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/chat_prompt_template_harness.md

## ChatPromptTemplateExperimentationHarness

### Overview
`ChatPromptTemplateExperimentationHarness` is a class that extends `ExperimentationHarness` and is designed to facilitate the testing of various prompt templates for chat models using `jinja` templating. It allows for the creation of prompts from templates, execution of experiments, and analysis of results.

### Attributes
- `_experiment_type`: A string indicating the type of experiment, set to "Template".
- `PIVOT_COLUMNS`: A list of column names used for pivoting data in the DataFrame, set to ["prompt_template", "user_input"].

### Initialization
The `__init__` method initializes the harness with the following parameters:
- `experiment`: A constructor for the experiment class to be executed within the harness.
- `model_name`: A string representing the name of the model.
- `message_templates`: A list of lists of dictionaries, where each list contains `jinja`-styled templates for system and user messages.
- `user_inputs`: A list of dictionaries representing user inputs.
- `model_arguments`: An optional dictionary of additional arguments for the model.

The method sets up the `jinja2` environment, stores the experiment class constructor, model name, message templates, user inputs, and model arguments. It then calls the superclass initializer.

### Methods

#### `prepare`
Prepares the experiment by creating prompts from templates and initializing the experiment with the appropriate arguments. It renders messages using the `_render_messages_openai_chat` function and sets up the experiment instance.

#### `run`
Executes the experiment and processes the results. It adds user inputs and prompt templates to the resulting DataFrame for analysis. It can clear previous results if specified.

#### `get_table`
Returns a DataFrame with the results of the experiment. It can return all columns or a subset by hiding specific columns. The method determines which columns to hide based on whether `get_all_cols` is `True` or `False`.

#### `visualize`
Displays the results of the experiment in a table format. If the environment is interactive (e.g., Jupyter Notebook), it uses `display.display`. Otherwise, it logs the table using the `logging` module and `tabulate`.

#### `aggregate`
Aggregates data based on a specified column and method (e.g., 'mean', 'sum', 'count', etc.). It can handle special cases for user inputs and templates by converting them to a suitable format for aggregation.

#### `_get_state`
Captures the current state of the experiment, including the experiment class constructor, model name, message templates, user inputs, model arguments, and the state of the child experiment. It returns this state as a tuple.

#### `_load_state`
A class method that loads the state of an experiment from a given state tuple. It reconstructs the harness and associated experiment from the saved state parameters.

### Usage
The `ChatPromptTemplateExperimentationHarness` is used in a project to test different chat prompt templates against a chat model. It allows for systematic experimentation with various user inputs and prompt styles, and it provides tools for analyzing the performance and responses of the model.

### Internal Functions

#### `_render_messages_openai_chat`
A helper function that takes a message template, user input, and a `jinja2` environment to render a complete message. It deep copies the template, renders the system and user messages with the provided user input, and returns the rendered message.

### Dependencies
- `typing`: For type annotations.
- `jinja2`: For rendering `jinja` templates.
- `pandas`: For handling data in DataFrame format.
- `copy`: For deep copying data structures.
- `IPython.display`: For displaying results interactively.
- `tabulate`: For formatting tables.
- `logging`: For logging information.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/chat_history_harness.md

# ChatHistoryExperimentationHarness Class

## Overview
The `ChatHistoryExperimentationHarness` class is a specialized experimentation harness designed for comparing multiple chat histories using a specified model. It extends the `ExperimentationHarness` class and integrates with the `OpenAIChatExperiment` class to facilitate the experimentation process.

## Attributes
- `experiment_cls_constructor`: A reference to the `OpenAIChatExperiment` class, which is used to instantiate an experiment object.
- `model_name`: A string representing the name of the model to be used in the experiment.
- `chat_histories`: A list of chat history lists, where each chat history is represented as a list of dictionaries with string keys and values. Each dictionary typically contains message data to be processed by the model.
- `model_arguments`: An optional dictionary of additional arguments that can be passed to the model. Defaults to an empty dictionary if `None` is provided.

## Methods

### `__init__(self, model_name: str, chat_histories: List[List[Dict[str, str]]], model_arguments: Optional[Dict[str, object]] = None)`
The constructor for the `ChatHistoryExperimentationHarness` class.

#### Parameters:
- `model_name`: The name of the model to be used in the experiment.
- `chat_histories`: A list of chat history lists to be fed into the model for comparison.
- `model_arguments`: Additional model arguments, if any.

#### Behavior:
- Initializes the `experiment_cls_constructor` with the `OpenAIChatExperiment` class.
- Stores the `model_name`, `chat_histories`, and `model_arguments` provided as arguments.
- Calls the superclass constructor to complete the initialization process.

### `prepare(self) -> None`
Initializes and prepares the experiment by creating an instance of the `OpenAIChatExperiment` class with the provided model name, chat histories, and model arguments.

#### Behavior:
- Instantiates the `OpenAIChatExperiment` using the `experiment_cls_constructor` with the `model_name`, `chat_histories`, and prepared model arguments.
- Calls the `prepare` method of the superclass to perform any additional preparation steps.

### `run(self)`
Executes the experiment by first ensuring that the experiment is prepared and then calling the `run` method of the superclass.

#### Behavior:
- Checks if the `experiment` attribute is set; if not, it calls the `prepare` method to initialize the experiment.
- Calls the `run` method of the superclass to execute the experiment.

## Usage
The `ChatHistoryExperimentationHarness` class is used in a project to compare the performance or responses of a model across different chat histories. It is instantiated with the required model name, chat histories, and any additional model arguments. The `prepare` method is called to set up the experiment, and the `run` method is called to execute the experiment and obtain results.

## Example
python
# Instantiate the harness with a model name and chat histories
harness = ChatHistoryExperimentationHarness(
    model_name='gpt-3',
    chat_histories=[
        [{'user': 'Hello, how are you?'}, {'bot': 'I am fine, thank you!'}],
        [{'user': 'What's the weather like today?'}, {'bot': 'It's sunny and warm.'}]
    ]
)

# Prepare the experiment
harness.prepare()

# Run the experiment
harness.run()


## Notes
- The `ChatHistoryExperimentationHarness` class is part of a larger project and is expected to be used in conjunction with other components, such as the `ExperimentationHarness` and `OpenAIChatExperiment` classes.
- The file is located at `/workspaces/documentation-generator/target_code/prompttools/harness/chat_history_harness.py` within the project directory structure.
- The source code's license information can be found in the `LICENSE` file in the root directory of the source tree.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/system_prompt_harness.md

# SystemPromptExperimentationHarness Class

## Overview
The `SystemPromptExperimentationHarness` class is a subclass of `ExperimentationHarness` designed to facilitate the testing of various system prompts in conjunction with human (user) messages. It is used to create, run, and analyze experiments that involve sending sequences of system-generated prompts and user messages to a model and observing the model's responses.

## Attributes
- `_experiment_type` (str): A class attribute that defines the type of experiment, set to "Instruction".
- `PIVOT_COLUMNS` (List[str]): A class attribute that specifies the columns to pivot on when displaying results, set to ["system_prompt", "user_input"].

## Constructor
The constructor takes the following parameters:
- `experiment` (Type[Experiment]): The class of the experiment to execute.
- `model_name` (str): The name of the model to be used in the experiment.
- `system_prompts` (List[str]): A list of system-generated prompts to test.
- `human_messages` (List[str]): A list of human messages to pair with system prompts.
- `model_arguments` (Optional[Dict[str, object]]): Additional arguments for the model, with default `None`.

The constructor initializes the following instance variables:
- `experiment_cls_constructor`: Stores the experiment class passed to the constructor.
- `model_name`: Stores the name of the model.
- `system_prompts`: Stores the list of system prompts.
- `human_messages`: Stores the list of human messages.
- `model_arguments`: Stores the model arguments as a dictionary, defaulting to an empty dictionary if `None` is passed.

## Methods

### `_create_system_prompt(content: str) -> Dict[str, str]`
A static method that creates a dictionary representing a system prompt with the given content.

### `_create_human_message(content: str) -> Dict[str, str]`
A static method that creates a dictionary representing a human message with the given content.

### `prepare() -> None`
Prepares the experiment by creating message pairs from system prompts and human messages, initializing the experiment with these pairs, and then calling the `prepare` method of the superclass.

### `run(clear_previous_results: bool = False)`
Runs the experiment. If the experiment is not already prepared, it calls the `prepare` method. It then calls the `run` method of the superclass with the `clear_previous_results` parameter.

### `_get_state()`
Retrieves the current state of the experiment, including the constructor of the experiment class, model name, system prompts, human messages, model arguments, and the state of the child experiment. It returns a tuple containing the state parameters and the full DataFrame of results.

### `_load_state(state, experiment_id: str, revision_id: str, experiment_type_str: str)`
A class method that loads the state of an experiment from the given parameters. It checks if the experiment type matches the current class and raises an error if not. It then reconstructs the harness and experiment from the state parameters.

### `get_table(get_all_cols: bool = False) -> pd.DataFrame`
Returns a DataFrame representing the results of the experiment. If `get_all_cols` is `True`, it returns the full DataFrame; otherwise, it returns a DataFrame with certain columns hidden.

### `visualize(get_all_cols: bool = False)`
Visualizes the results of the experiment. If the environment is interactive (e.g., a Jupyter notebook), it displays the table directly. Otherwise, it logs the table using the `logging` module and the `tabulate` library.

## Usage
The `SystemPromptExperimentationHarness` class is used in a project to conduct experiments on how different system prompts and human messages affect the responses of a model. It is instantiated with the necessary parameters, and then the `prepare` and `run` methods are called to execute the experiment. The results can be visualized or retrieved for further analysis.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/harness.md

# ExperimentationHarness Class

## Overview
The `ExperimentationHarness` class serves as a base class for creating experimentation harnesses within a project. It is designed to manage and facilitate the execution of experiments, including preparation, running, evaluation, visualization, ranking, and saving/loading of experiments. This class should not be directly instantiated; instead, it is intended to be subclassed to create specific experimentation harnesses tailored to particular needs.

## Attributes
- `experiment`: An instance of the `Experiment` class that represents the underlying experiment to be run.
- `PIVOT_COLUMNS`: A list of column names used for pivoting data during visualization and ranking.
- `input_pairs_dict`: A dictionary to store input pairs for feedback gathering (commented out in the current version).
- `runs`: An integer representing the number of times the experiment should be run.
- `_experiment_id`: A string representing the unique identifier of the experiment.
- `_revision_id`: A string representing the unique identifier of the experiment's revision.

## Methods

### `__init__(self) -> None`
Constructor for the `ExperimentationHarness` class. Initializes the `input_pairs_dict`, `experiment`, `runs`, `_experiment_id`, and `_revision_id` attributes.

### `_prepare_arguments(arguments: dict[str, object]) -> dict[str, list[object]]`
A static method that prepares the arguments for the experiment by converting each argument value into a list containing that value.

### `prepare(self) -> None`
Prepares the underlying experiment by calling the `prepare` method of the `Experiment` instance.

### `run(self, clear_previous_results: bool = False) -> None`
Runs the underlying experiment with the specified number of runs and an option to clear previous results.

### `evaluate(self, metric_name: str, eval_fn: Callable, static_eval_fn_kwargs: dict = {}, **eval_fn_kwargs) -> None`
Evaluates the results of the underlying experiment using a specified evaluation function and metric name.

### `visualize(self, pivot: bool = False) -> None`
Displays a visualization of the experiment results, with an option to pivot the data based on `PIVOT_COLUMNS`.

### `rank(self, metric_name: str, is_average: bool = False) -> dict[str, float]`
Scores and ranks the experiment inputs using the pivot columns and returns a dictionary of scores.

### `aggregate(self, groupby_column: str, aggregate_columns: Union[str, list[str]], method: str, custom_df: Optional[pd.DataFrame] = None) -> pd.DataFrame`
Aggregates data based on the specified column and method, returning a pandas DataFrame with the aggregated results.

### `save_experiment(self, name: Optional[str] = None)`
Saves the current state of the experiment to a backend service using an HTTP POST request. Requires an experiment name or an existing `_experiment_id`.

### `load_experiment(cls, experiment_id: str)`
Class method that loads an experiment from a backend service using an HTTP GET request based on the provided experiment ID.

### `load_revision(cls, revision_id: str)`
Class method that loads a specific revision of an experiment from a backend service using an HTTP GET request based on the provided revision ID.

### `_get_state(self)`
An abstract method that should be implemented by subclasses to return the current state of the experiment.

### `_load_state(cls, state, experiment_id: str, revision_id: str, experiment_type_str: str)`
An abstract class method that should be implemented by subclasses to load the state of an experiment.

## Properties
- `full_df`: Returns the full DataFrame of the experiment results.
- `partial_df`: Returns the partial DataFrame of the experiment results.
- `score_df`: Returns the DataFrame of the experiment scores.

## Usage
This class is used as a base for creating specific experimentation harnesses. Subclasses should implement the `_get_state` and `_load_state` methods to handle the saving and loading of experiment states. The class provides functionality to run experiments, evaluate results, visualize data, and rank inputs based on specified metrics. It also supports saving experiments to and loading experiments from a backend service, which requires an API key set in the environment variable `HEGELAI_API_KEY`.

## Dependencies
- `typing`: Provides type hints for function arguments and return types.
- `prompttools.experiment`: Contains the `Experiment` class used for running experiments.
- `prompttools.common`: Contains common constants and functions, such as `HEGEL_BACKEND_URL`.
- `os`: Provides functions for interacting with the operating system.
- `pickle`: Used for serializing and deserializing Python object structures.
- `requests`: Allows sending HTTP requests to a backend service.
- `pandas`: Used for data manipulation and analysis.

## Notes
- The `gather_feedback` method is commented out in the current version of the class.
- The class interacts with a backend service, and the base URL for this service is obtained from `prompttools.common.HEGEL_BACKEND_URL`.
- The class requires an API key (`HEGELAI_API_KEY`) to be set in the environment for saving and loading experiments.
- The class is designed to be flexible and extensible, allowing for customization through subclassing.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/model_comparison_harness.md

# ModelComparisonHarness Class

## Overview
`ModelComparisonHarness` is a subclass of `ExperimentationHarness` designed to facilitate the comparison of different models by running experiments with various system prompts and user messages. It allows for the execution of multiple runs and the evaluation of results using custom metrics.

## Attributes
- `model_names` (List[str]): Names of the models to be compared.
- `system_prompts` (List[str]): System messages corresponding to each model.
- `model_arguments` (List[Optional[dict]]): Arguments for each model, if any.
- `user_messages` (List[str]): User messages to be tested across all models.
- `runs` (int): Number of runs for the experiment.
- `experiments` (List[OpenAIChatExperiment]): List of experiments, one for each model.
- `_experiment_type` (str): Type of the experiment, set to "Comparison".
- `PIVOT_COLUMNS` (List[str]): Columns used for pivoting data in the DataFrame.

## Methods

### `__init__(self, model_names, system_prompts, user_messages, model_arguments=[], runs=1)`
Constructor for the `ModelComparisonHarness` class. It initializes the attributes and validates the lengths of `model_names`, `system_prompts`, and `model_arguments`.

### `prepare(self)`
Initializes and prepares the experiments by creating an `OpenAIChatExperiment` for each model with the corresponding system prompt and user messages.

### `_create_system_prompt(content)`
Static method that creates a dictionary representing a system prompt with the given content.

### `_create_human_message(content)`
Static method that creates a dictionary representing a human message with the given content.

### `full_df(self)`
Property that returns the full DataFrame containing all experiment results.

### `partial_df(self)`
Property that returns the partial DataFrame with a subset of the experiment results.

### `score_df(self)`
Property that returns the DataFrame containing the scores of the experiments.

### `run(self, clear_previous_results=False)`
Executes the experiments. If `clear_previous_results` is set to `True`, previous results are cleared before running.

### `evaluate(self, metric_name, eval_fn, static_eval_fn_kwargs={}, **eval_fn_kwargs)`
Evaluates the experiments using the provided evaluation function and metric name. Additional keyword arguments can be passed to the evaluation function.

### `get_table(self, get_all_cols=False)`
Returns a DataFrame with the experiment results. If `get_all_cols` is `True`, all columns are included; otherwise, certain columns are hidden based on their uniqueness across the results.

### `_update_dfs(self)`
Updates the full, partial, and score DataFrames by concatenating the results from all experiments.

### `visualize(self, get_all_cols=False)`
Displays the results table. If running in an interactive environment, the table is displayed inline; otherwise, it is logged using the `logging` module.

### `_get_state(self)`
Returns the state of the experiment, including model names, system prompts, user messages, model arguments, and the states of child experiments.

### `_load_state(cls, state, experiment_id, revision_id, experiment_type_str)`
Class method that loads the state of a `ModelComparisonHarness` from the provided state parameters. It validates the experiment type and reconstructs the harness and its experiments.

## Usage
The `ModelComparisonHarness` class is used in a project to compare the performance of different models by running them with specified system prompts and user messages. It allows for the evaluation of models using custom metrics and provides methods for visualizing and saving the state of the experiments.

## Example
python
# Initialize the harness with model names, system prompts, and user messages
harness = ModelComparisonHarness(
    model_names=["model1", "model2"],
    system_prompts=["Welcome to model1!", "Welcome to model2!"],
    user_messages=["Hello, how are you?", "What's the weather like today?"],
    runs=3
)

# Prepare the experiments
harness.prepare()

# Run the experiments
harness.run()

# Evaluate the experiments with a custom metric
harness.evaluate(metric_name="accuracy", eval_fn=my_custom_eval_function)

# Visualize the results
harness.visualize()

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/rag_harness.md

# RetrievalAugmentedGenerationExperimentationHarness Class

## Overview

The `RetrievalAugmentedGenerationExperimentationHarness` class is a specialized experimentation harness designed to facilitate the testing and evaluation of Retrieval-Augmented Generation (RAG) processes. This harness integrates a vector database (vector DB) with a Language Model (LLM) to perform experiments that involve retrieving relevant documents and using them to augment the generation capabilities of the LLM.

## Class Definition

python
class RetrievalAugmentedGenerationExperimentationHarness(ExperimentationHarness):


The class inherits from `ExperimentationHarness`, indicating that it is a type of experimentation framework.

## Constructor

python
def __init__(
    self,
    vector_db_experiment: Experiment,
    llm_experiment_cls: Type[Experiment],
    llm_arguments: dict,
    extract_document_fn: Callable,
    extract_query_metadata_fn: Callable,
    prompt_template: str = DOC_PROMPT_TEMPLATE,
):


### Parameters

- `vector_db_experiment`: An instance of `Experiment` that represents the initialized vector DB experiment.
- `llm_experiment_cls`: A class reference to the type of LLM experiment to be executed within the harness (e.g., `prompttools.experiment.OpenAICompletionExperiment`).
- `llm_arguments`: A dictionary containing the arguments to be passed to the LLM experiment.
- `extract_document_fn`: A callable function that takes a row of results from the vector DB experiment and extracts the relevant documents as a list of strings.
- `extract_query_metadata_fn`: A callable function that takes a row of results from the vector DB experiment and extracts relevant metadata for visualization in the final result table.
- `prompt_template`: A Jinja-styled template string where documents and prompts will be inserted. Defaults to `DOC_PROMPT_TEMPLATE`.

### Attributes

- `vector_db_experiment`: Stores the vector DB experiment instance.
- `llm_experiment_cls`: Stores the class reference for the LLM experiment.
- `experiment`: An optional `Experiment` instance that will be initialized and run.
- `llm_arguments`: A copy of the LLM arguments dictionary.
- `extract_document_fn`: The function to extract documents from vector DB results.
- `extract_query_metadata_fn`: The function to extract query metadata from vector DB results.
- `prompt_templates`: The Jinja-styled template for document and prompt insertion.

## Methods

### run

python
def run(self) -> None:


Executes the RAG experimentation process, which includes running the vector DB experiment, extracting documents, augmenting prompts with these documents, running the LLM experiment, and preparing the final results table with retrieval metadata.

### visualize

python
def visualize(self) -> None:


Visualizes the results of the RAG experiment. If the experiment has not been run yet, it calls the `run` method before visualization.

## Helper Functions

### _doc_list_to_str

python
def _doc_list_to_str(documents: list[str]) -> str:


Converts a list of document strings into a single string with each document separated by a newline.

### _generate_doc_prompt

python
def _generate_doc_prompt(documents: list[str], prompt_or_msg: Union[str, list[dict[str, str]]], is_chat: bool):


Generates a document-augmented prompt using the provided documents and either a prompt string or a chat message object, depending on whether the `is_chat` flag is set.

## Usage

The `RetrievalAugmentedGenerationExperimentationHarness` is used in a project to conduct experiments that combine document retrieval with language generation. It is particularly useful for evaluating how well a language model can generate responses when provided with additional context from relevant documents retrieved by a vector database.

## Example

To use this class, one would typically:

1. Initialize a vector DB experiment.
2. Define the LLM experiment class and its arguments.
3. Provide functions to extract documents and query metadata from the vector DB results.
4. Create an instance of `RetrievalAugmentedGenerationExperimentationHarness` with the above components.
5. Call the `run` method to execute the RAG experiment.
6. Optionally, call the `visualize` method to display the results.

python
# Example instantiation and execution
vector_db_exp = SomeVectorDBExperiment(...)
llm_exp_cls = SomeLLMExperiment
llm_args = {...}
extract_docs = lambda row: ...
extract_meta = lambda row: ...

rag_harness = RetrievalAugmentedGenerationExperimentationHarness(
    vector_db_experiment=vector_db_exp,
    llm_experiment_cls=llm_exp_cls,
    llm_arguments=llm_args,
    extract_document_fn=extract_docs,
    extract_query_metadata_fn=extract_meta
)

rag_harness.run()
rag_harness.visualize()

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/prompt_template_harness.md

# PromptTemplateExperimentationHarness Class

## Overview
The `PromptTemplateExperimentationHarness` class is a specialized experimentation harness designed for testing various prompt templates using the Jinja templating engine. It extends the `ExperimentationHarness` class and is tailored to work with experiments that involve generating prompts from templates and collecting responses from a model.

## Attributes
- `environment`: An instance of `jinja2.Environment` used to manage the Jinja templating environment.
- `experiment_cls_constructor`: A constructor for the experiment class that will be executed within the harness.
- `model_name`: A string representing the name of the model to be used in the experiment.
- `prompt_templates`: A list of strings, each a Jinja-styled template for generating prompts.
- `user_inputs`: A list of dictionaries, where each dictionary represents user inputs that will be rendered into the prompt templates.
- `model_arguments`: An optional dictionary of additional arguments for the model. Defaults to an empty dictionary if `None` is provided.
- `input_pairs_dict`: A dictionary that maps rendered prompts to their corresponding template and user input pair.
- `experiment`: An instance of the experiment class specified by `experiment_cls_constructor`.

## Constants
- `PIVOT_COLUMNS`: A list of strings defining the columns used to pivot data in the experiment results. It includes `"prompt_template"` and `"user_input"`.

## Methods

### `__init__`
The constructor initializes the harness with the necessary parameters for the experiment.

#### Parameters
- `experiment`: The experiment class constructor to be executed within the harness.
- `model_name`: The name of the model to be used in the experiment.
- `prompt_templates`: A list of Jinja-styled prompt templates.
- `user_inputs`: A list of dictionaries representing user inputs.
- `model_arguments`: Additional arguments for the model, if any.

### `prepare`
The `prepare` method is responsible for creating prompts from the provided templates and user inputs. It then initializes and prepares the experiment with these prompts.

#### Process
1. Initializes an empty dictionary for `input_pairs_dict`.
2. Iterates over each prompt template and user input pair.
3. Renders the prompt using the Jinja template and user input.
4. Appends the rendered prompt to the `rendered_inputs` list.
5. Maps the rendered prompt to its template and user input in `input_pairs_dict`.
6. Constructs the experiment instance with the model name, rendered inputs, and model arguments.
7. Calls the `prepare` method of the superclass (`ExperimentationHarness`).

### `run`
The `run` method executes the experiment. It ensures that the experiment is prepared before running it.

#### Process
1. Checks if the `experiment` instance is not initialized and calls `prepare` if necessary.
2. Calls the `run` method of the superclass (`ExperimentationHarness`).

## Usage
The `PromptTemplateExperimentationHarness` class is used in a project to conduct experiments on different prompt templates. It automates the process of generating prompts, running them through a specified model, and collecting the results. This is particularly useful for evaluating the performance of language models on a variety of templated prompts and user inputs.

## Example
To use the `PromptTemplateExperimentationHarness`, one would need to:

1. Define a list of Jinja-styled prompt templates.
2. Create a list of dictionaries representing different user inputs.
3. Specify the model name and any additional model arguments.
4. Instantiate the `PromptTemplateExperimentationHarness` with the appropriate experiment class, model name, prompt templates, user inputs, and model arguments.
5. Call the `prepare` method to set up the experiment.
6. Call the `run` method to execute the experiment and collect results.

---



File Path: /workspaces/documentation-generator/generated_documentation/prompttools/harness/__init__.md

# `__init__.py` Module in `prompttools/harness` Package

## Overview

The `__init__.py` file serves as the initialization module for the `harness` subpackage within the `prompttools` package of the project. This module is responsible for importing and exposing various experimentation harness classes that are used to conduct different types of experiments or comparisons within the project's scope.

## Detailed Description

### Imports

The module imports several classes from other modules within the same `harness` subpackage:

- `ExperimentationHarness`: A base class for creating experimentation harnesses.
- `ChatHistoryExperimentationHarness`: A class for conducting experiments involving chat history.
- `ChatModelComparisonHarness`: A class for comparing different chat models.
- `ChatPromptTemplateExperimentationHarness`: A class for experimenting with chat prompt templates.
- `ModelComparisonHarness`: A class for comparing different models.
- `MultiExperimentHarness`: A class for running multiple experiments in parallel or sequence.
- `PromptTemplateExperimentationHarness`: A class for experimenting with prompt templates.
- `RetrievalAugmentedGenerationExperimentationHarness`: A class for experimenting with retrieval-augmented generation models.
- `SystemPromptExperimentationHarness`: A class for experimenting with system-generated prompts.

### `__all__` Variable

The `__all__` variable is a list of strings that specifies which symbols will be exported when `from prompttools.harness import *` is used. It includes the names of all the imported classes, ensuring that they are accessible when the `harness` subpackage is imported elsewhere in the project.

### Usage

The classes defined in the `__all__` list can be used throughout the project to create instances of the experimentation harnesses for various purposes:

- To conduct experiments that require tracking and analyzing chat history.
- To compare the performance or behavior of different chat models.
- To test and refine chat prompt templates.
- To compare various models for specific tasks or under certain conditions.
- To manage and execute multiple experiments.
- To experiment with different prompt templates and their effects on model outputs.
- To explore the capabilities of retrieval-augmented generation models.
- To analyze the effectiveness of system-generated prompts.

Each class encapsulates specific functionality and methods that are tailored to the type of experimentation it is designed for. These classes likely provide methods to set up experiments, run them, collect results, and possibly analyze and report on the findings.

### File Metadata

The file begins with a copyright notice for Hegel AI, Inc., indicating the proprietary nature of the source code. It also mentions that the license for the source code can be found in the `LICENSE` file located in the root directory of the source tree.

## Conclusion

The `__init__.py` file in the `prompttools/harness` package is a central point for importing and exposing various experimentation harness classes. These classes are essential for conducting different types of experiments within the project, and their availability through this module simplifies their use in other parts of the project.

---



