import abc

class AbsFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_auto(self):
        pass