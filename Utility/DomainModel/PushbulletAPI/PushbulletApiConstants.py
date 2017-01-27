from Utility.DomainModel.IProvider import IProvider

'''
The constants class which provides static helper functions and constants
'''
class PushbulletApiConstants(IProvider):

    CreatePushEndpoint = "pushes"

    def __init__(self, keyCollection):
        super().__init__("Pushbullet", "https://api.pushbullet.com/v2", keyCollection)


    def IsApiKeyValid(self):

        #TODO: Actually hit endpoint and check

        if self.ApiKey is "":
            self.PrintInvalidKey()
            return False

        return True