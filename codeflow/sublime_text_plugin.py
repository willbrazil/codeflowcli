from installable_plugin import InstallablePlugin

class SublimeTextPlugin(InstallablePlugin):
	def __init__(self, repo):
		self.repo = repo

	def get_repo(self):
		return self.repo

	def get_name(self):
		return self.repo.split('/')[1].split('.')[0]