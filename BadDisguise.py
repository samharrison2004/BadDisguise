#!/usr/bin/env python
## The above is shebang syntax for running the program in UNIX systems

## Required to use the program on the command line
import argparse

## Required to change the MAC address of the device
import os

## Required to execute 'ping' command in the shell
import subprocess

## Required to 
import platform

## Scapy is required to interact with ARP requests
from scapy.all import *

ping_target = "google.com"

def is_connected(ping_target):
    if platform.system().lower() == "windows":
        argument = "-n"
    else:
        argument = "-c"
    command = ["ping", argument, "1", ping_target]
    return subprocess.call(command) == 1 ## Will return "True" if the target site can be reached

parser = argparse.ArgumentParser()


