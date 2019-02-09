#ifndef INCLUDED_I_LEAK_STELLATE_HR2005_HPP
#define INCLUDED_I_LEAK_STELLATE_HR2005_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_Leak_Stellate_HR2005 {
 public:
  static void current(state_type &variables, state_type &dxdt, const double t, int index) {
    double gl = 0.5, el = -65.0;
    
    int v_index = engine::neuron_index(index, "v");
    double v = variables[v_index];
    //std::cout<<v<<std::endl;
    // Current
    engine::neuron_value(index, "I_Leak_Stellate_HR2005", (gl * (v - el)));

  } // function current
}; // class I_Leak_Stellate

} // insilico

#endif
