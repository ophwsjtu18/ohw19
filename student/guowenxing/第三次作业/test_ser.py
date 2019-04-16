import serial
import time

port = serial.Serial(port = "/dev/ttyUSB0")
time.sleep(1)
for i in range(28):
    port.write(str(i).encode())
    time.sleep(1)
    print(i)

