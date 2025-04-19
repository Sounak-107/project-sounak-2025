# Copyright 2025 Sounak Banerjee
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import machine
import time

# Pin configuration
TRIG_PIN = 5
ECHO_PIN = 18
LED_PIN = 15  # PWM LED pin

# Initialize pins
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)
led = machine.PWM(machine.Pin(LED_PIN), freq=1000)

# Helper: Get distance from ultrasonic sensor
def get_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duration = machine.time_pulse_us(echo, 1, 30000)  # 30ms timeout
    if duration < 0:
        return None

    distance_cm = (duration / 2) / 29.15
    return distance_cm

# Helper: Map value from one range to another
def map_range(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Main loop
while True:
    dist = get_distance()

    if dist:
        print("Distance: {:.2f} cm".format(dist))

        # Clamp distance to a useful range, say 5 to 200 cm
        dist = max(5, min(200, dist))

        # Map 5–50 cm to 1023–0 brightness (closer = brighter)
        brightness = map_range(dist, 5, 200, 1023, 0)
        led.duty(brightness)

    else:
        print("Out of range")
        led.duty(0)  # Turn off LED if out of range

    time.sleep(0.2)

