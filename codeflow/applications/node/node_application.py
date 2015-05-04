from .. import Application

class NodeApplication(Application):

	name = 'node'

	def __init__(self, custom_dict={}):
		Application.__init__(self, NodeApplication.name, {'Linux': ['32bit', '64bit']}, custom_dict=custom_dict)
