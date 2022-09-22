import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

for i in dac: GPIO.setup(i, GPIO.OUT)

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

try:
    T = float(input())
    for k in range(1000):
        for j in range(256):
            binlist = dec2bin(j)
            for i in range(len(dac)): GPIO.output(dac[i], binlist[i])
            time.sleep(T/1024)
        for j in range(254, 0, -1):
            binlist = dec2bin(j)
            for i in range(len(dac)): GPIO.output(dac[i], binlist[i])
            time.sleep(T/1024)


except ValueError: print("you entered not a number") 


finally:
    for i in dac: GPIO.output(i, 0)
    GPIO.cleanup()