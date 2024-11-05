from http.client import HTTPException
from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep", response_model=list[Sheep])
def read_all_sheep():
    # Return all sheep in the database as a list
    return list(db.data.values())

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    sheep = db.get_sheep(id)
    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep

@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    # Check if the sheep ID already exists to avoid duplicates
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    # Add the new sheep to the database
    db.data[sheep.id] = sheep
    return sheep  # Return the newly added sheep data

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id: int, updated_sheep: Sheep):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")

    # Update the sheep data
    db.data[id] = updated_sheep
    return updated_sheep  # Return the updated sheep data

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")

    # Remove the sheep from the database
    del db.data[id]
    return  # Returning nothing as per HTTP 204 convention

