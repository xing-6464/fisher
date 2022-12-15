import requests


class HTTP:
    def get(self, url, return_json=True):
        # 发送http请求
        r = requests.get(url)

        # 处理错误
        if r.status_code != 200:
            return {} if return_json else ''

        # 成功返回数据
        return r.json() if return_json else r.text
