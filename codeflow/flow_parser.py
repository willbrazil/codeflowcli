from .applications import NodeApplication, SublimeTextApplication, NpmApplication

APPLICATION_MAP = {
	'ST3': SublimeTextApplication,
	'node': NodeApplication,
	'npm': NpmApplication
}

def parse(flow):
	print('parsiong...')
	applications = []

	for item in flow['applications']:
		print('Loading %s info.' % item['application'])
		print('ITEM %s' % item)
		app = APPLICATION_MAP[item['application']](item['custom'])
		#custom_dict = item['custom']
		applications.append(app)

	return {'applications': applications}
