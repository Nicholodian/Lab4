from hal import hal_input_switch as switch
from PiDemo import blink_led
from time import sleep, time
from hal import hal_led as led


switch.init()
led.init()
while True:
    if switch.read_slide_switch():
        blink_led(0.1)
    else:
        t_end = time() + 5
        while time() < t_end:
            blink_led(0.05)
        while True:
            sleep(1)

