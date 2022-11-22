import sys


from PyQt6.QtWidgets import QApplication
from WLHPy.gui.windows import window as mod_window

from WLHPy.gui.windows.main_window import window as gui_main_window

def main():
    app = QApplication(sys.argv)

    mod_window.display('main_window')
    gui_main_window.setup()
    # path = Path(os.getcwd(), 'gui', 'windows', 'main_window', 'main_window.ui')
    # gui_globals.main_window = uic.loadUi(str(path))

    # wlh_app.check_first_run()
    # main_window.setup()

    # window.display('main_window')
    # gui_globals.main_window.show()

    app.exec()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
