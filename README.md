# Gett blog

# Installation

```
docker-compose run web makemigrations
docker-compose run web migrate
docker-compose run web collectstatic --noinput
docker-compose run web createsuperuser
```

## Run

```
docker-compose up
```

### Links
[Site](http://127.0.0.1:8001)
[Admin](http://127.0.0.1:8001/admin)