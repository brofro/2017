from abc import ABCMeta, abstractmethod

class AbstractServiceBase(object):
    __metaclass__ = ABCMeta


    def __init__(self, name, endpoint):
        self.Name = name
        self.Endpoint = endpoint

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def Stop(self):
        pass