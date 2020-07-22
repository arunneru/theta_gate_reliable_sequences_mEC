# theta_gates_reliable_sequences_mEC
Helper files and libraries used for simulations

## Usage

### Step 1 - Aquaint with insilico
For a general introduction follow README.md in https://github.com/CollinsAssisi/insilico.
I have included in each subfolder, a seperate insilico folder with all the header files necessary for running the simulations.
Each folder is self-sufficient as a result.

## Step 2 - Interfacing python with insilico
I have used python and bash in linux to generate the helper files (nsets-holds neuron paramters, ssets-holds synapse parameters) required for insilico and to compile and run the simulations.

### Step 2a
Follow the notebook How_To_Neuron to get a sense of how to use insilico + python to run a simulation of a single neuron
### Step 2b
Follow the notebook How_To_Network to get a sense of how to use insilico + python to run a simulation of synaptically coupled neurons

## Step 3 -  Steps to generate figures

Fig 1.

enter into the folder "I2E2"

1. Generate the helper files (nsets, ssets)

```python
python scripts/gen_nsets_I2E2_autonomous.sh
python scripts/gen_nsets_I2E2_autonomous.sh
```





