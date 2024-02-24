```markdown
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
```
