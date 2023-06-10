from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from Motor import *
# from flask_ngrok import run_with_ngrok
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
# run_with_ngrok(app)
PWM = Motor()

print("Pineaplle")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

# One attempt at latency protection
# prior_heartbeat = 0
# @socketio.on('heartbeat')
# def heartbeat():
#     global prior_heartbeat
#     current_heartbeat = int(round(time.time() * 1000))
#     latency = current_heartbeat - prior_heartbeat - 500
#     # Unprint out this, as you will get a lot of latency indicators
#     print("Heartbeat Latency: " + str(latency))
#     # emit('server_message', latency)

#     if latency > 200:
#         print("SAFETY STOP")
#         emit('server_message', 'SAFETY STOP')
#         PWM.setMotorModel(0,0,0,0)
#     prior_heartbeat = current_heartbeat

# Second attempt at latency protection
@socketio.on('heartbeat')
def latency_heartbeat(client_time):
    server_time = int(time.time() * 1000)
    latency = server_time - int(client_time)
    print("Latency = " + str(latency))
    if latency > 2000:
        PWM.setMotorModel(0,0,0,0)
        socketio.send("LATENCY STOPPPPPPPPP")

@socketio.on('move_command')
def handle_my_custom_event(direction):
    print('Received Direction:', direction)
    direction = direction['data']

    if direction == 'STOP':
        PWM.setMotorModel(0,0,0,0)

    if direction == 'BACK':
        PWM.setMotorModel(0,0,0,0)
        PWM.setMotorModel(2000,2000,2000,2000)

    if direction == 'FORWARD':
        PWM.setMotorModel(0,0,0,0)
        PWM.setMotorModel(-2000,-2000,-2000,-2000)

    if direction == 'LEFT':
        PWM.setMotorModel(0,0,0,0)
        PWM.setMotorModel(0,0,-2000,-2000)
        
    if direction == 'RIGHT':
        PWM.setMotorModel(0,0,0,0)
        PWM.setMotorModel(-2000,-2000,0,0)

if __name__ == '__main__':
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True)