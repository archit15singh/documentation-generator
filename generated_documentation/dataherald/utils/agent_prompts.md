```markdown
# `agent_prompts.py` Technical Documentation

## Overview

The `agent_prompts.py` file contains predefined templates and instructions used by an agent designed to generate SQL queries in response to input questions. The agent interacts with a SQL database and utilizes various tools to ensure the generated SQL queries are syntactically correct and yield the correct results when executed against the database.

## Constants

### `AGENT_PREFIX`

This constant defines a template that outlines the agent's role, the expected format for the SQL query, and the tools available for interaction with the database. It also provides a plan for the agent to follow and restrictions on the use of certain SQL functions.

- **Usage**: This template is used as a prefix to guide the agent's behavior when generating SQL queries.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.
  - `{agent_plan}`: Placeholder for the specific plan the agent should follow.

### `PLAN_WITH_FEWSHOT_EXAMPLES_AND_INSTRUCTIONS`

This constant provides a detailed step-by-step plan for the agent to follow when few-shot examples are available, and database administrator instructions need to be considered.

- **Usage**: This plan is used when the agent has access to similar Question/SQL pairs and must adhere to specific instructions provided by a database administrator.
- **Parameters**:
  - `{max_examples}`: Placeholder for the maximum number of Question/SQL pairs the agent can request.
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `PLAN_WITH_INSTRUCTIONS`

This constant provides a step-by-step plan for the agent to follow when database administrator instructions need to be considered, but few-shot examples are not available.

- **Usage**: This plan is used when the agent must generate SQL queries while following specific instructions but does not have access to similar Question/SQL pairs.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `PLAN_WITH_FEWSHOT_EXAMPLES`

This constant provides a step-by-step plan for the agent to follow when few-shot examples are available, but there are no specific database administrator instructions to consider.

- **Usage**: This plan is used when the agent has access to similar Question/SQL pairs but does not need to follow additional instructions.
- **Parameters**:
  - `{max_examples}`: Placeholder for the maximum number of Question/SQL pairs the agent can request.
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `PLAN_BASE`

This constant provides a base step-by-step plan for the agent to follow when neither few-shot examples nor specific database administrator instructions are available.

- **Usage**: This plan is used as a fallback when the agent must generate SQL queries without additional guidance or examples.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.

### `FORMAT_INSTRUCTIONS`

This constant defines the expected format for the agent's thought process and actions when generating SQL queries.

- **Usage**: This format is used to structure the agent's workflow and ensure consistency in the output.
- **Parameters**:
  - `{tool_names}`: Placeholder for the list of tool names the agent can use.

### `SUFFIX_WITH_FEW_SHOT_SAMPLES`

This constant provides a suffix template for the agent to use when few-shot examples are available.

- **Usage**: This suffix is used to initiate the agent's process when similar Question/SQL pairs are to be considered.
- **Parameters**:
  - `{input}`: Placeholder for the input question.
  - `{agent_scratchpad}`: Placeholder for the agent's scratchpad content.

### `SUFFIX_WITHOUT_FEW_SHOT_SAMPLES`

This constant provides a suffix template for the agent to use when few-shot examples are not available.

- **Usage**: This suffix is used to initiate the agent's process when it needs to find relevant tables without the aid of examples.
- **Parameters**:
  - `{input}`: Placeholder for the input question.
  - `{agent_scratchpad}`: Placeholder for the agent's scratchpad content.

### `FINETUNING_SYSTEM_INFORMATION`

This constant provides additional information for the agent, emphasizing its role as an expert in generating SQL queries and the necessity to follow database administrator instructions.

- **Usage**: This information is used during the fine-tuning phase to reinforce the agent's understanding of its role and responsibilities.

### `FINETUNING_AGENT_SUFFIX`

This constant provides a suffix template for the agent to use during the fine-tuning phase.

- **Usage**: This suffix is used to initiate the agent's process during fine-tuning, with a focus on generating SQL queries.
- **Parameters**:
  - `{input}`: Placeholder for the input question.
  - `{agent_scratchpad}`: Placeholder for the agent's scratchpad content.

### `FINETUNING_AGENT_PREFIX`

This constant defines a template for the agent to use during the fine-tuning phase, outlining the agent's role, restrictions, and instructions from the database administrator.

- **Usage**: This prefix is used to guide the agent's behavior during fine-tuning.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.
  - `{admin_instructions}`: Placeholder for the instructions provided by the database administrator.

### `FINETUNING_AGENT_PREFIX_FINETUNING_ONLY`

This constant defines a template similar to `FINETUNING_AGENT_PREFIX` but is specifically tailored for the fine-tuning phase only.

- **Usage**: This prefix is used to guide the agent's behavior during fine-tuning when the focus is solely on generating and executing SQL queries.
- **Parameters**:
  - `{dialect}`: Placeholder for the SQL dialect to be used in the query.
  - `{admin_instructions}`: Placeholder for the instructions provided by the database administrator.

### `ERROR_PARSING_MESSAGE`

This constant provides a message to be used when the agent encounters a parsing error.

- **Usage**: This message is returned by the agent when it fails to parse the input correctly or when it needs to return an error message due to consistent parsing issues.

## Usage in the Project

The constants defined in `agent_prompts.py` are used throughout the project to provide structured guidance and instructions to the agent responsible for generating SQL queries. These templates ensure that the agent's output is consistent, follows the required format, and adheres to any specific instructions or constraints. The agent utilizes these prompts during both the fine-tuning phase and the actual query generation process to interact with the database and tools effectively.
```
