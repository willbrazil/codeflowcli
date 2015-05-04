import json
import os

def build_config_file(apps_config, codeflow_json):
	apps = codeflow_json['applications']
	config_file = {}
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