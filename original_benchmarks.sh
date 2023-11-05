#!/bin/bash

# Define the list of simulators and corresponding Python scripts
declare -A simulators
simulators["neuron"]="neuron_hh.py"
simulators["brian2"]="brian2_hh.py"

# Loop over each simulator and run the simulation
for sim in "${!simulators[@]}"; do
    script_name=${simulators[$sim]}

    # Check if the Python script exists
    if [ ! -f "$script_name" ]; then
        echo "Error: Python script '$script_name' does not exist."
        continue
    fi

    echo "Running simulation with $sim using script $script_name..."

    # Use /usr/bin/time to measure memory usage and time
    /usr/bin/time -f "\nTime taken: %E\nMaximum memory used: %M KB" -o memtime_$sim.txt python3 $script_name > output_$sim.txt 2>&1

    # Extract the memory and time information
    mem_usage=$(grep 'Maximum memory used' memtime_$sim.txt)
    time_taken=$(grep 'Time taken' memtime_$sim.txt)

    # Output the results
    echo -e "Results for $sim:\n$mem_usage\n$time_taken"
    echo "Output saved to output_$sim.txt"
done

# Clean up
rm memtime_*.txt
