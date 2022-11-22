from WLHPy.gui import globals as gui_globals


def setup():
	connect_actions()


def connect_actions():
	gui_globals.windows['main_window'].act_mn_project_quit.triggered.connect(lambda: _actions_router('quit'))
	gui_globals.windows['main_window'].act_tb_mn_characters.triggered.connect(lambda: _actions_router('list', 'characters'))

def _actions_router(action: str, *args):
	try:
		the_func = globals()[f'_action_{action}']
		if len(args) > 0:
			the_func(args)
		else:
			the_func()
	except Exception:
		if action == '':
			pass


# ---------------------------------------------------------------------------------
def _action_quit():
	exit(0)

def _action_list(*args):
	from WLHPy.gui.docks import dock
	from WLHPy.gui.docks.list import list
	dock.load('list', 'main_window')
	list.setup(args[0][0], 'list')
