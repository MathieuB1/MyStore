from common import *
from PINtrigger import *
import time
import machine

rotor_direction = 0
interrupt_pin = 0

def trigger_motor(motor, stop_pin, pin):
  global rotor_direction
  my_current_direction = rotor_direction

  pull_down_pin(motor)

  # Get the timestamp
  timeout = TIMEOUT
  start_time = time.ticks_ms()
  elaspsed_time = 0
  stop = False

  print("Will run Motor!")
  # Check if we reached the end course or sensors
  # Check if elaspsed time has been reached (watch dog)
  # Check if a pin has been triggered during motor rotation
  while not read_pin(stop_pin) and timeout >= elaspsed_time and not stop:
    pull_up_pin(motor)
    print("Motor running...")
    elaspsed_time = time.ticks_ms() - start_time
    if pin.value() == 1 or my_current_direction != rotor_direction:
      print("Stopping Motor!")
      stop = True
      time.sleep(0.2)

  print("stop pin")
  print(stop_pin)
  
  pull_down_pin(motor)


def handle_rotation(pin):
  global rotor_direction
  global interrupt_pin
  time.sleep(0.2)
  if pin.value() == 1:
    print("Interruption rotation received on pin: " + str(pin))
    rotor_direction = 1
    interrupt_pin = pin


def handle_rev_rotation(pin):
  global rotor_direction
  global interrupt_pin
  time.sleep(0.2)
  if pin.value() == 1:
    print("Interruption rev rotation received on pin: " + str(pin))
    rotor_direction = 2
    interrupt_pin = pin

# Trigger motor rotation
pin1 = machine.Pin(WATCH_PIN_1, machine.Pin.IN)
pin1.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_rotation)

# Trigger motor reverse rotation
pin2 = machine.Pin(WATCH_PIN_2, machine.Pin.IN)
pin2.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_rev_rotation)

while True:
  if rotor_direction == 1:
    print('direction 1')
    trigger_motor(RELAY_1, END_COURSE_1, interrupt_pin)
    rotor_direction = 0
  elif rotor_direction == 2:
    print('direction 2')
    print(interrupt_pin)
    trigger_motor(RELAY_2, END_COURSE_2, interrupt_pin)
    rotor_direction = 0
  else:
    time.sleep(0.2)