from abc import ABCMeta, abstractmethod

'''
Base notifier class
Notifier classes are responsible for sending data to a destination
Notifiers are either given response data fromm IServices or reformatted/reprocessed data
'''
class INotifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, destinationEndpoint):
        self.Destination = destinationEndpoint

    @abstractmethod
    def Notify(self, **kwargs):
        pass