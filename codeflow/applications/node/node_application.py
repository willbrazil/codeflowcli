from .. import Application

class NodeApplication(Application):
	def __init__(self, custom_dict={}):
		Application.__init__(self, 'node', {'Linux': ['32bit', '64bit']}, custom_dict=custom_dict)
