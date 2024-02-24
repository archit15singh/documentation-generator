```markdown
# RetrievalAugmentedGenerationExperimentationHarness Class

## Overview

The `RetrievalAugmentedGenerationExperimentationHarness` class is a specialized experimentation harness designed to facilitate the testing and evaluation of Retrieval-Augmented Generation (RAG) processes. This harness integrates a vector database (vector DB) with a Language Model (LLM) to perform experiments that involve retrieving relevant documents and using them to augment the generation capabilities of the LLM.

## Class Definition

```python
class RetrievalAugmentedGenerationExperimentationHarness(ExperimentationHarness):
```

The class inherits from `ExperimentationHarness`, indicating that it is a type of experimentation framework.

## Constructor

```python
def __init__(
    self,
    vector_db_experiment: Experiment,
    llm_experiment_cls: Type[Experiment],
    llm_arguments: dict,
    extract_document_fn: Callable,
    extract_query_metadata_fn: Callable,
    prompt_template: str = DOC_PROMPT_TEMPLATE,
):
```

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

```python
def run(self) -> None:
```

Executes the RAG experimentation process, which includes running the vector DB experiment, extracting documents, augmenting prompts with these documents, running the LLM experiment, and preparing the final results table with retrieval metadata.

### visualize

```python
def visualize(self) -> None:
```

Visualizes the results of the RAG experiment. If the experiment has not been run yet, it calls the `run` method before visualization.

## Helper Functions

### _doc_list_to_str

```python
def _doc_list_to_str(documents: list[str]) -> str:
```

Converts a list of document strings into a single string with each document separated by a newline.

### _generate_doc_prompt

```python
def _generate_doc_prompt(documents: list[str], prompt_or_msg: Union[str, list[dict[str, str]]], is_chat: bool):
```

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

```python
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
```
```