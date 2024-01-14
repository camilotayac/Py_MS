import importlib
import subprocess


def install_library():
    # Lista de bibliotecas a verificar e instalar si es necesario
    libraries_to_check = ['numpy', 'requests', 'matplotlib', 'pandas', 'shlex',
                          'nglview', 'jupyter', 'ipywidgets', 'plotly', 'biobb_io==4.1.0','biobb_structure_utils>=4.1.0', 'shutil',
                          'biobb_amber>=4.1.','biobb_chemistry>=4.1.0','acpype']
    for library in libraries_to_check:
        try:
            # Intenta importar la biblioteca
            importlib.import_module(library)
        except ImportError:
            # Si no se puede importar, instala la biblioteca
            print(f"{library} no está instalada. Instalando...")
            try:
                subprocess.run(['pip', 'install', library], check=True)
                print(f"{library} instalada correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"Error al instalar {library}: {e}")
    pass
