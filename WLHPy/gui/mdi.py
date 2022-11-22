from PyQt6.QtWidgets import QMdiArea, QMdiSubWindow, QTextEdit

from WLHPy.gui import globals as gui_globals


def init():
    gui_globals.mdi = QMdiArea()
    gui_globals.window_reference.setCentralWidget(gui_globals.mdi)
    add()


def add():
    sub = QMdiSubWindow()
    sub.setWidget(QTextEdit())
    sub.setWindowTitle("subwindow")
    gui_globals.mdi.addSubWindow(sub)
    sub.show()
