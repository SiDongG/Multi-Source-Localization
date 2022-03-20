from os.path import dirname, join as pjoin
from time import sleep
from scipy.io import wavfile
import numpy as np
import os
from scipy.interpolate import interp1d
from statistics import variance
from statistics import mean
import math
import subprocess

#p = subprocess.Popen("record_file", stdout=subprocess.PIPE, shell=True)
#p.communicate() 

#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_0.raw channel_0.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_1.raw channel_1.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_2.raw channel_2.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_3.raw channel_3.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_4.raw channel_4.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_5.raw channel_5.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_6.raw channel_6.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_7.raw channel_7.wav")
#os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_8.raw channel_8.wav")

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
    A=True
    a=[a1,a2,a3,a4]
    Value=a.count(360)
    if Value>=2:
        A=False
    return A

def ensemble(Data):
    Invalid=0
    for i in range(0,N):
        if Data[i]==111 or Data[i]==222 or Data[i]==333:
            Data[i]=0
            Invalid=Invalid+1
    Ens_Estimation=sum(Data)/(N-Invalid)
    return Ens_Estimation

fs=16000
N=5
while True:
    Data=np.zeros(N)
    for j in range(0,N):
        samplerate, data1 = wavfile.read('channel_0.wav')
        samplerate, data2 = wavfile.read('channel_1.wav')
        samplerate, data3 = wavfile.read('channel_2.wav')
        samplerate, data4 = wavfile.read('channel_3.wav')
        samplerate, data5 = wavfile.read('channel_4.wav')
        samplerate, data6 = wavfile.read('channel_5.wav')
        samplerate, data7 = wavfile.read('channel_6.wav')
        samplerate, data8 = wavfile.read('channel_7.wav')
        
        mic1=data1
        mic2=data2
        mic3=data3
        mic4=data4
        mic5=data5
        mic6=data6
        mic7=data7
        mic8=data8

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

        Peak=[0,0,0,0,0,0,0,0]
        estimation=[0,0,0,0,0,0,0,0]
        Index=[0,0,0,0,0,0,0,0]

        for i in range(0,len(xcor12)-1):
            if xcor11[i]>Peak[7]:
                estimation[7]=i-0.1*fs
                Index[7]=[i]
                Peak[7]=xcor11[i]
            if xcor12[i]>Peak[0]:
                estimation[0]=i-0.1*fs
                Index[0]=[i]
                Peak[0]=xcor12[i]
            if xcor13[i]>Peak[1]:
                estimation[1]=i-0.1*fs
                Index[1]=[i]
                Peak[1]=xcor13[i]
            if xcor14[i]>Peak[2]:
                estimation[2]=i-0.1*fs
                Index[2]=[i]
                Peak[2]=xcor14[i]
            if xcor15[i]>Peak[3]:
                estimation[3]=i-0.1*fs
                Index[3]=[i]
                Peak[3]=xcor15[i]
            if xcor16[i]>Peak[4]:
                estimation[4]=i-0.1*fs
                Index[4]=[i]
                Peak[4]=xcor16[i]
            if xcor17[i]>Peak[5]:
                estimation[5]=i-0.1*fs
                Index[5]=[i]
                Peak[5]=xcor17[i]
            if xcor18[i]>Peak[6]:
                estimation[6]=i-0.1*fs
                Index[6]=[i]
                Peak[6]=xcor18[i]

        estimation=np.divide(estimation,fs)
        Estimation_norm=np.subtract(estimation,estimation[7]*np.ones(8))
        Est_distance=Estimation_norm*340

        d12=Est_distance[0]
        d13=Est_distance[1]
        d14=Est_distance[2]
        d15=Est_distance[3]
        d16=Est_distance[4]
        d17=Est_distance[5]
        d18=Est_distance[6]

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
            Check=Sanity(theta2,theta4,theta5,theta7)
            if Check==False:
                Estimation=111
            else:
                Estimation=Outlier(theta2,theta4,theta5,theta7)
            if Estimation!=111 and (Estimation>71.7874 or Estimation<20.35119):
                Estimation=222
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
            Check=Sanity(theta3,theta4,theta6,theta8)
            if Check==False:
                Estimation=111
            else:
                Estimation=Outlier(theta3,theta4,theta6,theta8)
            if Estimation!=111 and (Estimation<71.7874 or Estimation>123.21704):
                Estimation=222
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
                theta5=180-180*math.acos(abs(d15)/0.0383)/math.pi+20.35119
            except:
                theta5=360
            try:
                theta7=90+180*math.acos(abs(d17)/0.0383)/math.pi
            except:
                theta7=360
            Check=Sanity(theta2,theta3,theta5,theta7)
            if Check==False:
                Estimation=111
            else:
                Estimation=Outlier(theta2,theta3,theta5,theta7)
            if Estimation!=111 and (Estimation<123.21704 or Estimation>174.63626):
                Estimation=222
        elif d15>=0 and d16>=0 and d13<=0 and d18<=0:
            try:
                theta5=20.35119-180*math.acos(abs(d15)/0.0383)/math.pi
            except:
                theta5=360
            try:
                theta6=-31.07149+180*math.acos(abs(d16)/0.0383)/math.pi
            except:
                theta6=360
            try:
                theta3=180*math.acos(abs(d13)/0.0383)/math.pi-56.78296
            except:
                theta3=360
            try:
                theta8=46.06855-180*math.acos(abs(d18)/0.0383)/math.pi
            except:
                theta8=360
            Check=Sanity(theta6,theta3,theta5,theta8)
            if Check==False:
                Estimation=111
            else:
                Estimation=Outlier(theta6,theta3,theta5,theta8)
            if Estimation!=111 and (Estimation>20.35119 or Estimation<-31.07149):
                Estimation=222
        elif d16>=0 and d17>=0 and d12<=0 and d14<=0:
            try:
                theta6=-31.07149-180*math.acos(abs(d16)/0.0383)/math.pi
            except:
                theta6=360
            try:
                theta7=-82.49829+180*math.acos(abs(d17)/0.0383)/math.pi
            except:
                theta7=360
            try:
                theta2=-180*math.acos(abs(d12)/0.0383)/math.pi-5.36374
            except:
                theta2=360
            try:
                theta4=71.7874+180*math.acos(abs(d14)/0.0383)/math.pi-180
            except:
                theta4=360
            Check=Sanity(theta6,theta7,theta2,theta4)
            if Check==False:
                Estimation=111
            else:
                stimation=Outlier(theta6,theta7,theta2,theta4)
            if Estimation!=111 and (Estimation>-31.07149 or Estimation<-82.49829):
                Estimation=222
        elif d17>=0 and d18>=0 and d13<=0 and d15<=0:
            try:
                theta7=-82.49829-180*math.acos(abs(d17)/0.0383)/math.pi
            except:
                theta7=360
            try:
                theta8=46.06855+180*math.acos(abs(d18)/0.0383)/math.pi-180
            except:
                theta8=360
            try:
                theta3=-180*math.acos(abs(d13)/0.0383)/math.pi-56.78296
            except:
                theta3=360
            try:
                theta5=20.35119+180*math.acos(abs(d15)/0.0383)/math.pi-180
            except:
                theta5=360
            Check=Sanity(theta8,theta7,theta3,theta5)
            if Check==False:
                Estimation=111
            else:
                Estimation=Outlier(theta8,theta7,theta3,theta5)
            if Estimation!=111 and (Estimation>-82.49829 or Estimation<-133.93145):
                Estimation=222
        elif d12>=0 and d18>=0 and d14<=0 and d16<=0:
            try:
                theta2=180*math.acos(abs(d12)/0.0383)/math.pi-5.36374-180
            except:
                theta2=360
            try:
                theta8=46.06855-180*math.acos(abs(d18)/0.0383)/math.pi-180
            except:
                theta8=360
            try:
                theta4=71.7874-180*math.acos(abs(d14)/0.0383)/math.pi-180
            except:
                theta4=360
            try:
                theta6=180*math.acos(abs(d16)/0.0383)/math.pi-31.07149-180
            except:
                theta6=360
            Check=Sanity(theta8,theta2,theta4,theta6)
            if Check==False:
                Estimation=111
            else:
                Estimation=Outlier(theta8,theta2,theta4,theta6)
            if Estimation!=111 and (Estimation>-133.93145 or Estimation<-180):
                Estimation=222
        else:
            Estimation=333
        
        print(j)
        Data[j]=Estimation

        print(Estimation)

        if j==4:
            Final=ensemble(Data)
            print(1)
            print(Data)
            print(Final)
            print(1)

