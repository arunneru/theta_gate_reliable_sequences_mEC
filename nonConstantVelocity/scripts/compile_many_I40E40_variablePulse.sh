#!/bin/bash
python scripts/write_noise.py 0 80 && g++ -O3  -std=c++11 -I../insilico-0.25/include -o bins/insilico_I40E40_varPulse_0trial.out main_files/main_I40E40_varPulse.cpp ;
