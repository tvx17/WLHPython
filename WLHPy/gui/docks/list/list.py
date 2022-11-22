from WLHPy.gui import globals as globals_gui
def setup(list_name, dock_name):
	try:
		globals_gui.docks[dock_name].setWindowTitle(list_name)
		globals_gui.docks[dock_name].lbl_name.setText(list_name)
	except Exception as ex:
		print(ex)
	_connect_actions()


def _connect_actions():
	pass


if __name__ == '__main__':
	setup()
