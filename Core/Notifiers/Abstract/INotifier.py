from abc import ABCMeta, abstractmethod


class INotifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, destinationEndpoint):
        self.Destination = destinationEndpoint

    @abstractmethod
    def Notify(self, **kwargs):
        pass