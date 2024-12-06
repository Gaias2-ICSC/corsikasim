#!/bin/bash

log_folder="test_prod_logs"
output_file="test_prod_logs.csv"

echo "cpuname,jobID,container_version,primary_cosmic_ray,minimal_energy,maximal_energy,zenith_min,zenith_max,real_time,user_time,sys_time" > "$output_file"


for log_file in "$log_folder"/*.err; do

    echo $log_file
    
    values=($(echo $log_file | grep -o '[0-9]\+e[0-9]\+\|\([0-9]\+\)'))

    jobID=${values[0]}
    container_version=${values[1]}
    primary_cosmic_ray=${values[2]}
    minimal_energy=${values[3]}
    maximal_energy=${values[4]}
    zenith_min=${values[5]}
    zenith_max=${values[6]}


    cpuname=$(grep -oP '(\S+): error:' "$log_file" | head -n 1 | cut -d: -f1)
    real_time=$(grep -oP 'real\s+\K[^\s]+' "$log_file")
    user_time=$(grep -oP 'user\s+\K[^\s]+' "$log_file")
    sys_time=$(grep -oP 'sys\s+\K[^\s]+' "$log_file")
    
    # Append the extracted information to the CSV file
    echo "$cpuname,$jobID,$container_version,$primary_cosmic_ray,$minimal_energy,$maximal_energy,$zenith_min,$zenith_max,$real_time,$user_time,$sys_time" >> "$output_file"
done

