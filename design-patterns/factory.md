# Factory Pattern

## Code Example

```python
class KoreanGetter(object):

    def __init__(self):
        self.trans = dict(dog="댕댕이", cat="고먐미")

    def get(self, text):
        return self.trans.get(text, str(text))


class EnglishGetter(object):

    def get(self, text):
        return str(text)


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Korean=KoreanGetter)
    return languages[language]()


if __name__ == '__main__':
    e, g = get_localizer(language="English"), get_localizer(language="Korean")
    for text in "dog parrot cat bear".split():
        print(e.get(text), g.get(text))

### OUTPUT ###
# dog 댕댕이
# parrot parrot
# cat 고먐미
# bear bear
```

## References

- [python-patterns: factory_method.py](https://github.com/faif/python-patterns/blob/master/creational/delegation_pattern.py)

