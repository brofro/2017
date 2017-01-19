import json

'''
The response model object for
OpenWeatherApiGET /weather
'''
class GetCurrentWeatherResponse(object):

    def __init__(self, response):
        self.__dict__ = json.loads(response)

    #TODO: Create helper functions to access nested/imporperly deserialized properties