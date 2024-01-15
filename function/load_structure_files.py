import linux_commands
from biobb_io.api.pdb import pdb
import os
def fetching_PDB_code_structe(*PDB):
    linux_commands.create_folder('data/PDB')
    os.chdir('data/PDB')
    for pdb_code_structure in PDB:
        print(pdb_code_structure)
        prop={
            'pdb_code': pdb_code_structure,
            'filter': False
        }
        pdb(output_pdb_path='{}.pdb'.format(pdb_code_structure), properties=prop)
    os.chdir('..')