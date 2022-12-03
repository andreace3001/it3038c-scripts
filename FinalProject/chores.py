from pydantic import BaseModel

class Chores(BaseModel):
  id: int
  chore_name: str
  chore_dore: str