import pytest
from codeflow.application import Application
from util import get_linux_32

class TestApplication(object):

	def test_install_linux_32(self):
		support = {'Linux': ['32bit', '64bit']}
		app = Application('random_app', support, env=get_linux_32())
		assert True == app.install()

		support = {'Linux': ['64bit']}
		app = Application('random_app', support, env=get_linux_32())
		with pytest.raises(ValueError):
			app.install()

	def test_install_app_already_installed(self):
		assert False == get_linux_32().is_app_installed('my_app')
		assert True == get_linux_32(pre_installed=['my_app']).is_app_installed('my_app')