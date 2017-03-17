# 클린 코드를 위한 테스트 주도 개발

> 원서 소개 링크 http://www.obeythetestinggoat.com



#### 실행 환경

- macOS 10.12.3
- python 3.5.2
- selenium 3.3.1
- firefox 52.0



### p. 5

#### Problem

첫 번째 테스트부터 책에 나온대로 되지 않는다.

###### 소스코드

```python
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
```

코드를 돌려보니 원하는 에러 메시지가 아니다. 아무래도 `geckodriver`를 가지고 해결해야 하는 듯 하다.


#### How to solve

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

#### How to solve

###### superlists/urls.py

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



### p.63

#### How to solve

csrf_token을 제거하고 비교하도록 한다.

###### lists/test.py

```python
class HomePageTest(TestCase):

    def remove_csrf(self, origin):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', origin)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = self.remove_csrf(render_to_string('home.html'))
        response_decode = self.remove_csrf(response.content.decode())

        self.assertEqual(response_decode, expected_html)

    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'

        response = home_page(request)

        self.assertIn('A new item', response.content.decode())

        expected_html = self.remove_csrf(render_to_string(
            'home.html',
            {'new_item_text': 'A new item'}
        ))
        response_decode = self.remove_csrf(response.content.decode())

        self.assertEqual(response_decode, expected_html)
```



### p.85

#### Problem

페이지 마지막의 기능 테스트를 성공하면 다음과 같은 메시지가 떠야한다.

```bash
Traceback (most recent call last):
  File "functional_test.py", line 77, in test_can_start_a_list_and_retrieve_it_later
    self.fail('Finish the test!')
AssertionError: Finish the test!
```

그러나 다음과 같은 에러 메시지가 떴다.

```bash
selenium.common.exceptions.InvalidSelectorException: Message: Given css selector expression "tr" is invalid: TypeError: can't access dead object
```

#### How to solve

이 문제에 대해서 [stackoverflow](http://stackoverflow.com/a/41206683)에 저자가 답변을 달아놨는데, 책에서는 Selenium2을 사용했는데 Selenium3으로 업데이트 되면서 `implicit wait`을 처리하는 방법이 달라졌기 때문에 에러가 난다고 한다. 다음과 같이 코드를 수정해주자.

###### functional_test.py

```python
...
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

class NewVisitorTest(unittest.TestCase):
    ...
    @contextmanager
    def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name("html")
        yield WebDriverWait(self.browser, timeout).until(
            staleness_of(old_page)
        )
    ...
    def test_can_start_list_and_retrieve_it_later(self):
        ...
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)

        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table("1: Buy peacock feathers")

        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table("1: Buy peacock feathers")
            self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
```



##### Refer to

- [원서 소개 링크](http://www.obeythetestinggoat.com)
- [hyesun03님의 블로그: 클린 코드를 위한 테스트 주도 개발](https://hyesun03.github.io/2016/09/19/djangoTDD01/)