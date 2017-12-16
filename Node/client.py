import requests

if __name__ == '__main__':
    name = '空调'
    payload = {'name': name, 'content': '节点信息'}
    res = requests.post('http://192.168.0.103:8088', data=payload)
    print(res.text)