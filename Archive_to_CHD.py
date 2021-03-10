import sys
import os
import time
import subprocess
import argparse
import fnmatch
import tempfile
import configparser
import patoolib

from shutil import copyfile
from pyunpack import Archive

#Arg setup
parser = argparse.ArgumentParser(description='A program for coverting GDIs to CHDs.')
parser.add_argument("-v", action="store_true", help="Enables verbose mode")
args = parser.parse_args()
#Setup verbose mode
verboseprint = print if args.v else lambda *a, **k: None

#Setup of config.ini
config = configparser.ConfigParser()
if os.path.isfile('config.ini'):
     verboseprint("Config File exist... Skipping")        
else:
    verboseprint("Config File missing... Creating")
    config['DEFAULT'] = {'GDIDir': os.getcwd() + "/GDI/",
                         'CHDDir': os.getcwd() + "/CHD/",
                         'ROMDir': os.getcwd() + "/ROM/",
                         'TMPDir': os.getcwd() + "/TMP/"}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
config.read('config.ini')
GDIDir = config['DEFAULT']['GDIDir']
CHDDir = config['DEFAULT']['CHDDir']
ROMDir = config['DEFAULT']['ROMDir']
TMPDir = config['DEFAULT']['TMPDir']


listOfFiles = sorted(os.listdir(ROMDir))
listOfGDI = sorted(os.listdir(GDIDir))
pattern = "*.7z"
for file in listOfFiles:
    if fnmatch.fnmatch(file, pattern):         
        print ('Processing: ' + file)
        for GDIName in listOfGDI:
            if fnmatch.fnmatch(GDIName, "*.gdi"):
                if os.path.splitext(GDIName)[0] == os.path.splitext(file)[0]:
                    GDIPath = GDIDir + GDIName
                    CHDPath = CHDDir + os.path.splitext(GDIName)[0] + '.chd'
                    if not os.path.isfile(CHDPath):
                        tmpdir = tempfile.TemporaryDirectory()
                        copyfile(GDIPath, (tmpdir.name + '/' + GDIName))
                        Archive(ROMDir + file).extractall(tmpdir.name)
                        verboseprint ('mame-chdman', "createcd",  "-i", '"' + tmpdir.name + '/' + GDIName + '"', "-o" ,'"' + CHDPath + '"')                       
                        print(os.system('mame-chdman createcd -i "' + tmpdir.name + '/' + GDIName + '" -o "' + CHDPath + '"'))
                        tmpdir.cleanup()
                    else:
                        verboseprint ("CHD already present, skipping.")
               

            
             
            
        