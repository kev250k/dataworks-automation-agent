from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    return {"message": f"Executing task: {task}"}

@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
