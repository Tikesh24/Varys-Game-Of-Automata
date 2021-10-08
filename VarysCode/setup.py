import os
import sys

from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/BEAST/AppData/Local/Programs/Python/Python36/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/BEAST/AppData/Local/Programs/Python/Python36/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
# buildOptions = dict(packages = [], excludes = [
#     'C:/Users/1360969/AppData/Local/Programs/Python/Python37/DLLs/tcl86t.dll',
#     'C:/Users/1360969/AppData/Local/Programs/Python/Python37/DLLs/tk86t.dll'
# ])
path = ["app"] + sys.path
print(path)
buildOptions = {"path": str(path), "packages": ["os"],"includes":["tkinter"], "optimize": 2}


base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('app.py', base=base, target_name = 'Varys', icon = "favicon.ico")
]


setup(name='Varys',
      version = '1.0.2',
      description = 'Game of automata - Automation tool',
      options = dict(build_exe = buildOptions),
      executables = executables)
