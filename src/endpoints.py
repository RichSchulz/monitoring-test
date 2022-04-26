from tktl.future import Tktl
from pydantic import BaseModel
# instantiate client
client = Tktl()


class NumericPayload(BaseModel):
    feature: int

class CategoricPayload(BaseModel):
    feature: str

@client.endpoint(X=NumericPayload, y=NumericPayload)
def numeric_endpoint(payload: NumericPayload, track_inputs=["feature"], track_outputs=["feature"]):
    return payload

@client.endpoint(X=CategoricPayload, y=CategoricPayload)
def categoric_endpoint(payload: CategoricPayload, track_inputs=["feature"], track_outputs=["feature"]):
    return payload
