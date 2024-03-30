#!/usr/bin/env bash

# Check if the user provided a file to run
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_to_run_in_server>"
    exit 1
fi

file_to_run=$1
server_ip="54.146.92.194"
user="ubuntu"
ssh_key="~/.ssh/id_rsa"

# Check if the file exists locally
if [ ! -f "$file_to_run" ]; then
    echo "Error: File '$file_to_run' not found."
    exit 1
fi

# Copy the file to the server
scp -i "$ssh_key" "$file_to_run" "$user@$server_ip:~/" || {
    echo "Error: Failed to copy file to the server."
    exit 1
}

# Execute the file on the server
ssh -i "$ssh_key" "$user@$server_ip" "./$file_to_run" || {
    echo "Error: Failed to execute the file on the server."
    exit 1
}

