#Base class for all handlers
class IHandler(object):

    @staticmethod
    def Handle(notifiers, **kwargs):
        pass