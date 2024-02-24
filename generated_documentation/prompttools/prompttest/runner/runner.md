```markdown
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
```