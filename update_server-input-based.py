# This script updates a server configuration file based on user input.
import os

file_path = input("Enter the path to the server configuration file: ")
key = input("Enter the key to update: ")
value = input("Enter the new value: ")

def update_server_config(file_path, key, value):
    # Read the existing content of the server configuration file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the configuration value for the specified key
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the line starts with the specified key
            if key in line:
                # Update the line with the new value
                file.write(key + "=" + value + "\n")
            else:
                # Keep the existing line as it is
                file.write(line)

# Path to the server configuration file
#server_config_file = 'server.conf'

# Key and new value for updating the server configuration
#key_to_update = 'MAX_CONNECTIONS'
#new_value = '200'  # New maximum connections allowed

# Update the server configuration file
update_server_config(file_path, key, value)

# Print a message indicating the update was successful
print(f"Updated {key} to {value} in {file_path}")
