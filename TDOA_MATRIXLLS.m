clear; clc; close all;
%% Least Square Problem for TDOA using Matrix Voice

x0=0;y0=0;z0=0;
x1=-0.03813;y1=0.00358;z1=0;
x2=-0.02098;y2=0.03204;z2=0;
x3=0.01197;y3=0.03638;z3=0;
x4=0.03591;y4=0.01332;z4=0;
x5=0.03281;y5=-0.01977;z5=0;
x6=0.005;y6=-0.03797;z6=0;
x7=-0.02657;y7=-0.02758;z7=0;

r=38.2978/1000; %In milimeter, radius of the circular array%
rx=0.1;ry=0.2;rz=0; %Source Location
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

d12=Distance_difference(1);
d13=Distance_difference(2);
d14=Distance_difference(3);
d15=Distance_difference(4);
d16=Distance_difference(5);
d17=Distance_difference(6);
d18=Distance_difference(7);
%%

H=[x1-x0,y1-y0,-d12;
    x2-x0,y2-y0,-d13;
    x3-x0,y3-y0,-d14;
    x4-x0,y4-y0,-d15;
    x5-x0,y5-y0,-d16;
    x6-x0,y6-y0,-d17;
    x7-x0,y7-y0,-d18];
x=[-d12^2-(x0^2+y0^2)+(x1^2+y1^2);
    -d13^2-(x0^2+y0^2)+(x2^2+y2^2);
    -d14^2-(x0^2+y0^2)+(x3^2+y3^2);
    -d15^2-(x0^2+y0^2)+(x4^2+y4^2);
    -d16^2-(x0^2+y0^2)+(x5^2+y5^2);
    -d17^2-(x0^2+y0^2)+(x6^2+y6^2);
    -d18^2-(x0^2+y0^2)+(x7^2+y7^2)];

Theta=0.5*inv(H.'*H)*H.'*x
