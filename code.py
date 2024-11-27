from gpiozero import LED, Button, AngularServo, Buzzer
from guizero import App, Slider, PushButton, Text
from tkgpio import TkCircuit
from enum import Enum
import time

# Configuration for TkCircuit visualization (Uncomment them if we you want to see Software Visualized)
# configuration = {
#     "width": 800,
#     "height": 600,
#     "leds": [
#         {"pin": 17, "name": "On LED", "x": 50, "y": 50},
#         {"pin": 27, "name": "Emergency LED", "x": 150, "y": 50}
#     ],
#     "buttons": [
#         {"pin": 22, "name": "Start Button", "x": 50, "y": 150},
#         {"pin": 23, "name": "Reset Button", "x": 150, "y": 150}
#     ],
#     "buzzers": [
#         {"pin": 24, "name": "Buzzer", "x": 50, "y": 250}
#     ],
#     "servos": [
#         {"pin": 18, "name": "Servo Motor", "x": 150, "y": 250, "min_angle": 0, "max_angle": 180}
#     ]
# }
# circuit = TkCircuit(configuration)
# @circuit.run

# Main function to control the states
def main():
    class State(Enum):
        idle = 1
        OnEntry_MonitorTemp = 3
        OnStay_MonitorTemp = 4
        OnEntry_TempHigh = 5
        OnStay_TempHigh = 6
        OnEntry_Emergency = 7
        OnStay_Emergency = 8

    # GPIO Setup
    on_led = LED(17)
    emergency_led = LED(27)
    start_button = Button(22)
    reset_button = Button(23)
    buzzer = Buzzer(24)
    servo = AngularServo(18, min_angle=0, max_angle=180)

    current = State.idle
    start_time = time.time()
    temperature = 0 

    def update_temperature(value):
        nonlocal temperature
        temperature = int(value)

    def start_monitoring():
        nonlocal current
        current = State.OnEntry_MonitorTemp

    def reset_system():
        nonlocal current
        current = State.idle

    # Detect if the hardware/software buttons are pressed 
    start_button.when_pressed = start_monitoring
    reset_button.when_pressed = reset_system

    while True:
        print(f"Current State : {current.name}")

        if current == State.idle:
            
            on_led.off()
            emergency_led.off()
            buzzer.off()
            servo.angle = 0
            
            if time.time() - start_time >= 10:
                current = State.OnEntry_MonitorTemp
                start_time = time.time()
            time.sleep(0.1)

        elif current == State.OnEntry_MonitorTemp:
            on_led.on()
            current = State.OnStay_MonitorTemp

        elif current == State.OnStay_MonitorTemp:
            print(f"Temperature: {temperature}")

            if 30 < temperature < 40:
                current = State.OnEntry_TempHigh
            elif temperature >= 40:
                current = State.OnEntry_Emergency

        elif current == State.OnEntry_TempHigh:
            servo.angle = 90
            on_led.on()
            emergency_led.off()
            buzzer.off()
            current = State.OnStay_TempHigh

        elif current == State.OnStay_TempHigh:
            print(f"Temperature: {temperature}")

            if temperature >= 40:
                current = State.OnEntry_Emergency
            elif temperature <=10:
                current = State.idle
            if reset_button.is_pressed:
                current = State.idle

        elif current == State.OnEntry_Emergency:
            emergency_led.on()
            buzzer.on()
            servo.angle = 180
            current = State.OnStay_Emergency

        elif current == State.OnStay_Emergency:
            if temperature < 40:
                current = State.OnEntry_TempHigh
            if reset_button.is_pressed:
                current = State.idle

        time.sleep(0.1)

