#creating a class to describe bank note measurements

#import libraries
from pydantic import BaseModel

class BankNote(BaseModel):
    varience: float
    skeweness: float
    curtosis: float
    entropy: float

#pydantic provides error messages if data is invalid