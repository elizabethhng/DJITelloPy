import time, cv2, sys, os
from threading import Thread
from djitellopy import Tello

x_vector = 70
y_vector = 90

"""Start Tello"""
tello = Tello()
tello.connect()
batt=tello.get_battery()
if int(batt)<20:
    print (" no battery", tello.get_battery())
    sys.exit(0)
print(batt)
time.sleep(5)
tello.send_command_with_return("command")
tello.takeoff()
# time.sleep(2)
tello.move_up(50)
tello.move_forward(y_vector)
time.sleep(0.1)

tello.move_left(x_vector)
time.sleep(0.5)

for i in range(4):
    tello.rotate_clockwise(90)
    # time.sleep(0.1)

tello.move_right(x_vector)
# time.sleep(0.5)

tello.move_back(y_vector)
time.sleep(1)

tello.land()
print(tello.get_battery())
tello.end()

