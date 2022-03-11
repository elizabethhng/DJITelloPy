import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
tello.send_command_with_return('downvision 1')
frame_read = tello.get_frame_read()
# video = cv2.VideoCapture("udp://@0.0.0.0:11111?overrunnonfatal=1&fifo_size=278877")
def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    # 创建一个VideoWrite对象，存储画面至./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
    new_h = int(height / 2)
    new_w = int(width / 2)
    
    while keepRecording:
        video.write(frame_read.frame)
        frame=frame_read.frame
        new_frame = cv2.resize(frame, (new_w, new_h))
        cv2.imshow('tello', new_frame )
        time.sleep(1 / 30)

    video.release()

# we need to run the recorder in a seperate thread, otherwise blocking options
#  would prevent frames from getting added to the video
# 我们需要在另一个线程中记录画面视频文件，否则其他的阻塞操作会阻止画面记录
recorder = Thread(target=videoRecorder)
recorder.start()
time.sleep(10)
tello.send_command_with_return('command')
time.sleep(10)

tello.send_command_with_return('command')
time.sleep(10)
# tello.takeoff()
# tello.move_up(100)
# tello.rotate_counter_clockwise(360)
# tello.land()

keepRecording = False
recorder.join()
