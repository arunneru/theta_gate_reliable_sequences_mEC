#include "insilico/core.hpp"
#include "neuron/N_InterNeuron_Wang96_I2E2_switch_autonomous.hpp"
#include "neuron/N_Stellate_HR2005_I1E1_ExtPulse.hpp"
#include "synapse/S_TanHSynapse.hpp"
#include <boost/numeric/odeint.hpp> 
#include <fstream> 
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <vector> 
#include <iostream> 
#include <fstream> 
#include <map> 
#include <random> 

//#include <omp.h>
//#include <boost/numeric/odeint/external/openmp/openmp.hpp>
using namespace boost::numeric::odeint; 
using namespace insilico; 
using namespace std;

int main(int argc, char **argv) {
	configuration::initialize(argc, argv);

	configuration::observe("v");

        configuration::observe_skipiters(10);

        engine::generate_neuron<N_Stellate_HR2005>(1);
	engine::generate_neuron<N_InterNeuron_Wang96>(1);
	engine::generate_synapse<S_TanHSynapse>(2);

	state_type variables = engine::get_variables();
	integrate_const(euler<state_type>(), engine::driver(), variables,
	0.0, 10000.0, 0.01, configuration::observer());
	configuration::finalize();
}
