import sys
from cx_Freeze import setup, Executable
import os

# Dependências do seu programa
build_exe_options = {
    "packages": ["tkinter", "PIL", "sqlite3"], 
    "includes": ["tkinter.simpledialog", "tkinter.messagebox", "datetime"],
    "include_files": ["IMG/", "dados_lanche.db"]
}

# Script principal do seu programa
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Pão da noite",
    version="1.0",
    description="Uma calculadora para registro de consumo de lanche da noite",
    options={"build_exe": build_exe_options},
    executables=[Executable("pao.py", base=base, icon="img/sandwich.ico")]
)
