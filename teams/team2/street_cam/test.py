import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
ser = None
for p in ports:
    print(p[1])
    if "Serial" in p[1]:
        ser1 = serial.Serial(port=p[0])
    elif "Arduino" in p[1]:
        ser = serial.Serial(port=p[0])
time.sleep(10)
for i in range(5):
    print("zuo")
    ser.write("3".encode())
    time.sleep(2)
