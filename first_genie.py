#!/usr/bin/python -tt
# Project: pyats
# Filename: first_genie
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "4/25/20"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

from genie.testbed import load
# from unicon import Connection
import json


def main():
    """
    This first pyATS Genie script instantiates the devnet_sbx_testbed.yml Testbed file which has two DevNet Always On
    Sandbox devices.   It then establishes a connection to each device and executes a show command ("show version").
    All of this is hardcoded and there is lots of code repetition but this first script is intended to show the basics
    without alot of "extras" or flexibility.
    :return:
    """

    # Instantiate the Testbed
    # testbed = load('devnet_sbx_testbed_secure.yml')
    testbed = load('devnet_sbx_testbed.yml')
    print(f"\n======= TESTBED INFO =======\n")
    print(f"\tTestbed Value (object): {testbed}")
    print(f"\n======= END TESTBED INFO =======\n")


    # Sandbox NXOS Device
    # CLI: genie parse "show version" --testbed-file "devnet_sbx_testbed.yml" --devices "sbx-n9kv-ao"
    # This CLI command outputs the results into a directory called "out1" which does not have to exist
    # CLI & SAVE: genie parse "show version" --testbed-file "devnet_sbx_testbed.yml" --devices "sbx-n9kv-ao" --output PRE
    # DIFF CLI:  genie diff PRE POST
    device = testbed.devices['sbx-n9kv-ao']
    # device = Connection(hostname='sbx-n9kv-ao', log_stdout=False)
    # print(dir(device))
    device.connect()
    response = device.parse('show version')
    print(f"\nResponse from sbx-n9kv-ao is of type {type(response)} and length {len(response)}")
    print(f"\n== RAW Response: \n{response}")
    print()
    print(f"== Formatted Response: \n{json.dumps(response, indent=4)}")
    print(response.keys())

    # csr1000v-1 IOS-XE
    # CLI: genie parse "show version" --testbed-file devnet_sbx_testbed.yml --devices "csr1000v-1"
    device = testbed.devices['csr1000v-1']
    device.connect()
    response = device.parse('show version')
    print(f"\nResponse from csr1000v-1 is of type {type(response)} and length {len(response)}")
    print(f"\n== RAW Response: \n{response}")
    print()
    print(f"== Formatted Response: \n{json.dumps(response, indent=4)}")
    print(response.keys())

# Standard call to the main() function.
if __name__ == '__main__':
    main()
