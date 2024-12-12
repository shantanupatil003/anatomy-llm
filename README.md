# ANATOMY LLM 

### Create conda environment 
```
conda create --name <env> --file requirements.txt
```

### Database Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Run the server
```
python manage.py runserver
```

### Swagger

http://127.0.0.1:8000/swagger-ui
