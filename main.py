from fastapi import FastAPI, HTTPException,status
from model.database import db
from model.model import Sheep
app= FastAPI()

@app.get("/sheep/{id}", response_model= Sheep)
def read_sheep(id: int):
    sheep = db.get_sheep(id)
    return sheep
@app.post("/sheep",status_code=status.HTTP_201_CREATED)
def add_sheep(newsheep: Sheep):
    try:
        return db.add_sheep(newsheep)
    except Exception as e:
        raise HTTPException(status_code= 400, detail=str(e) )

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    try:
        db.delete_sheep(id)
        return None  
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/sheep/{id}")
def update_sheep(id: int, updated_sheep: Sheep):
    try:
        return db.update_sheep(id, updated_sheep)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))    

@app.get("/sheep", response_model=list[Sheep])
def get_all_sheep():
    return db.get_all()
