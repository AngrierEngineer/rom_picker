import sys
import os
import time
import subprocess
import argparse
import fnmatch
import tempfile
import configparser

vermsg = '''Picker - Version 0.1

Conversion tool for image based ROMs.

By Matthew Greenlaw (AngrierEngineer)'''
 
# Initialize parser
parser = argparse.ArgumentParser(description = vermsg)
# Adding optional argument
parser.add_argument('-ot', default="CHD", type=str, metavar='EXT', help = "The type of file you're out putting too. (Some files may not be supported based on selected system)")
parser.add_argument('-op', default="CHD", type=str, metavar='PATH', help = "The path for the output file. Default: [Currect Directory]")
parser.add_argument('-it', default="CHD", type=str, metavar='EXT', help = "Type of file you wish to convert. Default: [Auto]")
parser.add_argument('-ip', default="CHD", type=str, metavar='PATH', help = "The path for the iutput file. Default: [Currect Directory]")
parser.add_argument("-v", action="store_true", help="Enables verbose mode.")

# Read arguments from command line
args = parser.parse_args()

#Setup verbose mode
verboseprint = print if args.v else lambda *a, **k: None

#Setup of config.ini
config = configparser.ConfigParser()
if os.path.isfile('config.ini'):
     verboseprint("Config File exist... Skipping")        
else:
    verboseprint("Config File missing... Creating")
    config['DEFAULT'] = {'GDIDir': os.getcwd() + "./",
                         'CHDDir': os.getcwd() + "./",
                         'ROMDir': os.getcwd() + "./",
                         'TMPDir': "/TMP/"}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
config.read('config.ini')
GDIDir = config['DEFAULT']['GDIDir']
CHDDir = config['DEFAULT']['CHDDir']
ROMDir = config['DEFAULT']['ROMDir']
TMPDir = config['DEFAULT']['TMPDir']

def get_roms(path, ext)
    