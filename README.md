# pyflame-context

pyflame-context.

Profile code with pyflame directly from code as a context manager.

Example:

```python
with pyflame("profile.svg", duration=360):
    for n in range(10000):
        # expensive loop body
```

