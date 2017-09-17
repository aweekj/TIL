# Adapter Pattern

## What is this?

- 어댑터 패턴은 클래스마다 다른 인터페이스를 제공할 때 사용한다. 실제로 사용되는 케이블 어댑터가 각각의 휴대폰을 충전하는 것을 생각해보면 이해하기 쉽다. 서로 맞지 않는 인터페이스 때문에 통합 하기 힘든 클래스를 통합해야 할 때 어댑터 패턴을 적용할 수 있다.

## Code Example

```python
class Dog(object):

    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):

    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):

    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):

    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__


def main():
    objects = []
    dog = Dog()
    print(dog.__dict__)
    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__)
    print(objects[0].original_dict())
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))


if __name__ == "__main__":
    main()
```

## References

- [python-patterns: adapter](https://github.com/faif/python-patterns/blob/master/structural/adapter.py)

