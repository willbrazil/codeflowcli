from sublime_plugin_manager import SublimePluginManager

APPLICATION_MAP = {'ST3': SublimePluginManager()}

def parse(flow):
	plugin_mgr = APPLICATION_MAP[flow['application']]
	plugins = flow['plugins']
	return {'plugin_mgr': plugin_mgr, 'plugins': plugins}
