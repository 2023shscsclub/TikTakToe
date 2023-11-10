import Arm_Lib


Arm = Arm_Lib.Arm_Device()
Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 0, 600)
