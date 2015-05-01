from .. import Application

class SublimeTextApplication(Application):
	def __init__(self):
		Application.__init__(self, 'sublimetext')

	def is_installed(self):
		return Application.is_installed('subl')