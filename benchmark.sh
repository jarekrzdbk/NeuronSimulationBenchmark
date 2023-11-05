#!/bin/bash

simulators=("neuron" "brian2")

script_name="hh.py"

for sim in "${simulators[@]}"; do
    echo "Running simulation with $sim..."

    /usr/bin/time -f "\nTime taken: %E\nMaximum memory used: %M KB" -o memtime_$sim.txt time python3 $script_name $sim > output_$sim.txt 2>&1

    mem_usage=$(grep 'Maximum memory used' memtime_$sim.txt)
    time_taken=$(grep 'Time taken' memtime_$sim.txt)

    echo -e "Results for $sim:\n$mem_usage\n$time_taken"
    echo "Output saved to output_$sim.txt"
done

rm memtime_*.txt
