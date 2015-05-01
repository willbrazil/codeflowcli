class AntPluginManager():
	def __init__(self):
		pass

	def install_plugins(self, plugin_list):
		print('\nAnt: Installing Plugins...')

	def set_plugins(self, plugin_list):
		self.plugin_list = plugin_list

	def get_plugins(self):
		return self.plugin_list