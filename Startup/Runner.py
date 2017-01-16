from Core.Handlers.CommuteHandler import CommuteHandler
from Core.Notifiers.PushbulletNotifier import PushbulletNotifier
from Core.Services.WeatherService import WeatherService

service = WeatherService(CommuteHandler, [PushbulletNotifier], handlerArgs="75F in Oakland")

service.Start()
service.Stop()