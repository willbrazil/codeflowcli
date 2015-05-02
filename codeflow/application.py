import os
import shutilwhich
from .environment import Environment

class Application(object):
	def __init__(self, app_name, support, custom_dict={}, env=Environment()):
		self.app_name = app_name
		self.custom_dict = custom_dict
		self.env = env
		self.support = support

	def __is_supported_by_environment(self):
		is_os_supported = not self.support[self.env.system] == None
		if is_os_supported:
			return self.env.architecture[0] in self.support[self.env.system]

	def __get_applications_dir(self):
		return '%s/applications' % os.path.dirname(os.path.realpath(__file__))

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

		path = '%s/%s/install_scripts/%s' % (self.__get_applications_dir(), self.app_name, install_script_name)
		if os.path.exists(path):
			return path
		else:
			raise IOError('Installation script not implemented.')

	def install(self, customize=False):
		if not self.__is_supported_by_environment():
			raise ValueError('The app is not supported by your current OS.')

		print('Installing %s.' % self.app_name)
		try:
			if not self.env.is_test: # We don't want to try to install in case of test.
				os.system(self.__get_install_script())
		except StandardError:
			raise

		#if customize:
		#		self.customize()
		return True

	def load_custom_dict(self, custom_dict):
		print('Loading custom...')
		self.custom_dict = custom_dict

	def customize(self):
		pass
