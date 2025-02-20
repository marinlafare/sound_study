# OPERATIONS
from pydantic import BaseModel

class CreateSong(BaseModel):
    name : str
    url : str
class CreatePitch(BaseModel):
    time : float
    confidence : float
    pitch : float
    actiation : float