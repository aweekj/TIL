# Abstract Factory Pattern

## Code Example

```python
class AbstractFactory(object):
    def create_product(self, *args):
        raise NotImplementedError()


class ConcreteFactory(AbstractFactory):
    def create_product(self, *args):
        return Product()


class Product(object):
    @staticmethod
    def do_something():
        print('This is product.')


class Client(object):
    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def get_product(self):
        product = self.factory.create_product()
        product.do_something()

if __name__ == '__main__':
    factory = ConcreteFactory()
    client = Client(factory)
    client.get_product()  # This is product.
```



## Related Patterns

- AbstractFactory는 **Factory** 나 **Prototype** 으로 구현
- ConcreteFactory는 **Singleton** 으로 구현