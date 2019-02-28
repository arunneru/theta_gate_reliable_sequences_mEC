#ifndef INCLUDED_I_K_STELLATE_HR2005_HPP
#define INCLUDED_I_K_STELLATE_HR2005_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_K_Stellate_HR2005 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double gk = 11, ek = -90;

    int v_index = engine::neuron_index(index, "v");
    int n_index = engine::neuron_index(index, "n");

    double v = variables[v_index];
    double n = variables[n_index];

    double alpha_n = -0.01*(v+27.0)/(exp(-0.1*(v+27.0))-1.0);
    double beta_n = 0.125*exp(-(v+37.0) / 80.0);

    // ODE set
    double tau_n = 1.0/(alpha_n+beta_n);
    double n_inf = alpha_n*tau_n ;
    
    dxdt[n_index]=(n_inf - n)/tau_n;

    // Current
    engine::neuron_value(index, "I_K_Stellate_HR2005", (gk * pow(n,4) * (v - ek)));

  } // function current
}; // class I_K_Stellate_HR2005

} // insilico



#endif
