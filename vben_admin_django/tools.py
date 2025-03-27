from typing import Any, Dict, List, Union
from ninja.pagination import PaginationBase
from ninja import Schema


class Result():
    @classmethod
    def success(self, message: str = "ok", data: dict = {}):
        return {
            "code": 0,
            "data": data,
            "error": None,
            "message": message
        }

    @classmethod
    def error(self, message: str = "error", data: dict = {}):
        return {
            "code": -1,
            "data": data,
            "error": message,
            "message": message
        }


class DataSchema(Schema):
    items: List[Any]
    total: int


class ResultModel(PaginationBase):
    items_attribute: str = "items"

    class Input(Schema):
        page: int = 1
        pageSize: int = 20

    class Output(Schema):
        code: int
        items: List[Any]
        total: int
        error: None
        message: str
        type: str

    def paginate_queryset(self, queryset, pagination: Input, **params):
        page = pagination.page
        pageSize = pagination.pageSize
        if pageSize >= 100:
            pageSize = 100
        start_index = (page - 1) * pageSize
        end_index = start_index + pageSize
        items = queryset.all()[start_index:end_index]
        total = queryset.count()

        return {
            'code': 0,
            'items': items,
            'total': total,
            'error': None,
            'message': 'ok',
            'type':'model'
        }
