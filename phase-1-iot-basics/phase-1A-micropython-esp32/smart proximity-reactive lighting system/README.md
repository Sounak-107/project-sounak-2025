# 📡 LED Brightness Control using Ultrasonic Sensor | ESP32 + MicroPython

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

This MicroPython project uses an **HC-SR04 ultrasonic distance sensor** to control the **brightness of an LED** via PWM on an ESP32. The closer an object is, the brighter the LED glows!

---

## 🎯 Objective

- Measure distance using an ultrasonic sensor.
- Dynamically control LED brightness using PWM.
- Brightness increases as distance decreases.

---

## 🧰 Components Used

| Component                 | Quantity |
| ------------------------- | -------- |
| ESP32 Dev Board           | 1        |
| HC-SR04 Ultrasonic Sensor | 1        |
| LED                       | 1        |
| 220Ω Resistor             | 1        |
| Breadboard + Jumper Wires | 1 set    |

---

## 🔌 Pin Configuration

| Module          | ESP32 GPIO            |
| --------------- | --------------------- |
| HC-SR04 Trig    | GPIO5                 |
| HC-SR04 Echo    | GPIO18                |
| LED Anode (+)   | GPIO15 (PWM)          |
| LED Cathode (–) | GND via 220Ω resistor |

---
