#ifndef INCLUDED_N_INTERNEURON_WANG96_HPP
#define INCLUDED_N_INTERNEURON_WANG96_HPP

#include <cmath>
#include <iostream>
#include "insilico/core/engine.hpp"

#include "currents/I_Na_InterNeuron_Wang96_hetero.hpp"
#include "currents/I_Leak_InterNeuron_Wang96_hetero.hpp"
#include "currents/I_K_InterNeuron_Wang96_hetero.hpp"
#include "currents/I_PeriodicPulse.hpp"
#include "currents/I_travelingPulse_clockwise_otherwise_phaseblocking.hpp"
#include "currents/I_travelingSwitch.hpp"
#include "currents/I_OscillatoryDrive_thphase.hpp"

#include "../../configure_files/noise.hpp"

namespace insilico {

class N_InterNeuron_Wang96 : public Neuron {
 public:
  void ode_set(state_type &variables, state_type &dxdt, const double t, unsigned index) {

    //std::cout << " index is I neuron " << index << std::endl ;

    int v_index = engine::neuron_index(index, "v");

    double v = variables[v_index];
    // note the spike
    
    double I_syn;// = engine::neuron_value(index,"I_syn");
    
    I_syn = 0;
    std::vector<unsigned int> s_indices = engine::get_pre_neuron_indices(index, "s");
    //std::cout<<s_indices[0]<<std::endl;
    std::vector<double> esyn_values = engine::get_pre_neuron_values(index, "esyn");
    std::vector<double> gsyn_values = engine::get_pre_neuron_values(index, "gsyn");

    for(std::vector<int>::size_type iterator = 0; iterator < s_indices.size(); ++iterator) {
      I_syn = I_syn + gsyn_values[iterator]*variables[s_indices[iterator]] * (v - esyn_values[iterator]);
    }

    engine::neuron_value(index,"I_syn",I_syn);

    // ODE set
    I_Na_InterNeuron_Wang96::current(variables, dxdt, t, index);
    I_K_InterNeuron_Wang96::current(variables, dxdt, t, index);
    I_Leak_InterNeuron_Wang96::current(variables, dxdt, t, index);
    I_PeriodicPulse::current(variables, dxdt, t, index);
    I_travelingPulse::current(variables, dxdt, t, index);
    I_travelingSwitch::current(variables, dxdt, t, index);
    I_OscillatoryDrive::current(variables,dxdt,t,index);
    //I_PulseForOsc::current(variables,dxdt,t,index);

    double I_Na = engine::neuron_value(index, "I_Na_InterNeuron_Wang96");
    double I_K = engine::neuron_value(index, "I_K_InterNeuron_Wang96");
    double I_Leak = engine::neuron_value(index, "I_Leak_InterNeuron_Wang96");
    double I_Ext = engine::neuron_value(index, "I_PeriodicPulse");
    double I_DC = engine::neuron_value(index, "I_DC");
    double I_OscillatoryDrive = engine::neuron_value(index, "I_OscillatoryDrive");
    double I_TravelingPulse = engine::neuron_value(index, "I_travelingPulse");
    double I_TravelingSwitch = engine::neuron_value(index, "I_travelingSwitch");
    //double I_PulseForOsc = 

    double current = 0;
    current = noise::inject(index);
    double ampNoise = engine::neuron_value(index, "ampNoise");
    double I_Noise = ampNoise*current*(v+65);

    engine::neuron_value(index,"I_Noise",I_Noise);
    
    dxdt[v_index] = I_Ext + I_DC + I_TravelingSwitch * I_TravelingPulse - I_Na - I_K - I_Leak - I_syn - I_Noise - I_OscillatoryDrive ;
  } // function ode_set
}; // class N_InterNeuron_Wang96

} // insilico

#endif
