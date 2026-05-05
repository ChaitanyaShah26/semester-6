from fastapi import FastAPI
import requests, itertools

app = FastAPI()

SERVERS = [
    "http://127.0.0.1:8001", 
    "http://127.0.0.1:8002", 
    "http://127.0.0.1:8003"
]
server_cycle = itertools.cycle(SERVERS)

@app.get("/")
def load_balancer():
    selected_server = next(server_cycle)

    try:
        response = requests.get(selected_server)
        return response.json()
    except:
        return {"error": f"Server {selected_server} is offline"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)