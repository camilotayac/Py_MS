import load_structure_files as lsf
import preparation_of_structures as pos
import linux_commands as lc


def protein_ligand_complex_md(*structure):
    lsf.fetching_PDB_code_structe(*structure)
    pos.reomve_water(*structure)
    pos.remove_ligands(*structure)
    


protein_ligand_complex_md('3htb')
