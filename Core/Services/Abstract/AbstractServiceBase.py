from abc import ABCMeta, abstractmethod

class AbstractServiceBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, endpoint, handler, notifiers, **kwargs):
        self.Name = name
        self.Endpoint = endpoint
        self.Handler = handler
        self.Notifiers = notifiers
        self.HandlerArgs = kwargs.get('handlerArgs', "DEFAULT")

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def Stop(self):
        pass