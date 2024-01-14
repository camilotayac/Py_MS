import os
from biobb_chemistry.acpype.acpype_params_ac import acpype_params_ac


def ligand_topology():
    os.chdir('PDB')
    ligands=input('ingrese los ligandos PARA TOPOLOGY: ')
    ligands=ligands.split()  
    for ligand in ligands:
        output_acpype_inpcrd = ligand+'_params.inpcrd'
        output_acpype_frcmod = ligand+'_params.frcmod'
        output_acpype_lib = ligand+'_params.lib'
        output_acpype_prmtop = ligand+'_params.prmtop'
        output_acpype = ligand+'_params'
        prop = {
            'basename' : output_acpype
        }
        acpype_params_ac(input_path='{}_addH_min.mol2'.format(ligand), 
                output_path_inpcrd=output_acpype_inpcrd,
                output_path_frcmod=output_acpype_frcmod,
                output_path_lib=output_acpype_lib,
                output_path_prmtop=str(output_acpype_prmtop),
                properties=prop)
    os.chdir('..')

