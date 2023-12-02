# django-psql
simple django rest with psql backend


## Generate Migration

    python manage.py makemigrations

## Apply Migration

    python manage.py migrate projects


## Payloads

### Post

```
localhost:8080/api/projects


{
  "title": "ello bird",
  "description": "the quick brown fox jumps over the lazy dog"
}
```

### GET

```
localhost:8080/api/projects

```
### DELETE 
```
localhost:8080/tutorials/:id Api
```
