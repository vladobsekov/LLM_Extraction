from pydantic import BaseModel



class ExperimentConfig(BaseModel):

    param1: int

    param2: float
