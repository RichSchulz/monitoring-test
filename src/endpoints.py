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

@client.endpoint(X=NumericPayload, y=NumericResponse, track_inputs=["feature"], track_outputs=["result"])
def numeric_endpoint(payload: NumericPayload):
    return NumericResponse(result=payload.feature)

@client.endpoint(X=CategoricPayload, y=CategoricResponse, track_inputs=["feature"], track_outputs=["result"])
def categoric_endpoint(payload: CategoricPayload):
    return CategoricResponse(result=payload.feature)
