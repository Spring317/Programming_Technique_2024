from abc import ABC, abstractmethod
import datetime
class UserCreditService(ABC):
    pass

class UserCreditServiceClient:
    class __Worker:
        def get_credit_limit(self, name: str, surname: str, dob: datetime.date) -> int:
            return 1500

    def __init__(self) -> None:
        pass

    def __enter__(self) -> __Worker:
        return self.__Worker()

    def __exit__(self, exc_type: Exception, exc_value: Exception, traceback: Exception) -> None:
        pass
