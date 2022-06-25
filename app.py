from flask import Flask, render_template, request
from Motor import *
from flask_ngrok import run_with_ngrok

# To Gitpush when you're logged in to the Rpi, here is PAT: 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

app = Flask(__name__)
run_with_ngrok(app)
PWM = Motor()
request_num = 0

@app.route('/', methods=['GET', 'POST'])
def on():
    # Need to access request_num inside the function
    global request_num
    print("START: SERVER REQUEST #" + str(request_num))
    print("Request type: " + str(request.method))
    # print("Header: " + str(request.headers))

    if request.method == 'POST':
        print("Request: " + str(request))
        # You recieve a wierd immutable dict as your async FORM. So need to make it to normal dict below
        dict_direction = request.form.to_dict()
        direction = dict_direction['direction']
        print("FORM DATA: " + str(dict_direction))

        if direction == 'FORWARD':
            PWM.setMotorModel(0,0,0,0)
            PWM.setMotorModel(2000,2000,2000,2000)
            time.sleep(0.5)
            PWM.setMotorModel(0,0,0,0)

        if direction == 'BACK':
            PWM.setMotorModel(0,0,0,0)
            PWM.setMotorModel(-2000,-2000,-2000,-2000)
            time.sleep(0.5)
            PWM.setMotorModel(0,0,0,0)

        if direction == 'LEFT':
            PWM.setMotorModel(0,0,0,0)
            PWM.setMotorModel(0,0,2000,2000)
            time.sleep(0.5)
            PWM.setMotorModel(0,0,0,0)
            
        if direction == 'RIGHT':
            PWM.setMotorModel(0,0,0,0)
            PWM.setMotorModel(2000,2000,0,0)
            time.sleep(0.5)
            PWM.setMotorModel(0,0,0,0)

        request_num += 1
        print("END OF REQUEST")
        return render_template('index.html')

    # On first load this will happen: 
    if request.method == 'GET':
        request_num += 1
        print("Request: " + str(request))
        print("END OF GET REQUEST")
        return render_template('index.html')

    # Error Handling: 
    else:
        return("NOT A GET OR POST REQUEST?")