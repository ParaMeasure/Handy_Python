#!/usr/bin/python3
import subprocess

# This function displays a menu for the user, allowing them to select which type of nmap scan to perform
def menu():
    print("Please select an option:")
    print("1. Scan using nmap -A")  # Detailed scan
    print("2. Scan using nmap -O")  # OS detection scan
    # Additional options with specific nmap flags...
    print("0. Exit")  # Option to exit the program
    choice = input("Enter your choice: ")  # User inputs their choice
    return choice  # Function returns the user's choice

# This function performs the actual nmap scan
def perform_scan(options):
    ip_address = input("Enter IP address: ")  # Prompt user for target IP address
    command = ["nmap"] + options + [ip_address]  # Construct the nmap command with chosen options and target IP
    # Use subprocess to execute the command and capture the output
    result = subprocess.run(command, capture_output=True)
    print(result.stdout.decode())  # Print the command output
    # Create a unique filename based on the IP address and scan options
    filename = f"{ip_address}_{options}.txt".replace('"', '')
    with open(filename, "w") as f:  # Write the output to a file
        f.write(result.stdout.decode())
    input("Press enter to continue...")  # Wait for user before proceeding

# This function controls the overall program flow
def main():
    while True:  # Main program loop
        choice = menu()  # Present the menu and get the user's choice
        # Perform the selected scan, or break the loop if the user chose to exit
        if choice == '1':
            perform_scan(["-A"])
        # More elif branches for other choices...
        elif choice == '0':
            break
        else:  # If the user didn't make a valid choice...
            print("Invalid choice. Please try again.")  # Print an error message
            continue  # Skip the rest of this loop iteration and go back to the start

# If this script is being run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()
