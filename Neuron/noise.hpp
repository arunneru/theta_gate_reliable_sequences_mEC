#pragma once
#include "insilico/core/engine.hpp"
#include <cmath>
#include<random>
#include<vector>

namespace insilico { namespace noise {

std::mt19937_64 gen(0);
std::normal_distribution<double> dist(0,1);
std::vector<double> randomize(1);
double inject(unsigned index)
 {
	randomize[index]= dist(gen);
	return randomize[index];

}
} } // insilico
