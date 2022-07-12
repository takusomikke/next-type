# base_env

1. Copy .env.sample to .env
2. Edit .env
3. ```docker compose build``` and ```docker compose up -d``` * EXITED is correct for the status
4. Enter container.
```docker compose run backend bash``` or ```docker compose run frontend bash```
5. Create project
6. Uncomment CMD line of Dockerfile both backend and frontend
7. Restart container ```docker compose up -d```

# Django
1. Edit https://github.com/takusomikke/base_env/blob/main/code/backend/requirements/common.txt
```
Django==3.2.13
django-debug-toolbar==3.2.4
django-jazzmin==2.4.9
django-extensions==3.1.5
django-cors-headers==3.11.0
djangorestframework==3.13.1
django-filter==21.1
djoser==2.1.0
```
2. Create project
```
docker compose run backend bash
pip install -r /opt/backend/app/requirements/develop.txt --user
django-admin startproject <project_name> .
```
3. Follow the Django manual
