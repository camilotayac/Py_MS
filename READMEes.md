# 👻 Py_MS es un programa que permite optimizar procesos de simulación molecular

# ⚙️ Instlación

```bash
git clone https://github.com/camilotayac/Py_MS.git
cd Py_MS
```

# 📕 ¿Qué se puede hacer?
* [Manipulación de archivos](#Manipulación-de-archivos)
  * [Descargar PDB de *Protein data bank*](#Descarga-PDB)



## Manipulación de archivos

### Descarga PDB
#### Esta la función dowloand-pdb que permite descargar uno o más PDB de *Protein data bank*
```bash
python Py_MS.py dowloand-pdb <ID_1PDB ID_2PDB ID_3PDB>
# Ejemplo
python Py_MS.py dowloand-pdb 3AKA 5FX0
```
##### dowloand-pdb tiene dos parametros:

* -f -> que indica si queremos que se cree una carpeta 🗂 para guardar los archivos PDB. La carpeta tiene por defecto el nombre *dowloand_pdb*
```bash
python Py_MS.py dowloand-pdb <ID_1PDB ID_2PDB ID_3PDB> -f
```
* -nf -> que idica el nombre de la carpeta que queremos que se guarden los archivos PDB
```bash
python Py_MS.py dowloand-pdb <ID_1PDB ID_2PDB ID_3PDB> -f -nf <Nombre de la carpeta>
# Ejemplo
python Py_MS.py dowloand-pdb 3AKA 5FX0 -f -nf canal_calcio
```

