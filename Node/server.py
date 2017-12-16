from flask import Flask, request

app = Flask(__name__)

count_node = 0
clients_ip = []


@app.route('/', methods=['POST'])
def loginRequest():  
    global count_node
    global clients_ip
    count_node += 1
    clients_ip.append(request.remote_addr)
    print('节点: ' + request.form['name'] + ' 信息: ' + request.form['content'] +
          ' ip: ' + request.remote_addr)
    print('当前节点数: ' + str(count_node))
    return 'Log in success'


@app.route('/', methods=['GET'])
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
