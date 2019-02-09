#ifndef INCLUDED_I_NAP_STELLATE_HR2005_HPP
#define INCLUDED_I_NAP_STELLATE_HR2005_HPP

#include "insilico/core/engine.hpp"

namespace insilico {

class I_NaP_Stellate_HR2005 {
	public:
		static void current(state_type &variables, state_type &dx_dt, const double t, int index){
                  double gNaP = 0.5;//0.03;//0.5;
                  double ENa = 55;
			
			int v_index = engine::neuron_index(index,"v");
			int ms_index = engine::neuron_index(index,"ms");

			double v = variables[v_index];
			double ms = variables[ms_index];
                        double shift = 0.0;
                        
			//double alpha_ms = 1.0/(0.15*(1.0+exp(-(v+38.0)/6.5)));
			//double beta_ms = exp(-(v+38.0)/6.5)/(0.15*(1.0+exp(-(v+38.0)/6.5)));
			
			double vr = v ;
			double tau_ms = 0.15;
			double ms_inf = 1.0/(1.0+exp(-(vr+38.0+shift)/6.5));; 
			//dx_dt[ms_index] = alpha_ms*(1.0-ms)-beta_ms*ms;
			dx_dt[ms_index] = (ms_inf - ms)/tau_ms;
			engine::neuron_value(index, "I_NaP_Stellate_HR2005", (gNaP * ms * (v - ENa)));
		}

};


} //insilico

#endif
