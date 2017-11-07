# Gett blog

# Installation

```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py collectstatic --noinput
docker-compose run web python manage.py createsuperuser
```

## Run

```
docker-compose up
```

### Links

- [Site](http://127.0.0.1:8001)
- [Admin](http://127.0.0.1:8001/admin)