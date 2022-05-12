#!/usr/bin/env python

# This is a simple program to change your Linux device's MAC address.
# While you can easily change your MAC address from the terminal,
# this program incorporates error-checking to ensure the user is
# entering the correct format, returning the current MAC address before
# comitting the change to the specified interface, and provide verbosity
# where applicable.
# This program will soon incorporate a simple GUI to provide new Linux users
# a simple and straightforward experience with early penetration testing techniques.
# *** Please utilize the help menu with either -h or --help if you need information on
# which flags to use in which order.

import subprocess
import optparse
import re


def get_arguments():    # parses arguments entered by the user
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()  # parses user input
    # if interface is not set
    if not options.interface:
        # code to handle error
        parser.error("[-] Please specify an interface, use --help for more info")
    # if new MAC is not set
    elif not options.new_mac:
        # code to handle error
        parser.error("[-] Please specify a new MAC, use --help for more info")
    return options


def mac_changer(interface, new_mac):
    print(f"[+] Changing MAC for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig", options.interface]))
    # regex to search for MAC address and store in variable
    mac_match = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_match:
        return mac_match.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()   # options and arguments are caught within this function
current_mac = get_current_mac(options.interface)
print("[+] Current MAC is " + str(current_mac))
mac_changer(options.interface, options.new_mac)


current_mac = get_current_mac(options.interface)


if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address has not been changed ({})".format(current_mac))
