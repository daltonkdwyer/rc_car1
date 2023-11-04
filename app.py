from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from Motor import *
import threading
import time

client_time = 0
server_time = 0
latency = 0
connection_status = False 
sent_latency_stop = False

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
PWM = Motor()

print("Pineapple 2")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    global connection_status
    connection_status = True
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    global connection_status
    connection_status = False
    print('Client disconnected')

# Fourth attempt at latency protection
@socketio.on('heartbeat')
def latency_heartbeat(client_time_received):
    global client_time 
    global connection_status
    global sent_latency_stop

    connection_status = True
    client_time = client_time_received
    server_message = {"Message": "Latency", "Data": latency}
    emit('Server message', server_message)

    if latency > 3000:                   
        server_message = {"Message": "Message", "Data": "Latency Stop"}
        emit('Server message', server_message)
        sent_latency_stop = True

    elif latency < 3000 and sent_latency_stop == True:
        server_message = {"Message": "Message", "Data": "blank"}
        emit('Server message', server_message)
        sent_latency_stop = False

def latency_protection():
    global connection_status
    global latency
    global client_time
    global server_time
    print("Connection status: " + str(connection_status))
    while True:
        while connection_status is True:
            server_time = int(time.time() * 1000)
            latency = server_time - client_time
            print("Latency: " + str(latency) + "ms")
            if latency > 3000:
                PWM.setMotorModel(0,0,0,0)
                print("LATENCY STOP")
            time.sleep(1)

threading.Thread(target=latency_protection).start()


@socketio.on('move_command')
def handle_my_custom_event(direction):
    print('Received Direction:', direction)
    direction = direction['data']

    if direction == 'STOP':
        PWM.setMotorModel(0,0,0,0)

    if direction == 'BACK':
        PWM.setMotorModel(2000,2000,2000,2000)

    if direction == 'FORWARD':
        PWM.setMotorModel(-2000,-2000,-2000,-2000)

    if direction == 'LEFT':
        PWM.setMotorModel(2000,2000,-2000,-2000)
        
    if direction == 'RIGHT':
        PWM.setMotorModel(-2000,-2000,2000,2000)

if __name__ == '__main__':
    # socketio.run(app, port=5000)
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True)



# Type=oneshot
# ExecStart=sudo -u daltonkdwyer git -C /home/daltonkdwyer/rc_car1 fetch --all
# ExecStart=sudo -u daltonkdwyer git -C /home/daltonkdwyer/rc_car1 reset --hard origin