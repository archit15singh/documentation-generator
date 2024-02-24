```markdown
# SpecWriter Class

## Overview
The `SpecWriter` class is a subclass of `Agent` and is responsible for refining a project's initial description by interacting with the user to gather more detailed information. It also reviews the refined specification to ensure completeness and accuracy.

## Attributes
- `save_dev_steps` (bool): A flag indicating whether to save the development steps.

## Methods

### `__init__(self, project)`
Constructor for the `SpecWriter` class.
- Parameters:
  - `project`: The project context in which the `SpecWriter` operates.
- Initializes the `SpecWriter` instance by calling the superclass constructor with the agent type `'spec_writer'` and the provided project context.
- Sets `self.save_dev_steps` to `True`.

### `analyze_project(self, initial_prompt)`
Interacts with the user to refine the project description.
- Parameters:
  - `initial_prompt` (str): The initial project description provided by the user.
- Behavior:
  - Prints a message suggesting the user to provide a more detailed project description, including a link to a guide on writing a good project description.
  - Initializes an `AgentConvo` instance for conversation management.
  - Constructs and adds a message to the conversation using a predefined prompt.
  - Enters a loop to interact with the user, sending and receiving messages to refine the project description.
  - Counts the number of questions asked during the interaction.
  - If the user's response is affirmative or 'continue', the loop breaks.
  - If the user chooses to 'skip questions', the loop also breaks, and the interaction is considered complete.
  - Logs the interaction details using `trace_code_event`.
- Returns:
  - The refined project description as a string.

### `review_spec(self, initial_prompt, spec)`
Reviews the refined project specification for completeness.
- Parameters:
  - `initial_prompt` (str): The initial project description provided by the user.
  - `spec` (str): The refined project specification.
- Behavior:
  - Initializes an `AgentConvo` instance with a temperature of 0 for deterministic responses.
  - Sends a message to review the specification using a predefined prompt.
  - Returns the response from the conversation, stripped of leading and trailing whitespace.

### `create_spec(self, initial_prompt)`
Creates a complete project specification based on the initial prompt.
- Parameters:
  - `initial_prompt` (str): The initial project description provided by the user.
- Behavior:
  - If the initial prompt is already detailed (more than 1500 characters), it is returned as the specification.
  - Otherwise, it calls `analyze_project` to refine the project description.
  - Calls `review_spec` to review the refined specification and append any missing information.
- Returns:
  - The complete project specification as a string.

## Usage
The `SpecWriter` class is used in a project to interactively refine and review a project's initial description. It ensures that the project specification is detailed enough for the GPT Pilot to understand the project requirements and generate appropriate outputs.

## Dependencies
- `helpers.AgentConvo`: Used for managing conversations with the user.
- `helpers.Agent`: The superclass from which `SpecWriter` inherits.
- `utils.files.count_lines_of_code`: Utility function to count lines of code (not directly used in the provided code).
- `utils.style.color_green_bold`, `utils.style.color_yellow_bold`: Utility functions to print colored and bold text.
- `prompts.prompts.ask_user`: Function to prompt the user for input.
- `const.messages.AFFIRMATIVE_ANSWERS`: A list of affirmative answers to check against user responses.
- `utils.exit.trace_code_event`: Function to log code events for analysis.

## Constants
- `INITIAL_PROJECT_HOWTO_URL`: A URL pointing to a guide on writing a good initial project description.
```