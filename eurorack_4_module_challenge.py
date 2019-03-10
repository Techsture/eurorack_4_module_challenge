#!/usr/bin/python


import os
import random


MODULE_FILE = "./modules.txt"


def generate_and_print_challenge(fx_list, modulators_list, sources_list):

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
  print(fx_list)
  print(modulators_list)
  print(sources_list)
  return fx_list, modulators_list, sources_list, utilities_list


def main():
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
  fx_list, modulators_list, sources_list, utilities_list = generate_module_lists()
  #print(module_list)
  generate_and_print_challenge(fx_list, modulators_list, sources_list, utilities_list)
  exit()


if __name__ == '__main__':
  main()
