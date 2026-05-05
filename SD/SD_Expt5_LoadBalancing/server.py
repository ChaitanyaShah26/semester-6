from fastapi import FastAPI
import sys

app = FastAPI()
port = int(sys.argv[1])

@app.get("/")
def home():
    return {"message": f"Connected to Backend Server on port {port}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=port)