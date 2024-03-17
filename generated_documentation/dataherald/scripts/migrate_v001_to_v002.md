```markdown
# Migration Script: migrate_v001_to_v002.py

## Overview
The `migrate_v001_to_v002.py` script is designed to perform data migration tasks within the DataHerald project. It updates the schema of certain collections, adds new fields to documents, and refreshes vector stores with updated information.

## Dependencies
- `os`: Standard Python module to interact with the operating system.
- `sql_metadata`: Third-party library used to parse SQL queries and extract metadata.
- `dataherald.config`: Module from the DataHerald project containing configuration settings.
- `dataherald.db`: Module from the DataHerald project for database interactions.
- `dataherald.vector_store`: Module from the DataHerald project for managing vector stores.

## Functions

### add_db_connection_id
This function adds a new field `db_connection_id` to documents in a specified collection.

#### Parameters
- `collection_name` (str): The name of the collection to update.
- `storage`: An instance of the `DB` class from `dataherald.db` module, used to interact with the database.

#### Process
1. Retrieves all documents from the specified collection.
2. Iterates over each document (referred to as `collection_row`).
3. Checks if the `db_alias` field exists in the document; if not, continues to the next document.
4. Finds the corresponding database connection document using the `db_alias` value.
5. If a database connection document is found, adds a new field `db_connection_id` to the `collection_row` with the value of the `_id` field from the database connection document.
6. Updates the document in the collection with the new `db_connection_id` field.

## Main Execution Flow

### Configuration and System Initialization
1. Instantiates a `Settings` object from `dataherald.config`.
2. Creates a `System` instance using the settings.
3. Calls the `start` method on the `System` instance to initialize the system.

### Database Instance
1. Retrieves an instance of the `DB` class from the `System` instance, which is used to interact with the database.

### Update Relations
1. Calls the `add_db_connection_id` function for the following collections:
   - `table_schema_detail`
   - `golden_records`
   - `nl_question`

### Refresh Vector Stores
1. Retrieves the name of the golden record collection from the environment variable `GOLDEN_SQL_COLLECTION`, defaulting to `"dataherald-staging"` if not set.
2. Retrieves an instance of the `VectorStore` class from the `System` instance.
3. Attempts to delete the existing collection from the vector store. If an exception occurs, it is silently ignored.

### Upload Golden Records
1. Retrieves all documents from the `golden_records` collection.
2. Iterates over each golden record document.
3. Parses the SQL query from the golden record using `sql_metadata.Parser` to extract the tables involved.
4. If no tables are found, defaults to an empty string.
5. Retrieves the question associated with the golden record.
6. Adds a new record to the vector store with the following information:
   - The question text as documents.
   - The `db_connection_id` from the golden record.
   - The name of the golden record collection.
   - Metadata containing the first table used in the SQL query and the `db_connection_id`.
   - The `_id` of the golden record as an identifier.

### Rename Collections
1. Attempts to rename the following collections:
   - `nl_query_response` to `nl_query_responses`
   - `nl_question` to `nl_questions`
   - `database_connection` to `database_connections`
   - `table_schema_detail` to `table_descriptions`
2. If an exception occurs during the renaming process, it is silently ignored.

## Usage
This script is executed as a standalone Python script, typically during a migration or upgrade process to transition from version 001 to version 002 of the DataHerald project. It is assumed to be run by a system administrator or automated deployment process with the necessary environment variables and permissions set up.
```