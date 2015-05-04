from .. import Application
from .sublime_plugin_manager import SublimePluginManager
import shutilwhich

class SublimeTextApplication(Application):

	name = 'sublimetext'

	def __init__(self, custom_dict={}):
		Application.__init__(self, SublimeTextApplication.name, {'Linux': ['32bit', '64bit'], 'Windows': ['32bit', '64bit']}, custom_dict=custom_dict)
		self.plugin_mgr = SublimePluginManager()

	def is_installed(self):
		return not shutilwhich.which('subl') == None

	def customize(self):
		print('Customizing %s' % self.app_name)
		self.plugin_mgr.install_plugins(self.custom_dict['plugins'])	

	def get_plugin_mgr(self):
		return self.plugin_mgr