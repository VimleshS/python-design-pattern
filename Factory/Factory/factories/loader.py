"""
Uses dynamic imports
Given the factory name, it tries to import else if it fails it loads null_factory
other solution:
    instead, we can also have used __init__ package as in case of SimpleFactory. (like metaprogramming)
    this is other way of loading..



"""

from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_factory import AbsFactory

def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'factories')
    except ImportError:
        factory_module = import_module('.null_factory', 'factories')
    
    classes = getmembers(factory_module, 
                        lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()