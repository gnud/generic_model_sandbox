# generic_model_sandbox
Sandbox to test Generic relationships in DRF

# Version 1

Single model named Comment having 2 sub models: Article, Post for the content.

DRF API that outputs content field object:
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
            "content": "The fox jumped over the rock"
        }
    },
    {
        "pk": 3,
        "content": {
            "pk": 3,
            "content": "Bob ate some peaches for breakfast"
        }
    }
]
```
