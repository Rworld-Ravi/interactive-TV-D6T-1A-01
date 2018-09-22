# interactive-TV

an interactive TV using omron's D6T-1A-01 Temperature sensor to show/hide a video with raspberry pi.

Dependencies:

0. pip3 install omxplayer-wrapper

1. On Pi, run “sudo apt-get install netatalk” (for transfering files)

2.On Mac, do cmd+k then afp://10.1.1.10  (replace this with your Raspberry Pi IP address) now you can drag and drop the video file on to pi. (Username: pi / Pass: raspberry

3. On Pi, Menu->Preference->Raspberry Pi Configuration-> Performance -> GPU Memory change to 256MB

4a. On Pi, run "pip3 install omxplayer-wrapper" (for python 3)
4b. On Pi, run "pip install omxplayer-wrapper" (for python 2)

5. sudo raspi-config -> 5 Interfacing Options -> P5 I2C -> Enable

6.sudo apt-get install -y i2c-tools
(https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial#i2c-on-pi)
“Sudo i2cdetect -y 1” will test and show the device address

7. https://www.denshi.club/pc/raspi/5raspberry-pi-zeroiot46-4-i2c-d6t-44l-06.html

6. Create python script

7. Autostart (in Desktop):
nano /home/pi/.config/lxsession/LXDE-pi/autostart
@lxterminal -e python /path_to_your_file/your_file.py

To quit: CTRL+C X2

8. For screen sharing, on pi run
Raspi-config > interfact options > enable SSH, VNC


For non i2c device: On Pi, run “sudo apt install python3-gpiozero” (watch out, this will disable i2c)

Bash tool:

Check process: 1. “top” 2. “ps -A”
Kill process: “kill $pid”


Useful:
A. RUN ON BOOT:
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
B. RUN ON Desktop:
http://blog.startingelectronics.com/auto-start-a-desktop-application-on-the-rapberry-pi/
