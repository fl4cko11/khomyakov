import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

object=GPIO.PWM(24, 1000)

try:
    while True:
        duty=float(input('duty'))
        object.start(duty)
    
finally:
    GPIO.cleanup()