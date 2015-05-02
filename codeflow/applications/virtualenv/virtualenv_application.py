from .. import Application
import subprocess

class VirtualEnvApplication(Application):
	def __init__(self, custom_dict={}):
		Application.__init__(self, 'virtualenv', {'Linux': ['32bit', '64bit']}, custom_dict=custom_dict)

	def create_env(self):
		pass

	def activate_env(self):
		pass
		#subprocess.call(["bash -c 'source ~/temporary_env_name/bin/activate'"], shell=True)

	def deactivate_env(self):
		pass

	def customize(self):
		modules = self.custom_dict['modules']
		if not modules == None:
			self.create_env()
			self.activate_env()
			for mod in modules:
				pass
				#subprocess.call(['pip install %s' % mod], shell=True)
