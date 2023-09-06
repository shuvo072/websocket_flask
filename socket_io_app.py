from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS
# import eventlet

# eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_precious'
CORS(app)
socketio = SocketIO(app, async_mode='eventlet')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    send(data, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)