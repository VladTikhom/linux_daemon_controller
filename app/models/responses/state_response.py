from pydantic import BaseModel, StrictBool


class StateResponseModel(BaseModel):
    state: bool
