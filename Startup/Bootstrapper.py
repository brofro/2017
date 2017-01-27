#These useless imports are not ideal but right now they are making reflection possible by hard binding
import json
import os

from pathlib import Path

import Core.Notifiers.PushbulletNotifier
import Core.Services.WeatherService

#Real imports
from Core.Handlers.Abstract.IHandler import IHandler
from Core.Handlers.CommuteHandler import CommuteHandler
from Core.Notifiers.Abstract.INotifier import INotifier
from Core.Services.Abstract.ServiceBase import ServiceBase

'''
The bootstrapper class which provides methods for application initialization
'''
class Bootstrapper(object):

    PropertiesFile = "properties.json"

    def GetNotifiers(self, keyCollection):
        notifiers = []
        print("Bootstrapper.GetNotifiers initializing notifiers")
        for notifier in INotifier.__subclasses__():
            notifiers.append(notifier(keyCollection))
        return notifiers

    def GetHandlers(self):
        handlers = []
        print("Bootstrapper.GetHandlers getting static handlers")
        for handler in IHandler.__subclasses__():
            handlers.append(handler.Handle)
        return handlers

    def GetSerivces(self, handlers, notifiers, keyCollection):
        services = []
        print("Bootstrapper.GetServices initializing services")
        for service in ServiceBase.__subclasses__():
            services.append(service(handlers, notifiers, keyCollection))
        return services

    def StartServices(self, services):
        for service in services:
            print("")
            service.Start()

    def StopServices(self, services):
        for service in services:
            service.Stop()

    def LoadApiKeys(self):
        curdir = os.getcwd()
        propFile = Path(curdir + "/../" + self.PropertiesFile)
        apiKeys = {}

        if not propFile.is_file():
            print("No properties file found in ROOT directory")
            return None

        with open(propFile) as pFile:
            props = json.load(pFile)

        if props.get("apiKeys") is None:
            print("No apiKeys object found")
            return None

        if type(props.get("apiKeys")) is not list:
            print("apiKeys object is of incorrect format")
            return None

        for key in props.get("apiKeys"):
            apiKeys.update(key)

        return apiKeys
