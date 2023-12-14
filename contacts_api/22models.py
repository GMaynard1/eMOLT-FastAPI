from typing import List,Optional
from uuid import UUID,uuid4
from pydantic import BaseModel
from enum import Enum

class No_contact(str,Enum):
    contact="1"
    nocontact="0"
class Role(str,Enum):
    phone ="phone"
    text_message ="text_message"
    email ="email"
class Contacts(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    no_contact: No_contact
    contact_roles: List[Role]
    phone: str
    email: Optional[str]
    street_1: Optional[str]
    street_2: Optional[str]
    city: Optional[str]
    state:Optional[str]
    zip_code: Optional[str]

class UserUpdaterequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]