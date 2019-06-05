# -*- coding: GBK -*-
import pyaudio
import viVoicecloud as vv
from sjtu.audio import findDevice
import urllib.parse
import urllib.request
import serial
import serial.tools.list_ports
import RPi.GPIO
import os
import cv2

import time
import platform

cv2.namedWindow("Image") 
face_cascade = cv2.CascadeClassifier(
    '/home/pi/lesson13/haarcascades/haarcascade_frontalface_default.xml') #使用面部分类器

cap = cv2.VideoCapture(0) #摄像头的打开

ser=serial.Serial("/dev/ttyACM1", 9600,timeout=1)   #端口名称ttyACM0，波特率9600
ser1=serial.Serial("/dev/ttyACM0", 9600,timeout=1)   #端口名称ttyACM1，波特率9600
str1="1"
#ser2=serial.Serial("/dev/ttyACM1",9600,timeout)
#ser.open()
'''
ports = list(serial.tools.list_ports.comports())
for p in ports:
    #print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
'''
isLinux = 'linux' in platform.system().lower()

if isLinux:
    from gpiozero import LED


url="http://tingapi.ting.baidu.com/v1/restserver/ting?"
url += "from=webapp_music"
url += "&method=baidu.ting.search.catalogSug"
url += "&format=json"



device_in=findDevice("ac108","input")
Sample_channels=1
Sample_rate=16000
Sample_width=2
time_seconds=0.5
p=pyaudio.PyAudio()
stream=p.open(
           rate=Sample_rate,
           format=p.get_format_from_width(Sample_width),
           channels=Sample_channels,
           input=True,
           input_device_index=device_in,
           start=False)
      
vv.Login()
ASR=vv.asr()
tts=vv.tts()
tr=vv.baidu_translate()
while True:
	try:
		#接收语音信息，等待“开炮”
		ASR.SessionBegin(language='Chinese')
		stream.start_stream()
		print('***Listening...')

		status=0
		while status!=3:
			frames=stream.read(int(Sample_rate*time_seconds),exception_on_overflow=False)
			ret,status,recStatus=ASR.AudioWrite(frames)
	
		stream.stop_stream()
		print('----GetResult...')
		words=ASR.GetResult()
		ASR.SessionEnd()
		print(words)
		print (words)
		if "开炮" in words:
			
			str0 = '2'
			str3 = '0'
			ser.write(str3.encode())
			#print("发射")
			
			i = 0
			while(cap.isOpened()): 
				
				ret,img = cap.read()  #摄像头读入
				gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
				faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.15,
													  minNeighbors = 5,
													  minSize = (5,5),)  #人脸识别
				
				x1=img.shape[0]
				y1=img.shape[1]

				for(x,y,w,h) in faces:
					cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)  #在图片上画矩形
				if ret == True:
					cv2.rectangle(img,(0,0),(2,100),(0,255,0),2)       
					cv2.imshow('Image',img)
					k = cv2.waitKey(100)
					if k == ord('a') or k == ord('A'):
						break
				if len(faces)>0:
					#tts.say("发现{0}个人脸！".format(len(faces)))    #发现人脸
					print("发现{0}个人脸！".format(len(faces)))
					img_title = "./img/img"+str(i)+".png" 
					cv2.imwrite(img_title,img)                     #发现人脸的保存
					i+=1
					print(x+w/2)
					print(0.45*y1)
					print(0.55*y1)
					if ((x+w/2) >0.45*y1) and ((x+w/2)<0.55*y1):
						print(y)
						print(y1)
						print(w)
						print(x1)
						ser.write(str0.encode())  #串口通讯
						ser1.write(str1.encode())
						cv2.imwrite("caxukun.jpg",img)
						cap.release()
						cv2.destroyAllWindows()
						print("发射")
						#播放歌曲
						keywords ="SWIN-S 只因你太美" 
						keywords_encoded=urllib.parse.quote(keywords)
						print("进入")

						url+="&query="+keywords_encoded

						ref =urllib.request.urlopen(url)

						result=ref.read()
						result=result.decode()
						#print(result)

						import json
						dict1=json.loads(result)
						songid=dict1["song"][0]["songid"]

						url2="http://music.taihe.com/data/music/fmlink?"
						url2+="songIds="+songid

						ref2=urllib.request.urlopen(url2)
						result2=ref2.read()
						result2=result2.decode()
						#print(result2)

						dict2=json.loads(result2)
						#print(dict2)
						songLink=dict2["data"]["songList"][0]["songLink"]
						#print(type(dict2))

						#songLink=dict2[""]
						import vlc
						p=vlc.MediaPlayer(songLink)
						p.play()
						break
						#s
			
		else:
			vv.Logout()
			vv.Login()
	except Exception as e:
		print(e)
		print('stopped')
		time.sleep()
		vv.Logout()
		stream.close()
		p.terminate()
		#ser.close()
		break
