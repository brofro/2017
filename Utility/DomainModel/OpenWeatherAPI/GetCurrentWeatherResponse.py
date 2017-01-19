import json

class GetCurrentWeatherResponse(object):

    def __init__(self, response):
        self.__dict__ = json.loads(response)