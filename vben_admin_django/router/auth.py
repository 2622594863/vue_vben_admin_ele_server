from g4f.Provider.deprecated.Myshell import models
from ninja import Router
from django.core.handlers.wsgi import WSGIRequest
from ..tools import Result as result
from ..schema import RequestSchema
from ninja_jwt.tokens import AccessToken
from django.contrib.auth import authenticate, login, logout
from .. import models
from ninja_jwt.tokens import AccessToken

api = Router()


@api.post('/login')
def fun_login(request: WSGIRequest, data: RequestSchema.LoginUserSchema):
    user = authenticate(username=data.username, password=data.password)
    if user is None:
        return result.error(message="用户名或密码错误")
    jwt = str(AccessToken.for_user(user))
    login(request, user)
    data = {
        "accessToken": jwt
    }
    return result.success(data=data)


@api.get("/codes")
def fun_codes(request: WSGIRequest):
    data = [
        "AC_100100",
        "AC_100110",
        "AC_100120",
        "AC_100010"
    ]
    return result.success(data=data)


@api.post("/logout")
def fun_logout(request: WSGIRequest):
    jwt = request.headers.get('Authorization')
    if jwt is None:
        return result.success()
    logout(request)
    return result.success()


@api.get("/info")
def fun_logout(request: WSGIRequest):
    first = models.Setting.objects.first()
    data = {}
    if first is None:
        data['title'] = '无标题'
        data['subheading'] = '无副标'
    else:
        data['title'] = first.title
        data['subheading'] = first.subheading
    return result.success(data=data)
