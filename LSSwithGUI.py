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
import scipy.signal
from scipy.interpolate import interp1d
from statistics import variance
from statistics import mean
import subprocess
from matrix_lite import led




Error=False
Threshold=125
fs=16000
Angle_Est=0
x0=0
y0=0
x1=-0.03813
y1=0.00358
x2=-0.02098
y2=0.03204
x3=0.01197
y3=0.03638
x4=0.03591
y4=0.01332
x5=0.03281
y5=-0.01977
x6=0.005
y6=-0.03797
x7=-0.02657
y7=-0.02758
Estimation=0
degree_freedom=50
brightness = 0.5




#BEGIN GUI CODE




import tkinter as tk
#import tksheet
import array as ar
#import psutil
import matplotlib.pyplot as plt

from tkinter import *
#from tkinter.ttk import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


data_size = 4



# This is a class of the code.
# It is used to store the x and y coordinates.
class graph():
    
    # An array of x coordinates
    x_coordinates = [0 for i in range(data_size)]

    # An array of y coordinates
    y_coordinates = [0 for i in range(data_size)]
    
    # Sets the the origin
    x_coordinates[0] = 0
    y_coordinates[0] = 0

    # Sets an angle for the graph
    angle=0

# Calculates a vector based on the graphing angle
# math.radians is used in oreder to convert degrees to radians
def calc_arc_points():
    # Assigns a point based on the angle given
    graph.x_coordinates[1]= 10 * math.cos( math.radians( graph.angle ) )
    graph.y_coordinates[1]= 10 * math.sin( math.radians( graph.angle ) )

    # Assigns two more set of point to give a range of the frequecy
    graph.x_coordinates[2]= 10 * math.cos( math.radians( graph.angle + 2 ) )
    graph.y_coordinates[2]= 10 * math.sin( math.radians( graph.angle + 2 ) )
    graph.x_coordinates[3]= 10 * math.cos( math.radians( graph.angle - 2 ) )
    graph.y_coordinates[3]= 10 * math.sin( math.radians( graph.angle - 2 ) )


def system_title():
     # Create Team Label
    team_label = Label(
        essex,
        text='SENIOR DESIGN TEAM SPOT',
        font=('Times New Roman', 12),
        foreground='black',
        background='white',
        width=100,
        anchor='center')
    team_label.grid(row = 1, column = 1, columnspan = 2)

fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)
axis_x=[-10,10]
axis_y=[-10,10]


ax.plot(axis_x,[0,0],color='black')
ax.plot([0,0],axis_y,color='black')
ax.plot([0,0],[0,0.1])

essex = Tk()

def change_threshold():
    global Threshold
    string = thresholdInput.get()
    Threshold = int(string)
    print(string)
    
    
    
    
def change_degrees():
    global degree_freedom
    sting = degInput.get()
    degree_freedom = int(string)
    
    
    

def change_degrees():
    global degree_freedom
    sting = degInput.get()
    degree_freedom = int(string)
    
    
def change_brightness():
    global brightness
    string = brightInput.get()
    brightness = float(string)
    
    
    
    
#threshinput = StringVar()
#def create_buttons():
#global threshinput
    
    
    
    
thresholdInput = Entry(essex,width=30)
thresholdInput.focus_set()
thresholdInput.grid(row = 3, column = 2)
#     threshold.grid(row=7, column =1 , padx =2, pady =2)
edit_threshold = Button(essex,text="Change Threshold (120-200)", width = 20, command = change_threshold,pady=10).grid(row =4 ,column=2)


degInput = Entry(essex,width=30)
degInput.focus_set()
degInput.grid(row = 5, column = 2)
edit_DoF = Button(essex,text="Degrees of Forgiveness (0-50)", width = 30, command = change_degrees,pady=10).grid(row =6 ,column=2)


brightInput = Entry(essex,width=30)
brightInput.focus_set()
brightInput.grid(row = 7, column = 2)
edit_bright = Button(essex,text="Brightness (0-1)", width = 20, command = change_brightness,pady=10).grid(row =8 ,column=2)
    
    
    
    


    
    
    
    
    
    
def plot_angle(c_d):
    # Code used to destroy previous graph when making a new graph
    # Without it multiple graphs are printed each time plot is called
    for widget in frame_graph.winfo_children():
        widget.destroy()

    # Controls the size of the graph
    # Also creates a plot called fig

        
    

    # Have no idea why 111
    # Uncomment the last part of the code in order to plot in a 3D plane


    # Used to call the fuction random_angle
    graph.angle = Estimation

    # Calls the function used to calculate the random angle
    calc_arc_points()

    # For loop used to create vectors that are ploted
    # The commented out sections of the code are used in a 3D graph
    
    ax.lines.pop(len(ax.lines)-1)
    
    
    for k in range(0,2):
       # Plots the coordintates on the graph
       #ax.scatter(graph.x_coordinates[k],graph.y_coordinates[k])
       # Used to create a vector coordinates
       vector_x=[graph.x_coordinates[0],graph.x_coordinates[k]]
       vector_y=[graph.y_coordinates[0],graph.y_coordinates[k]]
       ax.plot(vector_x,vector_y)

       
    #ax.plot(11,11)
    #ax.plot(-11,-11)
   

    # Creates a figure called graph_canvas
    # It is used to post the figure onto the canvas called graph_canvas
    graph_canvas = FigureCanvasTkAgg(fig,master=frame_graph)

    # This is left over code from the code I based mine off of
    # It has been commented out but I choose to leave it in just in case somthing goes wrong
    # graph_canvas.draw()

    # Placing the canvas on the Tkinter window
    # I am using pack because the graph is the only peice of information on the frame
    graph_canvas.get_tk_widget().pack()

    # Creating the Matplotlib toolbar
    # Will error if commented out
    #toolbar = NavigationToolbar2Tk(graph_canvas, frame_graph)

    # This is left over code from the code I based mine off of
    #toolbar.update()

    # Placing the toolbar on the Tkinter window
    #graph_canvas.get_tk_widget().pack()





#Main code starts here
#---------------------------------------------------------------------------

#Creates the tkinter window(root)
#I called it essex becase it is easy for me to remeber
#can be replaced in the rest of the code with anything the user wants

#Adds a title to the root
essex.title('Multi-Source Localization')
#This determines the dimensions of the roots
essex.geometry("800x400")
essex.resizable(False, False)

#Calls the functions system_specs()
#system_specs()
system_title()

#Calls the funtction create_buttons
#create_buttons()

#Create the background for the graph
#The bg changes the background and can be used on all lables/ buttons
#frame_graph=tk.Frame(essex, bg="black")
frame_graph = tk.Frame(essex)


#Places the frame on the root
#The frame is natural placed in location 1,10
#because of row span, the graph will automatically span rows 1-10
#Stickky forces the frame to the left- it is probably unecssary
#frame_graph.grid(row = 2, rowspan = 6, column = 2, columnspan = 8, sticky='w')
frame_graph.grid(row = 2, rowspan = 12, column = 1)

#used to start looping the root
#essex.mainloop()












#package main
#import ("github.com/matrix-io/matrix-lite-go")
#g++ -o mic_record_file mic_record_file.cpp -std=c++11 -lmatrix_creator_hal -lgflags

def LLS(d12,d13,d14,d15,d16,d17,d18):
    H=np.array([[x1-x0,y1-y0,-d12],
    [x2-x0,y2-y0,-d13],
    [x3-x0,y3-y0,-d14],
    [x4-x0,y4-y0,-d15],
    [x5-x0,y5-y0,-d16],
    [x6-x0,y6-y0,-d17],
    [x7-x0,y7-y0,-d18]])
    x=np.array([[-d12**2-(x0**2+y0**2)+(x1**2+y1**2)],
    [-d13**2-(x0**2+y0**2)+(x2**2+y2**2)],
    [-d14**2-(x0**2+y0**2)+(x3**2+y3**2)],
    [-d15**2-(x0**2+y0**2)+(x4**2+y4**2)],
    [-d16**2-(x0**2+y0**2)+(x5**2+y5**2)],
    [-d17**2-(x0**2+y0**2)+(x6**2+y6**2)],
    [-d18**2-(x0**2+y0**2)+(x7**2+y7**2)]])
   
    Theta=0.5*np.matmul(np.matmul(np.linalg.inv(np.matmul(H.transpose(),H)),H.transpose()),x)
    return Theta


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
    if Value==2:
        A=2
    elif Value>2:
        A=False
    return A

def Avg_filter(a1,a2,a3,a4):
    Estimation=(a1+a2+a3+a4-720)/2
    return Estimation


#everloop = [{'w':50}] * led.length
led.set('#BBC41C')

while True:
    
    
    essex.update_idletasks()
    essex.update()
    
    
    
    
    Error=False
    p = subprocess.Popen("./mic_record_file", stdout=subprocess.PIPE, shell=True)
    p.communicate()
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_0.raw channel_0.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_1.raw channel_1.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_2.raw channel_2.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_3.raw channel_3.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_4.raw channel_4.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_5.raw channel_5.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_6.raw channel_6.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_7.raw channel_7.wav")
    os.system("sox -r 16000 -c 1 -e signed -c 1 -e signed -b 16 mic_16000_s16le_channel_8.raw channel_8.wav")

    samplerate, data1 = wavfile.read('channel_0.wav')
    samplerate, data2 = wavfile.read('channel_1.wav')
    samplerate, data3 = wavfile.read('channel_2.wav')
    samplerate, data4 = wavfile.read('channel_3.wav')
    samplerate, data5 = wavfile.read('channel_4.wav')
    samplerate, data6 = wavfile.read('channel_5.wav')
    samplerate, data7 = wavfile.read('channel_6.wav')
    samplerate, data8 = wavfile.read('channel_7.wav')
    samplerate, data9 = wavfile.read('channel_8.wav')
    
    mic1=data1
    mic2=data2
    mic3=data3
    mic4=data4
    mic5=data5
    mic6=data6
    mic7=data7
    mic8=data8
    
    a1=max(mic1)/10
    a2=max(mic2)/10
    a3=max(mic3)/10
    a4=max(mic4)/10
    a5=max(mic5)/10
    a6=max(mic6)/10
    a7=max(mic7)/10
    a8=max(mic8)/10
    avg_peak=(a1+a2+a3+a4+a5+a6+a7+a8)/8
    print(avg_peak)
    if avg_peak>Threshold:
        
        try:
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
        except:
            Error=True
            
        Peak=[0,0,0,0,0,0,0,0]
        Estimate=[0,0,0,0,0,0,0,0]
        Index=[0,0,0,0,0,0,0,0]

        for i in range(0,len(xcor12)-1):
            if xcor11[i]>Peak[7]:
                Estimate[7]=i-0.1*fs
                Index[7]=[i]
                Peak[7]=xcor11[i]
            if xcor12[i]>Peak[0]:
                Estimate[0]=i-0.1*fs
                Index[0]=[i]
                Peak[0]=xcor12[i]
            if xcor13[i]>Peak[1]:
                Estimate[1]=i-0.1*fs
                Index[1]=[i]
                Peak[1]=xcor13[i]
            if xcor14[i]>Peak[2]:
                Estimate[2]=i-0.1*fs
                Index[2]=[i]
                Peak[2]=xcor14[i]
            if xcor15[i]>Peak[3]:
                Estimate[3]=i-0.1*fs
                Index[3]=[i]
                Peak[3]=xcor15[i]
            if xcor16[i]>Peak[4]:
                Estimate[4]=i-0.1*fs
                Index[4]=[i]
                Peak[4]=xcor16[i]
            if xcor17[i]>Peak[5]:
                Estimate[5]=i-0.1*fs
                Index[5]=[i]
                Peak[5]=xcor17[i]
            if xcor18[i]>Peak[6]:
                Estimate[6]=i-0.1*fs
                Index[6]=[i]
                Peak[6]=xcor18[i]

        Estimate=np.divide(Estimate,fs)
        Estimation_norm=np.subtract(Estimate,Estimate[7]*np.ones(8))
        Est_distance=Estimation_norm*340

        d12=Est_distance[0]
        d13=Est_distance[1]
        d14=Est_distance[2]
        d15=Est_distance[3]
        d16=Est_distance[4]
        d17=Est_distance[5]
        d18=Est_distance[6]
        
#         Theta=LLS(d12,d13,d14,d15,d16,d17,d18)
#         
#         print(Theta[0])
#         print(Theta[1])

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
                Estimation=1
            elif Check==2:
                Estimation=Avg_filter(theta2,theta4,theta5,theta7)
            else:
                Estimation=Outlier(theta2,theta4,theta5,theta7)
            if Estimation!=1 and (Estimation>71.7874+degree_freedom or Estimation<20.35119-degree_freedom):
                Estimation=2
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
                Estimation=1
            elif Check==2:
                Estimation=Avg_filter(theta3,theta4,theta6,theta8)
            else:
                Estimation=Outlier(theta3,theta4,theta6,theta8)
            if Estimation!=1 and (Estimation<71.7874-degree_freedom or Estimation>123.21704+degree_freedom):
                Estimation=2
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
                Estimation=1
            elif Check==2:
                Estimation=Avg_filter(theta2,theta3,theta5,theta7)
            else:
                Estimation=Outlier(theta2,theta3,theta5,theta7)
            if Estimation!=1 and (Estimation<123.21704-degree_freedom or Estimation>174.63626+degree_freedom):
                Estimation=2
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
                Estimation=1
            elif Check==2:
                Estimation=Avg_filter(theta3,theta5,theta6,theta8)
            else:
                Estimation=Outlier(theta6,theta3,theta5,theta8)
            if Estimation!=1 and (Estimation>20.35119+degree_freedom or Estimation<-31.07149-degree_freedom):
                Estimation=2
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
                Estimation=1
            elif Check==2:
                Estimation=Avg_filter(theta2,theta4,theta6,theta7)
            else:
                stimation=Outlier(theta6,theta7,theta2,theta4)
            if Estimation!=1 and (Estimation>-31.07149+degree_freedom or Estimation<-82.49829-degree_freedom):
                Estimation=2
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
                Estimation=1
            elif Check==2:
                Estimation=Avg_filter(theta3,theta5,theta7,theta8)
            else:
                Estimation=Outlier(theta8,theta7,theta3,theta5)
            if Estimation!=1 and (Estimation>-82.49829+degree_freedom or Estimation<-133.93145-degree_freedom):
                Estimation=2
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
                Estimation=1
            elif Check==2:
                Estimation=Avg_filter(theta2,theta4,theta6,theta8)
            else:
                Estimation=Outlier(theta8,theta2,theta4,theta6)
            if Estimation!=1 and (Estimation>-133.93145+degree_freedom or Estimation<-190):
                Estimation=2
        else:
            Estimation=3
        if 24<Estimation<25:
            Estimation=4
#         if Error==True:
#             Estimation=4
        print(Estimation)
        if Estimation != 1 and Estimation !=2 and Estimation !=3 and Estimation !=4:
            index = int(9 - Estimation/20)
            everloop = [{'b':50}] * led.length
            everloop[index] = {'g':100}
            led.set(everloop)
            plot_angle(0)
            
        else:
            everloop = [{'r':50}] * led.length
            led.set(everloop)
        
    else:
        print('No one speaking')
        everloop = [{'w':50}] * led.length
        led.set(everloop)
        
