from djitellopy import Tello

# create and connect
# 创建Tello对象并连接
tello = Tello()
tello.connect()
tello.land()
# configure drone
# 设置无人机
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)  # forward detection only  只识别前方

tello.takeoff()

pad = tello.get_mission_pad_id()

# detect and react to pads until we see pad #1
# 发现并识别挑战卡直到看见1号挑战卡
while pad != 1:
    if pad == 3:
        print("pad 3 detected")
        tello.move_back(30)
        tello.rotate_clockwise(90)

    if pad == 4:
        print("pad 4 detected")
        tello.go_xyz_speed_mid(0,0,20,10,4)
        tello.land()

    if pad == 2:
        print("pad 2 detected")
        tello.go_xyz_speed_mid(0,1,20,10,2)

    pad = tello.get_mission_pad_id()

# graceful termination
# 安全结束程序
tello.disable_mission_pads()
tello.land()
tello.end()
