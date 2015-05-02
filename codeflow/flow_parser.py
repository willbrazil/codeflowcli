from .applications import NodeApplication, SublimeTextApplication, NpmApplication

APPLICATION_MAP = {
	'ST3': SublimeTextApplication,
	'node': NodeApplication,
	'npm': NpmApplication
}

def parse(flow):
	print('parsing...')
	applications = []

	for item in flow['applications']:

		if not item['application'] in APPLICATION_MAP:
			print('Codeflow does not support %s yet.' % item['application'])
		else:
			print('Loading %s info.' % item['application'])
			print('ITEM %s' % item)
			app = APPLICATION_MAP[item['application']](item['custom'])
			#custom_dict = item['custom']
			applications.append(app)

	return {'applications': applications}