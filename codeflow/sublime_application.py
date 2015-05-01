from sublime_plugin_manager import SublimePluginManager

class SublimeApplication():
	def __init__(self, version="3"):
		self.version = version
		self.plugin_mgr = SublimePluginManager()

	def install(self):
		print('Installing Sublime Text. Version: %s' % self.version)

	def get_plugin_mgr(self):
		return self.plugin_mgr

	def is_installed(self):
		return True

	def install_plugins(self):
		self.plugin_mgr.install_plugins(self.plugin_mgr.get_plugins())