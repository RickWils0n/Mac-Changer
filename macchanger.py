#!usr/bin/env python

import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change")
    parser.add_option("-m", "--mac", dest="mac", help="Change MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]Please specify an interface.")
    elif not options.mac:
        parser.error("[-]Please specify a MAC address.")
    return options

def macchanger(mac, interface):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])

def m(interface):
    ix = subprocess.check_output(['ifconfig', interface]).decode("utf-8")
    pp = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", ix)
    if pp:
        return pp.group(0)
    else:
        print("No MAC address found.")

options = get_arguments()
x = m(options.interface)

if not x:
    d = 1
else:
    print('Your old MAC Address = ' + str(x))
gt = options.mac
macchanger(options.mac, options.interface)
o = m(options.interface)
if o == str(gt.lower()):
    print("Your new Mac Address = " + gt.lower())
else:
    print("[-] Failed to change the Mac Address.")
