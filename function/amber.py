from biobb_amber.pdb4amber.pdb4amber_run import pdb4amber_run
from biobb_amber.leap.leap_gen_top import leap_gen_top
import ambertools
import os
import preparation_of_structures as pos
import babel 
import acpype

def preparing_pdb_file_amber(*pdb:str):
    os.chdir('PDB')
    prop = {
    'remove_tmp': True,
    'remove_hidrogens': False,
    'remove_water':True,
    'constant_pH':False
    }
    for name in pdb:
        pdb4amber_run(input_pdb_path='{}_no_ligand_and_water.pdb'.format(name),output_pdb_path='{}_pdb4amber.pdb'.format(name),properties=prop )
  
    os.chdir('..')




def ligand_system_topology(*structures):
    preparing_pdb_file_amber(*structures)
    pos.extract_ligand_structure(*structures)
    ambertools.add_hidrogen_Atoms()
    babel.energetically_minimize()
    acpype.ligand_topology()

def protein_ligand_complex_system_topology(*structures):
    os.chdir('PDB')
    for structure in structures:
        ligands=input('ingrese los ligandos PARA TOPOLOGY-SISTEM: ')
        ligands=ligands.split()  
        for ligand in ligands:
            output_pdb_path = 'structure.leap.pdb'
            output_top_path = 'structure.leap.top'
            output_crd_path = 'structure.leap.crd'
            prop = {
            "forcefield" : ["protein.ff14SB","gaff"]
            }        
            leap_gen_top(input_pdb_path='{}_pdb4amber.pdb'.format(structure),
                input_lib_path='{}_params.lib'.format(ligand),
                input_frcmod_path='{}_params.frcmod'.format(ligand),
                output_pdb_path=output_pdb_path,
                output_top_path=output_top_path,
                output_crd_path=output_crd_path,
                properties=prop)
        os.chdir('..')