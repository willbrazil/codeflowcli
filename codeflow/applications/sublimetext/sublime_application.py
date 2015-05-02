from .. import Application
from .sublime_plugin_manager import SublimePluginManager

class SublimeTextApplication(Application):
	def __init__(self, custom_dict={}):
		Application.__init__(self, 'sublimetext', {'Linux': ['32bit', '64bit'], 'Windows': ['32bit', '64bit']}, custom_dict=custom_dict)
		self.plugin_mgr = SublimePluginManager()

	def customize(self):
		print('CUSTOMIZING!!!!!! %s' % self.custom_dict)

	def get_plugin_mgr(self):
		return self.plugin_mgr

	def is_installed(self):
		return self.env.is_app_installed('subl')