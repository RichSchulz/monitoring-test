from tktl.future import Tktl
from pydantic import BaseModel
# instantiate client
client = Tktl()


class NumericPayload(BaseModel):
    feature: int

class NumericResponse(BaseModel):
    result: int

class CategoricPayload(BaseModel):
    feature: str

class CategoricResponse(BaseModel):
    result: str

@client.endpoint(X=NumericPayload, y=NumericResponse)
def numeric_endpoint(payload: NumericPayload, track_inputs=["feature"], track_outputs=["result"]):
    return NumericResponse(result=payload.feature)

@client.endpoint(X=CategoricPayload, y=CategoricResponse)
def categoric_endpoint(payload: CategoricPayload, track_inputs=["feature"], track_outputs=["result"]):
    return CategoricResponse(result=payload.feature)
