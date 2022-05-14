import abc


class BaseTransformerError(Exception):
    pass


class BaseTransformer(metaclass=abc.ABCMeta):
    def __init__(self, payload: object):
        self.payload = payload

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError("execute method is not defined in Transformer.")
