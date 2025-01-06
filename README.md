## Setup
Follow the Xilinx VCU118 XDMA-based Getting Started Guide from https://docs.fires.im/en/1.17.1 (FrieSim 1.17.1 docs).

Instead of cloning the official FireSim repo, clone this repo. During repo setup, avoid overwriting the config.yaml files in the deploy directory. Making a copy of them before following any repo setup steps and then adding them back is an easy way to do this.

## Creating figures
https://github.com/crsullivan13/Graphing-BankDefense/tree/2fa3a1c1b6c9b24de34ccd5106bc7954d178e8a9

The Graphing-BankDefense submodule contains directory structure and gnuplot scripts for creating figures. Our collected data is included and you can build the figures from that (see submodule for details). Note that we don't include the SPEC2017 data.

# Running and Building Workloads for FireSim Figures

## Building Workloads

1. **Navigate to the `sw/firesim-software` Subdirectory**  
   - You may need to initialize submodules before proceeding.  

2. **Run the `build-workloads.sh` Script**  
   - To create a specific set of workloads, pass the corresponding figure number as an argument.  
     For example:  
     ```bash
     ./build-workloads.sh fig11
     ```  
   - To build all figure workloads, pass `all` as an argument. Note that this process will take a while:  
     ```bash
     ./build-workloads.sh all
     ```  

   **Note**: SPEC2017 benchmarks are not included in these workloads.

---

## Running Workloads and Generating Figures

1. **Return to the FireSim Root Directory**  
   - Once you have built the workloads for the figures you would like to generate, navigate back to the root of your FireSim directory.  

2. **Run Workload Scripts for Each Figure**  
   - For each figure, there is a dedicated script to execute all the necessary workloads. Simply run the script and wait for the workloads to finish.  

3. **Generate Figures**  
   - Follow the instructions in the graphing submodule to generate the figures.  

---

Our setup assumes a single local VCU118 FPGA, we have found automating the workload running process is a bit finicky. Currently, when automating all of the workloads, some data will fail to generate correctly. If this occurs, you will need to manually run the workloads by modifying the config_runtime.yaml to contain the correct hwdb config/workload and using the corresponding FireSim commands (infrasetup and runworkload). For generating the figures from manually run workloads, you should place the full path to the results directory that the simulator outputs in the graphing submodule. Ensure that the order these are listed in the graphing submodule follow the same order as if they were automatically generated (see workload figures scripts).

## Where is regulation unit code?
https://github.com/crsullivan13/BwReg/tree/BRU - This branch of the repo contains the baseline BRU from "_Farzad Farshchi, Qijing Huang, and Heechul Yun. BRU: Bandwidth Regulation Unit for Real-Time Multicore Processors._"

https://github.com/crsullivan13/BwReg/tree/per-bank-monitor - This branch of the repo contains the parameterized per-bank regulator
