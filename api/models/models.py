from pydantic import BaseModel


class Body(BaseModel):
    origin: str
    message: str
