#These useless imports are not ideal but right now they are making reflection possible by hard binding
import Core.Notifiers.PushbulletNotifier
import Core.Services.WeatherService

#Real imports
from Core.Handlers.Abstract.IHandler import IHandler
from Core.Handlers.CommuteHandler import CommuteHandler
from Core.Notifiers.Abstract.INotifier import INotifier
from Core.Services.Abstract.ServiceBase import ServiceBase

class Bootstrapper(object):

    def GetNotifiers(self):
        notifiers = []
        print("Bootstrapper.GetNotifiers initializing notifiers")
        for notifier in INotifier.__subclasses__():
            notifiers.append(notifier())
        return notifiers

    def GetHandlers(self):
        handlers = []
        print("Bootstrapper.GetHandlers getting static handlers")
        for handler in IHandler.__subclasses__():
            handlers.append(handler.Handle)
        return handlers

    def GetSerivces(self, handlers, notifiers):
        services = []
        print("Bootstrapper.GetServices initializing services")
        for service in ServiceBase.__subclasses__():
            services.append(service(handlers, notifiers, handlerArgs="**75F in Oakland"))
        return services

    def StartServices(self, services):
        for service in services:
            print("")
            service.Start()

    def StopServices(self, services):
        for service in services:
            service.Stop()