from abc import ABCMeta

from Core.Notifiers.Abstract.INotifier import INotifier
from Utility.Communication.HttpRequestHelper import PostHelper
from Utility.DomainModel.PushbulletAPI.PushbulletApiConstants import PushbulletApiConstants
from Utility.DomainModel.PushbulletAPI.PushNoteRequest import PushNoteRequest

'''
The distinct notifier which sends data to Pushbullet API
'''
class PushbulletNotifier(INotifier):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__(PushbulletApiConstants)

    def Notify(self, **kwargs):
        weatherData = kwargs.get('weatherData')
        print ("PushbulletNotifier sending data %s to %s" % (weatherData.name + " has " + weatherData.weather[0]['main'], self.Provider.Name))

        if not self.Provider.IsApiKeyValid():
            return

        route = self.Provider.GetRoute(PushbulletApiConstants.CreatePushEndpoint)
        request = PushNoteRequest(weatherData.name + " weather", weatherData.weather[0]['main']).ToJson()

        #TODO Figure out what to do with this response
        response = PostHelper(route, request, accessToken=self.Provider.ApiKey)




