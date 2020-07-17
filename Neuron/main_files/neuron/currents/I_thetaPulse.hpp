/*
 current/I_TravelingPulse.hpp - External current to be injected into the neuron

 Copyright (C) 2016 Collins Assisi Lab, IISER, Pune

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

/*
 Brief:
A pulse like current to be injected into the neuron. The baseline, maximum amplitude, start, end time
and the rise and fall time can be independently specified in the neuron.isf file for the respective
neuron.
*/

#ifndef INCLUDED_I_THETAPULSE_HPP
#define INCLUDED_I_THETAPULSE_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_thetaPulse {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {

    double PulseDuration;      //duration of each cycle covering all neurons
    double tau_rise = 2 ; //engine::neuron_value(index, "tau_rise");                //Exponential rise time
    double tau_fall = 2 ; //engine::neuron_value(index, "tau_fall");                //Exponential fall time
    double PulseMax = engine::neuron_value(index, "highDCMax");                //Pulse Saturation
    double PulseMin = engine::neuron_value(index, "highDCMin"); //Pulse baseline
    double pulsewidth = engine::neuron_value(index, "pulsewidth");
      
    int numIs = 2;

    double T;
    int neur_ind;
    double PulseEnd;
    double PulseStart;
    double P = PulseMin;
    
    if (index == 3){
      PulseDuration = engine::neuron_value(index, "highDCDuration");

      T = fmod(t,PulseDuration);
      neur_ind = index - numIs ;
      PulseStart =  PulseDuration - (neur_ind + 1) * (PulseDuration / numIs);
      PulseEnd = PulseStart + pulsewidth;//( neur_ind + 1 ) * (PulseDuration / numEs);
      P = PulseMin;
      if (T < PulseStart){
        P = PulseMin;
      }     
      else if ((T > PulseStart) && (T < PulseEnd)){
        P = PulseMax + (PulseMin - PulseMax)*exp(-(T - PulseStart)/tau_rise);
      }
      else if (T >= PulseEnd){
        P = PulseMin + (PulseMax - PulseMin)*exp(-(T - PulseEnd)/tau_fall);
      }
  
    }
   
    // Current
    engine::neuron_value(index, "I_thetaPulse", P);

  } // function current
}; // class I_PeriodicPulse

} // insilico

#endif
