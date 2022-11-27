from django.http import HttpResponse


def index(request):
    print("收到一个请求")
    return HttpResponse("Hello, world. You're at the polls index.")