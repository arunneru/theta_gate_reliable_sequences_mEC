#ifndef INCLUDED_I_HS_STELLATE_HR2005_HPP
#define INCLUDED_I_HS_STELLATE_HR2005_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_Hs_Stellate_HR2005 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double eh = -20.0;

    double gh = engine::neuron_value(index, "gh");//1.5
    int v_index = engine::neuron_index(index, "v");
    int mhs_index = engine::neuron_index(index, "mhs");
    double tau_fact = engine::neuron_value(index, "tau_fact");
    
    double v = variables[v_index];
    double mhs = variables[mhs_index];
    
    double mhsinf = 1.0 /(pow((1.0 + exp((v+2.83)/15.9)),58));
    //double mhsinf = 1.0/(1.0+exp((v+71.3)/7.9));
    double mhstau = tau_fact*(5.6/(exp((v-1.7)/14.0)+exp(-(v+260.0)/43.0))+1.0);
	
    // ODE set
    dxdt[mhs_index]=(mhsinf-mhs)/mhstau;

    // Current
    engine::neuron_value(index, "I_Hs_Stellate_HR2005", (gh * 0.35 * mhs * (v - eh)));

  } // function current
}; // class I_Hs_Stellate_HR2005

} // insilico

#endif
