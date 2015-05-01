from sublime_application import SublimeApplication
from ant_application import AntApplication

APPLICATION_MAP = {
	'ST3': SublimeApplication(),
	'Ant': AntApplication()
}

def parse(flow):

	applications = []

	for item in flow['applications']:
		app = APPLICATION_MAP[item['application']]
		plugins = item['plugins']
		app.get_plugin_mgr().set_plugins(plugins)
		applications.append(app)

	return {'applications': applications}
