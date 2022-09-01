class ParamSource:
    environment = 'environment'
    config_file = 'config_file'

    def __init__(self, param_source):
        self.param_source = param_source

    def __eq__(self, other):
        if isinstance(other, ParamSource):
            return self.__dict__ == other.__dict__
        return False
