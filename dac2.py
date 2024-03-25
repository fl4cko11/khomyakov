import RPi.GPIO as GPIO
import time

dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

t=float(input('time of tri: '))

try:
    while True:
        for i in range(256):
            signal=decimal2binary(i)
            GPIO.output(dac, signal)
            time.sleep(t)
        for i in range(255, -1, -1):
            signal=decimal2binary(i)
            GPIO.output(dac, signal)
            time.sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()