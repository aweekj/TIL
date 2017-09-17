# Decorator Pattern

## When to use?

- 다른 객체에 영향을 주지 않고 각각의 객체에 새로운 기능을 추가할 때. 필요한 비용만 그때그때 지불하는 방식
- 상속으로 서브클래스를 계속 만드는 것이 복잡해질때. 설계의 융통성을 증대시킬 수 있음

## Code Example

###### Example 1

```python
class TextTag(object):
    """Represents a base text tag"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())

if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())  # before: hello, world!
    print("after:", special_hello.render())  # after: <i><b>hello, world!</b></i>
```

###### Example 2

```python
from functools import wraps


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags('div')
@tags('p')
def get_text(name):
    return "Hello {0}!".format(name)

print(get_text("world"))  # <div><p>Hello world!</p></div>
print(get_text.__name__)  # get_text
print(get_text.__doc__)  # None
print(get_text.__module__)  # __main__

```

## References

- [python-patterns: decorator.py](https://github.com/faif/python-patterns/blob/master/fundamental/decorator.py)
- [A guide to Python's function decorators](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/)

