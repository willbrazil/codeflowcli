from codeflow.environment import Environment

class TestEnvironment(Environment):
	def __init__(self, **kargs):
		Environment.__init__(self, is_test=True, **kargs)

class LinuxEnvironment(TestEnvironment):
	def __init__(self, bit, linkage):
		TestEnvironment.__init__(self, system='Linux', architecture=(bit, linkage))