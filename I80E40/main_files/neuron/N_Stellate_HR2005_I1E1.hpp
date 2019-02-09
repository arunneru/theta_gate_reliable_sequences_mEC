#ifndef INCLUDED_N_STELLATE_HR2005_HPP
#define INCLUDED_N_STELLATE_HR2005_HPP
#include "insilico/core/engine.hpp"
#include "currents/I_Na_Stellate_HR2005.hpp"
#include "currents/I_NaP_Stellate_HR2005.hpp"
#include "currents/I_Leak_Stellate_HR2005.hpp"
#include "currents/I_K_Stellate_HR2005.hpp"
#include "currents/I_Hs_Stellate_HR2005.hpp"
#include "currents/I_Hf_Stellate_HR2005.hpp"
//#include "currents/I_Hs_Stellate_HR2005_consttau.hpp"
//#include "currents/I_Hf_Stellate_HR2005_consttau.hpp"
#include "currents/I_PeriodicPulse.hpp"
#include "currents/I_OscillatoryDrive.hpp"
#include "../../configure_files/noise.hpp"

namespace insilico {

class N_Stellate_HR2005 : public Neuron {
 public:
  void ode_set(state_type &variables, state_type &dxdt, const double t, unsigned index) {
    
    //std::cout <<" exc " << index << std::endl ;
    
    int v_index = engine::neuron_index(index, "v");
    double v = variables[v_index];
    // incoming synaptic currents
    
    double I_syn = 0;
    
    std::vector<unsigned int> s_indices = engine::get_pre_neuron_indices(index, "s");
    std::vector<double> esyn_values = engine::get_pre_neuron_values(index, "esyn");
    std::vector<double> gsyn_values = engine::get_pre_neuron_values(index, "gsyn");
    std::vector<double> pre_neurons = engine::get_pre_neuron_values(index, "pre");

    for(std::vector<int>::size_type iterator = 0; iterator < s_indices.size(); ++iterator) {
      I_syn = I_syn + gsyn_values[iterator]*variables[s_indices[iterator]] * (v - esyn_values[iterator]);
    }

    engine::neuron_value(index,"I_syn",I_syn);
    
    // ODE set
    I_Na_Stellate_HR2005::current(variables, dxdt, t, index);
    I_K_Stellate_HR2005::current(variables, dxdt, t, index);
    I_Leak_Stellate_HR2005::current(variables, dxdt, t, index);
    I_NaP_Stellate_HR2005::current(variables, dxdt, t, index);
    I_Hs_Stellate_HR2005::current(variables, dxdt, t, index);
    I_Hf_Stellate_HR2005::current(variables, dxdt, t, index);
    I_PeriodicPulse::current(variables, dxdt, t, index);
    I_OscillatoryDrive::current(variables,dxdt,t,index);
    
    double I_Na = engine::neuron_value(index, "I_Na_Stellate_HR2005");
    double I_K = engine::neuron_value(index, "I_K_Stellate_HR2005");
    double I_Leak = engine::neuron_value(index, "I_Leak_Stellate_HR2005");
    double I_NaP = engine::neuron_value(index,"I_NaP_Stellate_HR2005");
    double I_Hs = engine::neuron_value(index,"I_Hs_Stellate_HR2005");
    double I_Hf = engine::neuron_value(index,"I_Hf_Stellate_HR2005");
    double I_Ext = engine::neuron_value(index, "I_PeriodicPulse");
    double I_DC = engine::neuron_value(index, "I_DC");
    double I_OscillatoryDrive = engine::neuron_value(index, "I_OscillatoryDrive");

    double current = 0;
    current = noise::inject(index);
    double ampNoise = engine::neuron_value(index,"ampNoise");
    double I_Noise = ampNoise*current*(v + 65.0) ;
        
    dxdt[v_index] = I_Ext + I_DC - I_Na - I_K - I_Leak - I_NaP - I_Hs - I_Hf -  I_Noise - I_syn - I_OscillatoryDrive;//0.2*I_syn;
  } // function ode_set
}; // class N_SquidAxon_HH1952
} // insilico

#endif
