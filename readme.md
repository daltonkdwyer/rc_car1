Readme for the remotely operated car:

The solution has two servers: a Web RTC server for video, and a Flask server for remote control 

1) Web RTC Server: 
    1) Built from ChaimCode
        A) Source tutorial: https://www.youtube.com/watch?v=JhyY8LdAQHU
        B) Original source code: https://github.com/coding-with-chaim/native-webrtc
    2) It lives in this file structure
    3) It is deployed on Heroku: https://dashboard.heroku.com/apps/guarded-journey-06660
    4) To update the code, change whatever you want in this local Chaim file structure on this local machine, then:
        A) git add .
        B) git commit -m "blahblahblah"
        C) git push heroku master
    5) To access, go here: https://guarded-journey-06660.herokuapp.com/

2) Python Flask Server:
    A) Lives on Rasbery Pi
    B) 'rc_car1' on Github
    C) To Start:
        1) cd into rc_car1
        2) In a terminal on Pi run: ./ngrok http --subdomain=plntry33 5000 
            - This 'punches out' and lets anyone access this as a webpage
            - (where the port can be anything)
        3) Copy and paste the website from the terminal into the 'Index' page
        4) In separate terminal: flask run
            - This starts the flask server
        5) Can access from anywhere! 

- AUTOBOOT:
    - Vehicle Control: 
        - For Flask: 
            - Command: sudo nano /etc/rc.local
            - Tutorial: https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-1-rclocal
            - Autoboot code:
                - Edit rc.local using this command: sudo nano /etc/rc.local
                - Code to insert: python3 /home/pi/rc_car1/app.py &
        - For ngrok:
            - For some reason has to be in bash folder, not rc.local folder
            - Tutorial: https://rntlab.com/question/module-9-ngrok-install-and-work/ 
            - Autoboot code:
                - Edit bash file using this command: sudo nano /home/pi/.bashrc
                - Code to insert: screen -d -m /home/pi/./ngrok http --subdomain=plntry33 5000
    - Vehicle Video
        - To open browser on auto-start:
            - Tutorial: https://forums.raspberrypi.com/viewtopic.php?t=66206 (ctrl-f Ragnar)
            - Create a SH file on the desktop: testshell.sh
                - Write this command in the file: 
                    chromium-browser https://guarded-journey-06660.herokuapp.com/room/33
            - Go to pi>.config>autostart (will have to use ls -a to get there)
            - Create a .desktop file: plntry33autostart.desktop
            - Nano into the file, and write this:  
                [Desktop Entry]
                Encoding=UTF-8
                Name=Terminal autostart
                Comment=Start a terminal and list directory
                Exec=/usr/bin/lxterm -e 'bash /home/pi/Desktop/testshell.sh'


- SSH into Pi: ssh pi@192.168.1.219
- Restart Heroku: heroku restart

Change Log:
1) Started using aysnc buttons on FLASK server to submit form data instead of syncronous buttons (don't need to reload page)
2) Now using keystrokes instead of buttons
3) Flask server and ngrok start automatically on bootup
4) Open browser automatically on bootup
5) Made video larger

Notes:
- Does not support Chromium! 'On key up' events don't trigger anything
- To see what Python scripts are running on the Pi, use this command: ps -aef | grep python
- To stop a process, use 'kill <process ID>'. The process ID is the number in the second column above, maybe 462.

Startup:
1) Restart Heroku server
2) Put phone into Hotspot mode and plug into car
3) Turn car on
4) Navigate to plntry/33

