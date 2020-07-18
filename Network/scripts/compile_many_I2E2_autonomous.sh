#!/bin/bash
python scripts/write_noise.py 0 2 && g++ -O3 -Ofast -std=c++11 -I../insilico-0.25/include -o bins/insilico_Network.out main_files/main_Network.cpp ;
