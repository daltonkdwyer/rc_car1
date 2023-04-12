from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
# from Motor import *
# from flask_ngrok import run_with_ngrok
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
# run_with_ngrok(app)
# PWM = Motor()

print("TESTing")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

prior_heartbeat = 0
@socketio.on('heartbeat')
def heartbeat():
    global prior_heartbeat
    # print('Heartbeat')
    current_heartbeat = int(round(time.time() * 1000))
    latency = current_heartbeat - prior_heartbeat - 1000
    print("Heartbeat Latency: " + str(latency))
    emit('server_message', latency)

    if latency > 15:
        print("SAFETY STOP")
        # PWM.setMotorModel(0,0,0,0)

    prior_heartbeat = current_heartbeat

@socketio.on('move_command')
def handle_my_custom_event(direction):
    print('Received Direction:', direction)

    # if direction == 'STOP':
    #     PWM.setMotorModel(0,0,0,0)

    # if direction == 'BACK':
    #     PWM.setMotorModel(0,0,0,0)
    #     PWM.setMotorModel(2000,2000,2000,2000)
    #     # time.sleep(0.5)
    #     # PWM.setMotorModel(0,0,0,0)

    # if direction == 'FORWARD':
    #     PWM.setMotorModel(0,0,0,0)
    #     PWM.setMotorModel(-2000,-2000,-2000,-2000)
    #     # time.sleep(0.5)
    #     # PWM.setMotorModel(0,0,0,0)

    # if direction == 'LEFT':
    #     PWM.setMotorModel(0,0,0,0)
    #     PWM.setMotorModel(0,0,-2000,-2000)
    #     # time.sleep(0.5)
    #     # PWM.setMotorModel(0,0,0,0)
        
    # if direction == 'RIGHT':
    #     PWM.setMotorModel(0,0,0,0)
    #     PWM.setMotorModel(-2000,-2000,0,0)
    #     # time.sleep(0.5)
    #     # PWM.setMotorModel(0,0,0,0)

if __name__ == '__main__':
    socketio.run(app, port=5000)