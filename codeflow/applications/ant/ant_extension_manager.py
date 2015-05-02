
class AntExtensionManager():

    def __init__(self):
        pass

    def __install(self, ant_extension):
        has_ant, ant_version, package_dir = self.__has_ant()

        if not has_ant:
            print('Ant not installed')
            return False

        if os.path.exists(('%s/%s' % (package_dir, ant_extension.get_name(), ('%s/%s' % (package_dir, ant_extension.get_name())))))
            print('%s already installed.' % ant_extension.get_name())

    def install_extensions(self, extension_list):
        for url in extension_list:
            extension = AntExtension(url)
            self.__install(extension)

    def __has_ant(self):
        try:
            ant_version = ant_info.get_ant_version()
            package_dir = ant_info.get_package_directory()
            return True, ant_version, packager_dir
        except ant_info.errors.AntNotFoundError as e:
            return False, None, None

    def set_extensions(self, extension_list):
        self.extension_list = extension_list

    def get_extensions(self):
        return self.extension_list