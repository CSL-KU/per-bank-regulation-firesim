## Setup
Follow the Xilinx VCU118 XDMA-based Getting Started Guide from https://docs.fires.im/en/1.17.1 (FrieSim 1.17.1 docs).

Instead of cloning the official FireSim repo, clone this repo. During repo setup, avoid overwriting the config .yaml files in the deploy directory.

## Creating figures
The Graphing-BankDefense submodule contains directory structure and gnuplot scripts for creating figures. Our collected data is included and you can build the figures from that (see submodule for details). Note that we don't include the SPEC2017 data.

## Recreating data
First, navigate to the sw/firesim-software subdirectory (you may need to init submodules). Run the build-workloads.sh script. You can pass the figure numder to create a specific set of workloads. For example, to recreate figure 11, you would run ./build-workloads.sh fig11. You can also pass "all" to build all figure workloads (this will take a while). Note that we don't include the SPEC2017 benchmarks in these workloads.

Once you have built the workloads for the figures you would like to generate, navigate back to the root of your FireSim directory. For each figure, there is a script that will run all of the necessary workloads. Simply run the script, wait for the workloads to finish and then follow the steps in the graphing submodule to generate figures.

Since our setup assumes a single local VCU118 FPGA, the workload running process is a bit finicky. Currently, when automating all of the workloads, some data will fail to generate correctly. If this occurs, you will need to manually run the workloads by modifying the config_runtime.yaml to contain the correct hwdb config/workload and using the corresponding FireSim commands (infrasetup and runworkload).

## Where is regulation unit code?
https://github.com/crsullivan13/BwReg/tree/per-bank-monitor
