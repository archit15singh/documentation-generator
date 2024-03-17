```markdown
# `timeout_utils.py` Module

## Overview

The `timeout_utils.py` module provides a utility function `run_with_timeout` that allows the execution of any callable (function/method) with a specified timeout duration. If the callable does not complete its execution within the given timeout, a `TimeoutError` is raised.

## `run_with_timeout` Function

### Description

The `run_with_timeout` function is designed to execute a given callable with the ability to enforce a timeout. It uses threading to run the callable in a separate thread, allowing the main thread to continue execution and monitor the timeout.

### Parameters

- `func`: The callable (function or method) to be executed with a timeout.
- `args` (optional): A tuple containing positional arguments to pass to the callable. Defaults to an empty tuple `()`.
- `kwargs` (optional): A dictionary containing keyword arguments to pass to the callable. Defaults to `None`, which is then initialized to an empty dictionary `{}`.
- `timeout_duration` (optional): An integer or float specifying the maximum number of seconds to wait for the callable to complete. Defaults to `60` seconds.

### Returns

- The function returns the result of the callable `func` if it completes execution within the specified `timeout_duration`.

### Exceptions

- `TimeoutError`: Raised if the callable does not complete within the `timeout_duration`.
- Any exception raised by the callable `func` during its execution is re-raised by `run_with_timeout`.

### Usage

The function is used to wrap the execution of a callable that may potentially run for an indeterminate amount of time or is at risk of hanging. By setting a timeout, the function ensures that the rest of the application can continue to run or handle the timeout situation appropriately.

### Implementation Details

1. The function first checks if `kwargs` is `None` and initializes it to an empty dictionary if necessary.
2. A nested function `func_wrapper` is defined within `run_with_timeout`. This function takes a single argument `result_container`, which is a list used to store the result or exception from the callable.
3. The `func_wrapper` tries to execute the callable with the provided `args` and `kwargs`. The result or any exception is appended to `result_container`.
4. A list `result_container` is initialized to store the result of the callable.
5. A `Thread` object from the `threading` module is created with the target set to `func_wrapper` and `result_container` passed as an argument.
6. The thread is started with `thread.start()`, which begins the execution of `func_wrapper` in a separate thread.
7. The main thread waits for the callable to complete with `thread.join(timeout=timeout_duration)`. If the callable finishes before the timeout, the main thread resumes execution.
8. If the thread is still alive after the timeout, a `TimeoutError` is raised, indicating that the function execution exceeded the timeout.
9. If `result_container` is not empty, the function checks if the first element is an instance of `Exception`. If it is, the exception is raised; otherwise, the result of the callable is returned.
10. If `result_container` is empty after the thread join, a `TimeoutError` is raised, indicating that the function execution exceeded the timeout.

### Example

```python
from dataherald.utils.timeout_utils import run_with_timeout

def long_running_task(param1, param2):
    # Simulate a long-running task
    time.sleep(120)
    return param1 + param2

# This will raise a TimeoutError after 60 seconds
try:
    result = run_with_timeout(long_running_task, args=(10, 20), timeout_duration=60)
except TimeoutError:
    print("The task did not complete in time.")
```

In this example, `long_running_task` is a function that simulates a long-running operation. The `run_with_timeout` function is used to execute it with a timeout of 60 seconds. Since the task is designed to run longer than the timeout, a `TimeoutError` will be raised.
```