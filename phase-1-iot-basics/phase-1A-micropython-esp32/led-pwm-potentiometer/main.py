from machine import Pin, PWM, ADC
from time import sleep

# Initialize PWM on GPIO15 for LED
led = PWM(Pin(15), freq=1000)

# Initialize ADC on GPIO34 for potentiometer
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)  # Full range 0-3.3V
pot.width(ADC.WIDTH_10BIT)  # 0 to 1023

while True:
    pot_value = pot.read()  # Read analog value (0-1023)
    duty = int(pot_value / 1023 * 1023)  # Scale for 10-bit PWM
    led.duty(duty)
    print(f"Potentiometer: {pot_value}, PWM Duty: {duty}")
    sleep(0.05)
