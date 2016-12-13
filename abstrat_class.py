"""
First line is import abstract base class.
"""
import abc


class AbstractClass(object):
    """Abstract class definition"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def name(self):
        """ Required Value"""

    @abc.abstractproperty
    def balance(self):
        """Required Value"""


# On  h = Half()
# TypeError: Can't instantiate abstract class Half with abstract methods Balance, Name

class Half(AbstractClass):
    pass


# Implemented class
class Account(AbstractClass):

    def __init__(self):
        self._balance = 0.0

    def name(self):
        return "Hello World"

    # @property is required to implement property
    @property
    def balance(self):
        """Implementation of abstract property"""
        return self._balance

