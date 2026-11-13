"""Droplet dispenser control loop.

The controller exposes a small serial protocol used by the bench planner.
Volumes are expressed in microliters and converted through the calibration
table loaded from ``calibration.json``.
"""

import json
import time

from machine import Pin, PWM

STEP_PIN = Pin(2, Pin.OUT)
DIR_PIN = Pin(3, Pin.OUT)
HOME_PIN = Pin(4, Pin.IN, Pin.PULL_UP)
PUMP_PWM = PWM(Pin(5))


def load_calibration(path="calibration.json"):
    with open(path) as fh:
        return json.load(fh)


def step_pulse(delay_us=800):
    STEP_PIN.high()
    time.sleep_us(2)
    STEP_PIN.low()
    time.sleep_us(delay_us)


def dispense(volume_ul, calibration):
    steps = round(volume_ul * calibration["steps_per_ul"])
    DIR_PIN.high()
    for _ in range(steps):
        step_pulse()


def run_plate(volumes, calibration):
    for index, volume in enumerate(volumes):
        dispense(volume, calibration)
        print("well", index + 1, "volume", volume)
    print("plate complete")


if __name__ == "__main__":
    calibration = load_calibration()
    run_plate([5, 10, 25, 50], calibration)
