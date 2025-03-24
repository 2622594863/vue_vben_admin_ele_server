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
