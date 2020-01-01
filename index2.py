#source https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/?fbclid=IwAR1PsT6ui4pVTWT6xjvh1a5bNQ2Pdc7JYYHbOVIJY_A4c-2c1PqNm5MarTU
import pyaudio
import numpy as np
import time
import pyautogui

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

#for i in range(int(10*44100/1024)): #go for a few seconds
for i in range(int(100*44100/1024)): #go for a few seconds
	data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
	peak=np.average(np.abs(data))*2
	bars="#"*int(50*peak/2**16)
	#print("%04d %05d %s"%(i,peak,bars))

	if (int(50*peak/2**16)>1):
		print(bars)
		#pyautogui.click(x=620, y=595)
		pyautogui.click(x=635, y=405)
		
		#time.sleep(0.6)
	time.sleep(0.2)

stream.stop_stream()
stream.close()
p.terminate()