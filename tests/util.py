from codeflow.environment import Environment

class TestEnvironment(Environment):
	def __init__(self, **kargs):
		Environment.__init__(self, is_test=True, **kargs)

class LinuxEnvironment(TestEnvironment):
	def __init__(self, bit, linkage):
		TestEnvironment.__init__(self, system='Linux', architecture=(bit, linkage))

class WindowsEnvironment(TestEnvironment):
	def __init__(self, bit, linkage):
		TestEnvironment.__init__(self, system='Windows', architecture=(bit, linkage))

def get_linux_32():
	return LinuxEnvironment('32bit', 'ELF')

def get_linux_64():
	return LinuxEnvironment('64bit', 'ELF')

def get_windows_32():
	return WindowsEnvironment('32bit', '*')

def get_windows_64():
	return WindowsEnvironment('64bit', '*')

