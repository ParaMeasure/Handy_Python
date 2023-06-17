#!/usr/bin/python3
import subprocess
import os

# Define a function to prompt the user to select an option
def menu():
    print("Please select an option:")
    print("1. Scan using nmap -A (Enables OS detection, version detection, script scanning, and traceroute)")
    print("2. Scan using nmap -O (Enables OS detection)")
    print("3. Scan using nmap -O -osscan-guess (Enables OS detection and guesses OS more aggressively)")
    print("4. Scan using nmap -p- (Scan all 65535 ports)")
    print("5. Scan using nmap -sT (TCP connect scan)")
    print("6. Scan using nmap -A -iL /tmp/hosts.txt (Advanced scan on hosts in the given file)")
    print("7. Scan using nmap -sV (Service version detection)")
    print("8. Scan using nmap -sA (TCP ACK scan)")
    print("9. Scan using nmap -PN (Don't ping before scanning)")
    print("10. Scan using nmap -sN (TCP Null scan)")
    print("11. Scan using nmap -sS -f (TCP SYN scan, fragment packets)")
    print("12. Scan using nmap -sS (TCP SYN scan)")
    print("13. Scan using nmap -sU (UDP scan)")
    print("14. Scan using nmap -sS -sU (TCP SYN and UDP scan)")
    print("15. Scan using nmap -sn (Ping scan)")
    print("16. Scan using nmap -n -D (Scan without DNS resolution, and decoy scanning)")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

# Define a function to perform a scan using nmap with the specified options
def perform_scan(options, require_ports=False):
    ip_address = input("Enter IP address or range: ")
    if require_ports:
        port_spec = input("Would you like to specify ports? (y/n): ")
        if port_spec.lower() == "y":
            ports = input("Enter port(s) (separated by comma for multiple ports): ")
            options.extend(["-p", ports])
    command = ["nmap"] + options + [ip_address]
    result = subprocess.run(command, capture_output=True)
    print(result.stdout.decode())
    filename = f"{ip_address}_{'-'.join(options)}.txt".replace('"', '')
    directory = "scan_results"
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        f.write(result.stdout.decode())
    input("Press enter to continue...")

# Define the main function to prompt the user for options and perform scans
def main():
    while True:
        choice = menu()
        if choice == '1':
            perform_scan(["-A"])
        elif choice == '2':
            perform_scan(["-O"])
        elif choice == '3':
            perform_scan(["-O", "-osscan-guess"])
        elif choice == '4':
            perform_scan(["-p-"])
        elif choice == '5':
            perform_scan(["-sT"], require_ports=True)
        elif choice == '6':
            perform_scan(["-A", "-iL", "/tmp/hosts.txt"])
        elif choice == '7':
            perform_scan(["-sV"], require_ports=True)
        elif choice == '8':
            perform_scan(["-sA"], require_ports=True)
        elif choice == '9':
            perform_scan(["-PN"], require_ports=True)
        elif choice == '10':
            perform_scan(["-sN"], require_ports=True)
        elif choice == '11':
            perform_scan(["-sS", "-f"], require_ports=True)
        elif choice == '12':
            perform_scan(["-sS"], require_ports=True)
        elif choice == '13':
            perform_scan(["-sU"], require_ports=True)
        elif choice == '14':
            perform_scan(["-sS", "-sU"], require_ports=True)
        elif choice == '15':
            perform_scan(["-sn"])
        elif choice == '16':
            ip_address = input("Enter IP address: ")
            spoof_ip = input("Enter spoofed IP address: ")
            perform_scan(["-n", "-D", spoof_ip, ip_address])
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()
