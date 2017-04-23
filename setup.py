import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\Nobre\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Nobre\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(
    name='Grafic Builder',
    version='1.0.0',
    description='',
    options={"build_exe": {"packages": ["os", "turtle"], "include_files": ["helper.py", "draw.py"]}},
    executables=[Executable("main.py")]
)
