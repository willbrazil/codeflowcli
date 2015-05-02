import os
import shutilwhich

class Application(object):
	def __init__(self, app_name, support, custom_dict={}):
		self.app_name = app_name
		self.custom_dict = custom_dict
		self.support = support

	def __get_applications_dir(self):
		return '%s/applications' % os.path.dirname(os.path.realpath(__file__))

	def customize(self):
		pass

	def __get_install_script(self, system, architecture):
		install_script_name = None

		if system == 'Linux':
			(bit, link) = architecture
			if bit == '32bit':
				install_script_name = 'install_linux_32.sh'
			elif bit == '64bit':
				install_script_name = 'install_linux_64.sh'
		elif system == 'Windows':
			(bit, link) = architecture
			if bit == '32bit':
				install_script_name = 'install_windows_32.sh'
			elif bit == '64bit':
				install_script_name = 'install_windows_64.sh'

		path = '%s/%s/install_scripts/%s' % (self.__get_applications_dir(), self.app_name, install_script_name)
		if os.path.exists(path):
			return path

	def install(self, system, architecture):
		print('Installing %s.' % self.app_name)
		os.system(self.__get_install_script(system, architecture))
		return True

	def load_custom_dict(self, custom_dict):
		print('Loading custom...')
		self.custom_dict = custom_dict

	def is_installed(self):
		return not shutilwhich.which(self.app_name) == None
