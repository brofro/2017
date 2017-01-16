#The main runnner class to be started by the master init.py
#Service usage flow
#Initialize each service with the following:
#- Handlers which should process data and determine which (if any) messages should be sent to subscribers
#- Notifiers (or subscribers) which should send the data to specified places
#Handler args are placeholders for now

from Core.Handlers.CommuteHandler import CommuteHandler
from Core.Notifiers.Abstract.INotifier import INotifier
from Core.Notifiers.PushbulletNotifier import PushbulletNotifier
from Core.Services.Abstract.ServiceBase import ServiceBase
from Core.Services.WeatherService import WeatherService

#TODO: See how to handle Handlers
notifiers = INotifier.__subclasses__()
services = ServiceBase.__subclasses__()

notifierObjects = []
for notifier in notifiers:
    notifierObjects.append(notifier())

for service in services:
    serviceObject = service([CommuteHandler], notifierObjects, handlerArgs="**75F in Oakland**")
    serviceObject.Start()
    serviceObject.Stop()