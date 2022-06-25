from flask import Flask, render_template, request
from Motor import *
from flask_ngrok import run_with_ngrok

# To Gitpush when you're logged in to the Rpi, here is PAT: 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

app = Flask(__name__)
run_with_ngrok(app)
PWM = Motor()

@app.route('/', methods=['GET', 'POST'])
def on():
        if request.method == 'POST':
            print("START OF PROCESS")
            print("Request: " + str(request))
        # You recieve a wierd immutable dict as your async FORM. So need to make it to normal dict below
            dict_direction = request.form.to_dict()
            direction = dict_direction['direction']

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
        print("END OF PROCESS")
        return render_template('index.html')


#test comment to check Git. Please ignore6
