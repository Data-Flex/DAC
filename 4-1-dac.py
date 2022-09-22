import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

for i in dac: GPIO.setup(i, GPIO.OUT)

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

try:
    not_q = True
    while not_q:
        c = input()
        if c == 'q':
            not_q = False
        elif float(c)//1 != float(c): print("you entered not an integer number")
        elif int(c) < 0: print("entered number is below zero")
        elif int(c) > 255: print("entered number can not be converted to an octal number")   
        else:
            value = int(c)
            binlist = decimal2binary(value)
            for i in range(len(dac)): GPIO.output(dac[i], binlist[i])
            print("{:.3}".format(3.3 * value / 256))

except ValueError: print("you entered not a number") 


finally:
    for i in dac: GPIO.output(i, 0)
    GPIO.cleanup()    