#ifndef INCLUDED_I_K_INTERNEURON_WANG96_HPP
#define INCLUDED_I_K_INTERNEURON_WANG96_HPP
#include "insilico/core/engine.hpp"

namespace insilico {

class I_K_InterNeuron_Wang96 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double gk = 11.0;//9.0//11.0
    double ek = -90.0;

    int v_index = engine::neuron_index(index, "v");
    int n_index = engine::neuron_index(index, "n");
    
    double v = variables[v_index];
    double n = variables[n_index];
    
    double alpha_n = 0.01*(v+34.0)/(1.0-exp(-0.1*(v+34.0)));
    double beta_n = 0.125*exp(-(v+44.0)/80.0);
    double phi = 5.0;//engine::neuron_value(index,"phi");
    // ODE set
    dxdt[n_index]= phi*(alpha_n*(1-n)-beta_n*n);

    // Current
    engine::neuron_value(index, "I_K_InterNeuron_Wang96", (gk * pow(n, 4) * (v - ek)));

  } // function current
}; // class I_K_InterNeuron_Wang96

} // insilico

#endif
