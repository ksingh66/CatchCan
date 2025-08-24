import time
# Connect to robot
from ros_robot_controller_sdk import Board
board = Board("/dev/ttyACM0")
board.enable_reception(True)
time.sleep(1)

def face_camera_up():
    board.pwm_servo_set_position(0.3, [[1, 500]])  # (time,[[motorid, position]]) 500 = straight up

def face_camera_forward():
    board.pwm_servo_set_position(0.3, [[1, 1500]])  # (time,[[motorid, position]]) 1500 = forward

def drive_forward(duration, speed):
    board.set_motor_speed([[1, 0], [2, -speed], [3, 0], [4, speed]])  # Motor 2 is inversed
    time.sleep(duration)
    stop()

def drive_backward(duration, speed):
    board.set_motor_speed([[1, 0], [2, speed], [3, 0], [4, -speed]])  # Motor 2 is inversed
    time.sleep(duration)
    stop()

def stop():
    board.set_motor_speed([[1, 0], [2, 0], [3, 0], [4, 0]])

def steer_right():
    board.pwm_servo_set_position(0.3, [[3, 800]])
   
def steer_left():
    board.pwm_servo_set_position(0.3, [[3, 1400]])

steer_center():
    board.pwm_servo_set_position(0.3, [[3, 1100]])

drive_forward(4, 2)
drive_backward(4, 2)
stop()


time.sleep(0.5)
board.enable_reception(False)  # Stop the recv thread
time.sleep(0.5)
board.port.close()  # Explicitly close connection
