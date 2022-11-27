from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def test(request):
    # print(request.body["task_name"])
    res = {
            'code': 20000,
            'data': {'msg': '创建训练任务成功'}
        }
    return JsonResponse(res, safe=False)
