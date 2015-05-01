from .. import Application

class NpmApplication(Application):
	def __init__(self, custom_dict={}):
		Application.__init__(self, 'npm')