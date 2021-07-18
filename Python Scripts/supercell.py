# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:44:46 2016

@author: Isaac
"""

"""
POSCAR file must have positions only, no velocities, i.e. you can't use a
CONTCAR file.
"""

import os
import numpy as np
import sys

"""--------------------------------Parameters-------------------------------"""

# Input file name:

fpf = sys.argv[1]

# Output file name:

fp_out = ''.join(fpf,'.mult')


# Number of duplicate cells in a, b, c (x, y, z) directions:

an = sys.argv[2]
bn = sys.argv[3]

try:
    cn = sys.argv[4]
except:
    cn = 1

# z-axis offset in units of Angstroms:

try:
    z_off = sys.argv[5]
except:
    z_off = 0


"""------------------------------Function Definitions-----------------------"""

def read_in(filepath):
    
    lines = []    
    
    with open(filepath) as f:
        for line in f:
            if len(line.strip()) > 0:
                lines.append(line.strip())

    return lines
    
def parse_poscar(data):
    """
    Takes output from read_in()
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
    
def ei(ucell):
    """
    ['Mo','S'],[1,2] -> ['Mo','S','S']
    """
    
    elements = ucell['elements']  
    nums = ucell['num_elements']
    
    output = []
    
    for index, element in enumerate(ucell['elements']):
        
        output.extend([element for i in range(nums[index])])
        
    return output
    
def multiply_array(ucell,a=an,b=bn,c=cn):
    """
    Duplicates unitcell. 
    
    ucell - output from parse_poscar()
    
    a, b, c - integers, numbers of cells in vec1,vec2,vec3 directions
    """
    
    uatoms = [np.array(i) for i in ucell['atomic_positions']]
        
    if ucell['type'][:1].lower() != 'd':

        print("Error: positions must be formatted as 'Direct'")
        return ucell      
        
    vec1 = np.array(ucell['vec1'])
    vec2 = np.array(ucell['vec2'])
    vec3 = np.array(ucell['vec3'])
        
    new_atoms = {}

    for element in ucell['elements']:
        
        new_atoms[element] = []
    
    names = ei(ucell)
        
    for ai in range(a):
        
        for bi in range(b):
            
            for ci in range(c):
                
                offset = np.array([ai,bi,ci])
                
                print('')                
                print('Offset vector:',offset)
                
                for index, name in enumerate(names):
                
                    xn = np.add(uatoms[index], offset)
                    
                    x1 = np.multiply(xn[0],vec1)
                    x2 = np.multiply(xn[1],vec2)
                    x3 = np.multiply(xn[2],vec3)
                    
                    x4 = np.add(x1,x2)
                    
                    r= np.add(x4,x3)
                    
                    z = np.array([0,0,z_off])
                    
                    rz = np.add(r,z)
                    
                    print('r:',rz,name)
                    
                    new_atoms[name].append(rz)
                    
    return new_atoms

def write_new_data(data,savepath=fp_out):
    """
    Writes poscar dictionary into poscar format using data['new_atoms'] as
    atom positions to write
    """

    
    lines = []
    
    off = np.array([an,bn,cn])

    
    lines.append(data['name'])
    lines.append(str(data['volume_coefficient']))
    lines.append('    '.join([str(i) for i in np.multiply(data['vec1'],off)]))
    lines.append('    '.join([str(i) for i in np.multiply(data['vec2'],off)]))
    lines.append('    '.join([str(i) for i in np.multiply(data['vec3'],off)]))
    lines.append('    '.join(data['elements']))
    
    count = []    
    
    for elem in data['elements']:   
        
        count.append(str(len(data['new_atoms'][elem])))
        
    lines.append('    '.join([str(i) for i in count]))
    
    lines.append('Cartesian')
    
    for i, name in enumerate(data['elements']):
        
        for atom in data['new_atoms'][name]:
            
            lines.append('    '.join([str(j) for j in atom]))
            
    with open(savepath, 'w') as the_file:
        for line in lines:
            the_file.write(''.join([line,'\n']))
    
    

data = parse_poscar(read_in(fpf))
data['new_atoms'] = multiply_array(data,an,bn,cn)
write_new_data(data)
    

    
    
    