# Python Object Inspection Cheat Sheet

## Discovering Attributes & Methods

### List all attributes (public and private)

```python
dir(obj)
```

### Filter the list

```python
# Only public attributes (no underscores)
[attr for attr in dir(obj) if not attr.startswith('_')]

# Only methods (callable)
[attr for attr in dir(obj) if callable(getattr(obj, attr))]

# Only properties (not callable)
[attr for attr in dir(obj) if not callable(getattr(obj, attr))]
```

### Get more detailed information

```python
import inspect

inspect.getmembers(obj)           # returns (name, value) tuples
inspect.signature(obj.method)     # shows method parameters
help(obj.attribute)                # shows docstring
```

### Instance attributes only

```python
vars(obj)      # or obj.__dict__
```

## Finding Undocumented Features

1. Use `dir(object)` to list ALL attributes
2. Read library source code on GitHub
3. Search Stack Overflow for testing examples
4. Check library's own test files
5. Private attributes start with `_` (not in official docs)
