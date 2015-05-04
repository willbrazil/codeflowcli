from .. import Application
from ...config_manager import load_module_config
import subprocess

class NpmApplication(Application):

	name = 'npm'

	def __init__(self, custom_dict={}):
		Application.__init__(self, NpmApplication.name, {'Linux': ['32bit']}, custom_dict=custom_dict)

	def customize(self):
		config = load_module_config(NpmApplication.name)
		print(self.custom_dict['modules']) 
		for module in self.custom_dict['modules']:
			subprocess.call(['npm', 'install', '--prefix', config['node_modules_base'], module])
