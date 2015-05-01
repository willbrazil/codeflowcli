import pytest
from codeflow.application import Application
from util import TestEnvironment, LinuxEnvironment

class TestApplication(object):

	apps = [('node'), ('npm')]

	@pytest.mark.parametrize("app_name", apps)
	def test_install_linux_32(self, app_name):
		app = Application(app_name, env=LinuxEnvironment('32bit', 'ELF'))
		assert True == app.install()

	@pytest.mark.parametrize("app_name", apps)
	def test_install_linux_128(self, app_name):
		app = Application(app_name, env=LinuxEnvironment('128bit', 'ELF'))
		with pytest.raises(ValueError):
			app.install()

	@pytest.mark.parametrize("app_name", apps)
	def test_install_linux_64(self, app_name):
		app = Application(app_name, env=LinuxEnvironment('64bit', 'ELF'))
		with pytest.raises(IOError):
			app.install()

	def test_install_invalid_os(self):
		with pytest.raises(ValueError):
			env = TestEnvironment(system='KzooOS')
			Application('node', env=env).install()