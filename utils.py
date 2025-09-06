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


def set_steering_angle(strength):
    """
    Set steering angle based on strength
    strength: -1.0 (full left) to +1.0 (full right)
    """
    if board:
        # Map strength (-1.0 to +1.0) to servo range (800 to 1400)
        center_position = 1100
        max_range = 300  # Distance from center to either extreme
        
        servo_position = center_position + (strength * max_range)
        
        # Clamp to safe range
        servo_position = max(center_position - max_range, min(center_position+max_range, servo_position))
        servo_position = int(servo_position)
        
        board.pwm_servo_set_position(0.3, [[1, servo_position]])


def cleanup_robot():
    """Clean up robot resources"""
    global board
    if board:
        print("Cleaning up robot...")
        stop()  # Stop all motors
        steer_center()
        board = None
