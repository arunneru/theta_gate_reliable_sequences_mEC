#!/bin/bash
python scripts/write_noise.py 0 4 && g++ -O3 -Ofast -std=c++11 -I../insilico-0.25/include -o bins/insilico_I2E2_switching_toggle_0trial.out main_files/main_I2E2_switching_toggle.cpp ;
