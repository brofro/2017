'''
The constants class which provides static helper functions and constants
'''
class PushbulletApiConstants(object):

    Name = "PushbulletApi"

    ApiKey = ""

    MainRoute = "https://api.pushbullet.com/v2"

    CreatePushEndpoint = "pushes"

    @staticmethod
    def GetRoute(endpoint):
        return PushbulletApiConstants.MainRoute + "/" + endpoint