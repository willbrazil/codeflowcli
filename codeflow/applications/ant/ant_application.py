from .. import Application
from .ant_extension_manager import AntExtensionManager

class AntApplication(Application):

    def __init__(self, custom_dict={}):
        Application.__init__(self, 'ant', {'Linux': ['32bit', '64bit']}, custom_dict=custom_dict)
        self.extension_mgr = AntExtensionManager()

    def customize(self):
        print('Customizing ant: %s' % self.custom_dict)

    def get_plugin_mgr(self):
        return self.extension_mgr

    def is_installed(self):
        return self.env.is_app_installed('ant')