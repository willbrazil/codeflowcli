from .. import Application

class NpmApplication(Application):
	def __init__(self, custom_dict={}):
		Application.__init__(self, 'npm', {'Linux': ['32bit']}, custom_dict=custom_dict)