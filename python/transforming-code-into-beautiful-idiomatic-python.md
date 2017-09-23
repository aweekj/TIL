# Transforming Code into Beautiful, Idiomatic Python

-   Speaker: Raymond Hettinger(@raymondh), who is Python core developer
-   Lecture on Youtube: [Transforming Code into Beautiful, Idiomatic Python](https://www.youtube.com/watch?v=OSGv2VnC0go&t=503s)



## When you see this, do that instead!

-   Replace traditional index manipulation with Python's core looping idioms
-   Learn advanced techniques with for-else clauses and the two argument form of iter()
-   Improve your craftmanship and aim for clean, fast, idiomatic Python code

### Looping over a range of numbers

```python
for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)
  
# Pythonic-way
for i in range(6):
    print(i**2)
```


### Looping over a collection

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(colors[i])
  
# Pythonic-way
for color in colors:
    print(color)
```

### Looping backwards

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1, -1, -1):
    print(colors[i])
  
# Pythonic-way
for color in reversed(colors):
    print(color)
```

### Looping over a collection and indicies

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(i, '-->', colors[i])
  
# Pythonic-way
for i, color in enumerate(colors):
    print(i, '-->', colors)
```

### Looping over two collections

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])
  
# Pythonic-way
for name, color in zip(names, colors):
    print(name, '-->', color)
```

### Looping in sorted order

```python
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
    print(color)
  
for color in sorted(colors, reverse=True):
    print(color)
```

### Custom sort order

```python
colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

# in python2
print sorted(colors, cmp=compare_length)

# Pythonic-way
print(sorted(colors, key=len))
```

### Call a function until a sentinel value

```python
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

# Pythonic-way
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
```

### Distinguishing multiple exit points in loops

```python
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i

# Pythonic-way
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i
```

## Dictionary Skills

- Mastering dictionaries is a fundamental Python skill
- They are fundament tool for expressing relationships, linking, counting and grouping

### Looping over dictionary keys

```python
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d:
    print(k)

for k in d.keys():
    if k.startswith('r'):
        del d[k]
```

### Looping over a dictionary keys and values

```python
for k in d:
    print(k, '-->', d[k])
  
for k, v in d.items():
    print(k, '-->', v)
```

### Construct a dictionary in pairs

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))  # {'raymond': 'red', 'rachel': 'green', 'matthew': 'blue'}
d = dict(enumerate(names))  # {0: 'raymond', 1: 'rachel', 2: 'matthew'}
```

### Counting with dictionaries

```python
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
# {'blue': 1, 'green': 2, 'red': 3}

# Pythonic-way
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
    
# Pythonic and modern way
from collections import defaultdict

d = defaultdict(int)
for color in colors:
    d[color] += 1
```

### Grouping with dictionaries

```python
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
# {7: ['raymond', 'matthew', 'melissa', 'charlie'], 6: ['rachel', 'judith'], 5: ['roger', 'betty']}

# Pythonic-way
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
    
# Pythonic and modern way
from collections import defaultdict

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
```

### Is a dictionary popitem() atomic?

```python
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
    key, value = d.popitem()
    print(key, '-->', value)
```

### Linking dictionaries

```python
import argparse
import os

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

# Pythonic-way
from collections import ChainMap

d = ChainMap(command_line_args, os.environ, defaults)
```

## Improving Clarity

-   Positional arguments and indicies are nice
-   Keywords and names are better
-   The first way is convenient for the computer
-   The second corresponds to how human's think

### Clarify function calls with keyword arguments

>   *Microseconds of computer time is hours of programmer time.*

```python
twitter_search('@obama', False, 20, True)
twitter_search('@obama', retweets=False, numtweets=20, popular=True)
```

### Clarify multiple return values with named tuples

```python
doctest.testmod()  # (0, 4)
doctest.testmod()  # TestResults(failed=0, attempted=4)
TestResults = namedtuple('TestResults', ['failed', ['attempted']])
```

### Unpacking sequences

```python
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

# Pythonic-way
fname, lname, age, email = p
```

### Updating multiple state variables

```python
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t

# Pythonic-way
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x+y
```

## Tuple packing and unpacking

-   Don't under-estimate the advantages of updating state variables at the same time
-   It eliminates an entire class of errors due to out-of-order updates
-   It allows high level thinking: "chunking"

### Simultaneous state updates

```python
tmp_x = x + dx*t
tmp_y = y + dy+t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy

# Pythonic-way
x, y, dx, dy = (x + dx*t, 
                y + dy*t, 
                influence(m, x, y, dx, dy, partial='x'), 
                influence(m, x, y, dx, dy, partial='y'))           
```

## Efficiency

-   An optimization fundamental rule
-   Don't cause data to move around unnecessarily
-   It takes only a little care to avoid O(n**2) behavior instead of linear behavior

### Concatenating strings

```python
names = ['raymond', 'rachel', 'matthew', 'roger', 
         'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
    s += ', ' + name
print(s)  # raymond, rachel, matthew, roger, betty, melissa, judith, charlie

# Pythonic-way
print(', '.join(names))  # raymond, rachel, matthew, roger, betty, melissa, judith, charlie
```

### Updating sequences

```python
names = ['raymond', 'rachel', 'matthew', 'roger', 
         'betty', 'melissa', 'judith', 'charlie']

del names[0]
names.pop(0)
names.insert(0, 'mark')

# Pythonic-way
from collections import deque

names = deque(['raymond', 'rachel', 'matthew', 'roger', 
         'betty', 'melissa', 'judith', 'charlie'])
del names[0]
names.popleft()
names.appendleft('mark')
```

## Decorators and Context Managers

-   Helps separate business logic from administrative logic
-   Clean, beautiful tools for factoring code and improving code reuse
-   Good naming is essential
-   Remember the Spiderman rule: With great power, comes great responsibility!

### Using decorators to factor-out administrative logic

```python
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# Pythonic-way
# Caching decorator
def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
```

### Factor-out temporary contexts

```python
old_context = getcontext().copy()
getcontext().prec = 50
print(Decimal(355)/Decimal(113))
setcontext(old_context)

# Pythonic-way
with localcontext(Context(prec=50)):
    print(Decimal(355)/Decimal(113))
```

### How to open and close files

```python
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()
    
# Pythonic-way
with open('data.txt') as f:
    data = f.read()
```

### How to use locks

```python
# Make a lock
lock = threading.Lock()

# Old-way to use a lock
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()
    
# New-way to use a lock(# Pythonic-way)
with lock:
    print('Critical section 1')
    print('Critical section 2') 
```

### Factor-out temporary contexts

```python
try:
    os.remove('somefile.tmp')
except OSError:
    pass

# Pythonic-way
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

with ignored(OSError):
    os.remove('somefile.tmp')
```

```python
with open('help.txt', 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout

# Pythonic-way
@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fieldobj
    finally:
        sys.stdout = oldstdout

with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
    
```

## Concise Expressive One-Liners

-   Two conficting rules:
    -   Don't put too much on one line
    -   Don't break atoms of thought into subatomic particles
-   Raymond's rule:
    -   One logical line of code equals one sentence in English

### List Comprehensions and Generator Exprssions

```python
result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print(sum(result))

# Pythonic-way
result = sum(i**2 for i in range(10))
```

