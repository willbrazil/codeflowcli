from .flow_parser import parse
import subprocess
import json
import sys
from .applications.brackets.brackets_application import BracketsApplication

def load_flow_from_gist(gist_url, gist_file):
	subprocess.call(['git', 'clone', gist_url, '/tmp/codeflow_gist'])
	gist_path = '/tmp/codeflow_gist/%s' % gist_file
	flow_json = json.loads(open(gist_path, 'r').read())
	subprocess.call(['rm', '-rf', '/tmp/codeflow_gist/'])
	return flow_json

def main():
	n = BracketsApplication()
	n.install()

def main2(args = sys.argv[1:]):

	gist_repo = args[0]
	gist_file = args[1]

	flow = parse(load_flow_from_gist(gist_repo, gist_file))
	for app in flow['applications']:
		if not app.is_installed():
			app.install()
			
		app.install_plugins()
	#plugin_mgr = flow['plugin_mgr']
	#plugins = flow['plugins']
	#plugin_mgr.install_plugins(plugins)