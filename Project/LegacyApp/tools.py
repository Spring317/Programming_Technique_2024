import typing
from typing import Type, TypeVar, Protocol
T = TypeVar('T', bound='HasStaticInit')
class HasStaticInit(Protocol):
    @classmethod
    def static_init(cls: Type[T]) -> None:
        ...


def static_initializer(cls: Type[T]) -> Type[T]:
    if hasattr(cls, 'static_init'):
        cls.static_init()
    return cls

# class Toto:
    
#     @staticmethod
#     def sm(parameter):
#         return MyService().do_action(parameter)
        
        
# @static_initializer
# class Toto:
#     @classmethod
#     def static_init(cls):
#         cls.__myservice = MyService()
        
#     @classmethod
#     def set_MyService(cls, myservice):
#         cls.__myservice = myservice
        
#     @staticmethod
#     def sm(parameter):
#         return Toto.__myService.do_action(parameter)