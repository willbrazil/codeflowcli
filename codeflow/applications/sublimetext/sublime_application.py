from .. import Application
from .sublime_plugin_manager import SublimePluginManager

class SublimeTextApplication(Application):
	def __init__(self, custom_dict={}):
		Application.__init__(self, 'sublimetext', custom_dict)
		self.plugin_mgr = SublimePluginManager()

	def is_installed(self):
		return Application.is_installed(self,'subl')

	def customize(self):
		print('CUSTOMIZING!!!!!! %s' % self.custom_dict)

	def get_plugin_mgr(self):
		return self.plugin_mgr