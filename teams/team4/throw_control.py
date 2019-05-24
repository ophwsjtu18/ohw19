import serial
import serial.tools.list_ports
import time
import urllib.request
import re


def movement(lu,rd): #input:left_up and right_down
    # x and y
    x=640
    y=480
    shift = 10
    center_dot = [(lu[0]+rd[0])/2,(lu[1]+rd[1])/2]
    if center_dot[0]>x/2+shift:
        if center_dot[1]>y/2+shift: #right_up
            return 'p'
        elif y/2-shift<center_dot[1]<y/2+shift: #right
            return 'd'
        else: #right_down
            return 'l'
    elif center_dot[0]<x/2-shift:
        if center_dot[1]>y/2+shift: #left_up
            return 'o'
        elif y/2-shift<center_dot[1]<y/2+shift: #left
            return 'a'
        else: #left_down
            return 'k'
    else:
        if center_dot[1]>y/2+shift: #up
            return 'w'
        elif y/2-shift<center_dot[1]<y/2+shift: #stop
            return
        else: #down
            return 's'

def crawler(url):
    rq = urllib.request.Request(url)
    rq.add_header("user-agent", "mozilla/5.0")
    webSourceCode = urllib.request.urlopen(rq).read().decode("utf-8", "ignore")
    contentRe = re.compile(r'<p>(.*?)</p>')
    content = contentRe.findall(webSourceCode)
    for c in content:
        print(c)
    return content

def run():
    action = "empty"
    while True:
        url = "https://www.ittime.com.cn/news/zixun.shtml"
        dot_list = crawler(url)
        action = movement(dot_list[0],dot_list[1])
        ser.write(action.encode()) #output to arduino
        time.sleep(1)



print ('Program begin!')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
        ser=serial.Serial(port=p[0])
    else :
        print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
ser = serial.Serial(port = '/dev/cu.wchusbserial14430')
#wait 2 seconds for arduino board restart
time.sleep(2)
run()