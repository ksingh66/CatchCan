#!/usr/bin/env python3
"""
Robot Control Utilities
"""

import time
from ros_robot_controller_sdk import Board

# Global board instance
board = None

def init_robot():
    """Initialize robot connection"""
    global board
    try:
        print("Connecting to robot...")
        board = Board("/dev/ttyACM0")
        board.enable_reception(True)
        time.sleep(1)
        print("Robot connected successfully!")
        return True
    except Exception as e:
        print(f"Failed to connect to robot: {e}")
        return False

def face_camera_up():
    """Point camera upward"""
    if board:
        print("Moving camera up...")
        board.pwm_servo_set_position(0.3, [[1, 500]])   # 500 = straight up
        board.pwm_servo_set_position(0.3, [[2, 1550]])
        time.sleep(0.5)  # Give time for movement

def face_camera_forward():
    """Point camera forward"""
    if board:
        print("Moving camera forward...")
        board.pwm_servo_set_position(0.3, [[1, 1500]])  # 1500 = forward
        board.pwm_servo_set_position(0.3, [[2, 1550]])
        time.sleep(0.5)  # Give time for movement

def drive_forward(speed):
    """Drive robot forward"""
    if board:
        board.set_motor_speed([[1, 0], [2, -speed], [3, 0], [4, speed]])  # Motor 2 is inversed

def drive_backward(speed):
    """Drive robot backward"""
    if board:
        board.set_motor_speed([[1, 0], [2, speed], [3, 0], [4, -speed]])  # Motor 2 is inversed

def stop():
    """Stop all motors"""
    if board:
        board.set_motor_speed([[1, 0], [2, 0], [3, 0], [4, 0]])

def steer_left():
    """Steer left"""
    if board:
        board.pwm_servo_set_position(0.3, [[3, 1100]])

def steer_right():
    """Steer right"""
    if board:
        board.pwm_servo_set_position(0.3, [[3, 1400]])

def steer_center():
    """Center steering"""
    if board:
        board.pwm_servo_set_position(0.3, [[3, 1250]])

def cleanup_robot():
    """Clean up robot resources"""
    global board
    if board:
        print("Cleaning up robot...")
        stop()  # Stop all motors
        face_camera_forward()  # Return camera to forward position
        board = None
