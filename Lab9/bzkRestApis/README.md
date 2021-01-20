# Lab 9 Django + React (aplikacja CRUD)
<h1>Strona stworzona na podstawie poradnika <a href="https://bezkoder.com/django-react-axios-rest-framework/" rel="nofollow">strona</a></h1

## Wygląd strony:


![list](/Lab9/bzkRestApis/SCR/1.PNG "Start")


Settings.py
``` python 
INSTALLED_APPS = [
    ...
    'corsheaders',         
    'rest_framework',
    'todo',     
  ]
```

``` python 
 MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',      
    ...
]
```
``` python 
CORS_ORIGIN_WHITELIST = [
     'http://localhost:3000',
     'http://localhost:8000',
]
```
