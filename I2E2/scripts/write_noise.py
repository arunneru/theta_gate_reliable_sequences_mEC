import sys

def write_noise(l_pars):
    seed = l_pars[0]
    nNeurons = l_pars[1]
    
    str2write = "#pragma once\n#include \"insilico/core/engine.hpp\"\n#include <cmath>\n#include<random>\n#include<vector>\n\nnamespace insilico { namespace noise {\n\nstd::mt19937_64 gen(%s);\nstd::normal_distribution<double> dist(0,1);\nstd::vector<double> randomize(%s);\ndouble inject(unsigned index)\n {\n\trandomize[index]= dist(gen);\n\treturn randomize[index];\n\n}\n} } // insilico\n"%(seed,nNeurons)
    outfile = open("noise.hpp","w")

    outfile.write(str2write)
    outfile.close()

if __name__ == '__main__':
    write_noise([sys.argv[1],sys.argv[2]])

