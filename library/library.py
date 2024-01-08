import importlib
import subprocess

def install_library():
    # Lista de bibliotecas a verificar e instalar si es necesario
    libraries_to_check = ['numpy', 'requests', 'matplotlib']
    for library in libraries_to_check:
        try:
            # Intenta importar la biblioteca
            importlib.import_module(library)
            print(f"{library} está instalada.")
        except ImportError:
            # Si no se puede importar, instala la biblioteca
            print(f"{library} no está instalada. Instalando...")
            try:
                subprocess.run(['pip', 'install', library], check=True)
                print(f"{library} instalada correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"Error al instalar {library}: {e}")
    pass
