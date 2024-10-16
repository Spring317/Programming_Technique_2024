from LegacyApp.Client import Client
from typing import Generic, TypeVar, Optional
import datetime

T = TypeVar('T')

class User(Generic[T]):
    
    def __init__(self, client: Client, date_of_birth: datetime.date, email_address: str, first_name: str , surname: str) -> None:
        self.client = client
        self.date_of_birth = date_of_birth
        self.email_address = email_address
        self.first_name = first_name
        self.surname = surname
        self.has_credit_limit: Optional[bool] = None
        self.credit_limit = -1



