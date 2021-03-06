# Write your code here :-)
import board
import digitalio
import time

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
led.value = True

while True:
    print('Button value is ', buttonA.value)
    led.value = False
    if buttonA.value == True:
        print('Button value is ', buttonA.value)
        led.value = True
        while buttonA.value == True:
            print('Waiting for you to let go....')
            time.sleep(0.1)
    time.sleep(0.1)
