from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Backend corriendo"}

@app.get("/lidar")
def get_lidar_data():
    with open("data-files/data_lidar.json", encoding="utf-8") as f:
        data = json.load(f)
        return data