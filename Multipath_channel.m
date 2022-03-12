clear;clc;close all;
%% Multipath Localization TOA 
% Author: Sidong Guo 

%% Initialization
rx=5;ry=0;rz=0;

rxULA = phased.OmnidirectionalMicrophoneElement;
rxpos1 = [0;0;0];
rxvel1 = [0;0;0];

srcpos = [rx;ry;rz];
srcvel = [0;0;0];
srcax = azelaxes(0,0);
srcULA = phased.OmnidirectionalMicrophoneElement;

Carrier_Fre = 1.6e9;           
Propagation_Speed = 300000000;   
Operating_range = 10;     
pri = (2*Operating_range)/Propagation_Speed;
prf = 1/pri;
bw = 5e3;         
fs = 3e9;      
waveform = phased.LinearFMWaveform('SampleRate',fs,'SweepBandwidth',bw,'PRF',prf,'PulseWidth',pri/10);
signal = waveform();

radiator = phased.WidebandRadiator('Sensor',srcULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);
collector1 = phased.WidebandCollector('Sensor',rxULA,'PropagationSpeed',Propagation_Speed,'SampleRate',fs,...
    'CarrierFrequency',Carrier_Fre);

Num_path=5;

channel1 = phased.MultipathChannel('OperatingFrequency',Carrier_Fre,'SampleRate',fs);
rayleighchan = comm.RayleighChannel( ...
    'SampleRate',fs, ...
    'PathDelays',[0 1.5e-4 1.8e-4], ...
    'AveragePathGains',[2 3 0.4], ...
    'NormalizePathGains',true, ...
    'RandomStream','mt19937ar with seed', ...
    'Seed',22, ...
    'PathGainsOutputPort',true);

[~,ang1_transmit] = rangeangle(rxpos1,srcpos,srcax);

sig_transmit = radiator(signal,ang1_transmit);
sigp1 = rayleighchan(sig_transmit(1),srcpos,rxpos1,srcvel,rxvel1);


