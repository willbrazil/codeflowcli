import os
import shutilwhich
from .environment import Environment

class Application(object):
	def __init__(self, app_name, custom_dict={}, env=Environment()):
		self.app_name = app_name
		self.custom_dict = custom_dict
		self.env = env

	def is_installed(self, custom_name=None):

		name = self.app_name
		if not custom_name == None:
			name = custom_name

		if self.env.is_test and (not name in self.env.pre_installed_apps):
			return False

		return not shutilwhich.which(name) == None

	def __get_install_script(self):
		install_script_name = None

		print('SYSTEM:::: %s' % self.env.system)

		if self.env.system == 'Linux':
			(bit, link) = self.env.architecture
			if bit == '32bit':
				install_script_name = 'install_linux_32.sh'
			elif bit == '64bit':
				install_script_name = 'install_linux_64.sh'
			else:
				raise ValueError('Architecture not valid.')
		elif self.env.system == 'Windows':
			(bit, link) = self.env.architecture
			if bit == '32bit':
				install_script_name = 'install_windows_32.sh'
			elif bit == '64bit':
				install_script_name = 'install_windows_64.sh'
			else:
				raise ValueError('Architecture not valid.')

		if install_script_name == None:
			raise ValueError('Operating system not valid.')

		path = '%s/applications/%s/install_scripts/%s' % (os.path.dirname(os.path.realpath(__file__)), self.app_name, install_script_name)
		if os.path.exists(path):
			return path
		else:
			raise IOError('Installation script not implemented.')

	def install(self, customize=False):

		# todo, check if app_name is valid folder

		if not self.is_installed():
			print('Installing %s.' % self.app_name)
			try:
				os.system(self.__get_install_script())
			except StandardError:
				raise
		else:
			print('%s already installed.' % self.app_name)

		#if customize:
		#		self.customize()
		return True

	def load_custom_dict(self, custom_dict):
		print('Loading custom...')
		self.custom_dict = custom_dict

	def customize(self):
		pass
