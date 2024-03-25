import RPi.GPIO as GPIO

dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        digit=input()
        if digit == 'q':
            break
        if digit.isdigit():
            if 0<=int(digit)<=255:

                GPIO.output(dac, decimal2binary(int(digit)))
                print('u:', (3.3 / 256)*int(digit))
        elif digit != float(digit):
            print('ne 4islovoe')
        elif digit <0:
            print('<0')
        elif digit>=256:
            print('too big')
finally:
    GPIO.output(dac, 0)
    GPIO.clenaup()