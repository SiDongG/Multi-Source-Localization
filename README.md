# Multi-Source-Localization

MATRIX VOICE MODULE ACOUSTIC LOCALIZATION

This is an TDOA and RSS hybrid localization algorithm for MATRIX VOICE MODULE. 
The algorithm in LLS.py (linear least square) runs a C++ executable in python to record raw files for all 8 channels, then python script runs wav file conversion with subprocess. The algorithm then does GCC, peak detection, sampling rate conversions to calculate relative distances. 
The second part of the algorithm does multilateration with error filters for angle information and updates LED displays and GUI on every loop.  
