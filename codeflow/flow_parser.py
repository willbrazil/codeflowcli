import json
from sublime_plugin_manager import SublimePluginManager
from sublime_text_plugin import SublimeTextPlugin

APPLICATION_MAP = {'ST3': SublimePluginManager}

def parse(flow_path):
	flow = json.loads(open(flow_path, 'r').read())
	plugin_mgr = APPLICATION_MAP[flow['application']]
	print(plugin_mgr)
