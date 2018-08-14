import configparser
import yaml


class BaseUtil:
    root_path = '/Users/admin/PycharmProjects/SBG2018/'

    @staticmethod
    def get_config_value(section, key):
        config_path = BaseUtil.root_path + "/conf/config.ini"
        config = configparser.ConfigParser()
        config.read(config_path)
        value = config.get(section, key)
        return value

    @staticmethod
    def get_yaml_value(option, key):
        yaml_path = BaseUtil.root_path + "/yaml/browser.yaml"
        with open(yaml_path, 'r') as f:
            temp = yaml.load(f.read())
        value = temp[option][key]
        return value

    @staticmethod
    def set_root_path(p_path):
        BaseUtil.root_path = p_path

    @staticmethod
    def get_root_path():
        return BaseUtil.root_path
