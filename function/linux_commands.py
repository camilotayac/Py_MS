import os
import shutil


def delete_folder(name):
     shutil.rmtree(name)

def create_folder(*folder_name):
    for name in folder_name:
        if os.path.exists(name)==True:
            delete_folder(name)
            os.mkdir(name)
        else:
            os.mkdir(name)

def remove_files(*files_name):
    for name in files_name:
        if os.path.exists(name):
            os.remove(name)
