from flask import Flask, request

app = Flask(__name__)

AppCode = 'h28D3^1r*nhxc&213'


@app.route('/')
def index():
    return 'HelloWorld'


@app.route('/lump')
def lumpControl():
    if (request.headers['AppCode']):
        print('lump No.' + request.args['lumpNo'] + ' is ' +
              request.args['stat'])
    return 'Ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8881)
