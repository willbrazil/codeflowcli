from .. import Application

class NpmApplication(Application):

	name = 'npm'

	def __init__(self, custom_dict={}):
		Application.__init__(self, NpmApplication.name, {'Linux': ['32bit']}, custom_dict=custom_dict)

	def customize(self):
		print('customizing npm..')