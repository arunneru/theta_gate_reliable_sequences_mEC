/*
 synapse/S_DefaultSynapse.hpp - Default non-specialized synapse with last spike logic

 Copyright (C) 2014 Pranav Kulkarni, Collins Assisi Lab, IISER, Pune <pranavcode@gmail.com>

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

#ifndef INCLUDED_S_TANHSYNAPSE_HPP
#define INCLUDED_S_TANHSYNAPSE_HPP

#include "insilico/core/engine.hpp"
#include <cmath>

namespace insilico {

class S_TanHSynapse : public Synapse {
 public:
  void ode_set(state_type &variables, state_type &dxdt, const double t, unsigned index) {
    int s_index = engine::synapse_index(index, "s");
    
    double s = variables[s_index];

    int pre_neuron_index = engine::synapse_value(index, "pre");
    unsigned v_index = engine::neuron_index(pre_neuron_index, "v");
    double v = variables[v_index];

    // constantds from file
    double tau_r = engine::synapse_value(index, "tau_r");
    double tau_d = engine::synapse_value(index, "tau_d");

    double rho = (1+tanh(v/4.0))/2.0;

    // ODE set
    dxdt[s_index] = (rho/tau_r)*(1-s)-(1.0/tau_d)*s;

  } // function ode_set
}; // class S_DefaultSynapse

} // insilico

#endif
