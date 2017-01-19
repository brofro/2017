
'''
Base handler class
Handler classes are responsible for interpreting and processing data
Handlers determine if INotifiers need to forward the information
'''
class IHandler(object):

    @staticmethod
    def Handle(notifiers, **kwargs):
        pass