import sys

from ModuleFor16_Says import goodbye       # importing the hello() function from Sayings.py module

if len(sys.argv) == 2:
    goodbye(sys.argv[1])


# Look at the module Sayings.py