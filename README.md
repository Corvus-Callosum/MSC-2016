# TRiO Math and Science Center - Summer 2016

## Material Science Engineering Project

### Goals:


* Calculate the binding energy of a graphene-silicon heterostructure.
* Analyze how the binding energy changes with increasing "glassiness" of the silicon layer.

### Background:

* Graphene: Discovered in 2004, graphene is a single layer of carbon atoms arranged in a honeycomb lattice. It is a promising material for transparent conducting films due to its exceptional electrical conductivity and optical transparency.
* Silicon: Silicon is the most commonly used material in electronics due to its semiconducting properties. Crystalline silicon is the standard form used in transistors and solar cells, while amorphous silicon (glassy silicon) has different properties and potential applications.
* VASP: The Vienna Ab initio Simulation Package is a software used for performing electronic structure calculations based on density functional theory (DFT).

### Procedure:

<!-- Preparation:
Obtain a .cif file for graphite from the ICSD Database.
Use a text editor to convert the graphite structure to graphene.
Convert the graphene structure to a VASP input file (.vasp) using software like Vesta.
Calculate the dimensions of a rectangular unit cell for graphene and modify the .vasp file accordingly.
Utilize a provided Python script to generate a 4x2 supercell of the graphene unit cell.
Repeat steps 1a-1d for crystalline silicon, creating a 2D face-centered layer and a 2x2 supercell using the script.
Heterostructure Creation:
Match the unit cell lengths of graphene and silicon by taking an average between their initial lengths to minimize strain.
Offset the graphene layer by 1.5 angstroms relative to the silicon layer.
Use VASP to calculate the energy of both the individual graphene and silicon supercells.
Employ the Python script to generate a series of four progressively more "glassy" silicon supercells.
Combine each glassy silicon layer with the graphene supercell to form separate heterostructures. Additionally, create a heterostructure with crystalline silicon.
Binding Energy Calculation:
Use VASP to calculate the energy of each combined heterostructure.
Determine the binding energy for each case by subtracting the sum of the individual graphene and silicon supercell energies from the total energy of the heterostructure.
Analysis:
Plot the calculated binding energy versus the degree of "glassiness" in the silicon layer to analyze the relationship between silicon structure and binding strength. -->

* Get graphite .cif file from ICSD Database
    * Convert to graphene with text editor 
    * Convert to .vasp file using Vesta
    * Convert to rectangular unit cell by calculating on paper, using text editor
    * Generate 4x2 supercell using provided Python script

* Get silicon .cif file from ICSD Database
    * Convert to .vasp file with Vesta
    * Convert to 2D face-centered layer using text editor
    * Generate 2x2 supercell using provided Python script

* Modify the unit cell lengths of graphene and silicon to be equal, such that the new lengths are in between the initial lengths of the two supercells to minimize strain.

* Offset graphene by 1.5 angstroms

* Use VASP to calculate energy for both supercells

* Generate a series of 4 progressively more glassy silicon supercell using Python script

* Combine glassy layers with graphene supercell to form a layered heterostructure, as well as graphene with the crystalline silicon

* Calculate energy of combined heterostructures, take difference in energy between heterostructures and the energy of the graphene supercell alone plus silicon supercell energy alone, the difference = binding energy.

* Plot binding energy vs. ‘glassiness’

## Poster
![alt text](https://github.com/LumbermanOne/MSC-2016/blob/main/Images/_Poster_Final%20Slide%201.png)

![alt text](https://github.com/LumbermanOne/MSC-2016/blob/main/Images/_Poster_Final%20Slide%202.png)
