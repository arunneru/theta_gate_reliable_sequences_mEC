/*
 current/I_OscillatoryDrive.hpp - External oscillatory conductance based current to be injected into the neuron

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
A oscillatory current to be injected into the neuron.
neuron.
*/

#ifndef INCLUDED_I_OSCILLATORYDRIVE_HPP
#define INCLUDED_I_OSCILLATORYDRIVE_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_OscillatoryDrive {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    int v_index = engine::neuron_index(index,"v");

    double v = variables[v_index];
    double freq = engine::neuron_value(index, "freq");      //frequency of oscillation
    double phase = engine::neuron_value(index, "thetaPhase");    //phase of the oscillation
    double ampl = engine::neuron_value(index, "ampSin");      //amplitude
    double vth = engine::neuron_value(index,"V_th_Osc"); //threshold of the drive
    double I_OscillatoryDrive = ampl*(sin(2*M_PI*freq*t/1000.0 + phase))*(v - vth); //

    // Current
    engine::neuron_value(index, "I_OscillatoryDrive", I_OscillatoryDrive);

  } // function current
}; // class I_OscillatoryDrive

} // insilico

#endif
