# main.py
from fastapi import FastAPI
from mymodule import add, multiply

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome! Use /add or /multiply endpoints."}

@app.get("/add")
def add_numbers(a: float, b: float):
    return {"a": a, "b": b, "result": add(a, b)}

@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    return {"a": a, "b": b, "result": multiply(a, b)}
