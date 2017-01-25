from abc import ABCMeta, abstractmethod

'''
Base notifier class
Notifier classes are responsible for sending data to a destination
Notifiers are either given response data fromm IServices or reformatted/reprocessed data
'''
class INotifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, provider):
        self.Provider = provider

    @abstractmethod
    def Notify(self, **kwargs):
        pass

    #TODO Abstract this method and providers to a base class
    def IsApiKeyValid(self):
        if self.Provider.ApiKey is "":
            print ("API Key for %s is missing" % self.Provider.Name)
            return False
        return True