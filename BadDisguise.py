#!/usr/bin/env python
## The above is shebang syntax for running the program in UNIX systems

## Required to use the program on the command line
import argparse

## Required to change the MAC address of the device
import os

## Scapy is required to interact with ARP requests
from scapy.all import *


parser = argparse.ArgumentParser()


