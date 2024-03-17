```markdown
# Migration Script: migrate_v006_to_v100.py

## Overview
The `migrate_v006_to_v100.py` script is designed to perform data migration from version 0.0.6 to version 1.0.0 of the DataHerald application. It updates the database schema, migrates data to new collections, and ensures compatibility with the new version.

## Dependencies
- `os`: Provides a way to use operating system dependent functionality.
- `datetime.timedelta`: Used for date and time manipulation.
- `bson.objectid.ObjectId`: Represents BSON Object IDs.
- `pymongo`: Python driver for MongoDB.
- `pymongo.ASCENDING`: Sort order specifier for MongoDB queries.
- `pymongo.errors.DuplicateKeyError`: Exception for handling duplicate key errors in MongoDB operations.
- `dataherald.config`: Module containing application configuration settings.
- `dataherald.config.System`: Class representing the system configuration.
- `dataherald.db.DB`: Class for database operations.
- `dataherald.db_scanner.models.types.TableDescriptionStatus`: Enum for table description status.
- `dataherald.types.GoldenSQL`: Class representing a golden SQL record.
- `dataherald.vector_store.VectorStore`: Class for vector store operations.

## Functions

### update_object_id_fields
Converts `ObjectId` fields to string representation in the specified collection.

#### Parameters
- `field_name: str`: The name of the field to update.
- `collection_name: str`: The name of the collection where the field is located.

#### Process
1. Iterates over all documents in the specified collection.
2. Checks if the field exists, is not empty, and is an instance of `ObjectId`.
3. Converts the `ObjectId` to a string and updates the document in the collection.

## Main Execution

### Initialization
1. Loads settings from `dataherald.config.Settings`.
2. Initializes the `System` with the loaded settings and starts it.
3. Creates an instance of `DB` for database operations.
4. Retrieves the name of the golden SQL collection from the environment variable `GOLDEN_RECORD_COLLECTION` or defaults to "dataherald-staging".
5. Creates an instance of `VectorStore` for vector store operations.

### Golden SQL Records Migration
1. Finds all documents in the "golden_records" collection.
2. For each golden record, attempts to insert a new document into the "golden_sqls" collection with the necessary fields.
3. Ignores documents that cause a `DuplicateKeyError`.

### Data Type Conversion
1. Calls `update_object_id_fields` for various fields across multiple collections to convert `ObjectId` fields to strings.

### Vector Store Operations
1. Attempts to delete the existing vector store collection.
2. Finds all documents in the "golden_sqls" collection.
3. Converts each document to a `GoldenSQL` object and appends it to a list.
4. Adds the list of `GoldenSQL` objects to the vector store.

### Table Descriptions Status Update
1. Finds all documents in the "table_descriptions" collection.
2. Updates the status field based on the current status, changing "SYNCHRONIZED" to `TableDescriptionStatus.SCANNED` and "NOT_SYNCHRONIZED" to `TableDescriptionStatus.NOT_SCANNED`.
3. Updates or creates the document in the "table_descriptions" collection.

### Prompts and Responses Migration
1. Finds all documents in the "questions" collection.
2. For each question, finds associated responses and attempts to insert a new document into the "prompts" collection.
3. Ignores documents that cause a `DuplicateKeyError`.
4. For each response, attempts to create documents in the "sql_generations" and "nl_generations" collections with the necessary fields.
5. Ignores documents that cause a `DuplicateKeyError`.

## Notes
- The script uses exception handling to ignore `DuplicateKeyError` exceptions, allowing the migration to continue even if some records already exist in the target collections.
- The script prints status messages to the console to indicate the progress of the migration.
- The script uses environment variables to allow configuration of collection names.
- The script assumes that the MongoDB connection and authentication are handled by the `DB` class instance.
- The script does not provide rollback functionality in case of failure, so it is assumed that the migration is run in a controlled environment where backups are available if needed.
```