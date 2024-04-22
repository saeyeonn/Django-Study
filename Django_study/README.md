## Django

- Allow us to write Python code that dynamically generates HTML & CSS

```
$ django-admin startproject PROJECT_NAME
```

<br>

- manage.py : what we use to execute cmds on our terminal (won't have to edit)
- settins.py : contains important configuration settings for project
- urls.py : contains directions for where users should be routed after navigating to certain URL

<br>

```
$ python manage.py runserver
```

- open dev server which I can access by visiting URL provided
- Dev server is being run locally on my machine = other can't access

<br>

```
$ python manage.py startapp APP_NAME
```

<br><br>

### views

- contain number of different views
- can think of view as 1 page the user might like to see

<br><br>

### urls - specific app

1. give ability to reroute URLs

```python
from django.urls import path
```

2. import any functions created in views.py

```python
from . import views
```

3. For each desired URL, add item to urlpatterns list that contains call to path function with 2 / 3 args

- String : represent URL path
- Function : from views.py that wish to call when URL is visited
- Name (optional) : for path

<br><br>

### urls - entire app

- include all of paths from url.py within app
- include : function we gain access to by also importing include from django.urls

```python
include("APP_NAME.urls)
```

<br><br>

### html

- {% ... %} : tell Django to fill this block with some text from other file