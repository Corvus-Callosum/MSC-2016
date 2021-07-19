# TRiO Math and Science Center - Summer 2016

## Material Science Engineering Project

### Goal:

* Calculate binding energy of graphene - silicon heterostructure

* Calculate binding energy for a series of graphene - silicon layers beginning with pristine crystalline silicon and ending with pristine graphene layered with glassy (amorphous) silicon. This will provide a theoretical estimation for how well graphene might stick to crystalline silicon vs. glassy silicon.

### Background:
What is graphene, when and how was it discovered, why is it interesting, what are possible uses for it -> graphene is a potential Transparent conducting film
What is silicon (glass and amorphous, why is it interesting, what are possible uses for it -> e.g. solar cells
Energy calculated using VASP -> density functional theory (DFT)

### Procedure:

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
![alt text](https://github.com/LumbermanOne/MSC-2016/blob/main/IMAGES/Poster_Final%20Slide%201.png)

![alt text](https://github.com/LumbermanOne/MSC-2016/blob/main/IMAGES/Poster_Final%20Slide%202.png)
