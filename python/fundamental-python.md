## Fundamental Python

### String

#### [`str.join`](https://docs.python.org/3.6/library/stdtypes.html#str.join)

```python
>>> list = ["a", "b", "c", "3", "4", "5"]
>>> print("".join(list))
abc345
>>> print("\n".join(list))
a
b
c
3
4
5
```

#### [`str.split`](https://docs.python.org/3.6/library/stdtypes.html#str.split)

```python
>>> s = '1,2,3'
>>> s.split(',')
['1', '2', '3']
>>> s.split(',', maxsplit=1)
['1', '2,3']

>>> s = '1,2,,3'
>>> s.split(',')
['1', '2', '', '3']
```

