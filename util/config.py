class GlobalVar:
    root_path = '/Users/admin/PycharmProjects/SBG2018/'

    @staticmethod
    def set_root_path(p_path):
        GlobalVar.root_path = p_path

    @staticmethod
    def get_root_path():
        return GlobalVar.root_path
