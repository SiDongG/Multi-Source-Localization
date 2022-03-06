from os.path import dirname, join as pjoin
import time
import io
import random
from time import sleep
from scipy.io import wavfile
import scipy.io
import numpy as np
import os
import csv
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

fs=16000;
print (os.path.exists("matlab.mat"))
data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
wav_fname = pjoin(data_dir, 'output.wav')
samplerate, data1 = wavfile.read('channel_0.wav')
samplerate, data2 = wavfile.read('channel_1.wav')
samplerate, data3 = wavfile.read('channel_2.wav')
samplerate, data4 = wavfile.read('channel_3.wav')
samplerate, data5 = wavfile.read('channel_4.wav')
samplerate, data6 = wavfile.read('channel_5.wav')
samplerate, data7 = wavfile.read('channel_6.wav')
samplerate, data8 = wavfile.read('channel_7.wav')

print('1')

#cwd = os.getcwd()  
#files = os.listdir(cwd) 
#print("Files in %r: %s" % (cwd, files))

#print(mat['sig'])

#print(total)
#print(len(data))
#print(len(data[0]))
mic1=data1
mic2=data2
mic3=data3
mic4=data4
mic5=data5
mic6=data6
mic7=data7
mic8=data8

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(np.arange(len(mic1)), mic1)
axs[0, 0].set_title('Channel1')
axs[0, 1].plot(np.arange(len(mic2)), mic2, 'tab:orange')
axs[0, 1].set_title('Channel2')
axs[1, 0].plot(np.arange(len(mic3)), mic3, 'tab:green')
axs[1, 0].set_title('Channel3')
axs[1, 1].plot(np.arange(len(mic7)), mic7, 'tab:red')
axs[1, 1].set_title('Channel7')
plt.show()

cor11=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic1)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic1)))
xcor11=abs(np.fft.fftshift(np.fft.ifft(cor11)))
cor12=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic2)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic2)))
xcor12=abs(np.fft.fftshift(np.fft.ifft(cor12)))
cor13=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic3)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic3)))
xcor13=abs(np.fft.fftshift(np.fft.ifft(cor13)))
cor14=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic4)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic4)))
xcor14=abs(np.fft.fftshift(np.fft.ifft(cor14)))
cor15=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic5)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic5)))
xcor15=abs(np.fft.fftshift(np.fft.ifft(cor15)))
cor16=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic6)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic6)))
xcor16=abs(np.fft.fftshift(np.fft.ifft(cor16)))
cor17=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic7)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic7)))
xcor17=abs(np.fft.fftshift(np.fft.ifft(cor17)))
cor18=np.divide(np.fft.fft(mic1)*np.conj(np.fft.fft(mic8)),abs(np.fft.fft(mic1))*abs(np.fft.fft(mic8)))
xcor18=abs(np.fft.fftshift(np.fft.ifft(cor18)))

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(np.arange(len(xcor12)), xcor12)
axs[0, 0].set_title('xcor12')
axs[0, 1].plot(np.arange(len(xcor13)), xcor13, 'tab:orange')
axs[0, 1].set_title('xcor13')
axs[1, 0].plot(np.arange(len(xcor16)), xcor16, 'tab:green')
axs[1, 0].set_title('xcor16')
axs[1, 1].plot(np.arange(len(xcor17)), xcor17, 'tab:red')
axs[1, 1].set_title('xcor17')
plt.show()

Peak=[0,0,0,0,0,0,0,0]
Estimation=[0,0,0,0,0,0,0,0]
Index=[0,0,0,0,0,0,0,0]

for i in range(0,len(xcor12)-1):
    if xcor11[i]>Peak[7]:
        Estimation[7]=i-0.1*fs
        Index[7]=[i]
        Peak[7]=xcor11[i]
    if xcor12[i]>Peak[0]:
        Estimation[0]=i-0.1*fs
        Index[0]=[i]
        Peak[0]=xcor12[i]
    if xcor13[i]>Peak[1]:
        Estimation[1]=i-0.1*fs
        Index[1]=[i]
        Peak[1]=xcor13[i]
    if xcor14[i]>Peak[2]:
        Estimation[2]=i-0.1*fs
        Index[2]=[i]
        Peak[2]=xcor14[i]
    if xcor15[i]>Peak[3]:
        Estimation[3]=i-0.1*fs
        Index[3]=[i]
        Peak[3]=xcor15[i]
    if xcor16[i]>Peak[4]:
        Estimation[4]=i-0.1*fs
        Index[4]=[i]
        Peak[4]=xcor16[i]
    if xcor17[i]>Peak[5]:
        Estimation[5]=i-0.1*fs
        Index[5]=[i]
        Peak[5]=xcor17[i]
    if xcor18[i]>Peak[6]:
        Estimation[6]=i-0.1*fs
        Index[6]=[i]
        Peak[6]=xcor18[i]

Estimation=np.divide(Estimation,fs)
Estimation_norm=np.subtract(Estimation,Estimation[7]*np.ones(8))
Est_distance=Estimation_norm*340

d12=Est_distance[0]
d13=Est_distance[1]
d14=Est_distance[2]
d15=Est_distance[3]
d16=Est_distance[4]
d17=Est_distance[5]
d18=Est_distance[6]

def Outlier(a1,a2,a3,a4):
    average=(a1+a2+a3+a4)/4
    if abs(a1-average)>10:
        Estimation=(a2+a3+a4)/3
    elif abs(a2-average)>10:
        Estimation=(a1+a3+a4)/3
    elif abs(a3-average)>10:
        Estimation=(a2+a1+a4)/3
    elif abs(a4-average)>10:
        Estimation=(a2+a3+a1)/3
    else:
        Estimation=average
    return Estimation

if d12>0.0383:
    d12=0.0383
if d13>0.0383:
    d13=0.0383
if d14>0.0383:
    d14=0.0383
if d15>0.0383:
    d15=0.0383
if d16>0.0383:
    d16=0.0383
if d17>0.0383:
    d17=0.0383
if d18>0.0383:
    d18=0.0383

if d14>=0 and d15>=0 and d12<=0 and d17<=0:
    theta2=180*math.acos(abs(d12)/0.0383)/math.pi-5.3637
    theta4=71.7874-180*math.acos(abs(d14)/0.0383)/math.pi
    theta5=180*math.acos(abs(d15)/0.0383)/math.pi+20.3512
    theta7=180-82.5-180*math.acos(abs(d17)/0.0383)/math.pi
    Estimation=Outlier(theta2,theta4,theta5,theta7)
elif d13>=0 and d14>=0 and d18<=0 and d16<=0:
    theta4=180*math.acos(abs(d14)/0.0383)/math.pi+71.7874
    theta3=90-180*math.acos(abs(d13)/0.0383)/math.pi+33.217
    theta6=180-180*math.acos(abs(d16)/0.0383)/math.pi-31.07149
    theta8=math.acos(abs(d18)/0.0383)/math.pi+46.06855
    Estimation=Outlier(theta3,theta4,theta6,theta8)
elif d12>=0 and d13>=0 and d15<=0 and d17<=0:
    theta2=180-180*math.acos(abs(d12)/0.0383)/math.pi-5.3637
    theta3=180-56.78296+180*math.acos(abs(d13)/0.0383)/math.pi
    theta5=180-math.acos(abs(d15)/0.0383)/math.pi+20.35119
    theta7=90+math.acos(abs(d17)/0.0383)/math.pi
    Estimation=Outlier(theta2,theta3,theta5,theta7)
elif d15>=0 and d16>=0 and d13<=0 and d18<=0:
    theta5=20.35119-math.acos(abs(d15)/0.0383)/math.pi
    theta6=-31.07149+math.acos(abs(d16)/0.0383)/math.pi
    theta3=math.acos(abs(d13)/0.0383)/math.pi-56.78296
    theta8=46.06855-math.acos(abs(d18)/0.0383)/math.pi
    Estimation=Outlier(theta6,theta3,theta5,theta8)
elif d16>=0 and d17>=0 and d12<=0 and d14<=0
    theta6=-31.07149-math.acos(abs(d16)/0.0383)/math.pi
    theta7=-82.49829+math.acos(abs(d17)/0.0383)/math.pi
    theta2=-math.acos(abs(d12)/0.0383)/math.pi-5.36374
    theta4=71.7874+math.acos(abs(d14)/0.0383)/math.pi-180
    Estimation=Outlier(theta6,theta7,theta2,theta4)
elif d17>=0 and d18>=0 and d13<=0 and d15<=0
    theta7=-82.49829-math.acos(abs(d17)/0.0383)/math.pi
    theta8=46.06855+math.acos(abs(d18)/0.0383)/math.pi-180
    theta3=-math.acos(abs(d13)/0.0383)/math.pi-56.78296
    theta5=20.35119+,math.acos(abs(d15)/0.0383)/math.pi-180
    Estimation=Outlier(theta8,theta7,theta3,theta5)
elif d12>=0 and d18>=0 and d14<=0 and d16<=0
    theta2=math.acos(abs(d12)/0.0383)/math.pi-5.36374-180
    theta8=46.06855-math.acos(abs(d18)/0.0383)/math.pi-180
    theta4=71.7874-math.acos(abs(d14)/0.0383)/math.pi-180
    theta6=math.acos(abs(d16)/0.0383)/math.pi-31.07149-180
    Estimation=Outlier(theta8,theta2,theta4,theta6)
print(Estimation)
