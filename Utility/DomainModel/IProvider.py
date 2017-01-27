from abc import abstractmethod

'''
The base class each provider implements
Each
'''
class IProvider(object):

    def __init__(self, name, mainRoute):
        self.Name = name
        self.MainRoute = mainRoute

    @abstractmethod
    def IsApiKeyValid(self):
        pass

    @staticmethod
    def PrintInvalidKey(self):
        print("API Key for %s Provider was invalid" % self.Name)

    def GetRoute(self, endpoint):
        return self.MainRoute + "/" + endpoint