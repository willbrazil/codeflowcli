import json
import os
import sys

def build_config_file(gist_url, gist_file, apps_config, codeflow_json):
	apps = codeflow_json['applications']
	config_file = {"gist_url": gist_url, "gist_file": gist_file}
	for app in apps:
		if app['application'] in apps_config:
			config_file[app['application']] = apps_config[app['application']] 

	config_path = '%s/codeflow_config.json' % os.getcwd()
	f = open(config_path, 'w')
	f.write(json.dumps(config_file, indent=4))
	f.close()
	print('Configuration file generated.')

def load_module_config(module_name):
	config_path = '%s/codeflow_config.json' % os.getcwd()
	config = json.loads(open(config_path, 'r').read())
	return config[module_name]

def get_gist_info():
	config_path = '%s/codeflow_config.json' % os.getcwd()

	if not os.path.exists(config_path):
		print('[ERROR] Unable to read codeflow_config.json. \nUse \'load\' command before \'install\'.  codeflow -h for help.')
		sys.exit(1)

	config = json.loads(open(config_path, 'r').read())
	return (config['gist_url'], config['gist_file'])