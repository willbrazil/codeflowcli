from .flow_parser import parse
import subprocess
import json
import sys
from .applications.sublimetext.sublime_application import SublimeTextApplication
from .environment import Environment
from .errors import AppAlreadyInstalledError

def load_flow_from_gist(gist_url, gist_file):
	subprocess.call(['git', 'clone', gist_url, '/tmp/codeflow_gist'])
	gist_path = '/tmp/codeflow_gist/%s' % gist_file
	flow_json = json.loads(open(gist_path, 'r').read())
	subprocess.call(['rm', '-rf', '/tmp/codeflow_gist/'])
	return flow_json

def main2():
	n = SublimeTextApplication()
	#n.install(customize=True)
	#n.get_plugin_mgr().install_plugins(['git@github.com:Microsoft/TypeScript-Sublime-Plugin.git'])

	#b = BracketsApplication()
	#b.install()

def main(args = sys.argv[1:], env=Environment()):

	if len(args) < 2:
		print('Please provide a gist URL and gist file.\n i.e., codeflow https://gist.github.com/36f2a45f756a5832fa64.git salesforce')
		return 1

	gist_repo = args[0]
	gist_file = args[1]

	flow = parse(load_flow_from_gist(gist_repo, gist_file))
	for app in flow['applications']:
		try:
			env.install_app(app)
		except AppAlreadyInstalledError as e:
			print('%s is already installed on the system.' % app.app_name)
		except ValueError as e:
			print(str(e))

		app.customize()
			
		#app.install_plugins()
	#plugin_mgr = flow['plugin_mgr']
	#plugins = flow['plugins']
	#plugin_mgr.install_plugins(plugins)