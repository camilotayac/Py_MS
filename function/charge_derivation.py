#realizara una optimización de la estructura con Gaussian

#Librerias
import subprocess
import os

def convert_ESP_to_RESP():
    import subprocess
    subprocess.run(['grep', 'Atomic Center', sys.argv[1]], stdout=open('a', 'w'))
    subprocess.run(['grep', 'ESP Fit', sys.argv[1]], stdout=open('b', 'w'))
    subprocess.run(['grep', 'Fit    ', sys.argv[1]], stdout=open('c', 'w'))
    subprocess.run(['./a.out'])
    for filename in ['a', 'b', 'c', 'a.out', 'readit.o']:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

    return