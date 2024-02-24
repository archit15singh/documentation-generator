```markdown
# custom_print.py Module

## Overview

The `custom_print.py` module provides a mechanism for overriding the default `print` function in Python with a custom print function that can either output messages locally or send them to an external logging process via inter-process communication (IPC). This module is part of the `/workspaces/documentation-generator/target_code/pilot/utils/` directory and is used within the project to handle logging and message output in a more flexible way.

## Dependencies

- `builtins`: A module that provides access to the built-in functions of the Python interpreter.
- `helpers.ipc`: A custom module that likely provides IPC functionality, including the `IPCClient` class.
- `const.ipc`: A custom module that likely contains constants related to IPC, such as `MESSAGE_TYPE` and `LOCAL_IGNORE_MESSAGE_TYPES`.

## Functions

### get_custom_print(args)

The `get_custom_print` function is the main entry point of the module. It takes a dictionary `args` as an argument, which should contain command-line arguments or other configuration options.

#### Parameters

- `args`: A dictionary containing configuration options or command-line arguments.

#### Returns

- A tuple containing the custom print function and an instance of `IPCClient` if applicable.

#### Behavior

1. The function first saves a reference to the built-in `print` function as `built_in_print`.
2. It then defines two nested functions: `print_to_external_process` and `local_print`.

#### Nested Functions

##### print_to_external_process(*args, **kwargs)

This function is designed to send print messages to an external process for logging.

###### Parameters

- `*args`: Variable length argument list for the messages to be printed.
- `**kwargs`: Arbitrary keyword arguments, including a 'type' that specifies the message type.

###### Behavior

- If the 'type' keyword argument is not provided, it defaults to 'verbose'.
- If the 'type' is 'local', it calls `local_print` and returns immediately.
- It sends a message to the external process using the `ipc_client_instance.send` method with the message type and content.
- If the message type is 'user_input_request', it waits for a response from the external process using `ipc_client_instance.listen` and returns the response.

##### local_print(*args, **kwargs)

This function is a wrapper around the built-in `print` function that respects certain message types.

###### Parameters

- `*args`: Variable length argument list for the messages to be printed.
- `**kwargs`: Arbitrary keyword arguments, including a 'type' that specifies the message type.

###### Behavior

- It constructs a message string by joining all arguments with a space.
- If the 'type' keyword argument is present and is in `LOCAL_IGNORE_MESSAGE_TYPES`, the function returns without printing.
- If the 'type' keyword argument is present and not in `LOCAL_IGNORE_MESSAGE_TYPES`, it is removed from `kwargs`.
- It calls the built-in `print` function with the constructed message and any remaining keyword arguments.

#### Initialization

- The function initializes `ipc_client_instance` to `None`.
- If the `--external-log-process-port` argument is present in `args`, it creates an `IPCClient` instance with the provided port and returns `print_to_external_process` and the `ipc_client_instance`.
- If the `--external-log-process-port` argument is not present, it returns `local_print` and `ipc_client_instance` as `None`.

## Usage

The `get_custom_print` function is typically called at the start of the application or script to determine the appropriate print function based on the provided arguments. The returned print function is then used throughout the project instead of the built-in `print` to allow for more controlled and configurable output handling.
```
