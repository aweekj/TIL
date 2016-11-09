# [Django Bluebook](http://www.hanbit.co.kr/store/books/look.php?p_code=B7703021280) Study

# Chapter14. 장고 핵심 기능 - Model

## 14.1 모델 정의
* 장고는 ORM(Object-Relational Mappging)방식 - 테이블을 클래스로 처리, 클래스의 특징인 속성과 메소드를 가질 수 있음 - 을 기반으로 한다.

> 테이블을 클래스로 매핑해서 테이블에 대한 생성, 조회, 수정, 삭제 기능을 클래스 객체에 대해 수행하면, 장고가 내부적으로 DB에 반영해주는 방식.
객체를 클래스로 표현하는 것과 같이 관계형 데이터베이스를 객체처럼 쉽게 사용할 수 있다.
#### 모델 예시 코드

```python
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One line Description', max_length=100, blank=True)
    owner = models.ForeignKey(User, null=True)
    # objects = models.Manager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
`
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))
```

### 14.1.1 모델 속성
* 모델 클래스의 속성 = 테이블의 컬럼(필드)
* 필드는 항상 필드명, 필드 타입, 필드 옵션을 지정해야 함.
  * 필드 타입 : 테이블의 컬럼 타입. 폼으로 렌더링 되는 경우 HTML 위젯을 지정. 필드 또는 폼에 대한 유효성 검사 시 최소 기준이 됨.
  * 커스텀 필드 타입 : [참고1](https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-attribute-reference), [참고2](https://docs.djangoproject.com/en/1.10/howto/custom-model-fields/)

### 14.1.2 모델 메소드

* 클래스 메소드(테이블 레벨에서 동작)와 객체 메소드(레코드 레벨에서 동작)를 구분해야 함.
* 장고에서는 객체 메소드만 사용 -> 레코드 단위에만 영향을 미침.
* 클래스 메소드 대신 별도의 Manager 클래스를 정의하여 이를 통해 테이블의 CRUD 수행.

#### 많이 사용되는 모델 메소드
1. `__unicode__()`(in Python2) or `__str__()`(in Python3)
2. get_absolute_url()
3. get_next_by_FOO(**kwargs)
4. get_previous_by_FOO(**kwargs)
5. get_FOO_display()

### 14.1.3 Meta 내부 클래스 속성
* 모델 클래스의 필드는 아니나, 모델 클래스에 필요한 항목을 정의.

#### 많이 사용되는 Meta 내부 클래스 속성
1. ordering
2. db_table
3. verbose_name
4. verbose_name_plural

* [참고](https://docs.djangoproject.com/en/1.10/ref/models/options/)

### 14.1.4 Manager 속성
* 모든 모델은 반드시 Manager 속성을 가져야 한다. 명시적으로 지정하지 않으면 디폴트로 `objects = models.Manager()`를 가짐.
* Manager 클래스를 통해서 데이터베이스 쿼리가 이뤄짐.
* Manager 속성은 모델 클래스를 통해서만 접근이 가능.
* 테이블 레벨에서의 동작은 Manager 클래스의 메소드를 통해 이뤄짐.
* `all()`, `filter()`, `exclude()`, `get()`, `count()` 등의 QuerySet 메소드는 모두 Manager 클래스의 메소드로도 사용
* 모델 클래스에서 여러 개의 Manager 속성을 정의할 수 있으며, 첫 번째로 정의된 것이 디폴트 Manager이다.
