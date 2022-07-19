from tktl.future import Tktl
from pydantic import BaseModel
# instantiate client
client = Tktl()


class NumericPayload(BaseModel):
    feature: int
    this_is_a_super_long_variable_name_similar_to_branch: int
    this_is_an_even_longer_variable_name_similar_to_branch_1: int
    this_is_an_even_longer_variable_name_similar_to_branch_2: int
    this_is_an_even_longer_variable_name_similar_to_branch_3: int
    user.events.timing_0.6__credit_score_clicked_app_rating_dialog_seconds_total: int


class NumericResponse(BaseModel):
    result: int

class CategoricPayload(BaseModel):
    feature: str

class CategoricResponse(BaseModel):
    result: str

@client.endpoint(X=NumericPayload, y=NumericResponse, track_inputs=["feature", "this_is_a_super_long_variable_name_similar_to_branch", "this_is_an_even_longer_variable_name_similar_to_branch_1", "this_is_an_even_longer_variable_name_similar_to_branch_2", "this_is_an_even_longer_variable_name_similar_to_branch_3", "user.events.timing_0.6__credit_score_clicked_app_rating_dialog_seconds_total"], track_outputs=["result"])
def numeric_endpoint(payload: NumericPayload):
    return NumericResponse(result=payload.feature)

@client.endpoint(X=CategoricPayload, y=CategoricResponse, track_inputs=["feature"], track_outputs=["result"])
def categoric_endpoint(payload: CategoricPayload):
    return CategoricResponse(result=payload.feature)
