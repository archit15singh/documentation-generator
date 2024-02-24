```markdown
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
```python
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
```

In this example, the `ChatModelComparisonHarness` is used to compare two models, `model_1` and `model_2`, over three runs using a predefined chat history. After running the experiment, the results are compared to evaluate the performance of each model.
```