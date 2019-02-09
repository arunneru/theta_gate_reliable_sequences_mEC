#ifndef INCLUDED_I_NA_INTERNEURON_WANG96_HPP
#define INCLUDED_I_NA_INTERNEURON_WANG96_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_Na_InterNeuron_Wang96 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double gna = engine::neuron_value(index, "gna");
    double ena = 55.0;
    double phi = 5.0;//engine::neuron_value(index, "phi");
    
    int v_index = engine::neuron_index(index, "v");
    int h_index = engine::neuron_index(index, "h");
    
    double v = variables[v_index];
    double h = variables[h_index];
    
    double alpha_m = (0.1*(v+35.0)/(1.0-exp(-(v+35.0)/10.0)));
    double beta_m = 4.0*exp(-(v+60.0)/18.0);
    double m = alpha_m/(alpha_m+beta_m);

    
    double alpha_h = 0.07*exp(-(v+58) / 20.0);
    double beta_h  = 1.0/(exp(-0.1*(v+28.0))+1.0);
    
    // ODE set
    dxdt[h_index] = (alpha_h*(1-h)-beta_h*h);

    // Current
    engine::neuron_value(index, "I_Na_InterNeuron_Wang96", (gna * pow(m, 3) * h * (v - ena)));

  } // function current
}; // class I_Na_InterNeuron_Wang96

} // insilico

#endif
