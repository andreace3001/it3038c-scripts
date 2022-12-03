from typing import List
from fastapi import FastAPI
from chores import Chores


app = FastAPI()

db: List[Chores] = [
  Chores(id=1, chore_name="Take out the trash", chore_dore="Andre"),
  Chores(id=2, chore_name="Water the plants", chore_dore="Blake")
]

# Basic http getter -> to make sure that the project is working, has no other purpose.
@app.get("/")
async def root():
    return {"Hello": "World"}

# This allows the user to get data from the db above
@app.get("/chores/")
async def fetch_users():
  return db;

# This allows the user to add more chores
@app.post("/chores/")
async def register_chores(chores: Chores):
  db.append(chores)
  return {"id": chores.id}

# This allows the user to delete chores
@app.delete("/chores/{chore_id}")
async def delete_chore(chore_id: int):
  for chore in db:
    if chore.id == chore_id:
      db.remove(chore)
      return