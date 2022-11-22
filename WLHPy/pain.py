import gettext
import gettext
import os
import sys
from pathlib import Path

import i18n
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QMdiSubWindow, QTextEdit, QHBoxLayout, QDockWidget, QListWidget, \
    QMdiArea, QApplication


class MainWindow(QMainWindow):
    count = 0

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ImageManager")

        # ----------------- Docking
        layout = QHBoxLayout()
        bar = self.menuBar()

        file = bar.addMenu('File')
        file.setObjectName('Fili')
        file.addAction('Hallo')
        file.addAction('quit')
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowaction)

        self.items = QDockWidget('Dockable', self)

        self.listWidget = QListWidget()
        self.listWidget.addItem('Item1')
        self.listWidget.addItem('Item2')
        self.listWidget.addItem('Item3')
        self.listWidget.addItem('Item4')

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        # --------------------------- MIDI
        self.mdi = QMdiArea()

        # --------------------------- Central
        self.setCentralWidget(self.mdi)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.items)

        self.setLayout(layout)
        self.setWindowTitle('Dock')

    def windowaction(self, q):
        print("triggered")

        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle(f"subwindow{str(MainWindow.count)}")
            self.mdi.addSubWindow(sub)
            sub.show()

        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()

        if q.text() == "Tiled":
            self.mdi.tileSubWindows()


# self.addToolBar(self._toolbar())

# self.setStatusBar(self._statusbar())

# layout = QGridLayout()

# layout.addWidget(self._progressbar(), 1, 0, 1, 1)
# layout.addWidget(self._progressbar_two(), 2, 0, 1, 1)

# widget = QWidget()
# widget.setLayout(layout)
# self.setCentralWidget(widget)

# def _toolbar(self):
#     toolbar = QToolBar("Toolbar")
# for button in self._get_buttons():
#     button = self._create_toolbar_buttons(button)
#     toolbar.addAction(button)
#  return toolbar

# def _statusbar(self):
#     mod_globals.statusbar = QStatusBar()
#     mod_globals.statusbar.showMessage('Boing')
#     return mod_globals.statusbar


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
    sys.exit(app.exec_())
