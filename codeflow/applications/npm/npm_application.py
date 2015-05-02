from .. import Application

class NpmApplication(Application):
	def __init__(self, custom_dict={}):
		suport = [
			{'Linux', ['32']},
			{'OSX', ['32, 64']}
		]
		Application.__init__(self, 'npm', support)