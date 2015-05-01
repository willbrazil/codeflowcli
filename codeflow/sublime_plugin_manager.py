import sublime_info
import subprocess
from sublime_text_plugin import SublimeTextPlugin
import os

class SublimePluginManager():

	def __init__(self):
		pass

	def __install(self, sublime_text_plugin):
		has_subl, subl_version, package_dir = self.__has_sublime()
		if not has_subl:
			print('Sublimei not installed.')
			return False

		#print('Sublime Version: %s' % subl_version)
		#print('Sublime Package Dir: %s' % package_dir)
		if os.path.exists(('%s/%s' % (package_dir, sublime_text_plugin.get_name()))):
			print('%s already installed.' % sublime_text_plugin.get_name())
		else:
			print('Installing sublime plugin from: %s' % sublime_text_plugin.get_name())
			f = open(os.devnull, 'w')
			subprocess.call(['git', 'clone', sublime_text_plugin.get_repo(), ('%s/%s' % (package_dir, sublime_text_plugin.get_name()))], stdout=f, stderr=subprocess.STDOUT)
			#f.close()

	def install_plugins(self, plugin_list):
		for repo in plugin_list:
			plugin = SublimeTextPlugin(repo)
			self.__install(plugin)

	def __has_sublime(self):
		try:
			subl_version = sublime_info.get_sublime_version()
			package_dir = sublime_info.get_package_directory()
			return True, subl_version, package_dir
		except sublime_info.errors.STNotFoundError as e:
			return False, None, None

	def set_plugins(self, plugin_list):
		self.plugin_list = plugin_list

	def get_plugins(self):
		return self.plugin_list