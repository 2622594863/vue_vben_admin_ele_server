from ninja import Schema

class UserSchema(Schema):
    selectAccount: str
    username: str
    password: str
    captcha: bool


class DataSchema(Schema):
    name: str
