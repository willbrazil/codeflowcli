import platform
import shutilwhich

class Environment(object):

	pre_installed_apps = []
	is_test = False

	system = platform.system()
	architecture = platform.architecture()

	def __init__(self, **kargs):

		assert all(hasattr(type(self), attr) for attr in kargs.keys())
		self.__dict__.update(**kargs)

	def is_app_installed(self, app_name):
		if self.is_test:
			return (app_name in self.pre_installed_apps)

		return not shutilwhich.which(name) == None
