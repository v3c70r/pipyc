import RPi.GPIO as GPIO
import time
import sys

class Motor:
    def __init__(self):
        self._turn_left_pin     = 15 #7
        self._turn_right_pin    = 13 #11
        self._forward_pin       = 11 #13
        self._backward_pin      = 7 #15

        self._pins = \
                [
        self._turn_left_pin,
        self._turn_right_pin,
        self._forward_pin,
        self._backward_pin,
        ]
        GPIO.setmode(GPIO.BOARD)
        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin,GPIO.LOW)
    def dispose(self):
        for pin in self._pins:
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()

    def forward_start(self):
        GPIO.setup(self._backward_pin, GPIO.LOW)
        GPIO.output(self._forward_pin, GPIO.HIGH)
    def forward_stop(self):
        GPIO.output(self._forward_pin, GPIO.LOW)

    def backward_start(self):
        GPIO.setup(self._forward_pin, GPIO.LOW)
        GPIO.output(self._backward_pin, GPIO.HIGH)
    def backward_stop(self):
        GPIO.output(self._backward_pin, GPIO.LOW)

    def turn_left_start(self):
        GPIO.setup(self._turn_right_pin, GPIO.LOW)
        GPIO.output(self._turn_left_pin, GPIO.HIGH)
    def turn_left_end(self):
        GPIO.output(self._turn_left_pin, GPIO.LOW)

    def turn_right_start(self):
        GPIO.setup(self._turn_left_pin, GPIO.LOW)
        GPIO.output(self._turn_right_pin, GPIO.HIGH)
    def turn_right_end(self):
        GPIO.output(self._turn_right_pin, GPIO.LOW)



