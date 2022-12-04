import requests

APPKEY = "BC-080f24802f2f489b8e9c89d2854ed63f"
GOEASY_URL = "http://rest-hangzhou.goeasy.io/publish"


def ws_establish(channel):
    content = "websocket 尝试建立 " + channel
    print(content)
    data = {"appkey": APPKEY, "channel": channel, "content": content}
    res = requests.post(GOEASY_URL, data=data)
    resp = {}
    if res.status_code == 200:
        resp.update({
            'code': 20000,
            'data': {'channel': channel}
        })
        return {
            'done': True,
            'data': resp
        }
    else:
        resp.update({
            'code': 50000,
            'data': {'msg': 'RL_PLATFORM 建立WebSocket连接错误，请稍后再试'}
        })
        return {
            'done': False,
            'data': resp
        }


def ws_send(channel, content):
    data = {"appkey": APPKEY, "channel": channel, "content": content}
    res = requests.post(GOEASY_URL, data=data)
    return True if res.status_code == 200 else False
