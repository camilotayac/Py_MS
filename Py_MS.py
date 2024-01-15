import click
import os
import function.load_structure_files as flsf
import function.linux_commands as flc

@click.group()
def cli():
    pass



@cli.command(help='Función dowloand-pdb permite descargar archivos PDB a partir de su ID')
@click.argument('name_pdb',nargs=-1)
@click.option('--folder/--not_folder','-f',default=False)
@click.option('--name_folder','-nf',type=str,default='dowloand_pdb')
def dowloand_pdb(name_pdb,folder,name_folder):
    '''
    Automatiza el proceso de descargas de archivos PDB, utilizando el modulo create_folder de linux_commands
    '''
    if folder:
        flc.create_folder(name_folder)
        os.chdir(name_folder)
        for id_pdb in name_pdb:
            flsf.fetching_PDB_code_structe(id_pdb)
        os.chdir('..')
    else:
        for id_pdb in name_pdb:
            flsf.fetching_PDB_code_structe(id_pdb)





if __name__ == "__main__":
    if not os.path.isdir('data'):
        flc.create_folder('data')
        os.chdir('data')
    else:
        os.chdir('data')
    cli()
        

