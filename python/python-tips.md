# Python Tips


## 1. Encoding Error

### Problem

```bash
Traceback (most recent call last):
  File "build.py", line 63, in <module>
    readme.write(header)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 26-27: ordinal not in range(128)
```

### Solved

Use [`io.open()`](https://docs.python.org/2/library/io.html#io.open) to create a file object that'll encode for you as you write to the file:

```python
import io

f = io.open(filename, 'w', encoding='utf8')
```

## 2. [`@python_2_unicode_compatible`](https://docs.djangoproject.com/en/1.8/ref/utils/#django.utils.encoding.python_2_unicode_compatible)

To support Python 2 and 3 with a single code base, define a `__str__` method returning text and apply this decorator to the class.

