from pydantic import BaseModel,Field
from typing import Annotated

#pydantic model to validate input data
class RequestBody(BaseModel):
    text : Annotated[str,Field(...,description = "Enter your email here.")] 
