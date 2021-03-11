import sys
import argparse

vermsg = "Picker - Version 0.1"
 
# Initialize parser
parser = argparse.ArgumentParser(description = vermsg)
# Adding optional argument
parser.add_argument('-ot', default="CHD", type=str, metavar='EXT', help = "Output file type for conversion")
parser.add_argument('-in', default="CHD", type=str, metavar='EXT', help = "Output file type for conversion")
parser.add_argument('-of', default="CHD", type=str, metavar='EXT', help = "Output file type for conversion")
parser.add_argument('-it', default="CHD", type=str, metavar='EXT', help = "Output file type for conversion")


# Read arguments from command line
args = parser.parse_args()
