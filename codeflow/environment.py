import platform

class Environment(object):

	pre_installed_apps = []
	is_test = False

	system = platform.system()
	architecture = platform.architecture()

	def __init__(self, **kargs):

		assert all(hasattr(type(self), attr) for attr in kargs.keys())
		self.__dict__.update(**kargs)