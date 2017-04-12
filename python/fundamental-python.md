# Python References

## 2. Built-in Functions

##### [`print`](https://docs.python.org/3.6/library/functions.html?highlight=print#print)(**objects*, *sep=' '*, *end='\n'*, *file=sys.stdout*, *flush=False*)x

```python
>>> for x in range(1, 5):
...     print(x, end='')
12345
```



## 4. Built-in Types

### 4.6. Sequence Types — [`list`](https://docs.python.org/3/library/stdtypes.html?highlight=list#list), [`tuple`](https://docs.python.org/3/library/stdtypes.html?highlight=list#tuple), [`range`](https://docs.python.org/3/library/stdtypes.html?highlight=list#range)

#### 4.6.1. Common Sequence Operations

##### s[i:j:k] 

slice of *s* from *i* to *j* with step *k*



### 4.7. Text Sequence Type — [`str`](https://docs.python.org/3.6/library/stdtypes.html#str)

#### 4.7.1. String Methods

##### [`str.center`](https://docs.python.org/3.6/library/stdtypes.html?highlight=dict#str.center)

> 문자열을 주어진 길이 안에서 가운데 정렬

```python
>>> print("center".center(16))
     center     
>>> print("center".center(16, '-'))
-----center-----
```

##### [`str.ljust`](https://docs.python.org/3.6/library/stdtypes.html?highlight=dict#str.ljust)

> 문자열을 주어진 길이 안에서 왼쪽 정렬

```python
>>> print("left".ljust(16))
left            
>>> print("left".ljust(16, '-'))
left------------
```

##### [`str.rjust`](https://docs.python.org/3.6/library/stdtypes.html?highlight=dict#str.rjust)

> 문자열을 주어진 길이 안에서 오른쪽 정렬

```python
>>> print("right".rjust(16))
           right
>>> print("right".rjust(16, '-'))
-----------right
```

##### [`str.join`](https://docs.python.org/3.6/library/stdtypes.html#str.join)

> 리스트를 문자열로 변환

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

##### [`str.split`](https://docs.python.org/3.6/library/stdtypes.html#str.split)

> 문자열을 리스트로 변환

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



### 4.10. Mapping Types — [`dict`](https://docs.python.org/3.6/library/stdtypes.html?highlight=dict#dict)

#### `d[key]` vs `get(key[, default])`

>  딕셔너리에서 키 값에 해당하는 값을 가지고 올 때 두 방법의 차이점

`d[key]` Return the item of d with key *key*. **Raises a KeyError** if *key* is not in the map. 

`get(key[, default])` Return the value for *key* if *key* is in the dictionary, else *default*. If *default* is not given, it defaults to `None`, so that this method **never raises a KeyError**.



## 6. Expressions

### 6.3. Primaries

#### 6.3.4 [Calls](https://docs.python.org/3/reference/expressions.html#calls)

`function(*[arg1, arg2, arg3])` is same as `function(arg1, arg2, arg3)`

```python
>>> arr = [2, 3, 4, 1]
>>> print(*(int(x) for x in arr[::-1]))
1 4 3 2
```



## 19. Internet Data Handling

### 19.2. [`json`](https://docs.python.org/3/library/json.html?highlight=json#module-json) - JSON encoder and decoder

#### 19.2.1. Basic Usage

##### [`json.dumps`](https://docs.python.org/3/library/json.html?highlight=json#json.dumps)

> Python Object (Dictionary, List, Tuple 등) 를 JSON 형식으로 인코딩

- `ensure_ascii=False` - 한글 인코딩 문제 해결
- `indent=4` - indent 설정
- `sort_keys=True` - key 값을 알파벳 순으로 정렬

```python
>>> import json
>>> customer = {'id': 346725, 'name': 'Jamie', 'history': [{'date': '2017-02-19', 'item': 'coffee'}, {'date': '2017-02-20', 'item': 'tea'}]}
>>> print(json.dumps(customer))
{"name": "Jamie", "id": 346725, "history": [{"item": "coffee", "date": "2017-02-19"}, {"item": "tea", "date": "2017-02-20"}]}
>>> print(json.dumps(customer, ensure_ascii=False, indent=4, sort_keys=True))
{
    "history": [
        {
            "date": "2017-02-19",
            "item": "coffee"
        },
        {
            "date": "2017-02-20",
            "item": "tea"
        }
    ],
    "id": 346725,
    "name": "Jamie"
}
```

##### [`json.dump`](https://docs.python.org/3/library/json.html?highlight=json#json.dump)

> Python Object (Dictionary, List, Tuple 등) 를 JSON 형식으로 인코딩 후 파일 저장

```python
>>> with open("file.json", 'w') as f:
...     json.dump(customer, f, indent=4)
```

##### [`json.load`](https://docs.python.org/3/library/json.html?highlight=json#json.load)

> JSON 파일을 Python Object로 디코딩

```python
>>> with open("file.json") as f:
...     data = json.load(f)
>>> data
{'name': 'Jamie', 'id': 346725, 'history': [{'item': 'coffee', 'date': '2017-02-19'}, {'item': 'tea', 'date': '2017-02-20'}]}
```



## 21. Internet Protocols and Support

### 21.22. [http.server](https://docs.python.org/3.6/library/http.server.html?highlight=http.server#module-http.server)

#### [`http.server.SimpleHTTPRequestHandler`](https://docs.python.org/3.6/library/http.server.html?highlight=http.server#http.server.SimpleHTTPRequestHandler)

> 원하는 경로에서 이 명령어를 실행시키면 웹서버로 제공된다.

```bash
$ python3 -m http.server 8000
```

