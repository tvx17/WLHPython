import os
from pathlib import Path

from PyQt6 import uic

from PyQt6.QtCore import Qt

from WLHPy.gui import globals as globals_gui


def load(dock, window):
	path = Path(os.getcwd(), 'gui', 'docks', dock)
	globals_gui.docks[dock] = uic.loadUi(str(Path(path, f'{dock}.ui')))

	globals_gui.windows[window].addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, globals_gui.docks[dock])


if __name__ == '__main__':
	load()
