from ninja import Router
from django.core.handlers.wsgi import WSGIRequest
from ..tools import Result as result
from ninja_jwt.tokens import RefreshToken, AccessToken
from django.http import HttpResponse
api = Router()


@api.get("/get")
def fun(request: WSGIRequest):
    import random
    jwt: str = request.headers.get('Authorization').replace('Bearer ', '')
    name_list = ['小红', '小蓝', '小绿', '小黄']
    return result.success(data={"name": random.choice(name_list), "age": 18})


@api.get("/list")
def getlist(request: WSGIRequest):
    return {
        "code": 0,
        "data": {
            "items": [
                {
                    "id": "85ce6e1b-bd95-4662-ba9c-b0aedaaa4fb2",
                    "imageUrl": "https://avatars.githubusercontent.com/u/53427358",
                    "imageUrl2": "https://avatars.githubusercontent.com/u/25100854",
                    "open": False,
                    "status": "warning",
                    "productName": "Bespoke Metal Hat",
                    "price": "939.79",
                    "currency": "MAD",
                    "quantity": 21,
                    "available": True,
                    "category": "Toys",
                    "releaseDate": "2024-05-08T17:33:57.773Z",
                    "rating": 1.010501810275216,
                    "description": "The sleek and rewarding Bike comes with red LED lighting for smart functionality",
                    "weight": 2.0019532156934274,
                    "color": "teal",
                    "inProduction": True,
                    "tags": [
                        "Tasty",
                        "Soft",
                        "Soft"
                    ]
                },
                {
                    "id": "c12bde2f-967d-4fb5-b0b5-f65e30bbf1b3",
                    "imageUrl": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/37.jpg",
                    "imageUrl2": "https://cdn.jsdelivr.net/gh/faker-js/assets-person-portrait/male/512/10.jpg",
                    "open": False,
                    "status": "error",
                    "productName": "Refined Steel Chicken",
                    "price": "49.09",
                    "currency": "LKR",
                    "quantity": 57,
                    "available": False,
                    "category": "Toys",
                    "releaseDate": "2024-08-12T07:27:23.158Z",
                    "rating": 2.1241952537237556,
                    "description": "New Chicken model with 58 GB RAM, 248 GB storage, and awesome features",
                    "weight": 4.285223965689625,
                    "color": "lavender",
                    "inProduction": True,
                    "tags": [
                        "Intelligent",
                        "Intelligent",
                        "Sleek"
                    ]
                },
            ],
            "total": 100
        },
        "error": None,
        "message": "ok"
    }
