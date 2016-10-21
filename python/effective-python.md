# [파이썬 코딩의 기술](http://www.gilbut.co.kr/book/bookView.aspx?bookcode=BN001430)

## 1장 파이썬 다운 생각

### 10. range 보다는 enumerate를 사용하자

**Code**

```python
for i, flaver in enumerate(flavor_list):
    print('%d: %s' % (i+1, flavor))
```

또는

```python
for i, flaver in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
```

**Result**
```bash
>>>
1: vanilla
2: chocolate
3: pecan
4: strawberry
```

### 12. for와 while 루프 뒤에는 else 블록을 쓰지 말자

루프가 종료되자마자 else 블록이 실행되고, 루프에서 break 문을 사용해야 else 블록을 건너뛸 수 있다. 이는 직관적이지 않아서 혼동하기 쉬우므로 사용하지 말 것. 대신 헬퍼 함수를 사용하자.

**Code**
*Don't*

```python
a = 4
b = 9
for i in range(2, min(a, b))+1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
    print('Not coprime')
    break
else:
    print('Coprime')
```

**Code**
*Do*

```python
def coprime(a,b):
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            return False
    return True

# or

def coprime(a, b):
    is_coprime = True
    for i in range(2, min(a, b)+1)"
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime
```

**Result**

```
>>>
Testing 2
Testing 3
Testing 4
Coprime
```