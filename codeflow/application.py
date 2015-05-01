import os
import shutilwhich

class Application(object):
	def __init__(self, app_name, custom_dict={}):
		self.app_name = app_name
		self.custom_dict = custom_dict

	def is_installed(self, custom_name=None):
		if custom_name == None:
			return not shutilwhich.which(self.app_name) == None
		return not shutilwhich.which(custom_name) == None

	def install(self, customize=False):
		if not self.is_installed():
			print('Installing %s.' % self.app_name)
			os.system('%s/applications/%s/install_scripts/install_linux.sh' % (os.path.dirname(os.path.realpath(__file__)), self.app_name))
		else:
			print('%s already installed.' % self.app_name)

		if customize:
				self.customize()

	def load_custom_dict(self, custom_dict):
		print('Loading custom...')
		self.custom_dict = custom_dict

	def customize(self):
		pass
