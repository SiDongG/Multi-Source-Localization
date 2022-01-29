
clear;clc;close all;
%% Source Localization with Microphone array
% Method: Generalized Cross-correlation with The phase transform and
% smoothed coherence transform and triangulation
% Phased Array toolbox
% Author: Sidong Guo
% Date: Jan 23rd 2022
%% Initialization
d=0.2; %Microphone distance to the middle reference microphone
rx=10;ry=6;rz=10;
% Initialize Square array 
rxULA = phased.OmnidirectionalMicrophoneElement;
rxpos1 = [0;0;0];
rxvel1 = [0;0;0];
rxax1 = azelaxes(0,0);
rxpos2 = [d;0;0];
rxvel2 = [0;0;0];
rxax2 = azelaxes(0,0);
rxpos3 = [0;d;0];
rxvel3 = [0;0;0];
rxax3 = azelaxes(0,0);
rxpos4 = [-d;0;0];
rxvel4 = [0;0;0];
rxax4 = azelaxes(0,0);
rxpos5 = [0;-d;0];
rxvel5 = [0;0;0];
rxax5 = azelaxes(0,0);
rxpos6 = [0;0;d];
rxvel6 = [0;0;0];
rxax6 = azelaxes(0,0);
srcpos = [rx;ry;rz];
srcvel = [0;0;0];
srcax = azelaxes(0,0);
srcULA = phased.OmnidirectionalMicrophoneElement;
% Parameters definition
Carrier_Fre = 20e3;             % 20 kHz
Propagation_Speed = 340;            % 340 m/s
Operating_range = 34;            % 34 m
pri = (2*Operating_range)/Propagation_Speed;
prf = 1/pri;
bw = 5e3;              % 5 kHz
fs = 4*bw;
waveform = phased.LinearFMWaveform('SampleRate',fs,'SweepBandwidth',bw,'PRF',prf,'PulseWidth',pri/10);
signal = waveform();
% Set up Transmitting and Receiving objects 
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
% Set up channel objects 
channel1 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel2 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel3 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel4 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel5 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);
channel6 = phased.WidebandFreeSpace('PropagationSpeed',Propagation_Speed,...
    'SampleRate',fs,'OperatingFrequency',Carrier_Fre);

%channel1 = phased.MultipathChannel('SampleRate',fs,'OperatingFrequency',Carrier_Fre);
%channel2 = phased.MultipathChannel('SampleRate',fs,'OperatingFrequency',Carrier_Fre);
%channel3 = phased.MultipathChannel('SampleRate',fs,'OperatingFrequency',Carrier_Fre);
%channel4 = phased.MultipathChannel('SampleRate',fs,'OperatingFrequency',Carrier_Fre);

[~,ang1_transmit] = rangeangle(rxpos1,srcpos,srcax);
[~,ang2_transmit] = rangeangle(rxpos2,srcpos,srcax);
[~,ang3_transmit] = rangeangle(rxpos3,srcpos,srcax);
[~,ang4_transmit] = rangeangle(rxpos4,srcpos,srcax);
[~,ang5_transmit] = rangeangle(rxpos5,srcpos,srcax);
[~,ang6_transmit] = rangeangle(rxpos6,srcpos,srcax);
sig_transmit = radiator(signal,[ang1_transmit ang2_transmit ang3_transmit ang4_transmit ang5_transmit ang6_transmit]);
% Set up Propagation Objects 
sigp1 = channel1(sig_transmit(:,1),srcpos,rxpos1,srcvel,rxvel1);
sigp2 = channel2(sig_transmit(:,2),srcpos,rxpos2,srcvel,rxvel2);
sigp3 = channel3(sig_transmit(:,3),srcpos,rxpos3,srcvel,rxvel3);
sigp4 = channel4(sig_transmit(:,4),srcpos,rxpos4,srcvel,rxvel4);
sigp5 = channel5(sig_transmit(:,5),srcpos,rxpos5,srcvel,rxvel5);
sigp6 = channel6(sig_transmit(:,6),srcpos,rxpos6,srcvel,rxvel6);

[~,ang1_receive] = rangeangle(srcpos,rxpos1,rxax1);
[~,ang2_receive] = rangeangle(srcpos,rxpos2,rxax2);
[~,ang3_receive] = rangeangle(srcpos,rxpos3,rxax3);
[~,ang4_receive] = rangeangle(srcpos,rxpos4,rxax4);
[~,ang5_receive] = rangeangle(srcpos,rxpos5,rxax5);
[~,ang6_receive] = rangeangle(srcpos,rxpos6,rxax6);

% Receiver Signal 
sigr1 = collector1(sigp1,ang1_receive);
sigr2 = collector2(sigp2,ang2_receive);
sigr3 = collector3(sigp3,ang3_receive);
sigr4 = collector4(sigp4,ang4_receive);
sigr5 = collector5(sigp5,ang5_receive);
sigr6 = collector6(sigp6,ang6_receive);
%{
figure()
hold on; box on
subplot(2,3,1)
plot(1:2000,signal)
subplot(2,3,2)
plot(1:2000,sigr1)
subplot(2,3,3)
plot(1:2000,sigr2)
subplot(2,3,4)
plot(1:2000,sigr3)
subplot(2,3,5)
plot(1:2000,sigr4)
subplot(2,3,6)
plot(1:2000,sigr5)
%}
%% Time Difference of Arrival Estimation--GCC
%{
xcor12=xcorr(sigr1,sigr2);
xcor13=xcorr(sigr1,sigr3);
xcor14=xcorr(sigr1,sigr4);
xcor15=xcorr(sigr1,sigr5);
xcor23=xcorr(sigr2,sigr3);
xcor24=xcorr(sigr2,sigr4);
xcor34=xcorr(sigr3,sigr4);

figure()
hold on;box on
subplot(2,3,1)
plot(1:length(xcor12),abs(xcor12))
subplot(2,3,2)
plot(1:length(xcor13),abs(xcor13))
subplot(2,3,3)
plot(1:length(xcor14),abs(xcor14))
subplot(2,3,4)
plot(1:length(xcor23),abs(xcor23))
subplot(2,3,5)
plot(1:length(xcor24),abs(xcor24))
subplot(2,3,6)
plot(1:length(xcor34),abs(xcor34))
title('Cross-correlation using xcorr')

xcor12_fft=fftshift(ifft(fft(sigr1).*conj(fft(sigr2))));
xcor13_fft=fftshift(ifft(fft(sigr1).*conj(fft(sigr3))));
xcor14_fft=fftshift(ifft(fft(sigr1).*conj(fft(sigr4))));
xcor23_fft=fftshift(ifft(fft(sigr2).*conj(fft(sigr3))));
xcor24_fft=fftshift(ifft(fft(sigr2).*conj(fft(sigr4))));
xcor34_fft=fftshift(ifft(fft(sigr3).*conj(fft(sigr4))));

figure()
hold on;box on
subplot(2,3,1)
plot(1:length(xcor12_fft),abs(xcor12_fft))
subplot(2,3,2)
plot(1:length(xcor13_fft),abs(xcor13_fft))
subplot(2,3,3)
plot(1:length(xcor14_fft),abs(xcor14_fft))
subplot(2,3,4)
plot(1:length(xcor23_fft),abs(xcor23_fft))
subplot(2,3,5)
plot(1:length(xcor24_fft),abs(xcor24_fft))
subplot(2,3,6)
plot(1:length(xcor34_fft),abs(xcor34_fft))
title('Cross-correlation using fft')
%}
% Phase Transform (PHAT)
xcor12_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr2)))./(abs(fft(sigr1)).*abs(fft(sigr2))))));
xcor13_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr3)))./(abs(fft(sigr1)).*abs(fft(sigr3))))));
xcor14_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr4)))./(abs(fft(sigr1)).*abs(fft(sigr4))))));
xcor15_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr5)))./(abs(fft(sigr1)).*abs(fft(sigr5))))));
xcor16_PHAT=abs(fftshift(ifft((fft(sigr1).*conj(fft(sigr6)))./(abs(fft(sigr1)).*abs(fft(sigr6))))));

figure()
hold on;box on
subplot(2,3,1)
plot(1:length(xcor12_PHAT),(xcor12_PHAT))
subplot(2,3,2)
plot(1:length(xcor13_PHAT),(xcor13_PHAT))
subplot(2,3,3)
plot(1:length(xcor14_PHAT),(xcor14_PHAT))
subplot(2,3,4)
plot(1:length(xcor15_PHAT),(xcor15_PHAT))
subplot(2,3,5)
plot(1:length(xcor16_PHAT),(xcor16_PHAT))

title('Generalized Cross-correlation using phase transform')

%{
% Smoothed Coherence Transform (SCOT)
xcor12_SCOT=fftshift(ifft((fft(sigr1).*conj(fft(sigr2)))./(sqrt(fft(sigr1).*conj(fft(sigr1)).*fft(sigr2).*conj(fft(sigr2))))));
xcor13_SCOT=fftshift(ifft((fft(sigr1).*conj(fft(sigr3)))./(sqrt(fft(sigr1).*conj(fft(sigr1)).*fft(sigr3).*conj(fft(sigr3))))));
xcor14_SCOT=fftshift(ifft((fft(sigr1).*conj(fft(sigr4)))./(sqrt(fft(sigr1).*conj(fft(sigr1)).*fft(sigr4).*conj(fft(sigr4))))));
xcor23_SCOT=fftshift(ifft((fft(sigr2).*conj(fft(sigr3)))./(sqrt(fft(sigr2).*conj(fft(sigr2)).*fft(sigr3).*conj(fft(sigr3))))));
xcor24_SCOT=fftshift(ifft((fft(sigr2).*conj(fft(sigr4)))./(sqrt(fft(sigr2).*conj(fft(sigr2)).*fft(sigr4).*conj(fft(sigr4))))));
xcor34_SCOT=fftshift(ifft((fft(sigr3).*conj(fft(sigr4)))./(sqrt(fft(sigr3).*conj(fft(sigr3)).*fft(sigr4).*conj(fft(sigr4))))));

figure()
hold on;box on
subplot(2,3,1)
plot(1:length(xcor12_SCOT),abs(xcor12_SCOT))
subplot(2,3,2)
plot(1:length(xcor13_SCOT),abs(xcor13_SCOT))
subplot(2,3,3)
plot(1:length(xcor14_SCOT),abs(xcor14_SCOT))
subplot(2,3,4)
plot(1:length(xcor23_SCOT),abs(xcor23_SCOT))
subplot(2,3,5)
plot(1:length(xcor24_SCOT),abs(xcor24_SCOT))
subplot(2,3,6)
plot(1:length(xcor34_SCOT),abs(xcor34_SCOT))
%}
%% Time Difference of Arrival Estimation--Peak detection and distance calculation
Actual_Arrival=zeros(1,6);
Actual_Arrival(1)=(sqrt(rx^2+ry^2+rz^2)/Propagation_Speed);
Actual_Arrival(2)=(sqrt((rx-d)^2+ry^2+rz^2)/Propagation_Speed);
Actual_Arrival(3)=(sqrt(rx^2+(ry-d)^2+rz^2)/Propagation_Speed);
Actual_Arrival(4)=(sqrt((rx+d)^2+ry^2+rz^2)/Propagation_Speed);
Actual_Arrival(5)=(sqrt(rx^2+(ry+d)^2+rz^2)/Propagation_Speed);
Actual_Arrival(6)=(sqrt(rx^2+ry^2+(rz-d)^2)/Propagation_Speed);

Actual_difference=zeros(1,4);
Actual_difference(1)=Actual_Arrival(1)-Actual_Arrival(2);
Actual_difference(2)=Actual_Arrival(1)-Actual_Arrival(3);
Actual_difference(3)=Actual_Arrival(1)-Actual_Arrival(4);
Actual_difference(4)=Actual_Arrival(1)-Actual_Arrival(5);
Actual_difference(5)=Actual_Arrival(1)-Actual_Arrival(6);

Peak_Value=zeros(1,5);
Estimated_difference=zeros(1,5);
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
end
Estimated_difference=Estimated_difference/fs;
Distance_difference=Estimated_difference*Propagation_Speed;
Actual_Distance=Actual_difference*Propagation_Speed;

Distance_difference
Actual_Distance
%% Triangulation
%Matlab syms method, direct calculation
%{
syms x y z
[x,y,z]=solve(sqrt(x^2+y^2+z^2)-sqrt((x-d)^2+y^2+z^2)==Distance_difference(1),...
sqrt(x^2+y^2+z^2)-sqrt(x^2+(y-d)^2+z^2)==Distance_difference(2),...
sqrt(x^2+y^2+z^2)-sqrt((x+d)^2+y^2+z^2)==Distance_difference(3),...
sqrt(x^2+y^2+z^2)-sqrt(x^2+(y+d)^2+z^2)==Distance_difference(4));
%}

%Far-field approximation method 
u=Distance_difference(1)/d;
v=Distance_difference(2)/d;
w=Distance_difference(5)/d;
%Use law of cosine%
u,v,w
