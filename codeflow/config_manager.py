from .applications import config 
import json
import os

class ConfigManager(object):
	def __init__(self, codeflow_json):
		self.codeflow_json = codeflow_json

	def build_config_file(self):
		apps = self.codeflow_json['applications']
		config_file = {}
		for app in apps:
			if app['application'] in config:
				config_file[app['application']] = config[app['application']] 

		config_path = '%s/codeflow_config.json' % os.getcwd()
		f = open(config_path, 'w')
		f.write(json.dumps(config_file, indent=4))
		f.close()
		print('Configuration file generated.')