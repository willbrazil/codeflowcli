from setuptools import setup

setup(
	name = 'codeflow',
	version = '0.0.0',
	author = 'William Guedes',
	author_email = 'willbrazil.usa@gmail.com',
	description = "Open source workflow",
	packages = ['codeflow'],
	install_requires = ['sublime_info==0.1.1'],
	entry_points = {'console_scripts': [
		'codeflow = codeflow.main:main']}
)