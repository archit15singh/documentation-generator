```markdown
# `moderation.py` Module Documentation

## Overview

The `moderation.py` module is part of the `prompttools.utils` package and is responsible for interfacing with OpenAI's moderation API. It provides a function `apply_moderation` that checks if a given text complies with OpenAI's usage policies by using a specified moderation model.

## Functions

### `apply_moderation`

#### Description

The `apply_moderation` function takes a row from a pandas DataFrame and a text column name to perform moderation on the specified text. It can optionally extract and return specific category flags and scores from the moderation response.

#### Parameters

- `row` (`pandas.core.series.Series`): A single row of data from a pandas DataFrame. This row should contain the text to be moderated along with any other relevant information.
- `text_col_name` (`str`): The name of the column within the row that contains the text to be moderated. Defaults to `"response"`.
- `moderation_model` (`str`): The identifier for the OpenAI moderation model to be used. Defaults to `"text-moderation-latest"`.
- `category_names` (`Optional[list[str]]`): A list of category names for which flags should be extracted from the moderation response and added to the result. This parameter is optional.
- `category_score_names` (`Optional[list[str]]`): A list of category names for which scores should be extracted from the moderation response and added to the result. This parameter is optional.

#### Returns

- `Union[bool, dict]`: The function returns a boolean flag indicating whether the text violates any of OpenAI's usage policies if neither `category_names` nor `category_score_names` are provided. If either of these parameters is provided, it returns a dictionary with keys corresponding to the specified categories and their respective flags or scores, as well as a `moderation_flag` key indicating the overall moderation result.

#### Behavior

1. The function extracts the text to be moderated from the specified column in the input row.
2. It calls the `openai.moderations.create` method with the moderation model and the text to be moderated.
3. The moderation response is parsed to determine if the text has been flagged as violating policies.
4. If `category_names` is provided, the function extracts flags for the specified categories from the moderation response and adds them to the result dictionary.
5. If `category_score_names` is provided, the function extracts scores for the specified categories from the moderation response and adds them to the result dictionary.
6. If either `category_names` or `category_score_names` is provided, the result dictionary also includes the overall moderation flag. Otherwise, only the boolean moderation flag is returned.

#### Example Usage

```python
import pandas as pd
from prompttools.utils.moderation import apply_moderation

# Assuming df is a pandas DataFrame with a 'response' column that contains text to be moderated
row = df.iloc[0]  # Get the first row of the DataFrame
moderation_result = apply_moderation(
    row=row,
    text_col_name="response",
    category_names=["harassment", "violence"],
    category_score_names=["harassment", "violence"]
)

# moderation_result will be a dictionary with keys 'harassment', 'violence', 'harassment_score', 'violence_score', and 'moderation_flag'
```

## Dependencies

- `openai`: The OpenAI Python client library used to interact with the OpenAI API.
- `pandas`: A powerful data manipulation library used for handling the input data row.

## License

The source code is licensed under the license found in the LICENSE file in the root directory of this source tree, and the copyright belongs to Hegel AI, Inc.
```
