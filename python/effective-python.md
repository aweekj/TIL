# [파이썬 코딩의 기술](http://www.gilbut.co.kr/book/bookView.aspx?bookcode=BN001430)

## 1장 파이썬 다운 생각

### 10. range 보다는 enumerate를 사용하자

### 12. for와 while 루프 뒤에는 else 블록을 쓰지 말자

루프가 종료되자마자 else 블록이 실행되고, 루프에서 break 문을 사용해야 else 블록을 건너뛸 수 있다. 이는 직관적이지 않아서 혼동하기 쉬우므로 사용하지 말 것. 대신 헬퍼 함수를 사용하자.

## 2장 함수

## 3장 클래스와 상속

## 4장 메타클래스와 속성

## 5장 병행성과 병렬성

## 6장 내장 모듈

### 45. 지역 시간은 time이 아닌 datetime으로 표현하자

- time 모듈은 UTC를 호스트 컴퓨터의 Local Time으로 변환할 때만 유용하다. 
- datetime 모듈은 어떤 Local Time을 다른 Local Time으로 변환할 때 유용하다. datetime 모듈을 사용할 때는 [pytz](https://pypi.python.org/pypi/pytz/)를 함께 사용하자.
- pytz를 사용할 때는, Local Time을 UTC로 먼저 변경하여 datetime 연산을 수행한 다음, 시간을 표시하기 전에 마지막 단계로 UTC를 Local Time으로 변환할 것.

### 46. 내장 알고리즘과 자료 구조를 사용하자

**[더블 엔디드 큐(deque)](https://docs.python.org/3/library/collections.html?highlight=defaultdict#deque-objects)**

**[정렬된 딕셔너리(OrderedDict)](https://docs.python.org/3/library/collections.html?highlight=ordereddict#ordereddict-objects)**

**[기본 딕셔너리(defaultdict)](https://docs.python.org/3/library/collections.html?highlight=defaultdict#collections.defaultdict)**

**[힙 큐(heapq)](https://docs.python.org/3/library/heapq.html?highlight=heapq#module-heapq)**

**[바이섹션(bisect)](https://docs.python.org/3/library/collections.html?highlight=defaultdict#defaultdict-objects)**

**[이터레이터 도구(itertools)](https://docs.python.org/3/library/itertools.html?highlight=itertools#module-itertools)**

### 47. 정밀도가 중요할 때에는 decimal을 사용하자

Decimal 클래스는
- 화폐 연산처럼 정밀도가 높고 정확한 반올림이 필요한 상황에 안성맞춤.
- 기본적으로 소수점이 28자리인 고정 소수점 연산을 제공, 필요하면 자릿수를 더 늘릴 수 있음.
- IEEE 754 부동 소수점 수의 정확도 문제를 피해갈 수 있음.
- 반올림 연산을 더 세밀하게 제어할 수 있음.

## 7장 협력

## 8장 제품화


---
## 참고 링크
- [예제소스](https://github.com/gilbutITbook/006764)
