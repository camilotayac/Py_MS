import load_structure_files as lsf
import preparation_of_structures as pos
import linux_commands as lc
import amber


def protein_ligand_complex_md(*structure):
    lsf.fetching_PDB_code_structe(*structure)
    pos.reomve_water(*structure)
    pos.remove_ligands(*structure)
    amber.ligand_system_topology(*structure)
    amber.protein_ligand_complex_system_topology(*structure)
    


protein_ligand_complex_md('3htb')
