from fastapi import FastAPI, HTTPException
from tasks import run_task
import os

app = FastAPI()

@app.post("/run")
async def execute_task(task: str):
    result = run_task(task)
    return {"message": result}

@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
