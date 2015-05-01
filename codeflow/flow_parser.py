from .applications import NodeApplication, SublimeTextApplication, NpmApplication

APPLICATION_MAP = {
	'ST3': SublimeTextApplication(),
	'node': NodeApplication(),
	'npm': NpmApplication()
}

def parse(flow):

	applications = []

	for item in flow['applications']:
		print('Loading %s info.' % item['application'])
		app = APPLICATION_MAP[item['application']]
		#plugins = item['plugins']
		#app.get_plugin_mgr().set_plugins(plugins)
		applications.append(app)

	return {'applications': applications}
