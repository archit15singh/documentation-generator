```markdown
# Renderer Class

## Overview

The `Renderer` class is a utility for rendering Jinja2 templates to strings. It is designed to work with a directory of templates and can render individual templates or an entire directory tree of templates. The class does not write the rendered output to disk; instead, it returns the rendered templates as strings.

## Class Methods

### `__init__(self, template_dir: str)`

The constructor method initializes the `Renderer` instance.

#### Parameters:

- `template_dir`: A string specifying the path to the directory containing the Jinja2 templates.

#### Behavior:

- Initializes the `template_dir` attribute with the provided directory path.
- Sets up the Jinja2 environment with the following configurations:
  - `loader`: Uses `FileSystemLoader` to load templates from the `template_dir`.
  - `autoescape`: Disabled to prevent automatic escaping of values.
  - `lstrip_blocks`: Enabled to strip leading spaces and tabs from the start of a line to the start of a block.
  - `trim_blocks`: Enabled to strip trailing newline and spaces from the end of a block.
  - `keep_trailing_newline`: Enabled to preserve the trailing newline when rendering templates.

### `render_template(self, template: str, context: Any) -> str`

Renders a single Jinja2 template to a string.

#### Parameters:

- `template`: A string representing the name of the template file, relative to the `template_dir`.
- `context`: A dictionary or object providing the context variables for rendering the template.

#### Returns:

- A string containing the rendered template.

#### Behavior:

- Normalizes the template path to use forward slashes (`/`), even on Windows systems.
- Retrieves the template object from the Jinja2 environment using the normalized path.
- Renders the template with the provided context and returns the result as a string.

### `render_tree(self, root: str, context: Any, filter: Callable = None) -> dict[str, str]`

Renders all Jinja2 templates within a directory tree to a dictionary of strings.

#### Parameters:

- `root`: A string representing the root directory of the tree to render, relative to the `template_dir`.
- `context`: A dictionary or object providing the context variables for rendering the templates.
- `filter`: An optional callable that determines whether a file should be processed and its output file path. It should accept a single string argument (the file name relative to the tree root) and return a non-empty string to process the file or `None`/an empty string to skip it.

#### Returns:

- A dictionary with the structure `{file_name: contents}`, where `file_name` is the relative path of the file from the tree root and `contents` is the rendered template as a string.

#### Behavior:

- Iterates over the files in the directory tree starting from the `full_root` (the absolute path of the `root` within the `template_dir`).
- For each file, calculates the relative path to the `template_dir` (`tpl_location`) and the relative path to the `root` (`output_location`).
- If a `filter` is provided, it is called with `output_location`. If the `filter` returns a non-empty string, the file is rendered; otherwise, it is skipped.
- Renders each template using the `render_template` method with the provided context.
- Adds the rendered content to the return dictionary with the key as the `output_location`.

## Usage Example

```python
from render import Renderer

r = Renderer('path/to/templates')
output_string = r.render_template('template.html', {'key': 'value'})
output_tree = r.render_tree('tree/root', {'key': 'value'})
```

## Notes

- The `Renderer` class is designed to be used within a project that requires rendering of Jinja2 templates to strings.
- The class does not handle writing the rendered output to disk; this must be managed by the calling code if needed.
- The `filter` parameter in `render_tree` allows for selective rendering of files within the directory tree.
- The `Renderer` class can be extended to include additional Jinja2 filters by adding them to the `jinja_env.filters` dictionary in the constructor.
```