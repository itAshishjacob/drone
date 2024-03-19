import RPi.GPIO as gpio
from time import sleep

ch1 = 11
ch2 = 12
ch3 = 15
ch4 = 16

throttle_max = 9
throttle_min = 3

max_stick_position = 9
mid_stick_position = 7
min_stick_position = 4

signal_frequency = 50


gpio.setmode(gpio.BOARD)
gpio.setup(ch1, gpio.OUT)
gpio.setup(ch2, gpio.OUT)
gpio.setup(ch3, gpio.OUT)
gpio.setup(ch4, gpio.OUT)

aileron_ch1 = gpio.PWM(ch1, signal_frequency)
aileron_ch1.start(mid_stick_position)
elevator_ch2 = gpio.PWM(ch2, signal_frequency)
elevator_ch2.start(mid_stick_position)
throttle_ch3 = gpio.PWM(ch3, signal_frequency)
throttle_ch3.start(throttle_min)
rudder_ch4 = gpio.PWM(ch4, signal_frequency)
rudder_ch4.start(mid_stick_position)

