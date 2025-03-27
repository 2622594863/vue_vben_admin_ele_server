from ninja import Router
from django.core.handlers.wsgi import WSGIRequest
from ..tools import Result as result


api = Router()


@api.get("/info")
def fun(request: WSGIRequest):
    roles = []
    for o in request.user.groups.all():
        roles.append(o.name)
    data = {
        "id": 0,
        "realName": request.user.first_name,
        "roles": roles,
        "username": request.user.username,
        "money": 234.43
    }
    return result.success(data=data)
