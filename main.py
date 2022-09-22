from datetime import date
from enum import Enum
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile


app = FastAPI()
# User Model Class


class User(BaseModel):
    id: int
    name: str
    joined: date


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {
        "code": 1,
        "message": "Successful",
        "data": [
            {
            "filename": file.filename,
        }
        ]
    }
