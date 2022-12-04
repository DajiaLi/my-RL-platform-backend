import threading

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from trainify_bridge.modules.websocket import ws_establish
from trainify_bridge.modules.run_trainify import check_task, TrainifyTasks


# Create your views here.

@csrf_exempt
def test(request):
    # print(request.body["task_name"])
    res = {
            'code': 20000,
            'data': {'msg': '创建训练任务成功'}
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
def run(request):
    body = json.loads(request.body)
    channel = body['channel']
    res = {}

    ws_res = ws_establish(channel)
    if ws_res['done']:
        print("Websocket 建立成功 " + channel)
        res.update({
            'code': 20000,
            'data': {'msg': '创建训练任务成功'}
        })
        print('开始检查是否存在task')
        if not check_task(body['task_name']):
            res.update({
                'code': 50000,
                'data': {'msg': '不存在此实验名称'}
            })
        else:
            print('执行task')
            # 根据上传的任务类型执行对应的任务
            thread = threading.Thread(target=getattr(TrainifyTasks, f"task_{body['task_name']}"),
                                      kwargs={'body': {**body['params']}, 'channel': body['channel']})
            thread.start()
    else:
        res.update({
            'code': 50000,
            'data': {'msg': '未能创建训练任务,建立WebSocket连接出错，请稍后再试'}
        })
    return JsonResponse(res, safe=False)




















