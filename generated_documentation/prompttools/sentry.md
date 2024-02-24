```markdown
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
```