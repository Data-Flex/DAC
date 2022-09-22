import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(2, 1000)
p.start(0)


try:
    while True:
        value = int(input())

        p.stop()
        p.start(value)
        print("{:.3}".format(3.3*value/100))

except ValueError: print("you entered not a number") 


finally:
    p.stop()
    GPIO.output(2, 0)
    GPIO.cleanup()