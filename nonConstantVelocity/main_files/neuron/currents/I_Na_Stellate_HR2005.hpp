#ifndef INCLUDED_I_NA_STELLATE_HR2005_HPP
#define INCLUDED_I_NA_STELLATE_HR2005_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_Na_Stellate_HR2005 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double gna = 52, ena = 55;

    int v_index = engine::neuron_index(index, "v");
    int m_index = engine::neuron_index(index, "m");
    int h_index = engine::neuron_index(index, "h");
    
    double v = variables[v_index];
    double m = variables[m_index];
    double h = variables[h_index];
    
    double alpha_m = -0.1*(v+23.0)/(exp(-0.1*(v+23.0))-1.0);
    double beta_m  = 4.0*exp(-(v+48) /18.0);

    double alpha_h = 0.07*exp(-(v+37.0)/ 20.0);
    double beta_h  = 1.0/(exp(-0.1 * (v+7.0)) + 1.0);

    double tau_m = 1.0/(alpha_m+beta_m);
    double m_inf = alpha_m*tau_m;

    double tau_h = 1.0/(alpha_h+beta_h);
    double h_inf = alpha_h*tau_h;

    // ODE set
    //dxdt[m_index]=(alpha_m*(1-m)-beta_m*m);
    dxdt[m_index]=(m_inf - m)/tau_m;
    //dxdt[h_index]=(alpha_h*(1-h)-beta_h*h);
    dxdt[h_index]=(h_inf - h)/tau_h;

    // Current
    engine::neuron_value(index, "I_Na_Stellate_HR2005", (gna * pow(m, 3) * h * (v - ena)));

  } // function current
}; // class I_Na_Stellate_HR2005

} // insilico

#endif
