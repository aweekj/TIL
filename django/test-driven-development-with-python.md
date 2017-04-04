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

##### 1. on Mac OS

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



#### 2. on Ubuntu

```bash
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz # install
$ tar -xvzf geckodriver-v0.15.0-linux64.tar.gz geckodriver # unpack
$ rm geckodriver-v0.15.0-linux64.tar.gz # delete tar file
$ chmod +x geckodriver
$ export PATH=$PATH:/YOUR/DIRECTORY/PATH/geckodriver
```





### p.33

#### Problem

`python manage.py runserver`를 실행하면 다음과 같은 에러메시지가 나온다.

```bash
Error: view must be a callable or a list/tuple in the case of include().
```

#### How to solve

###### superlists/urls.py

```python
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home')
]
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



### p.95

#### YAGNI

> 설계에 대해 한번 생각하기 시작하면 생각을 멈추는 것이 쉽지 않다. 여러 가지 생각이 떠오르기 시작한다. [중략] 하지만 애자일 복음인 **YAGNI**에 순종해야 한다(야그니라 읽는다). "You ain't gonna need it."(그것을 사용할 일이 없을 것이다)의 약자다. 소프트웨어 개발자로서 우리는 무언가 만드는 것을 즐긴다. 또한 아이디어가 생각나서 그것을 직접 구축해보고 싶어서 안달이 나는 경우도 있을 것이다. 하지만 아이디어가 정말 끝내주더라도 대개는 그걸 사용하지 않고 끝나는 경우가 많다 오히려 사용하지 않는 코드로 가득 차서 애플리케이션이 복잡해지기도 한다. YAGNI는 창의적이지만 과도한 열정을 억제해주는 경전이라고 할 수 있다.



### p.101

#### Problem

p.97에서 다음과 같이 기능 테스트를 수정했다. `self.wait_for_page_load` 부분은 이 포스트의 윗부분(p.85)에 수정했던 부분이다.

###### functional_tests/tests.py

```python
# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
inputbox.send_keys(Keys.ENTER)
edith_list_url = self.browser.current_url
self.assertRegex(edith_list_url, '/lists/.+')
with self.wait_for_page_load(timeout=10):
    self.check_for_row_in_list_table("1: Buy peacock feathers")
```

p.100에서 home_page 뷰를 수정했는데도, 기능 테스트를 실행하면 이전에 나왔던 에러 메시지가 똑같이 나온다.

```bash
self.assertRegex(edith_list_url, '/lists/.+')
AssertionError: Regex didn't match: '/lists/.+' not found in 'http://localhost:8081/'
```

#### How to solve

###### functional_tests/tests.py

```python
# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
inputbox.send_keys(Keys.ENTER)
with self.wait_for_page_load(timeout=10):
    self.check_for_row_in_list_table("1: Buy peacock feathers")
edith_list_url = self.browser.current_url
self.assertRegex(edith_list_url, '/lists/.+')
```

기존의 코드에서 순서를 조금 바꿨는데, 엔터를 입력받은 후에 암묵적인 대기 시간(implicit wait)을 주도록 수정했다. 이제 다시 기능 테스트를 실행하면 원하는 메시지를 얻을 수 있다.

```bash
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="id_list_table"]
```



### p.103

#### How to solve

```python
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(
        r'^lists/the-only-list-in-the-world/$',
        views.view_list,
        name='view_list')
]
```



### p.104

#### Problem

책에서는 다음과 같은 에러가 나길 원한다.

```
AssertionError: '2: Use peacock feathers to make a fly' not found in ['1: Buy peacock feathers']
```

그런데 다음과 같은 에러가 나는 것은 implicit wait를 설정해주었기 때문이고, 자세히 살펴보면 같은 곳에서 에러가 나는 것이므로 문제될 것이 없다.

```bash
	raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:
```



### p.107

원하지 않는 에러가 나타났다. 기능 테스트 과정에서 브라우저를 껐다가 다시 켰는데도 이전의 쿠키가 남아있는 모양이다.

```bash
	self.assertIn(row_text, [row.text for row in rows])
AssertionError: '1: Buy milk' not found in ['1: Buy peacock feathers', '2: Use peacock feathers to make a fly', '3: Buy milk']
```





### p.171

#### Problem

```bash
AttributeError: type object 'NewVisitorTest' has no attribute 'server_thread'
```

#### How to Solve

tearDownClass가 다음과 같은 에러를 만들어내서 주석처리 해주었다.

```python
class NewVisitorTest(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    # @classmethod
    # def tearDownClass(cls):
    #     if cls.server_url == cls.live_server_url:
    #         super().tearDownClass()
```



### p.177

이제 Ubuntu에서 upstart 를 사용하지 않는다고 한다.[^4] 대신 service 를 사용했다.

###### nginx.conf

```bash
server {
    listen 80;
    server_name tdd.aweek-jo.com;

    location /static {
        alias /home/modo/projects/tdd.aweek-jo.com/static;
    }

    location / {
        proxy_set_header Host $host;
        proxy_pass http://unix:/home/modo/projects/tdd.aweek-jo.com/gunicorn.sock;
    }
}
```

###### gunicorn.service

```bash
[Unit]
Description=Gunicorn daemon
After=network.target

[Service]
User=modo
Group=www-data
WorkingDirectory=/home/modo/projects/tdd.aweek-jo.com/source
ExecStart=/home/modo/projects/tdd.aweek-jo.com/env/bin/gunicorn \
        --workers 3 \
        --bind unix:/home/modo/projects/tdd.aweek-jo.com/gunicorn.sock \
        superlists.wsgi:application

[Install]
WantedBy=multi-user.target
```

``` bash
$ sudo ln -s ~/Path/to/yourfile/gunicorn.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
$ sudo systemctl status gunicorn
```



### p.243

#### Problem

```bash
ERROR: test_cannot_add_empty_list_items (functional_tests.test_list_item_validation.ItemValidationTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  ...
    error = self.browser.find_element_by_css_selector('.has-error')
  ...
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: .has-error
```

#### How to solved[^5]

form에 `novalidate` 속성을 추가한다.

###### base.html

```html
<form method="post" action="{% block form_action %}{% endblock %}" novalidate>
	{{ form.text }}
	{% csrf_token %}
	{% if form.errors %}
	<div class="form-group has-error">
		<span class="help-block">
			{{ form.text.errors }}
		</span>
	</div>
	{% endif %}
</form>
```



##### Refer to

- [원서 소개 링크](http://www.obeythetestinggoat.com)
- [hyesun03님의 블로그: 클린 코드를 위한 테스트 주도 개발](https://hyesun03.github.io/2016/09/19/djangoTDD01/)


[^4]: [참고 링크](http://askubuntu.com/a/621209)
[^5]: [참고 링크](https://hyesun03.github.io/2016/09/29/djangoTDD08/), [참고 링크2](https://www.w3schools.com/tags/att_form_novalidate.asp)

 