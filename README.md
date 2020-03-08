# generic_model_sandbox
Sandbox to test Generic relationships in DRF

# Quick start

```sh
git clone https://github.com/gnud/generic_model_sandbox
cd generic_model_sandbox
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata generic_app/fixtures/full_data.json
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@example.com', 'password')"
```

Run server

```sh
./manage.py runserver
```

# Quick links

http://localhost:8000/admin/

Demo credentials:
```
user: root
pass: password
```

## All the links

- [Admin](http://localhost:8000/admin/)

    - [Admin comment](http://localhost:8000/admin/generic_app/comment/)

    - [Admin comment2](http://localhost:8000/admin/generic_app/comment2/)

- [DRF API](http://localhost:8000/api/app/v1/)

    - [API comment](http://localhost:8000/api/app/v1/comment/)

    - [API  comment2](http://localhost:8000/api/app/v1/comment2/)

# Problems solving 

## Version 1

Single model named Comment having 2 sub models: Article, Post for the content.
Content is retrieved and automatically determined via RelatedField.  

DRF API that outputs content field object:
URL: GET /api/app/v1/comment/
```json
[
    {
        "pk": 1,
        "content": null
    },
    {
        "pk": 2,
        "content": {
            "pk": 2,
            "content": "Post2"
        }
    },
    {
        "pk": 3,
        "content": {
            "pk": 3,
            "content": "article3"
        }
    }
]
```

## Version 2

Model named CommentNormal having 2 sub models: Article, Post using 2 separate related fields,
with rules one has to be null.
Content object is determined by serializer method by hand, poorly.

DRF API that outputs content field object:
URL: GET /api/app/v1/comment2/
```json

[
    {
        "pk": 1,
        "content": {
            "pk": 1,
            "content": "article1"
        }
    },
    {
        "pk": 2,
        "content": {
            "pk": 1,
            "content": "Post1"
        }
    },
    {
        "pk": 3,
        "content": {
            "pk": 1,
            "content": "Post1"
        }
    }
]
```