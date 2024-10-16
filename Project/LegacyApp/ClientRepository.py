# from DB import DBAccess
# from .Client import Client
# from .ClientStatus import ClientStatus
# from .tools import static_initializer
# from typing import Type

# @static_initializer
# class ClientRepository:
#     __table_name = 'clients'
#     __table_description = ['name', 'status']
#     __table_datatypes = [str, ClientStatus]

#     @classmethod
#     def static_init(cls: Type['ClientRepository']) -> None:
#         cls.__clients = DBAccess.add_table(cls.__table_name, cls.__table_description, cls.__table_datatypes)
#         cls.__clients.add_entry(1, ["Hugo Lasticot", ClientStatus.VIP])
#         cls.__clients.add_entry(2, ["Madeleine Proust", ClientStatus.IP])
#         cls.__clients.add_entry(3, ["Huguette Ponsif", ClientStatus.NORMAL])
#         cls.__clients.add_entry(4, ["Georges Amphitryon", ClientStatus.VIP])
#         cls.__clients.add_entry(5, ["Anibal Dupont", ClientStatus.IP])
#         cls.__clients.add_entry(7, ["Georina Dupond", ClientStatus.NORMAL])
#         cls.__clients.add_entry(8, ["Victor Elysea", ClientStatus.IP])
#         cls.__clients.add_entry(9, ["Céline Quiboit", ClientStatus.NORMAL])
#         cls.__clients.add_entry(10, ["Muriel Labeille", ClientStatus.NORMAL])

#     @classmethod
#     def get_by_id(cls: Type['ClientRepository'], id: int) -> Client:
#         entry = cls.__clients.get_entry(id)
#         return Client(id, entry.get_value_by_column('name'), entry.get_value_by_column('status'))
            

from typing import Type, Optional
from DB import DBAccess
from .Client import Client
from .ClientStatus import ClientStatus
from .tools import static_initializer


@static_initializer
class ClientRepository:
    _table_name: str = 'clients'
    _table_description: list[str] = ['name', 'status']
    _table_datatypes: list[type] = [str, ClientStatus]
    _clients = None  # Protected attribute, accessible within the class

    @classmethod
    def static_init(cls) -> None:
        cls._clients = DBAccess.add_table(cls._table_name, cls._table_description, cls._table_datatypes)
        # if cls._clients is None:
        #     raise RuntimeError("Failed to initialize the clients table")
        cls._clients.add_entry(1, ["Hugo Lasticot", ClientStatus.VIP])
        cls._clients.add_entry(2, ["Madeleine Proust", ClientStatus.IP])
        cls._clients.add_entry(3, ["Huguette Ponsif", ClientStatus.NORMAL])
        cls._clients.add_entry(4, ["Georges Amphitryon", ClientStatus.VIP])
        cls._clients.add_entry(5, ["Anibal Dupont", ClientStatus.IP])
        cls._clients.add_entry(7, ["Georina Dupond", ClientStatus.NORMAL])
        cls._clients.add_entry(8, ["Victor Elysea", ClientStatus.IP])
        cls._clients.add_entry(9, ["Céline Quiboit", ClientStatus.NORMAL])
        cls._clients.add_entry(10, ["Muriel Labeille", ClientStatus.NORMAL])

    @classmethod
    def get_by_id(cls, id: int) -> Client:
        if cls._clients is None:
            raise RuntimeError("Clients table has not been initialized")
        
        entry = cls._clients.get_entry(id)
        if entry is None:
            raise ValueError(f"No client found with ID: {id}")
        
        name = entry.get_value_by_column('name')
        status = entry.get_value_by_column('status')

        if not isinstance(name, str) or not isinstance(status, ClientStatus):
            raise TypeError("Data types do not match expected types for 'name' or 'status'")

        return Client(id, name, status)
