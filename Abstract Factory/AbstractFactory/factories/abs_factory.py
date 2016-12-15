import abc

class AbsFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractstaticmethod
    def create_economy():
        pass

    @abc.abstractstaticmethod
    def create_sport():
        pass

    @abc.abstractstaticmethod
    def create_luxury():
        pass
