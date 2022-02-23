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

fs=96000;
print (os.path.exists("matlab.mat"))
data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
wav_fname = pjoin(data_dir, 'output.wav')
#samplerate, data = wavfile.read(wav_fname)

print('1')

#cwd = os.getcwd()  
#files = os.listdir(cwd) 
#print("Files in %r: %s" % (cwd, files))
data=0
mat = scipy.io.loadmat('matlab.mat')

data=mat['sig']
#print(mat['sig'])

total=np.sum(data)
#print(total)
#print(len(data))
#print(len(data[0]))
mic1=data[:,0]
mic2=data[:,1]
mic3=data[:,2]
mic4=data[:,3]
mic5=data[:,4]
mic6=data[:,5]
mic7=data[:,6]
mic8=data[:,7]

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

Peak=[0,0,0,0,0,0,0]
Estimation=[0,0,0,0,0,0,0]

for i in range(0,len(xcor12)-1):
    if xcor12[i]>Peak[0]:
        Estimation[0]=i-0.1*fs
        Peak[0]=xcor12[i]
    if xcor13[i]>Peak[1]:
        Estimation[1]=i-0.1*fs
        Peak[1]=xcor13[i]
    if xcor14[i]>Peak[2]:
        Estimation[2]=i-0.1*fs
        Peak[2]=xcor14[i]
    if xcor15[i]>Peak[3]:
        Estimation[3]=i-0.1*fs
        Peak[3]=xcor15[i]
    if xcor16[i]>Peak[4]:
        Estimation[4]=i-0.1*fs
        Peak[4]=xcor16[i]
    if xcor17[i]>Peak[5]:
        Estimation[5]=i-0.1*fs
        Peak[5]=xcor17[i]
    if xcor18[i]>Peak[6]:
        Estimation[6]=i-0.1*fs
        Peak[6]=xcor18[i]

Estimation=np.divide(Estimation,fs)
Est_distance=Estimation*340

d12=Est_distance[0]
d13=Est_distance[1]
d14=Est_distance[2]
d15=Est_distance[3]
d16=Est_distance[4]
d17=Est_distance[5]
d18=Est_distance[6]

theta2=180*math.acos(abs(d12)/0.0383)/math.pi-5.3637
theta3=90-(180*math.acos(abs(d13)/0.0383)/math.pi-33.217)
theta6=180*math.acos(abs(d16)/0.0383)/math.pi-20.3512
theta7=180-82.5-180*math.acos(abs(d17)/0.0383)/math.pi

avg_theta=(theta3+theta2+theta6+theta7)/4

if abs(theta2-avg_theta)>10:
    Estimated_angle=(theta3+theta6+theta7)/3
elif abs(theta3-avg_theta)>10:
    Estimated_angle=(theta2+theta6+theta7)/3
elif abs(theta6-avg_theta)>10:
    Estimated_angle=(theta2+theta3+theta7)/3
elif abs(theta7-avg_theta)>10:
    Estimated_angle=(theta2+theta6+theta3)/3
else:
    Estimated_angle=(theta3+theta2+theta6+theta7)/4


print(Estimated_angle)







