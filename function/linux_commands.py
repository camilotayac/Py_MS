import os
import shutil


def delete_folder(name):
     shutil.rmtree(name)

def create_folder(name):
        '''
        Crear carpetas en linux con OS
        '''
        if os.path.exists(name)==True:
            pass
        else:
            os.mkdir(name)

def remove_files(*files_name):
    for name in files_name:
        if os.path.exists(name):
            os.remove(name)
