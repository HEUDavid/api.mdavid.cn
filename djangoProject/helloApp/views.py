from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from django.views.decorators.http import require_http_methods
from django.template import Template, Context
import os


# Create your views here.


class BaseApp(object):
    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def index(request):
        return HttpResponse("hello api.mdavid.cn")

    @staticmethod
    def httpRes(request):
        response = HttpResponse()
        response.write("<h1>HttpResponse</h1>")
        response.write("<h2>这是h2</h2>")
        return response

    @staticmethod
    def jsonRes(request):
        data = {
            "type": "JsonResponse",
            "name": "David",
            "age": 23
        }
        response = JsonResponse(data)
        return response

    @staticmethod
    def otherRes(request, type):
        print("type =", type)
        if type == 'http':
            return BaseApp.httpRes(request)
        elif type == 'json':
            return BaseApp.jsonRes(request)
        elif type == 'streaming':
            # 可以是文件，也可以是任何大规模数据响应
            def file_iterator(file_name, chunk_size=512):
                with open(file_name) as f:
                    while True:
                        c = f.read(chunk_size)
                        if c:
                            yield c
                        else:
                            break

            cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            fname = cwd + "/djangoProject/templates/" + "data.txt"
            print("fname =", fname)
            response = StreamingHttpResponse(file_iterator(fname))
            return response
        elif type == 'file':
            cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            response = FileResponse(
                open(cwd + "/djangoProject/templates/pylogo.jpg", 'rb'))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="pylogo.jpg"'
            return response
        else:
            return HttpResponse("未实现")

    @staticmethod
    @require_http_methods(['GET', 'POST'])
    def templateAndData(request):
        # I can assume now that only GET or POST requests make it this far
        template = Template("<h1>这个程序的作者是{{ name }}</h1>")
        context = Context({"name": "大卫"})
        return HttpResponse(template.render(context))
