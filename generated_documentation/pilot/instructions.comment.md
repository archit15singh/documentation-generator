```markdown
# Technical Documentation for `instructions.comment.py`

## Overview
The `instructions.comment.py` file serves as a blueprint for a command-line interface (CLI) tool that guides users through the process of setting up and configuring a new application. The file outlines a series of steps and interactions that the CLI will facilitate, ensuring that the user can define the application type, user flow, components, and file structure. Additionally, it includes a workflow for creating and running tests, debugging, and preparing the application for execution.

## Detailed Step-by-Step Description

### Step 1: Initialize CLI
- Display the default type of application to be created.
- Prompt the user to press enter to accept the default app type or to input a different app type they desire.
  - If the user inputs a different app type, the CLI checks if the requested type can be created.
    - If the requested app type is valid, a confirmation message is displayed, and the process continues.
    - If the requested app type is invalid, an error message is shown, and the CLI exits.

### Step 2: Define Main Application
- Ask the user for the main definition of the application.
- Begin the processing queue.

### Step 3: User Flow
- Display the current user flow of the application.
- Prompt the user to press enter to accept the displayed user flow or to input their desired user flow.
  - Continue to request input until the user just presses enter.
  - Recompute the user flow based on user input and ask for confirmation again.

### Step 4: Application Components
- Show the different components of the application, including:
  - Frontend
  - Backend
  - Database
  - Configuration
- Prompt the user to press enter to accept the displayed components or to input their desired components.
  - Continue to request input until the user just presses enter.
  - Recompute the components based on user input and ask for confirmation again.

### Step 5: File Breakdown
- Break down the files needed to support each of the components.
- Prompt the user to press enter to accept the file structure or to input their desired files.
  - Continue to request input until the user just presses enter.
  - Recompute the files based on user input and ask for confirmation again.

### Step 6: Component and Use Case Processing
- Loop through each component of the application.
  - For each component, loop through its use cases.
    - Break down the files, functions, and dependencies that need to be created for each case.
    - Provide a description for each function.
    - In each loop, send all previously defined files and functions to the language model (LLM) for potential modifications.

### Step 7: Test Breakdown
- Outline the tests that need to be created, starting from high-level tests down to unit tests.
- Include all files and functions in the prompt for test creation.
- Prompt the user to press enter to accept the tests or to input their desired tests.
  - Continue to request input until the user just presses enter.
  - Recompute the tests based on user input and ask for confirmation again.

### Step 8: Test Writing
- Write the tests for the application.

### Step 9: File Writing for Tests
- Write the necessary files to support each test.

### Step 10: Test Execution
- Run each created test once the corresponding code is written.
  - Begin with low-level tests and proceed to high-level tests.
  - Track the relationship between tests and code.
  - Before running a test, specify which functions it will use and check if any of those functions are already written.
  - If a function is already written, send it to the LLM for potential changes.
  - Track code coverage and aim to reach 100%.
  - If the code requires configuration, prompt the user to add it.
  - When files overlap, request the LLM to combine them.

### Step 11: Debugging
- Attempt debugging five times.
  - If debugging is unsuccessful, prompt the user to debug the issue.
    - Provide explanations to the user.
    - Request input from the user if they wish to contribute to the debugging process and retry up to five debugging attempts.

### Step 12: Build/Run Script Creation
- Create a script to build and/or run the application.

### Step 13: Application Execution
- Execute the application.

## Additional Setup Components

### Installation Process
- Outline the steps required for installing the application.

### Configuration Process
- Detail the configuration steps necessary for preparing the application for use.

### Running Process
- Describe the process for running the application.

### Building Process
- Provide instructions for building the application.

### Testing Process
- Explain the process for testing the application.

## Comments
- Consider using an additional model to extract actionable items from the GPT responses, such as commands to run, updates to make, and comments to organize. This would alleviate the need to teach the original model these context-specific tasks in-context.
```