import abc

class AbsAuto(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
