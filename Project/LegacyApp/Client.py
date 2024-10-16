from .ClientStatus import ClientStatus
# from abc import ABC, abstractmethod

class Client:
    def __init__(self, id: int =-1, name: str ='', status: ClientStatus =ClientStatus.UNDEFINED) -> None:
        self.__id = -1
        self.__name = ''
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def status(self) -> ClientStatus:
        return self.__status

    @status.setter
    def status(self, status: ClientStatus) -> None:
        self.__status = status
