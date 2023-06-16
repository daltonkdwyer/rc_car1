from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from Motor import *
import time
client_time = 0
global_counter = 0

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
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

# Third attempt at latency protection
@socketio.on('heartbeat')
def latency_heartbeat(client_time_received):
    global client_time 
    global global_counter
    current_counter = global_counter

    # Update client time every time a heartbeat is recieved. Probably must be global so the next heartbeat still will update
    client_time = client_time_received
    server_time = server_time_function()
    latency = server_time - client_time
    # print("Real Latency: ", str(latency))
    server_message = {"Message": "Latency", "Data": latency}
    emit('Server message', server_message)

    time.sleep(3)

    if current_counter == global_counter:
        server_message = {"Message": "Message", "Data": "Got a latency stop"}
        emit('Server message', server_message)
        PWM.setMotorModel(0,0,0,0)



    server_time2 = server_time_function()
    delayed_latency = server_time2 - client_time
    print("Delayed Latency: ", str(delayed_latency))

    server_message = {"Message": "Delayed Latency", "Data": delayed_latency}
    emit('Server message', server_message)

    if delayed_latency > 3000:
        print("LATENCY STOP")
        server_message = {"Message": "Message", "Data": "Latency Stop!"}
        emit('Server message', server_message)
        PWM.setMotorModel(0,0,0,0)

def server_time_function():
    server_time = int(time.time() * 1000)
    return server_time



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
    # socketio.run(app, port=5000)
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True)
