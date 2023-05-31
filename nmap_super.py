#!/usr/bin/python3
import subprocess

# Function that prompts the user for their choice of scan type
def menu():
    print("Please select an option:")
    # Each print statement provides a different scan option for the user
    print("1. Scan using nmap -A")  # -A: Enables OS detection, version detection, script scanning, and traceroute
    print("2. Scan using nmap -O")  # -O: Enables OS detection
    print("3. Scan using nmap -O -osscan-guess")  # -O -osscan-guess: Enables OS detection with guessing
    print("4. Scan using nmap -p-")  # -p-: Scan all 65535 ports
    print("5. Scan using nmap -sT")  # -sT: TCP connect scan
    print("6. Scan using nmap -A -iL /tmp/hosts.txt")  # -A -iL /tmp/hosts.txt: Scan hosts from a file with -A option
    print("7. Scan using nmap -sV")  # -sV: Version detection
    print("8. Scan using nmap -sA")  # -sA: TCP ACK scan
    print("9. Scan using nmap -PN")  # -PN: Treat all hosts as online
    print("10. Scan using nmap -sN")  # -sN: TCP Null scan
    print("11. Scan using nmap -sS -p 80 -f")  # -sS -p 80 -f: SYN scan for port 80 with fragmentation
    print("12. Scan using nmap -n -D")  # -n -D: Decoy scan with no DNS resolution
    print("0. Exit")  # Exit the script
    choice = input("Enter your choice: ")  # Prompt the user for their choice
    return choice  # Return the user's choice

# Function to perform the actual nmap scan
def perform_scan(options):
    ip_address = input("Enter IP address: ")  # Prompt for target IP
    # Construct the nmap command with the selected options and IP address
    command = ["nmap"] + options + [ip_address]
    # Execute the nmap command and capture the output
    result = subprocess.run(command, capture_output=True)
    print(result.stdout.decode())  # Print the command output to the console
    # Construct a filename based on the IP address and scan options
    filename = f"{ip_address}_{options}.txt".replace('"', '')
    with open(filename, "w") as f:  # Open the file
        f.write(result.stdout.decode())  # Write the command output to the file
    input("Press enter to continue...")  # Pause before moving on

# Main function to run the menu and perform the selected scan
def main():
    while True:  # Loop to allow repeated scans
        choice = menu()  # Get the user's choice of scan
        # Based on the user's choice, perform the appropriate scan
        if choice == '1':
            perform_scan(["-A"])
        elif choice == '2':
            perform_scan(["-O"])
        elif choice == '3':
            perform_scan(["-O", "-osscan-guess"])
        elif choice == '4':
            perform_scan(["-p-"])
        elif choice == '5':
            perform_scan(["-sT"])
        elif choice == '6':
            perform_scan(["-A", "-iL", "/tmp/hosts.txt"])
        elif choice == '7':
            perform_scan(["-sV"])
        elif choice == '8':
            perform_scan(["-sA"])
        elif choice == '9':
            perform_scan(["-PN"])
        elif choice == '10':
            perform_scan(["-sN"])
        elif choice == '11':
            perform_scan(["-sS", "-p", "80", "-f"])
        elif choice == '12':
            ip_address = input("Enter IP address: ")  # Prompt for target IP
            spoof_ip = input("Enter spoofed IP address: ")  # Prompt for decoy IP
            perform_scan(["-n", "-D", spoof_ip, ip_address])  # Run the scan with the given decoy IP
        elif choice == '0':  # If the user chose to exit...
            break  # Exit the loop, ending the script
        else:  # If the user entered an invalid choice...
            print("Invalid choice. Please try again.")  # Show an error message

# If this script is being run directly, call the main function
if __name__ == "__main__":
    main()
