# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:08:14 2016

@author: isaacbredeson
"""

import os
import numpy as np
import sys


"""-------------------------------Parameters--------------------------------"""

poscar_filename = sys.argv[1]

new_poscar_filename = sys.argv[2]

thresh = sys.argv[3]

"""--------------------------Function Definitions---------------------------"""

#%%
def read_in(filepath):
    """
    Reads in lines of POSCAR file.
    
    Returns list of strings, one for each line in the file.
    """
    
    lines = []    
    
    with open(filepath) as f:
        for line in f:
            if len(line) > 0:
                lines.append(line.strip())


    return lines

#%%    
def parse_poscar(data):
    """
    Takes output from read_in()
    
    returns a dictionary with parsed data
    """
    
    unitcell = {}  
    
    unitcell['name'] = data[0]
    
    unitcell['volume_coefficient'] = float(data[1])
    
    unitcell['vec1'] = [float(i) for i in data[2].split()]
    unitcell['vec2'] = [float(i) for i in data[3].split()]
    unitcell['vec3'] = [float(i) for i in data[4].split()]
    
    unitcell['elements'] = data[5].split()
    
    unitcell['num_elements'] = [int(i) for i in data[6].split()]
    
    unitcell['type'] = data[7]
    
    unitcell['atomic_positions'] = []
    
    for atom in data[8:]:
        unitcell['atomic_positions'].append([float(i) for i in atom.split()])
        
    return unitcell
    
#%%
   
def str_list(list_object):
    """
    Returns list with all elements converted to string and joined with spaces.
    """
    return '    '.join([str(i) for i in list_object])

#%%
    
def format_poscar(poscar):
    """
    Formats parsed POSCAR dictionary, i.e. output from parse_poscar()
    
    returns list of strings, one for each line
    """
    
    lines = []
    
    lines.append(poscar['name'])
    
    lines.append(str(poscar['volume_coefficient']))
    
    lines.append(str_list(poscar['vec1']))
    lines.append(str_list(poscar['vec2']))
    lines.append(str_list(poscar['vec3']))
    
    lines.append(' '.join(poscar['elements']))
    lines.append(str_list(poscar['num_elements']))
    
    lines.append(poscar['type'])
    
    for position in poscar['atomic_positions']:
        
        lines.append(str_list(position))
        
    return lines
 
#%%
def write_lines(lines,filepath):
    """
    Writes formatted POSCAR file, i.e. output from format_poscar()
    
    lines - output from format_poscar()
    
    filepath - file path for the saved file
    """
    
    with open(filepath, 'w') as the_file:
        for line in lines:
            the_file.write(''.join([line,'\n']))
            
#%%
def range_random(x):
    
    output = random.random()
    
    output = (output - 0.5) * 2
    
    output = output * x
    
    return output
#%%
    """Random"""

def random_add(atomic_position, threshold):
    """
    Takes an atomic position and adds the output from range_random() to it
    """
    
    random_number = range_random(threshold)
    
    return atomic_position + random_number

def range_random(x):
    
    output = random.random()
    
    output = output - 0.5
    
    return output
    
def random_add(atomic_position, threshold):
    
    random_number = range_random(threshold)
    
    return atomic_position + random_number
    
#%% 
"""-------------------------------Begin Script------------------------------"""
    
poscar_lines = read_in(poscar_filename)

poscar_data = parse_poscar(poscar_lines)

""" Process POSCAR here, save as new_poscar """

new_poscar = poscar_data

write_lines(format_poscar(new_poscar), new_poscar_filename)