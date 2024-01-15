import function.linux_commands as fl
import library.library as library
#import load_structure_files as lsf
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--pdb')
def a(pdb):
    print(pdb)


#library.install_library()

if __name__ == "__main__":
    fl.create_folder('data')
    a()
    cli()
        
    