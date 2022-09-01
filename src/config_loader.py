import os

from src.config import Config
from src.param_source import ParamSource


class ConfigLoader:
    config:Config = None

    @staticmethod
    def load_param_source():
        param_source = os.environ["param_source"]
        if os.environ["param_source"] is not None:
            if param_source in [ParamSource.config_file, ParamSource.environment]:
                Config.param_source = param_source
            else:
                raise Exception(
                    f'Invalid config: param_source = {param_source}. Must be {ParamSource.config_file} or {ParamSource.environment}')

    @staticmethod
    def load():
        ConfigLoader.load_param_source()
        if Config.param_source == ParamSource(ParamSource.config_file):
            ConfigLoader.config = Config
        elif Config.param_source == ParamSource(ParamSource.environment):
            ConfigLoader.config = Config
            for filed_name in Config.__dict__.keys():
                ConfigLoader.config.__setattr__(filed_name, os.environ[filed_name])
        else:
            raise Exception(f'Unknown param source. {Config.param_source.param_source}')
        
        ConfigLoader.config.rest_server_url.rstrip("/")
