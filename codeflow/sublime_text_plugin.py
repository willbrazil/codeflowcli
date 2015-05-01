class SublimeTextPlugin():
	def __init__(self, repo):
		self.repo = repo

	def get_repo(self):
		return self.repo

	def get_name(self):
		return self.repo[str.rfind(self.repo.encode('utf-8'), '/')+1:].split('.')[0]