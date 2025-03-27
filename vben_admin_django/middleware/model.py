from django.utils.deprecation import MiddlewareMixin
from django.http.response import HttpResponse
import json
class M1(MiddlewareMixin):

    def __call__(self, request):
        response:HttpResponse = self.get_response(request)
        #判断状态码是不是200 并且是json
        if response.status_code == 200 and 'application/json' in response['Content-Type']:
            s = response.content.decode('utf-8')
            obj = json.loads(s)
            t = obj.get('type')
            if t is None:
                return response
            if t == 'model':
                obj['data']={}
                obj['data']['items']=obj.get('items',[])
                obj['data']['total'] = obj.get('total', 0)
                del obj['items']
                del obj['total']
                del obj['type']
                response.content = json.dumps(obj).encode('utf-8')

        return response