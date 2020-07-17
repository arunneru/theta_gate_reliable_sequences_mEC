#!/bin/bash
python scripts/write_noise.py 0 1 && g++ -O3 -Ofast -std=c++11 -I../insilico-0.25/include -o bins/insilico_Neuron_0trial.out main_files/main_Neuron.cpp ;
