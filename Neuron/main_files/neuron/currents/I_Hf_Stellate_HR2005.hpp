#ifndef INCLUDED_I_HF_STELLATE_HR2005_HPP
#define INCLUDED_I_HF_STELLATE_HR2005_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_Hf_Stellate_HR2005 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double eh = -20.0;

    double gh = engine::neuron_value(index, "gh");//1.5
    int v_index = engine::neuron_index(index, "v");
    int mhf_index = engine::neuron_index(index, "mhf");
    double tau_fact = engine::neuron_value(index, "tau_fact");
        
    double v = variables[v_index];
    double mhf = variables[mhf_index];
    
    double mhfinf = 1.0/(1.0+exp((v+79.2)/9.78));
    double mhftau = tau_fact*(0.51/(exp((v-1.7)/10.0)+exp(-(v+340.0)/52.0))+1.0);
	
    // ODE set
    dxdt[mhf_index]=(mhfinf-mhf)/mhftau;

    // Current
    engine::neuron_value(index, "I_Hf_Stellate_HR2005", (gh * 0.65 * mhf * (v - eh)));

  } // function current
}; // class I_Hf_Stellate_HR2005

} // insilico

#endif
