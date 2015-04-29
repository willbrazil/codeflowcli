from .flow_parser import parse
import subprocess
import json

def load_flow_from_gist(gist_url, gist_file):
	subprocess.call(['git', 'clone', gist_url, '/tmp/codeflow_gist'])
	gist_path = '/tmp/codeflow_gist/%s' % gist_file
	flow_json = json.loads(open(gist_path, 'r').read())
	subprocess.call(['rm', '-rf', '/tmp/codeflow_gist/'])
	return flow_json

def main():
	flow = parse(load_flow_from_gist('https://gist.github.com/6f0092ed10a4a849e506.git', 'will_node_codeflow'))
	plugin_mgr = flow['plugin_mgr']
	plugins = flow['plugins']
	plugin_mgr.install_plugins(plugins)