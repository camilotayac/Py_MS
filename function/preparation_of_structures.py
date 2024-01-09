from biobb_structure_utils.utils.remove_pdb_water import remove_pdb_water
from biobb_structure_utils.utils.remove_ligand import remove_ligand
import os
import linux_commands as lc



def reomve_water(*structure):
    os.chdir('PDB')
    for structures in structure:
        remove_pdb_water(input_pdb_path='{}.pdb'.format(structures),output_pdb_path='{}_no_water.pdb'.format(structures))
    os.chdir('..')

def remove_ligands(*structure):
    os.chdir('PDB')
    for protein in structure:
        ligands=input('ingrese los ligandos a eliminar para la proteina {}: '.format(protein))
        ligands=ligands.split() 
        name_ligand_input='' 
        for prop_id in ligands:
            prop={}
            prop['ligand']=prop_id
            print(prop)                      
            if prop_id == ligands[0]:
                remove_ligand(input_structure_path='{}_no_water.pdb'.format(protein),
                        output_structure_path='{}_no_{}_and_water.pdb'.format(protein,prop_id),
                        properties=prop)
                name_ligand_input=prop_id
            elif prop_id!= ligands[-1]:
                remove_ligand(input_structure_path='{}_no_{}_and_water.pdb'.format(protein,name_ligand_input),
                        output_structure_path='{}_no_{}_and_water.pdb'.format(protein,prop_id),
                        properties=prop)
                lc.remove_files('{}_no_{}_and_water.pdb'.format(protein,name_ligand_input))
                name_ligand_input=prop_id                
            elif prop_id== ligands[-1]:
                remove_ligand(input_structure_path='{}_no_{}_and_water.pdb'.format(protein,name_ligand_input),
                        output_structure_path='{}_no_ligand_and_water.pdb'.format(protein),
                        properties=prop)
                lc.remove_files('{}_no_{}_and_water.pdb'.format(protein,name_ligand_input))
    os.chdir('..')