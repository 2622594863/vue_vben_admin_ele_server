from ninja import Schema, FilterSchema, Field
from typing import Optional


class RequestSchema:
    # 接收请求和响应的Schema
    class LoginUserSchema(Schema):
        selectAccount: str
        username: str
        password: str
        captcha: bool

    class AdminUserSchema(Schema):
        username: str
        first_name: str
        password: str

    class DataSchema(Schema):
        name: str


class SearchSchema:
    # 条件查询的Schema
    class AdminUserSchema(FilterSchema):
        username: Optional[str] = Field('', q='username__icontains')
        first_name: Optional[str] = Field('', q='first_name__icontains')
