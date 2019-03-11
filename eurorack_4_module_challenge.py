#!/usr/bin/python

# This script is inspired by YouTuber "Comparative Irrelevance" and their #3modulechallenge.
# https://www.youtube.com/channel/UCQBQ6F7VD78Ic_FkTexeE8g
# Use this to generate a list of four modules from a file in the same folder called 'modules.txt'.
# The format of the modules.txt file is:
#
# <module_name>,<type>
#   module_name: This is the name of the module.  Spaces are OK.
#   type: This is the type of module.  Choose one of the following letters to categorize:
#     f: FX (delays, reverbs)
#     m: Modulator (function generators, LFOs, sequencers)
#     s: Sound Source (oscillators, sample players)
#     u: Utility (VCAs, EGs, quantizers, touch controllers)
#
# Anyways, I wanted to do four modules instead of three because mentally it just makes more sense
# to me a the moment in how I think of modular.  Also, logically separating the modules into types 
# ensure that you'll be able to make some noise at the very least.
# 
# I did add an optional switch to this script ("--ci") to allow you to do the true #3modulechallenge.  
# It's kind of dumb though since it randomly chooses any three modules from the list provided and 
# prints them out.  There's a chance you could end up with nothing but VCAs, for example.

import argparse
import os
import random


MODULE_FILE = "./modules.txt"


def generate_and_print_challenge(fx_list, modulators_list, sources_list, utilities_list):
  random.shuffle(fx_list)
  random.shuffle(modulators_list)
  random.shuffle(sources_list)
  random.shuffle(utilities_list)
  print("Your four module challenge is:")
  print("Sound Source: {}".format(sources_list.pop()))
  print("Modulator:    {}".format(modulators_list.pop()))
  print("FX:           {}".format(fx_list.pop()))
  print("Utility:      {}".format(utilities_list.pop()))
  print("\nGood luck!")
  return


def generate_and_print_three_module_challenge():
  module_list = []
  with open(MODULE_FILE) as file:
    for line in file.readlines():
      split_line = line.strip('\n').split(',')
      module_list.append(split_line[0])
  file.close()
  random.shuffle(module_list)
  print("Your three module challenge is:")
  for i in range(0, 3):
    print("  {}".format(module_list.pop()))
  return


def generate_module_lists():
  fx_list = []
  modulators_list = []
  sources_list = []
  utilities_list = []
  with open(MODULE_FILE) as file:
    # For troubleshooting if files aren't loading:
    #print(module_name)
    for line in file.readlines():
      split_line = line.strip('\n').split(',')
      #print(split_line)
      if split_line[1] is 'f':
        fx_list.append(split_line[0])
      elif split_line[1] is 'm':
        modulators_list.append(split_line[0])
      elif split_line[1] is 's':
        sources_list.append(split_line[0])
      else:
        utilities_list.append(split_line[0])
  file.close()
  #print(fx_list)
  #print(modulators_list)
  #print(sources_list)
  #print(utilities_list)
  return fx_list, modulators_list, sources_list, utilities_list


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--ci", action="store_true")
  args = parser.parse_args()
  ci = args.ci
  # http://patorjk.com/software/taag/#p=display&h=1&v=1&f=Stop&t=Eurorack%0A4%20Module%0AChallenge
  print(""" _______                                         _       
(_______)                                       | |      
 _____   _   _   ____  ___    ____  ____   ____ | |  _   
|  ___) | | | | / ___)/ _ \  / ___)/ _  | / ___)| | / )  
| |_____| |_| || |   | |_| || |   ( ( | |( (___ | |< (   
|_______)\____||_|    \___/ |_|    \_||_| \____)|_| \_)  
   __       ______              _         _              
  / /      |  ___ \            | |       | |             
 / /____   | | _ | |  ___    _ | | _   _ | |  ____       
|___   _)  | || || | / _ \  / || || | | || | / _  )      
    | |    | || || || |_| |( (_| || |_| || |( (/ /       
    |_|    |_||_||_| \___/  \____| \____||_| \____)      
  ______  _             _  _                             
 / _____)| |           | || |                            
| /      | | _    ____ | || |  ____  ____    ____   ____ 
| |      | || \  / _  || || | / _  )|  _ \  / _  | / _  )
| \_____ | | | |( ( | || || |( (/ / | | | |( ( | |( (/ / 
 \______)|_| |_| \_||_||_||_| \____)|_| |_| \_|| | \____)
                                           (_____|       """)
  if ci:
    generate_and_print_three_module_challenge()
  else:
    fx_list, modulators_list, sources_list, utilities_list = generate_module_lists()
    #print(module_list)
    generate_and_print_challenge(fx_list, modulators_list, sources_list, utilities_list)
  exit()


if __name__ == '__main__':
  main()
