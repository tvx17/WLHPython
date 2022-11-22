import importlib
import os
from pathlib import Path
from WLHPy.gui import globals as globals_gui
from PyQt6 import uic


def display(which_window):
	path = Path(os.getcwd(), 'gui', 'windows', which_window)

	globals_gui.windows[which_window] = uic.loadUi(str(Path(path, f'{which_window}.ui')))
	globals_gui.windows[which_window].show()
	#if which_window == 'main_window':
		# from WLHPy.gui.windows.main_window import window
		# window.setup()


# mod = importlib.import_module('window', str(path))
# print(mod)



