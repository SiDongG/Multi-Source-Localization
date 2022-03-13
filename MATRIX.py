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
from statistics import variance
from statistics import mean

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
    if a1==360:
        var0=variance((a2,a3,a4))
        var1=variance((a2,a3))
        var2=variance((a2,a4))
        var3=variance((a3,a4))
        Minimum=min(var0,var1,var2,var3)
        if var0<10:
            Estimation=(a2+a3+a4)/3
        else:
            if Minimum==var0:
                Estimation=(a2+a3+a4)/3
            elif Minimum==var1:
                Estimation=(a2+a3)/2
            elif Minimum==var2:
                Estimation=(a2+a4)/2
            else:
                Estimation=(a3+a4)/2
        State=1
    elif a2==360:
         var0=variance((a1,a3,a4))
         var1=variance((a1,a3))
         var2=variance((a1,a4))
         var3=variance((a3,a4))
         Minimum=min(var0,var1,var2,var3)
         if var0<10:
             Estimation=(a1+a3+a4)/3
         else:
             if Minimum==var0:
                 Estimation=(a1+a3+a4)/3
             elif Minimum==var1:
                 Estimation=(a1+a3)/2
             elif Minimum==var2:
                 Estimation=(a1+a4)/2
             else:
                 Estimation=(a3+a4)/2
         State=1
    elif a3==360:
           var0=variance((a1,a2,a4))
           var1=variance((a1,a2))
           var2=variance((a1,a4))
           var3=variance((a2,a4))
           Minimum=min(var0,var1,var2,var3)
           if var0<10:
                Estimation=(a1+a2+a4)/3
           else:
                if Minimum==var0:
                     Estimation=(a1+a2+a4)/3
                elif Minimum==var1:
                     Estimation=(a1+a2)/2
                elif Minimum==var2:
                     Estimation=(a1+a4)/2
                else:
                     Estimation=(a2+a4)/2
           State=1
    elif a4==360:
            var0=variance((a1,a2,a3))
            var1=variance((a1,a2))
            var2=variance((a1,a3))
            var3=variance((a2,a3))
            Minimum=min(var0,var1,var2,var3)
            if var0<10:
                Estimation=(a1+a2+a3)/3
            else:
                if Minimum==var0:
                    Estimation=(a1+a2+a3)/3
                elif Minimum==var1:
                    Estimation=(a1+a2)/2
                elif Minimum==var2:
                    Estimation=(a1+a3)/2
                else:
                    Estimation=(a2+a3)/2
            State=1
    else:
        State=0

    if State==0:
        var0=variance((a1,a2,a3,a4))
        var1=variance((a1,a2,a3))
        var2=variance((a1,a2,a4))
        var3=variance((a1,a3,a4))
        var4=variance((a2,a3,a4))
        Min=min(var0,var1,var2,var3,var4)
        if var0<20:
            Estimation=mean((a1,a2,a3,a4))
        else:
            if Min==var1:
                Estimation=(a1+a2+a3)/3
            elif Min==var2:
                Estimation=(a1+a2+a4)/3
            elif Min==var3:
                Estimation=(a1+a3+a4)/3
            elif Min==var4:
                Estimation=(a2+a3+a4)/3
            else:
                Estimation=(a1+a2+a3+a4)/4
    return Estimation 

def Sanity(a1,a2,a3,a4):
    return 0



if d14>=0 and d15>=0 and d12<=0 and d17<=0:
    try:
        theta2=180*math.acos(abs(d12)/0.0383)/math.pi-5.3637
    except:
        theta2=360
    try:
        theta4=71.7874-180*math.acos(abs(d14)/0.0383)/math.pi
    except:
        theta4=360
    try:
        theta5=180*math.acos(abs(d15)/0.0383)/math.pi+20.3512
    except:
        theta5=360
    try:
        theta7=180-82.5-180*math.acos(abs(d17)/0.0383)/math.pi
    except:
        theta7=360
    Estimation=Outlier(theta2,theta4,theta5,theta7)
elif d13>=0 and d14>=0 and d18<=0 and d16<=0:
    try:
        theta4=180*math.acos(abs(d14)/0.0383)/math.pi+71.7874
    except:
        theta4=360
    try: 
        theta3=90-180*math.acos(abs(d13)/0.0383)/math.pi+33.217
    except:
        theta3=360
    try:
        theta6=180-180*math.acos(abs(d16)/0.0383)/math.pi-31.07149
    except:
        theta6=360
    try:
        theta8=180*math.acos(abs(d18)/0.0383)/math.pi+46.06855
    except:
        theta8=360
    Estimation=Outlier(theta3,theta4,theta6,theta8)
elif d12>=0 and d13>=0 and d15<=0 and d17<=0:
    try:
        theta2=180-180*math.acos(abs(d12)/0.0383)/math.pi-5.3637
    except:
        theta2=360
    try:
        theta3=180-56.78296+180*math.acos(abs(d13)/0.0383)/math.pi
    except:
        theta3=360
    try:
        theta5=180-math.acos(abs(d15)/0.0383)/math.pi+20.35119
    except:
        theta5=360
    try:
        theta7=90+math.acos(abs(d17)/0.0383)/math.pi
    except:
        theta7=360
    Estimation=Outlier(theta2,theta3,theta5,theta7)
elif d15>=0 and d16>=0 and d13<=0 and d18<=0:
    theta5=20.35119-180*math.acos(abs(d15)/0.0383)/math.pi
    theta6=-31.07149+180*math.acos(abs(d16)/0.0383)/math.pi
    theta3=180*math.acos(abs(d13)/0.0383)/math.pi-56.78296
    theta8=46.06855-180*math.acos(abs(d18)/0.0383)/math.pi
    Estimation=Outlier(theta6,theta3,theta5,theta8)
elif d16>=0 and d17>=0 and d12<=0 and d14<=0:
    theta6=-31.07149-180*math.acos(abs(d16)/0.0383)/math.pi
    theta7=-82.49829+180*math.acos(abs(d17)/0.0383)/math.pi
    theta2=-180*math.acos(abs(d12)/0.0383)/math.pi-5.36374
    theta4=71.7874+180*math.acos(abs(d14)/0.0383)/math.pi-180
    Estimation=Outlier(theta6,theta7,theta2,theta4)
elif d17>=0 and d18>=0 and d13<=0 and d15<=0:
    theta7=-82.49829-180*math.acos(abs(d17)/0.0383)/math.pi
    theta8=46.06855+180*math.acos(abs(d18)/0.0383)/math.pi-180
    theta3=-180*math.acos(abs(d13)/0.0383)/math.pi-56.78296
    theta5=20.35119+180*math.acos(abs(d15)/0.0383)/math.pi-180
    Estimation=Outlier(theta8,theta7,theta3,theta5)
elif d12>=0 and d18>=0 and d14<=0 and d16<=0:
    theta2=180*math.acos(abs(d12)/0.0383)/math.pi-5.36374-180
    theta8=46.06855-180*math.acos(abs(d18)/0.0383)/math.pi-180
    theta4=71.7874-180*math.acos(abs(d14)/0.0383)/math.pi-180
    theta6=180*math.acos(abs(d16)/0.0383)/math.pi-31.07149-180
    Estimation=Outlier(theta8,theta2,theta4,theta6)
print(Estimation)