from codeflow.environment import Environment

class TestEnvironment(Environment):
	def __init__(self, **kargs):
		Environment.__init__(self, is_test=True, **kargs)

class LinuxEnvironment(TestEnvironment):
	def __init__(self, bit, linkage, pre_installed=[]):
		TestEnvironment.__init__(self, system='Linux', architecture=(bit, linkage), pre_installed_apps=pre_installed)

class WindowsEnvironment(TestEnvironment):
	def __init__(self, bit, linkage, pre_installed=[]):
		TestEnvironment.__init__(self, system='Windows', architecture=(bit, linkage), pre_installed_apps=pre_installed)

def get_linux_32(pre_installed=[]):
	return LinuxEnvironment('32bit', 'ELF', pre_installed=pre_installed)

def get_linux_64():
	return LinuxEnvironment('64bit', 'ELF')

def get_windows_32():
	return WindowsEnvironment('32bit', '*')

def get_windows_64():
	return WindowsEnvironment('64bit', '*')

