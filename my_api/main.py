from fastapi import FastAPI
import joblib
import uvicorn
import os
import pandas as pd 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int,q: str = None):
    return {"item_id": item_id, "q": q, }

@app.post("/students/")
def create_item(students: dict):
    pipeline=joblib.load('codigo/pipeline_total.gz')
    DF=pd.DataFrame([students])
    prediction=pipeline.predict_proba(DF)
    result=float(prediction[0][1])
    return{"prediction":result}

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)