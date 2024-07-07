# Model Registry

Storing intermediate result in here only. For long term, it should be stored in
model repository separately.

Besides binary model, you should also store model metadata such as date, size of
training data.

This folder path for these directories is loaded as an environment variable by
the `.envrc` file; to load them in Python, use the following code:

```python
import os

# Load environment variables for the `models` folder
DIR_MODELS = os.getenv("DIR_MODELS")
```
