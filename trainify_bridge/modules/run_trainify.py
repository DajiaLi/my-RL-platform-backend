from trainify_bridge.modules.websocket import ws_send
import time

_TASKS = [
    'trainify_verify',
    'bbreach',
    'test'
]


def check_task(name):
    return True if name in _TASKS else False


class TrainifyTasks:

    @staticmethod
    def task_trainify_verify(body, channel):
        for i in range(10):
            ws_send(channel, '现在是 ' + str(i))
            time.sleep(1)


