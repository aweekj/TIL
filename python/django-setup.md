# Django Setup

1. Activate virtual env.

2. Install django.

```bash
$ pip install --upgrade pip
$ pip install django
```

3. Create project.
> Don't forget . at the end!!

```bash
$ mkdir tutorial
$ cd tutorial
$ django-admin startproject tutorial .
$ tree
.
├── manage.py
└── tutorial
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

4. Create application

```bash
$ ./manage.py startapp community
$ tree
.
├── community
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── tutorial
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   └── settings.cpython-35.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

5. Create Database Table

```bash
$ ./manage.py migrate
```

6. Create Superuser

```bash
$ ./manage.py createsuperuser
```

7. Run Server

```bash
$ ./manage.py runserver
```
