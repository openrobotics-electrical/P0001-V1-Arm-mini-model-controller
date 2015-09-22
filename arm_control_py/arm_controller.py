import serial
import numpy as np
import time
import subprocess
from Servo import *

proc = subprocess.Popen("ls /dev/tty*usb*", stdout = subprocess.PIPE, shell = True)
out, err = proc.communicate()
usb_list = out.split("\n")
print("USBS: "+out)
for usb in usb_list:
    try:
        if find_servos(USB2Dynamixel_Device(usb, 57600)):
            servos = find_servos(USB2Dynamixel_Device(usb, 57600))
            if len(servos) == 2:
                global upper_arm_dyn
                global upper_arm_servo
                global shoulder_servo
                upper_arm_dyn = USB2Dynamixel_Device(usb)
                upper_arm_servo = Robotis_Servo(upper_arm_dyn, servos[0])
                shoulder_servo = Robotis_Servo(upper_arm_dyn, servos[1])
                print("ARM DYN: "+usb)

        elif find_servos(USB2Dynamixel_Device(usb, 1000000)):
            servos = find_servos(USB2Dynamixel_Device(usb, 1000000))
            if len(servos) == 2:
                global grasper_dyn
                global wrist_servo
                global claw_servo
                grasper_dyn = USB2Dynamixel_Device( usb , 1000000)
                wrist_servo = Robotis_Servo( grasper_dyn, servos[1] )
                claw_servo = Robotis_Servo( grasper_dyn, servos[0])
                print("GRASPER DYN: "+usb)
        else:
            print("Hello2")
            continue
    except:
        continue
# Serial init
mots = [None, None, None, None, None, None]
mots[4] = wrist_servo
mots[5] = claw_servo

ardSer = serial.Serial(10,timeout=1)  # 9600,8,N,1
print("Connected to " + ardSer.name)

# Motor angle mapping and constants

#From Arduino code:
#const int shPivot = A0;  //Shoulder yaw pivot //Higher is right, 900-200, mid 520
#const int shBase = A1; //Shoulder up/down joint //Higher is up, 700-300, mid 500
#const int elPivot = A2; //Elbow yaw pivot //Higher is right, 900-200, mid 520
#const int elBase = A3; //Elbow up/down pivot //Higher is down, 750-350, mid 500
#const int wrist = A4; //Wrist rotation //Higher is CCW, 0-1023, mid 510
#const int handButt = 2; //Gripper button //1 is close, 0 is open

armPosMap = [[200, 520, 850],  # Shoulder yaw
             [350, 520, 650],  # Shoulder joint
             [200, 520, 875],  # Elbow yaw pivot
             [370, 520, 700],  # Elbow joint
             [0, 530, 1023],  # Wrist
             [0,0.5, 1]]  # Gripper

angMap = [[-90, 0, 90],  # Shoulder yaw
          [-45, 0, 60],  # Shoulder joint
          [-90, 0, 90],  # Elbow yaw pivot
          [45, 0, -60],  # Elbow joint
          [-135, 0, 125],  # Wrist
          [0,45, 90]]  # Gripper


# TODO Motor port array definition
mots = range(6)

while True:
    time.sleep(.01)
    print(ardSer.inWaiting()) #debug

    # Not enough characters to make command string
    if ardSer.inWaiting() < 60:
        continue

    # Parse serial into array of arm positions
    serDat = (ardSer.read(ardSer.inWaiting()))
    print(serDat)
    serDat = str(serDat)
    print(serDat)
    serDat = serDat[0:serDat.rfind(";")+1]
    print(serDat)
    serDat = serDat[serDat.rfind(";", 0, len(serDat)-1)+1:-1]
    print(serDat)
    armDat = serDat.split()
    while "" in armDat: armDat.remove("")
    armDat = [int(x) for x in armDat]
    print(armDat)


    # Write motor angles
    for i in range(6):
        ang = np.interp(armDat, armPosMap[i], angMap[i])[i]
        if mots[i]:
            port = mots[i]
            port.move_angle(ang)
        print("{}: {} => {:.4f}".format(port, armDat[i], ang))  # debug

    # if armDat[5]:
    #     # motor.write(gripClose, mots[6])
    #     print("Hand close")  # debug
    #     pass
    # else:
    #     pass
    #     # motor.write(gripOpen, mots[6])
    #     print("Hand open")  # debug