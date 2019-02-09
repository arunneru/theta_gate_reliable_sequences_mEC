#ifndef INCLUDED_I_LEAK_INTERNEURON_WANG96_HPP
#define INCLUDED_I_LEAK_INTERNEURON_WANG96_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_Leak_InterNeuron_Wang96 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double gl = engine::neuron_value(index, "gl");
    //double gl = 0.1,
    double el = -65.0;

    int v_index = engine::neuron_index(index, "v");
    double v = variables[v_index];

    // Current
    engine::neuron_value(index, "I_Leak_InterNeuron_Wang96", (gl * (v - el)));

  } // function current
}; // class I_Leak_InterNeuron_Wang96

} // insilico

#endif
