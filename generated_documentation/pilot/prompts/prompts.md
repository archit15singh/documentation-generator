```markdown
# Technical Documentation for prompts.py

## Overview
The `prompts.py` module is part of a larger project and is responsible for interacting with the user to gather information about the application they want to build. It provides a series of prompts to the user and processes their responses. The module also generates messages for further processing by other components of the system.

## Functions

### ask_for_app_type
- **Purpose**: To prompt the user to select the type of application they want to build from a predefined list of app types.
- **Returns**: The selected app type as a string.
- **Behavior**:
  - The function presents the user with a selection prompt using `styled_select`.
  - If the user selects an option marked as 'unavailable', they are informed that the option is not available and are prompted again.
  - If the user exits the selection (e.g., by pressing Ctrl+C), the application prints an exit message and terminates.
  - The chosen app type is logged using the `logger` module.
  - The function returns the chosen app type.

### ask_for_main_app_definition
- **Purpose**: To ask the user to describe their application in detail.
- **Parameters**:
  - `project`: An object representing the current project context.
- **Returns**: The user's description of the app as a string, or `None` if no input is provided.
- **Behavior**:
  - The function prints a question asking the user to describe their app.
  - It calls `ask_user` to get the user's input.
  - If no input is provided, it logs a message and returns `None`.
  - The description is logged and then returned.

### ask_user
- **Purpose**: To ask the user a question and process their response.
- **Parameters**:
  - `project`: The current project context.
  - `question`: A string containing the question to be asked.
  - `require_some_input`: A boolean indicating whether the function should require input before proceeding.
  - `hint`: An optional string providing a hint to the user.
  - `ignore_user_input_count`: A boolean indicating whether to ignore the count of user inputs.
- **Returns**: The user's response as a string, or `None` if the user exits.
- **Behavior**:
  - The function enters a loop where it presents the question to the user using `styled_text`.
  - If a hint is provided, it is displayed in bold white color.
  - The user's response is logged.
  - If the user provides no input and `require_some_input` is `True`, the function prompts the user again.
  - If the user exits, the application prints an exit message and terminates.
  - The function returns the user's response.

### generate_messages_from_description
- **Purpose**: To generate a sequence of messages based on the user's app description and selected app type.
- **Parameters**:
  - `description`: A string containing the user's description of the app.
  - `app_type`: A string representing the type of app the user wants to build.
  - `name`: A string representing the project name.
- **Returns**: A list of message dictionaries with roles and content.
- **Behavior**:
  - The function constructs a user prompt using the provided description, app type, and project name.
  - It retrieves additional instructions for specifying the app using `get_prompt`.
  - It returns a list of messages, including system messages and user prompts, to guide the user through the specification process.

### generate_messages_from_custom_conversation
- **Purpose**: To generate a sequence of messages for a custom conversation based on the role and provided messages.
- **Parameters**:
  - `role`: A string representing the user's role in the conversation.
  - `messages`: A list of strings representing the conversation messages.
  - `start_role`: A string indicating the role that starts the conversation.
- **Returns**: A list of message dictionaries with roles and content.
- **Behavior**:
  - The function retrieves a system message for the given role using `get_sys_message`.
  - It alternates between the `start_role` and the assistant (or user, if the `start_role` is not 'user') to construct a conversation flow.
  - Each message is logged for debugging purposes.
  - The function returns the constructed list of messages.

## Usage
The functions in `prompts.py` are typically called during the initial stages of the project to gather information from the user about the application they wish to build. The responses are used to guide the development process and to generate further conversations with the user.

## Notes
- The `ask_for_app_type` function contains a hardcoded return statement at the beginning, which should be removed to enable the actual functionality.
- The `generate_messages_from_description` function contains a TODO comment indicating that the `MAX_QUESTIONS` variable should be made configurable.
- The `generate_messages_from_custom_conversation` function also contains a TODO comment suggesting a refactor to comply with the `AgentConvo` class.
- The module relies on other utility modules such as `utils.style`, `const.common`, `const.llm`, `utils.llm_connection`, `utils.utils`, `utils.questionary`, and `logger.logger`.
- The module handles user input and system exit scenarios gracefully, ensuring that the user is informed before the application terminates.
- The module is designed to be extensible, allowing for additional prompts and conversation flows to be added as needed.
```
