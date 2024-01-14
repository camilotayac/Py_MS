from biobb_chemistry.babelm.babel_minimize import babel_minimize
import os


def energetically_minimize():
    os.chdir('PDB')
    ligands=input('ingrese los ligandos minimizar: ')
    ligands=ligands.split()  
    for ligand in ligands:
        prop = {
        'method' : 'sd',
        'criteria' : '1e-10',
        'force_field' : 'GAFF'}
        babel_minimize(input_path='{}_addH.pdb'.format(ligand),
                output_path='{}_addH_min.mol2'.format(ligand),
                properties=prop)
    os.chdir('..')