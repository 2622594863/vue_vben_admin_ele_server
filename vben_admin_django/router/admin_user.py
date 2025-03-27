from ninja import Router
from typing import List
from ninja.pagination import paginate
from ninja import Query
from .. import tools
from .. import models
from ..schema import RequestSchema, SearchSchema

api = Router()


@api.get('/users', response=List[RequestSchema.AdminUserSchema])
@paginate(tools.ResultModel)
def list_users(request, filters: SearchSchema.AdminUserSchema = Query(...)):
    queryset = models.AuthUser.objects.all()
    data = filters.filter(queryset)
    return data
