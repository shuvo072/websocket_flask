from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sockets = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

@sockets.route('/websocket')
def websocket_handler(ws):
    while True:
        message = ws.receive()
        if message:
            print('Received message:', message)
            ws.send('Server received your message: ' + message)

# if __name__ == '__main__':
#     from gevent import pywsgi
#     from geventwebsocket.handler import WebSocketHandler
#     server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
#     server.serve_forever()
