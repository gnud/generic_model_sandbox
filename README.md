# generic_model_sandbox
Sandbox to test Generic relationships in DRF

# Version 1

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

# Version 2

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