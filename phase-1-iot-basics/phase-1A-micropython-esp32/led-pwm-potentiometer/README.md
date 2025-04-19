# 🔦 LED Brightness Control using PWM & Potentiometer | ESP32 + MicroPython

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

This task demonstrates how to control the brightness of an LED using a potentiometer with PWM (Pulse Width Modulation) on the ESP32, programmed using MicroPython.

---

## 🎯 Objective

Control an LED's brightness based on the position of a potentiometer using:

- PWM signal on a GPIO pin
- Analog input from the potentiometer

---

## 🧰 Components Used

| Component                 | Quantity |
| ------------------------- | -------- |
| ESP32 Dev Board           | 1        |
| LED                       | 1        |
| 220Ω Resistor             | 1        |
| Potentiometer (10kΩ)      | 1        |
| Breadboard + Jumper Wires | 1 set    |

---

## 🔌 Circuit Diagram

        coming soon...

### 🔗 Connections:

| Component         | ESP32 Pin             |
| ----------------- | --------------------- |
| LED Anode (+)     | GPIO15 (PWM Output)   |
| LED Cathode (–)   | GND via 220Ω resistor |
| Potentiometer VCC | 3.3V                  |
| Potentiometer GND | GND                   |
| Potentiometer OUT | GPIO34 (Analog Input) |

> Schematic image will be added soon (Fritzing diagram).

---
