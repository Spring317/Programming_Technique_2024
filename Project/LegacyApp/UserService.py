import datetime

from .ClientStatus import ClientStatus
from .ClientRepository import ClientRepository
from .Client import Client
from .User import User
from .UserCreditService import UserCreditServiceClient
from .UserDataAccess import UserDataAccess
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T', bound= Client)

class IClientRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> ClientRepository:
        ...

class IInvalidUser(ABC):
    @abstractmethod
    def is_empty_name(self, firname: str, surname: str) -> bool:
        ...

    @abstractmethod
    def is_invalid_email(self, email: str) -> bool:
        ...

    @abstractmethod
    def is_under_21(self, dateOfBirth: datetime.date) -> bool:
        ...

    @abstractmethod
    def is_vip(self, status: ClientStatus) -> bool:
        ...

    @abstractmethod
    def is_ip(self, status: ClientStatus) -> bool:
        ...


class ICreditService(ABC):
    @abstractmethod
    def get_credit_limit(self, first_name: str, surname: str, date_of_birth: datetime.date) -> int:
        pass




# class ClientRepository(IClientRepository):
#     def get_by_id(self, id: str) -> ClientRepository:
#         return ClientRepository()


class InvalidUser(IInvalidUser):
    def is_empty_name(self, firname: str, surname: str) -> bool:
        return (firname == '') or (surname == '')

    def is_invalid_email(self, email: str) -> bool:
        return ('@' in email) and ('.' not in email)

    def is_under_21(self, dateOfBirth: datetime.date) -> bool:
        now = datetime.datetime.now()
        age = now.year - dateOfBirth.year
        if (now.month < dateOfBirth.month) or ((now.month == dateOfBirth.month) and (now.day < dateOfBirth.day)):
            age = age - 1
        return age < 21

    def is_vip(self, status: ClientStatus) -> bool:
        return status == ClientStatus.VIP

    def is_ip(self, status: ClientStatus) -> bool:
        return status == ClientStatus.IP
        

class CreditService(ICreditService):
    def get_credit_limit(self, first_name: str, surname: str, date_of_birth: datetime.date) -> int:
        with UserCreditServiceClient() as user_credit_service:
            credit_limit = user_credit_service.get_credit_limit(first_name, surname, date_of_birth)
            return credit_limit

class UserService:
    # THIS METHOD SHOULD STAY STATIC, with same prototype...
    @staticmethod
    def add_user(firname: str, surname: str, email: str, dateOfBirth: datetime.date, clientId: int) -> bool:
        # but you may add typing and you should modify its implementation...
        # if (firname == '') or (surname == ''):
        #     return False
        # if ('@' in email) and ('.' not in email):
        # #     return False
        # now = datetime.now()
        # age = now.year - dateOfBirth.year
        # if (now.month < dateOfBirth.month) or ((now.month == dateOfBirth.month) and (now.day < dateOfBirth.day)):
        #     age = age - 1
        # if age < 21:
        #     return False
        invalidUser = InvalidUser()
        if not (invalidUser.is_empty_name(firname, surname)):
            return False

        if not (invalidUser.is_invalid_email(email)):
            return False

    
        client_repository = ClientRepository()
        client = client_repository.get_by_id(clientId)
        user: User[Client] = User(client=client, date_of_birth=dateOfBirth, email_address=email, first_name = firname, surname=surname)
            
        # if client.status == ClientStatus.VIP:
        #     user.has_credit_limit = False
        # elif client.status == ClientStatus.IP:
        #     user.has_credit_limit = True
        if invalidUser.is_vip(client.status):
            user.has_credit_limit = False
        elif invalidUser.is_ip(client.status):
            user.has_credit_limit = True
            
            # with UserCreditServiceClient() as user_credit_service:
            #     credit_limit = user_credit_service.get_credit_limit(user.first_name, user.surname, user.date_of_birth)
            #     credit_limit = credit_limit * 2
            #     user.credit_limit = credit_limit
        else:
            user.has_credit_limit = True
        #     with UserCreditServiceClient() as user_credit_service:
        #         credit_limit = user_credit_service.get_credit_limit(user.first_name, user.surname, user.date_of_birth)
        #         user.credit_limit = credit_limit
        
        # if user.has_credit_limit and (user.credit_limit < 500):
        #     return False
        creditservice = CreditService()
        if user.has_credit_limit and creditservice.get_credit_limit(user.first_name, user.surname, user.date_of_birth) < 500:
            return False 
        
        UserDataAccess.add_user(user)
        
        return True
