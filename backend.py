from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items():
    return {"message": "GET request received Adam!!!!"}

# @app.post("/items/")
# async def create_item():
#     return {"message": "POST request received"}


# To host run: uvicorn backend:app --reload --port 8001
