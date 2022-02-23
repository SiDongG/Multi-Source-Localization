clear;clc;close all;
%% Source Localization with Microphone array
% Method: Generalized Cross-correlation with The phase transform and
% far-field simplification

% Author: Sidong Guo
% Date: Feb 3rd 2022
%% Initialization

r=38.2978/1000; %In milimeter, radius of the circular array%
rx=4;ry=6;rz=0; %Source Location
rxULA = phased.OmnidirectionalMicrophoneElement;
rxpos1 = [0;0;0];
rxvel1 = [0;0;0];
rxax1 = azelaxes(0,0);
rxpos2 = [-38.13;3.58;0]/1000;
rxvel2 = [0;0;0];
rxax2 = azelaxes(0,0);
rxpos3 = [-20.98;32.04;0]/1000;
rxvel3 = [0;0;0];
rxax3 = azelaxes(0,0);
rxpos4 = [11.97;36.38;0]/1000;
rxvel4 = [0;0;0];
rxax4 = azelaxes(0,0);
rxpos5 = [35.91;13.32;0]/1000;
rxvel5 = [0;0;0];
rxax5 = azelaxes(0,0);
rxpos6 = [32.81;-19.77;0]/1000;
rxvel6 = [0;0;0];
rxax6 = azelaxes(0,0);
rxpos7 = [5;-37.97;0]/1000;
rxvel7 = [0;0;0];
rxax7 = azelaxes(0,0);
rxpos8 = [-26.57;-27.58;0]/1000;
rxvel8 = [0;0;0];
rxax8 = azelaxes(0,0);

srcpos = [rx;ry;rz];
srcvel = [0;0;0];
srcax = azelaxes(0,0);
srcULA = phased.OmnidirectionalMicrophoneElement;

% Parameters definition

Carrier_Fre = 96e3;             % 20 kHz
Propagation_Speed = 340;            % 340 m/s
Operating_range = 34;            % 34 m
pri = (2*Operating_range)/Propagation_Speed;
prf = 1/pri;
bw = 5e3;              % 5 kHz
fs = 9.6e4;            % 96 kHz
waveform = phased.LinearFMWaveform('SampleRate',fs,'SweepBandwidth',bw,'PRF',prf,'PulseWidth',pri/10);
signal = waveform();

radiator = phased.WidebandRadiator('Sensor',srcULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector1 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector2 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector3 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector4 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector5 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector6 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector7 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector8 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);

channel1 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel2 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel3= phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel4 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel5 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel6 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel7= phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel8 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);


[~,ang1_transmit] = rangeangle(rxpos1,srcpos,srcax);
[~,ang2_transmit] = rangeangle(rxpos2,srcpos,srcax);
[~,ang3_transmit] = rangeangle(rxpos3,srcpos,srcax);
[~,ang4_transmit] = rangeangle(rxpos4,srcpos,srcax);
[~,ang5_transmit] = rangeangle(rxpos5,srcpos,srcax);
[~,ang6_transmit] = rangeangle(rxpos6,srcpos,srcax);
[~,ang7_transmit] = rangeangle(rxpos7,srcpos,srcax);
[~,ang8_transmit] = rangeangle(rxpos8,srcpos,srcax);

sig_transmit = radiator(signal,[ang1_transmit ang2_transmit ang3_transmit ang4_transmit ang5_transmit ang6_transmit ang7_transmit ang8_transmit]);

sigp1 = channel1(sig_transmit(:,1),srcpos,rxpos1,srcvel,rxvel1);
sigp2 = channel2(sig_transmit(:,2),srcpos,rxpos2,srcvel,rxvel2);
sigp3 = channel3(sig_transmit(:,3),srcpos,rxpos3,srcvel,rxvel3);
sigp4 = channel4(sig_transmit(:,4),srcpos,rxpos4,srcvel,rxvel4);
sigp5 = channel5(sig_transmit(:,5),srcpos,rxpos5,srcvel,rxvel5);
sigp6 = channel6(sig_transmit(:,6),srcpos,rxpos6,srcvel,rxvel6);
sigp7 = channel7(sig_transmit(:,7),srcpos,rxpos7,srcvel,rxvel7);
sigp8 = channel8(sig_transmit(:,8),srcpos,rxpos8,srcvel,rxvel8);

[~,ang1_receive] = rangeangle(srcpos,rxpos1,rxax1);
[~,ang2_receive] = rangeangle(srcpos,rxpos2,rxax2);
[~,ang3_receive] = rangeangle(srcpos,rxpos3,rxax3);
[~,ang4_receive] = rangeangle(srcpos,rxpos4,rxax4);
[~,ang5_receive] = rangeangle(srcpos,rxpos5,rxax5);
[~,ang6_receive] = rangeangle(srcpos,rxpos6,rxax6);
[~,ang7_receive] = rangeangle(srcpos,rxpos7,rxax7);
[~,ang8_receive] = rangeangle(srcpos,rxpos8,rxax8);

sigr1 = collector1(sigp1,ang1_receive);
sigr2 = collector2(sigp2,ang2_receive);
sigr3 = collector3(sigp3,ang3_receive);
sigr4 = collector4(sigp4,ang4_receive);
sigr5 = collector5(sigp5,ang5_receive);
sigr6 = collector6(sigp6,ang6_receive);
sigr7 = collector7(sigp7,ang7_receive);
sigr8 = collector8(sigp8,ang8_receive);

xcor12_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr2)))./(abs(fft(sigr1)).*abs(fft(sigr2))))));
xcor13_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr3)))./(abs(fft(sigr1)).*abs(fft(sigr3))))));
xcor14_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr4)))./(abs(fft(sigr1)).*abs(fft(sigr4))))));
xcor15_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr5)))./(abs(fft(sigr1)).*abs(fft(sigr5))))));
xcor16_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr6)))./(abs(fft(sigr1)).*abs(fft(sigr6))))));
xcor17_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr7)))./(abs(fft(sigr1)).*abs(fft(sigr7))))));
xcor18_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr8)))./(abs(fft(sigr1)).*abs(fft(sigr8))))));

Actual_Arrival=zeros(1,5);
Actual_Arrival(1)=sqrt(rx^2+ry^2+rz^2)/Propagation_Speed;
Actual_Arrival(2)=sqrt((rx+0.03813)^2+(ry-0.00358)^2+rz^2)/Propagation_Speed;
Actual_Arrival(3)=sqrt((rx+0.02098)^2+(ry-0.03204)^2+rz^2)/Propagation_Speed;
Actual_Arrival(4)=sqrt((rx-0.01197)^2+(ry-0.03638)^2+rz^2)/Propagation_Speed;
Actual_Arrival(5)=sqrt((rx-0.03591)^2+(ry-0.01332)^2+rz^2)/Propagation_Speed;

Actual_difference=zeros(1,4);
Actual_difference(1)=Actual_Arrival(1)-Actual_Arrival(2);
Actual_difference(2)=Actual_Arrival(1)-Actual_Arrival(3);
Actual_difference(3)=Actual_Arrival(1)-Actual_Arrival(4);
Actual_difference(4)=Actual_Arrival(1)-Actual_Arrival(5);

Peak_Value=zeros(1,7);
Estimated_difference=zeros(1,7);

for i=1:length(xcor12_PHAT)
    if xcor12_PHAT(i)>Peak_Value(1)
        Estimated_difference(1)=(i-0.1*fs-1);
        Peak_Value(1)=xcor12_PHAT(i);
    end
    if xcor13_PHAT(i)>Peak_Value(2)
        Estimated_difference(2)=(i-0.1*fs-1);
        Peak_Value(2)=xcor13_PHAT(i);
    end
    if xcor14_PHAT(i)>Peak_Value(3)
        Estimated_difference(3)=(i-0.1*fs-1);
        Peak_Value(3)=xcor14_PHAT(i);
    end
    if xcor15_PHAT(i)>Peak_Value(4)
        Estimated_difference(4)=(i-0.1*fs-1);
        Peak_Value(4)=xcor15_PHAT(i);
    end
    if xcor16_PHAT(i)>Peak_Value(5)
        Estimated_difference(5)=(i-0.1*fs-1);
        Peak_Value(5)=xcor16_PHAT(i);
    end
    if xcor17_PHAT(i)>Peak_Value(6)
        Estimated_difference(6)=(i-0.1*fs-1);
        Peak_Value(6)=xcor17_PHAT(i);
    end
    if xcor18_PHAT(i)>Peak_Value(7)
        Estimated_difference(7)=(i-0.1*fs-1);
        Peak_Value(7)=xcor18_PHAT(i);
    end
end
Estimated_difference=Estimated_difference/fs;
Distance_difference=Estimated_difference*Propagation_Speed
Actual_Distance=Actual_difference*Propagation_Speed

d12=Distance_difference(1);
d13=Distance_difference(2);
d14=Distance_difference(3);
d15=Distance_difference(4);
d16=Distance_difference(5);
d17=Distance_difference(6);
d18=Distance_difference(7);


%Distance_Matrix=[-38.13,3.58;-20.98,32.04]/1000;

%v=(1817.45*d13+1000*d12)/54.65;
%u=(3.58*v-1000*d12)/38.13;
theta2=acosd(abs(d12)/0.0383)-5.3637
theta3=90-(acosd(abs(d13)/0.0383)-33.217)
theta6=acosd(abs(d16)/0.0383)-20.3512
theta7=180-82.5-acosd(abs(d17)/0.0383)
sig=[sigr1,sigr2,sigr3,sigr4,sigr5,sigr6,sigr7,sigr7];
average_theta=(theta3+theta2+theta6+theta7)/4;
if abs(theta2-average_theta)>10
    Estimated_angle=(theta3+theta6+theta7)/3;
elseif abs(theta3-average_theta)>10
    Estimated_angle=(theta2+theta6+theta7)/3;
elseif abs(theta6-average_theta)>10
    Estimated_angle=(theta2+theta3+theta7)/3;
elseif abs(theta7-average_theta)>10
    Estimated_angle=(theta2+theta6+theta3)/3;
else
    Estimated_angle=(theta3+theta2+theta6+theta7)/4;
end
Estimated_angle
real_angle=atand(ry/rx)









































