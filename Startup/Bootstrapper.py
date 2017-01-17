#These useless imports are not ideal but right now they are making reflection possible by hard binding
import Core.Notifiers.PushbulletNotifier
import Core.Services.WeatherService

#Real imports
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

    def GetSerivces(self, notifiers):
        services = []
        print("Bootstrapper.GetServices initializing services")
        for service in ServiceBase.__subclasses__():
            services.append(service([CommuteHandler], notifiers, handlerArgs="**75F in Oakland"))
        return services

    def StartServices(self, services):
        for service in services:
            print("")
            service.Start()

    def StopServices(self, services):
        for service in services:
            service.Stop()