import time, cv2, sys, os
from threading import Thread
from djitellopy import Tello


video_file="HOUSETEST.avi"
path= "C:/Users/65965/Desktop/School/FYPS2"
path_to_weights= f"{path}/yolov5/weights/v8best.pt"

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avic
    # 创建一个VideoWrite对象，存储画面至./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter( f'{path}\DJITelloPy\elizabeth\drone_video_capture\{video_file}', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
    time.sleep(5)
    while keepRecording:
        try:
            frame= cv2.cvtColor(frame_read.frame, cv2.COLOR_RGB2BGR)
            video.write(frame)
            time.sleep(1 / 30)
        except KeyboardInterrupt:
            # keepRecording = False
            sys.exit(0)
    video.release()

def yolov5():
    cmd= f"python {path}/yolov5/detect.py --weights {path_to_weights} --img 416 --conf 0.5 --source {path}\DJITelloPy\elizabeth\drone_video_capture\{video_file} --device 0 --name result_{video_file} "
    os.system(cmd)



"""Load Revit Coordinates"""
x_vector= int(sys.argv[1])
y_vector= int(sys.argv[2])
if x_vector <0:
    x_left=True
    x_vector=abs(x_vector)
else:
    x_left=False

"""Start Tello"""
tello = Tello()
tello.connect()
batt=tello.get_battery()
if int(batt)<20:
    print (" no battery", tello.get_battery())
    sys.exit(0)
print(batt)

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()
time.sleep(5)
tello.send_command_with_return("command")
time.sleep(5)
while frame_read.frame.all == 0:
    print('0')
print(frame_read.frame, f"moving by {x_vector}, {y_vector}")

recorder = Thread(target=videoRecorder)
recorder.start()

""""Ensure frame and start recording"""



"""mission pad landing"""
# tello.enable_mission_pads()
# tello.set_mission_pad_detection_direction(2) 

tello.takeoff()
time.sleep(2)

# print(tello.get_mission_pad_id())
# for i in range (0,4):
#     pad = tello.get_mission_pad_id()
#     if pad==1:
#         tello.go_xyz_speed_mid(0,0,150,10,1)
#         print("m1 found")
#         time.sleep(5)
#         break
#     print("try" , i)
# tello.move_up(100)

"""Move according to revit coordinates"""
tello.move_forward(y_vector)
time.sleep(0.1)

if x_left:
    tello.move_left(x_vector)
else:
    tello.move_right(x_vector)
time.sleep(0.5)

tello.rotate_counter_clockwise(360)
time.sleep(1)

if x_left:
    tello.move_right(x_vector)
else:
    tello.move_left(x_vector)
time.sleep(0.5)

tello.move_back(y_vector)
time.sleep(1)

"""mission pad landing"""
# pad = tello.get_mission_pad_id()
# print("mission pad ", pad)
# # tello.move_down(20)

# for i in range(1):
#     for i in range (10):
#         if pad != 1:
#             print("mission pad not found, trying")
#             time.sleep(5)
#             tello.send_command_with_return("command",5)
#             pad = tello.get_mission_pad_id()
#     print ("took ",i, " tries")
#     print("mission pad found")
#     time.sleep(1)
#     tello.go_xyz_speed_mid(0,0,20,10,1)
#     print("sleep")
#     time.sleep(5)

tello.land()
tello.disable_mission_pads()
tello.streamoff()
print(tello.get_battery())

keepRecording = False
recorder.join()
print("video saved")


yolo = Thread(target=yolov5)
yolo.start()
tello.end()

