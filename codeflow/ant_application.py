from ant_plugin_manager import AntPluginManager
import subprocess
from shutilwhich import which

class AntApplication():
	def __init__(self, version="1.0"):
		self.version = version
		self.plugin_mgr = AntPluginManager()

	def install(self):
		print('Installing Ant. Version: %s' % self.version)
		subprocess.call(['sudo', 'apt-get', 'install', 'ant'])

	def get_plugin_mgr(self):
		return self.plugin_mgr	

	def is_installed(self):
		return not which('ant') == None

	def install_plugins(self):
		self.plugin_mgr.install_plugins(self.plugin_mgr.get_plugins())