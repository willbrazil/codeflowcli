from .. import Application
from .sublime_plugin_manager import SublimePluginManager

class SublimeTextApplication(Application):
	def __init__(self):
		Application.__init__(self, 'sublimetext')
		self.plugin_mgr = SublimePluginManager()

	def is_installed(self):
		return Application.is_installed(self,'subl')

	def get_plugin_mgr(self):
		return self.plugin_mgr