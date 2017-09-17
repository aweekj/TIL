# Delegation Pattern

## What is this?

> **"Delegation is like inheritance done manually through object composition."** *[Lecture slides of course 601: "Object-Oriented Software Development" at the University of San Francisco ]*
>
> 위임(delegation)은 객체 구성을 일일이 하는 상속(inheritance)과도 같다.

- 어떤 객체(the *delegator*: 위탁자)의 일부 기능을 다른 객체(the *delegate*: 수탁자)에게 넘김

## When to use?

- 클래스의 메소드 결합을 줄여야 할 때 >> 한 클래스의 변경이 다른 클래스에 미치는 영향이 적어짐
- 같은 동작을 하는 컴포턴트들이 있는데, 이들이 나중에 각자 다른 동작을 하도록 변경되어야 하는 상황이 생길때
- Generally spoken: 상속(ingeritance) 대신 위임(delegation)을 사용. 상속은 부모 객체와 자식 객체의 관계가 너무 가까운데 위임은 상속 보다는 flexible 함

## Code Example

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference: https://en.wikipedia.org/wiki/Delegation_pattern
Author: https://github.com/IuryAlves
"""


class Delegator(object):
    """
    >>> delegator = Delegator(Delegate())
    >>> delegator.do_something("nothing")
    'Doing nothing'
    >>> delegator.do_anything()
    """

    def __init__(self, delegate):
        self.delegate = delegate

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            if hasattr(self.delegate, name):
                attr = getattr(self.delegate, name)
                if callable(attr):
                    return attr(*args, **kwargs)
        return wrapper


class Delegate(object):

    def do_something(self, something):
        return "Doing %s" % something


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

## Related Patterns

- Decorator Pattern: Delegation Pattern은 Decorator Pattern의 하위 분류로서 '확장 기능 제공'을 위한 패턴 중 하나
- Delegation은 상당히 자주 사용되는데, Visitor, Observer, Stratege, Event Listener 패턴에서도 쓰임

## References

- [Wikipedia](https://en.wikipedia.org/wiki/Delegation_pattern)
- [best-practice-software-engineering.ifs.tuwien.ac.at](http://best-practice-software-engineering.ifs.tuwien.ac.at/patterns/delegation.html)
- [python-patterns: delegation_pattern.py](https://github.com/faif/python-patterns/blob/master/fundamental/delegation_pattern.py)
