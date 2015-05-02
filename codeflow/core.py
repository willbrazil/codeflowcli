from .flow_parser import parse
import subprocess
import json
import sys
from .applications.sublimetext.sublime_application import SublimeTextApplication
from .applications.brackets.brackets_application import BracketsApplication
from .environment import Environment

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

	gist_repo = args[0]
	gist_file = args[1]

	flow = parse(load_flow_from_gist(gist_repo, gist_file))
	for app in flow['applications']:
		if not env.is_app_installed(app.name):
			app.install(customize=True)
		else:
			print('%s already installed.' % self.app_name)
			
		#app.install_plugins()
	#plugin_mgr = flow['plugin_mgr']
	#plugins = flow['plugins']
	#plugin_mgr.install_plugins(plugins)