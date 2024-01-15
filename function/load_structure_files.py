from biobb_io.api.pdb import pdb

def fetching_PDB_code_structe(PDB):
    '''
    Función permite descargar archivos PSB utilizando la libreria BIOBB
    '''   
    prop={
            'pdb_code': PDB,
            'filter': False
        }
    pdb(output_pdb_path='{}.pdb'.format(PDB), properties=prop)
    