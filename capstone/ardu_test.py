from img_serial_v03 import *
from serial_test_v01 import *
import time

port = 'COM12' #변동가능
ard = serial.Serial(port, 9600)
k = 0

while k < 30:
    k += 1
    interact_ser('d', ard)
    interact_ser('2', ard)
    interact_ser('0', ard)
    interact_ser('0', ard)
    interact_ser('`', ard)
    interact_ser('l', ard)
    interact_ser('2', ard)
    interact_ser('0', ard)
    interact_ser('0', ard)
    interact_ser('`', ard)
    interact_ser('r', ard)
    interact_ser('2', ard)
    interact_ser('0', ard)
    interact_ser('0', ard)
    interact_ser('`', ard)

ard.close()