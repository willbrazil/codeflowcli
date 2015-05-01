import os
import shutilwhich

class Application():
	def __init__(self, app_name):
		self.app_name = app_name

	def is_installed(self, custom_name=None):
		if custom_name == None:
			return not shutilwhich.which(self.app_name) == None
		return not shutilwhich.which(custom_name) == None

	def install(self):
		if not self.is_installed():
			print('Installing %s.' % self.app_name)
			os.system('%s/applications/%s/install_scripts/install_linux.sh' % (os.path.dirname(os.path.realpath(__file__)), self.app_name))
		else:
			print('%s already installed.' % self.app_name)