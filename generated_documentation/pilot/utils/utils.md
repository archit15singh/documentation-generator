```markdown
# utils/utils.py

This file contains utility functions used throughout the project. It provides a set of helper methods for string manipulation, template rendering, system information retrieval, step execution logic, data hashing, JSON handling, and file name sanitization.

## Functions

### `capitalize_first_word_with_underscores(s)`
- Takes a string `s` as input.
- Splits the string into words based on underscores.
- Capitalizes the first word and leaves the rest unchanged.
- Joins the words back into a string with underscores.
- Returns the modified string.

### `get_prompt(prompt_name, original_data=None)`
- Accepts a `prompt_name` indicating the template name and an optional `original_data` dictionary.
- Deep copies `original_data` if provided, otherwise initializes an empty dictionary.
- Calls `get_prompt_components(data)` to read and render all prompts inside `/prompts/components`.
- Logs the action of getting a prompt.
- Loads the Jinja2 template specified by `prompt_name`.
- Renders the template with the provided data.
- Returns the rendered template output as a string.

### `get_prompt_components(data)`
- Accepts a dictionary `data` to be updated with prompt components.
- Updates `data` with constants `MAX_QUESTIONS` and `END_RESPONSE`.
- Loads Jinja2 templates from `/prompts/components`.
- Iterates over each template, rendering it with the provided `data`.
- Updates `data` with the rendered content of each template, using the filename without extension as the key.
- Returns the updated `data` dictionary.

### `get_sys_message(role, args=None)`
- Accepts a `role` string and an optional `args` dictionary.
- Calls `get_prompt` with the appropriate system message template for the given `role` and `args`.
- Returns a dictionary with the keys `"role"` set to `"system"` and `"content"` set to the rendered template content.

### `find_role_from_step(target)`
- Accepts a `target` step name.
- Iterates over the `ROLES` dictionary to find a role that includes the `target` step.
- Returns the role name if found, otherwise defaults to `'product_owner'`.

### `get_os_info()`
- Retrieves system information such as OS, version, architecture, machine, node, and release.
- Adds distribution information for Linux, Windows version, or Mac version as applicable.
- Converts the system information dictionary to a readable text format.
- Returns the formatted system information string.

### `should_execute_step(arg_step, current_step)`
- Accepts `arg_step` (which may be `None`) and `current_step`.
- Determines the index of `arg_step` and `current_step` within the `STEPS` list.
- Returns `True` if `current_step` should be executed based on the index comparison.

### `step_already_finished(args, step)`
- Updates `args` with `step['app_data']`.
- Constructs a message indicating the step has been finished, capitalizing the first word of the step.
- Prints the message in green color and logs the information.
- No return value.

### `generate_app_data(args)`
- Accepts a dictionary `args` containing `'app_id'` and `'app_type'`.
- Returns a new dictionary with `'app_id'` and `'app_type'` extracted from `args`.

### `array_of_objects_to_string(array)`
- Accepts a dictionary `array`.
- Converts the dictionary into a string with each key-value pair on a new line.
- Returns the formatted string.

### `hash_data(data)`
- Serializes the input `data` dictionary into a JSON string, ensuring keys are sorted.
- Encodes the serialized data to UTF-8.
- Computes the SHA256 hash of the serialized data.
- Returns the hexadecimal digest of the hash.

### `replace_functions(obj)`
- Recursively processes an input `obj` (which can be a dictionary, list, or other).
- If `obj` is a dictionary or list, applies itself to each element.
- If `obj` is a callable (function), replaces it with the string `"function"`.
- Returns the processed object with functions replaced.

### `fix_json(s)`
- Accepts a JSON-like string `s`.
- Replaces occurrences of `True` with `true` and `False` with `false`.
- Calls `fix_json_newlines(s)` to handle newline characters.
- Returns the fixed JSON string.

### `fix_json_newlines(s)`
- Accepts a string `s` containing JSON data.
- Uses a regular expression to find JSON string literals.
- Replaces newline characters within the string literals with `\\n`.
- Returns the JSON string with fixed newlines.

### `clean_filename(filename)`
- Accepts a `filename` string.
- Removes invalid characters for filenames using a regular expression.
- Replaces whitespace with underscores.
- Returns the sanitized filename.

### `json_serial(obj)`
- JSON serializer for objects not serializable by default JSON code.
- Handles `datetime.datetime`, `datetime.date`, and `uuid.UUID` by returning their ISO format or string representation.
- For other types, returns the string representation.

### `remove_lines_with_string(file_content, matching_string)`
- Accepts `file_content` as a string and a `matching_string` to match lines against.
- Splits `file_content` into lines.
- Filters out lines that contain `matching_string` (case-insensitive).
- Joins the remaining lines back into a single string.
- Returns the string with matching lines removed.
```