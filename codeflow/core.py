from .flow_parser import parse
import subprocess
import json
import sys
from .environment import Environment
from .errors import AppAlreadyInstalledError
import argparse
import config_manager
from .applications import config as apps_config

def load_flow_from_gist(gist_url, gist_file):
	subprocess.call(['git', 'clone', gist_url, '/tmp/codeflow_gist'])
	gist_path = '/tmp/codeflow_gist/%s' % gist_file
	flow_json = json.loads(open(gist_path, 'r').read())
	subprocess.call(['rm', '-rf', '/tmp/codeflow_gist/'])
	return flow_json


def main(args = sys.argv[1:], env=Environment()):

	parser = argparse.ArgumentParser()
	parser.add_argument('cmd')
	parser.add_argument('-u', '--gist_url')
	parser.add_argument('-f', '--gist_file')
	args = parser.parse_args()

	if args.cmd == 'load':
		gist_repo = args.gist_url
		gist_file = args.gist_file
		codeflow_json = load_flow_from_gist(gist_repo, gist_file)
		config_manager.build_config_file(gist_repo, gist_file, apps_config, codeflow_json)
		pass	
	elif args.cmd == 'install':

		(gist_repo, gist_file) = config_manager.get_gist_info()

		if not gist_file or not gist_repo:
			print('Use load command before installing.')

		codeflow_json = load_flow_from_gist(gist_repo, gist_file)

		flow = parse(codeflow_json)
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