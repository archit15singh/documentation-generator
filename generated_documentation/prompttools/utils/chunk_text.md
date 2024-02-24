```markdown
# `chunk_text.py` Module

## Overview

The `chunk_text.py` module contains a single function `chunk_text` which is designed to split a given string of text into smaller chunks. These chunks are constrained by a specified maximum length, ensuring that no individual chunk exceeds this length. The function is careful to avoid breaking words across chunks, preserving whole words within the boundaries of each chunk.

## Function: `chunk_text`

### Description

The `chunk_text` function takes a string of text and divides it into a list of smaller strings, or "chunks", based on a specified maximum length for each chunk. The function ensures that words are not split across chunks by only breaking the text at spaces.

### Usage

The function is used when there is a need to process or display long strings of text in smaller, more manageable parts. This can be particularly useful in scenarios where there are constraints on the amount of text that can be processed or displayed at once, such as in user interfaces, text processing pipelines, or when interfacing with APIs that have a limit on the size of text input.

### Arguments

- `text` (`str`): The source text that needs to be chunked. This argument takes a string that represents a paragraph or any long form of text.
- `max_chunk_length` (`int`): The maximum allowed length for each chunk. This integer value determines the upper limit on the size of each chunk of text.

### Returns

- `list[str]`: A list of strings, where each string is a chunk of the original text. Each chunk is guaranteed to be less than or equal to the specified `max_chunk_length`, and words are not split across chunks.

### Algorithm

1. The input text is split into words based on spaces using the `split()` method.
2. An empty list called `chunks` is initialized to store the resulting chunks of text.
3. A temporary string `current_chunk` is used to build each chunk.
4. The function iterates over each word in the split text:
   - If adding the next word to `current_chunk` (including a space if `current_chunk` is not empty) does not exceed `max_chunk_length`, the word is appended to `current_chunk`.
   - If adding the next word would exceed `max_chunk_length`, the current `current_chunk` is added to the `chunks` list, and `current_chunk` is reset to the current word.
5. After the loop, if `current_chunk` contains any text, it is appended to the `chunks` list to ensure the last chunk is not lost.
6. The `chunks` list is returned.

### Example

```python
text_to_chunk = "This is an example of a long text that needs to be chunked into smaller parts."
max_length = 20
chunks = chunk_text(text_to_chunk, max_length)
print(chunks)
# Output: ['This is an example', 'of a long text that', 'needs to be chunked', 'into smaller parts.']
```

### Notes

- The function assumes that the input text does not contain words longer than `max_chunk_length`. If such a word exists, it will be placed in its own chunk, potentially exceeding the maximum length.
- The function does not account for punctuation or special characters when determining word boundaries; it simply uses spaces to identify words.
- The function is designed to be used with text data and may not be suitable for binary or non-text content.
```