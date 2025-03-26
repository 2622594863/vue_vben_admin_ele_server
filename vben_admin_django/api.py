from ninja import NinjaAPI
from .router import auth, user, test
from typing import Any, List
from ninja_jwt.authentication import JWTBaseAuthentication
from ninja_extra.security import HttpBearer
from django.http import HttpRequest
from django.contrib.auth.models import User


class Auth(JWTBaseAuthentication, HttpBearer):
    def __init__(self, role_list: List[str] = []):
        self.role_list = role_list
        super().__init__()

    def authenticate(self, request: HttpRequest, token: str) -> Any:
        result = self.jwt_authenticate(request, token)
        if not self.role_list:
            return True
        user: User = request.user
        for o in user.groups.all():
            if o.name in self.role_list:
                return result
        return False

api = NinjaAPI()

api.add_router("/auth/", auth.api)
api.add_router("/user/", user.api, auth=Auth([]))
api.add_router("/test/", test.api)
