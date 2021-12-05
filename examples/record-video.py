import time, cv2, sys
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    # 创建一个VideoWrite对象，存储画面至./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video4.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        try:
            video.write(frame_read.frame)
            time.sleep(1 / 30)
        except KeyboardInterrupt:
            keepRecording = False
            recorder.join()
            sys.exit(0)
    video.release()

# we need to run the recorder in a seperate thread, otherwise blocking options
#  would prevent frames from getting added to the video
# 我们需要在另一个线程中记录画面视频文件，否则其他的阻塞操作会阻止画面记录
recorder = Thread(target=videoRecorder)
recorder.start()

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2) 

tello.takeoff()
time.sleep(2)

print(tello.get_mission_pad_id())
for i in range (0,4):
    pad = tello.get_mission_pad_id()
    if pad==1:
        tello.go_xyz_speed_mid(0,0,100,10,1)
        print("m1 found")
        time.sleep(5)
        break

# tello.move_up(100)
tello.move_forward(50)
tello.rotate_counter_clockwise(360)
tello.move_back(55)
pad = tello.get_mission_pad_id()
# tello.move_down(20)
while pad != 1:
    time.sleep(5)
    print("mission pad not found")
    pad = tello.get_mission_pad_id()
tello.go_xyz_speed_mid(0,0,20,10,1)
time.sleep(5)
tello.disable_mission_pads()
tello.land()
tello.streamoff()
print(tello.get_battery())

keepRecording = False
recorder.join()
