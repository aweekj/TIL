# 클린 코드를 위한 테스트 주도 개발

> 원서 소개 링크 http://www.obeythetestinggoat.com

### p. 5

첫 번째 테스트부터 책에 나온대로 되지 않는다.

###### 소스코드

```python
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
```

코드를 돌려보니 원하는 에러 메시지가 아니다. 아무래도 `geckodriver`를 가지고 해결해야 하는 듯 하다.



#### 실행 환경

- macOS 10.12.3
- python 3.5.2
- selenium 3.3.1
- firefox 52.0



#### 해결방법

먼저 [geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.15.0)를 설치하고 적당한 위치에 넣어주자. 나는 최신 릴리즈 버전인 0.15.0을 설치했다. 그리고 아래 사항들을 진행한다.

```bash
# 파일을 열어 다음을 추가한다. 폴더의 경로는 자신의 것에 맞게 수정한다.
$ vim ~/.bash_profile
export PATH=$PATH:/YOUR/DIRECTORY/PATH/geckodriver-v0.15.0-macos

# 변경사항을 쉘에 적용한다.
$ source ~/.bash_profile

# 변경이 잘 되었는지 확인한다.
$ geckodriver --version
geckodriver 0.15.0

The source code of this program is available at
https://github.com/mozilla/geckodriver.

This program is subject to the terms of the Mozilla Public License 2.0.
You can obtain a copy of the license at https://mozilla.org/MPL/2.0/.
```



이번에는 `http://localhost:8000` 를 접속하는 데서 에러가 난다. 이를 무시하고 책을 계속 따라가다보면, Django 테스트에서 이 코드가 사용되기 때문에 그다지 문제가 없다. 그러나 만약 `geckodriver` 문제가 잘 해결되었는지 확인하고 싶다면, `http://localhost:8000` 대신 `http://www.google.com`와 같은 실재하는 주소를 넣어보자. 그러면 원하는 `AssertionError` 를 얻을 수 있을 것이다.

```bash
$ python functional_test.py
Traceback (most recent call last):
  File "functional_test.py", line 6, in <module>
    assert 'Django' in browser.title
AssertionError
```



### p.33

###### 소스코드

```python
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home')
]
```

###### 결과

```
TypeError: view must be a callable or a list/tuple in the case of include().
```



