from abc import abstractmethod

'''
The base class each provider implements
Each
'''
class IProvider(object):

    def __init__(self, name, mainRoute, keyCollection):
        self.Name = name
        self.MainRoute = mainRoute

        if keyCollection.get(name) is not None:
            self.ApiKey = keyCollection[name]
        else:
            self.ApiKey = ""

    @abstractmethod
    def IsApiKeyValid(self):
        pass

    def PrintInvalidKey(self):
        print("API Key for %s Provider was invalid" % self.Name)

    def GetRoute(self, endpoint):
        return self.MainRoute + "/" + endpoint