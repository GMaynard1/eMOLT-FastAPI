from typing import Union,List
import uuid
from uuid import UUID,uuid4
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from models import Contacts,No_contact,Role
app = FastAPI()
db: List[Contacts]=[
    Contacts(
        id=uuid4(),
        first_name="Rob",
        last_name="Martin",
        no_contact= No_contact.contact,
        contact_roles= 'active users',
        phone= "5088888888",
        email= "Robm@gmail.com",
        street_1="123 abc st",
        street_2= "ste 1",
        city="Falmouth",
        state="MA",
        zip_code="02532",
    ),
    Contacts(
        id=uuid4(),
        first_name="Jim",
        last_name="Ford",
        no_contact=No_contact.contact,
        contact_roles="active admin",
        phone="123456789",
        email="Jimford@gmail.com",
        street_1="456 def rd",
        street_2="ste 9",
        city="Kingston",
        state="RI",
        zip_code="02892",
    )
]


@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/api/v1/users")
async def fetch_users():
    return db
@app.get("/api/v1/users2/{First_name}/{Last_name}")
async def check_users(user:Contacts,First_name,Last_name):
    for user in db:
        if str(First_name) in user.first_name:
            if str(Last_name) in user.last_name:
                return {"id": user.id}

@app.post("/api/v1/users")
async def register_user(user:Contacts):
    db.append(user)
    return {"id": user.id}
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exit"
    )





#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}


#@app.put("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, "item_id": item_id}