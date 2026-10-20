# Saving a product with no tags crashes

If I leave the "Tags" field blank on the product form, saving fails with a
500. The form sends `null` for the field when it's empty. The docs for
`parse_tags` say an empty or missing field should just give no tags.

Traceback:

```
Traceback (most recent call last):
  ...
  File "tagparser.py", line 10, in parse_tags
    for part in raw.split(","):
                ^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'split'
```

Repro:

```python
from tagparser import parse_tags
parse_tags(None)
```

Typing a tag works fine. It only happens when the field is left empty.
