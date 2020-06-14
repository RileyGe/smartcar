import RPi.GPIO as GPIO
import time

front_left_plus = 13
front_left_minus = 6
front_right_plus = 26
front_right_minus = 19

back_left_plus = 16
back_left_minus = 12
back_right_plus = 20
back_right_minus = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(front_right_minus, GPIO.OUT)
GPIO.setup(front_right_plus, GPIO.OUT)
GPIO.setup(front_left_minus, GPIO.OUT)
GPIO.setup(front_left_plus, GPIO.OUT)
GPIO.setup(back_right_minus, GPIO.OUT)
GPIO.setup(back_right_plus, GPIO.OUT)
GPIO.setup(back_left_minus, GPIO.OUT)
GPIO.setup(back_left_plus, GPIO.OUT)

 
# while True: 
GPIO.output(front_left_minus, GPIO.HIGH)
GPIO.output(front_left_plus, GPIO.LOW)
GPIO.output(front_right_minus, GPIO.HIGH)
GPIO.output(front_right_plus, GPIO.LOW)
GPIO.output(back_left_minus, GPIO.HIGH)
GPIO.output(back_left_plus, GPIO.LOW)
GPIO.output(back_right_minus, GPIO.HIGH)
GPIO.output(back_right_plus, GPIO.LOW)
time.sleep(2)
GPIO.output(front_left_minus, GPIO.LOW)
GPIO.output(front_left_plus, GPIO.LOW)
GPIO.output(front_right_minus, GPIO.LOW)
GPIO.output(front_right_plus, GPIO.LOW)
GPIO.output(back_left_minus, GPIO.LOW)
GPIO.output(back_left_plus, GPIO.LOW)
GPIO.output(back_right_minus, GPIO.LOW)
GPIO.output(back_right_plus, GPIO.LOW)
