from biobb_chemistry.ambertools.reduce_add_hydrogens import reduce_add_hydrogens
import os

def add_hidrogen_Atoms():
    os.chdir('PDB')
    ligands=input('ingrese los ligandos agregar hidrogenos: ')
    ligands=ligands.split()  
    for ligand in ligands:
        prop = {
        'nuclear' : 'true'
        }
        reduce_add_hydrogens(input_path='{}.pdb'.format(ligand),
                   output_path='{}_addH.pdb'.format(ligand),
                   properties=prop)
    os.chdir('..')

