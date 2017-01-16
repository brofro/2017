#The main runnner class to be started by the master init.py
#Service usage flow
#Initialize each service with the following:
#- Handlers which should process data and determine which (if any) messages should be sent to subscribers
#- Notifiers (or subscribers) which should send the data to specified places
#Handler args are placeholders for now

from Core.Handlers.CommuteHandler import CommuteHandler
from Core.Notifiers.PushbulletNotifier import PushbulletNotifier
from Core.Services.WeatherService import WeatherService

service = WeatherService([CommuteHandler], [PushbulletNotifier()], handlerArgs="**75F in Oakland**")

service.Start()
service.Stop()