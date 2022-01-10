import os 
video_file="avivideotest.avi"
path= "C:/Users/65965/Desktop/School/FYPS2"
path_to_weights= f"{path}/yolov5/weights/v8best.pt"

cmd= f"python {path}/yolov5/detect.py --weights {path_to_weights} --img 416 --conf 0.5 --source {path}\DJITelloPy\elizabeth\drone_video_capture\{video_file} --device 0 --name result_{video_file} "
# cmd= "python C:/Users/65965/Desktop/School/FYPS2/yolov5/detect.py --weights C:/Users/65965/Desktop/School/FYPS2/yolov5/weights/v8best.pt --img 416 --conf 0.5 --source C:/Users/65965/Desktop/School/FYPS2/avivideotest.avi --device 0"
os.system(cmd)