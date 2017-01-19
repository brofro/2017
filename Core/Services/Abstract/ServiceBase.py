from abc import ABCMeta, abstractmethod

'''
The base class each service implements
Each service retrieves a specific set of data and passes it off to its handlers
Once the handler processes the data, it will pass it to each notfier for sending
'''
class ServiceBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, handlers, notifiers, provider, **kwargs):

        #The handlers to process each the data
        self.Handlers = handlers

        #The notfiers to send data
        self.Notifiers = notifiers

        #The API provider for this servicce
        self.Provider = provider

        self.Name = self.Provider.Name
        self.Endpoint = self.Provider.MainRoute

        #TODO: Placeholders for now
        self.HandlerArgs = kwargs.get('handlerArgs', "DEFAULT")

    #Starts the service
    @abstractmethod
    def Start(self):
        pass

    #Stops the service
    @abstractmethod
    def Stop(self):
        pass

    #Retrieves data delegated to this service
    #TODO Refactor this since we can only get one set of data from one endpoint using this way
    @abstractmethod
    def GetData(self):
        pass