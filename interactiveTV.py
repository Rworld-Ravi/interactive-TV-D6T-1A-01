#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import logging
import atexit
import smbus
import time
import numpy
import os

# from gpiozero import Button

# button = Button(2)
sensorStatus = "notTriggered"
videoStatus = "fadeIn"
alpha = 255
fadeInSpeed = 1
fadeOutSpeed = 0.5

readings = numpy.array([])
max_samples = 20
avg = 0
firstTimeCalibration = True

i2c = smbus.SMBus(1)
addr=0x0a
lastTime = 0


def goodbye():
    print("stop! closing omxplayer before leaving")
    player.stop()

# def checkButton():
#     global status
#
#     if button.is_pressed:
#         # print("Button is pressed")
#         status = "fadeIn"
#     else:
#         # print("Button is not pressed")
#         status = "fadeOut"
#     # print("local status:",status)




def checkSensor():
    global sensorStatus
    global readings, avg, firstTimeCalibration

    if(firstTimeCalibration):
        for x in range(0,max_samples-1):
            data = i2c.read_i2c_block_data(addr,0x4c,5)
            temp = (data[3]*256 +data[2])/10.0
            readings = numpy.append(readings, temp)
            avg = numpy.mean(readings)
            print("avg Temp ",avg)
            sleep(0.5)
        firstTimeCalibration = False


    data = i2c.read_i2c_block_data(addr,0x4c,5)
    Device_temp=(data[1]*256 +data[0])/10.0
    # Device_temp=27
    temp = (data[3]*256 +data[2])/10.0

    print("--------------------------")
    print(sensorStatus)
    print("device Temp ",Device_temp)
    print("avg Temp ",avg)
    print("detect Temp ","\x1b[K\x1b[48;5;88m"+str(temp)+"\x1b[0m")
    # print("check error code", data[4])

    if(data[4]>0):
        if (temp-avg)>0.3:
            sensorStatus = "triggered"
        else:
            sensorStatus = "notTriggered"
            readings = numpy.append(readings, temp)
            print(readings)
            avg = numpy.mean(readings)
            if len(readings) == max_samples:
                readings = numpy.delete(readings, 0)
        # sensor error
    else:
        print("sensor error, restarting pi")
        sensorStatus = "notTriggered"
        os.system('sudo shutdown -r now')

        # exit(0)
        #todo: relaunch python or rpi




VIDEO_1_PATH = "/home/pi/Desktop/TestVideo_Left.mp4"
# player_log = logging.getLogger("Player 1")
# player = OMXPlayer(VIDEO_1_PATH, args=['--orientation', '90'])
player = OMXPlayer(VIDEO_1_PATH, args=['--loop', '--no-osd','--orientation', '90' , '-b'])
# player = OMXPlayer(VIDEO_1_PATH, args=['--loop']) #debug for showing text


sleep(2.5)
# player.set_position(170)
# player.playEvent += lambda _: player_log.info("Play")
# player.stopEvent += lambda _: player_log.info("Stop")



atexit.register(goodbye)

while True:
    # checkButton()
    milli_sec = int(round(time.time() * 1000))
    if((milli_sec-lastTime)>500):
        try:
            checkSensor()
            lastTime=milli_sec
        except IOError:
            print("IO(sensor) error, restarting pi")
            os.system('sudo shutdown -r now')


    if(sensorStatus == "triggered"):
        videoStatus = "fadeIn"


    if(videoStatus == "fadeIn"):
        if(alpha >= 255):
            alpha = 255
            videoStatus = "fadeOut"
        else:
            alpha+=fadeInSpeed

    elif(videoStatus == "fadeOut"):
        if(alpha>0):
            alpha-=fadeOutSpeed
        else:
            alpha = 0
    # print("alpha", alpha)
    player.set_alpha(alpha)

    # print("global status:",status)


#
#
#     char = getch()
#
#     if (char == "q" or char == chr(27)):
#         print("stop! quiting omxplayer")
#         # player.quit()
#         player.stop()
#         exit(0)
#     elif(char == "i"):
#         print("fade in, set alpha 255")
#         hide = False
#     elif(char == "o"):
#         print("fade out, set alpha 0")
#         hide = True



# player = OMXPlayer(VIDEO_1_PATH,
#         dbus_name='org.mpris.MediaPlayer2.omxplayer1')
# player.playEvent += lambda _: player_log.info("Play")
# player.pauseEvent += lambda _: player_log.info("Pause")
# player.stopEvent += lambda _: player_log.info("Stop")



# it takes about this long for omxplayer to warm up and start displaying a picture on a rpi3


# player.set_position(5)
# player.pause()


# sleep(5)

# player.set_aspect_mode('stretch')
# player.set_video_pos(0, 0, 200, 200)
# player.play()

# sleep(5)

# player.quit()
