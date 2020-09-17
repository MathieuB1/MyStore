import machine
import time
from common import *

# For Relays
def pull_down_pin(pin):
  led = machine.Pin(pin, machine.Pin.PULL_DOWN)

def pull_up_pin(pin,):
  led = machine.Pin(pin, machine.Pin.PULL_UP)

# Read activated Pins
def read_pin(pin, threshold=4090):
  adc = machine.ADC(machine.Pin(pin))  
  value = adc.read()
  return True if value > threshold else False
