import platform
import shutilwhich
from .errors import AppAlreadyInstalledError

class Environment(object):

	pre_installed_apps = []
	is_test = False
	system = platform.system()
	architecture = platform.architecture()

	def __init__(self, **kargs):

		assert all(hasattr(type(self), attr) for attr in kargs.keys())
		self.__dict__.update(**kargs)

	def __is_supported(self, app):
		supported_dict = app.support
		is_os_supported = (not supported_dict[self.system] == None)
		if is_os_supported:
			return self.architecture[0] in supported_dict[self.system]

	def install_app(self, app):

		# is supported by environment.
		if self.__is_supported(app):

			if not self.is_test:
				if not app.is_installed():
					app.install(self.system, self.architecture)
				else:
					raise AppAlreadyInstalledError('App already in the system.')
			else:
				if app.app_name in self.pre_installed_apps:
					raise AppAlreadyInstalledError('App already in the system.')

			app.customize()
		else:
			raise ValueError('The app is not supported by your current OS.')

		return True