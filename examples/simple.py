from djitellopy import Tello
import time, cv2, sys, os, math
from threading import Thread

def rotate():
    for i in range(4):
        tello.rotate_clockwise(90)
        time.sleep(0.1)
tello = Tello()

tello.connect()
tello.takeoff()

# tello.query_speed()
# tello.move_left(100)
# tello.set_speed(100)
# tello.rotate_clockwise(360)
# tello.send_rc_control(0,0,0,1)
# tello.move_forward(100)
# tello.set_speed(10)
# tello.rotate_clockwise(360)
keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()
print('initialising frame_read')
time.sleep(5)
tello.send_command_with_return("command")
time.sleep(5)
print(frame_read.frame, f"moving by {d1}, {d2}")

recorder = Thread(target=videoRecorder)
recorder.start()

""""takeoff"""
tello.takeoff()
time.sleep(1)

"""Move according to coordinates"""

rotate()

"""Land Tello"""
tello.land()
# tello.disable_mission_pads()
tello.streamoff()
print(tello.get_battery())

"""Stop Recording"""
keepRecording = False
recorder.join()
print("video saved")



tello.land()
