import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from app.routes_sql import router as sql_router
from app.routes_nosql import router as nosql_router
from app import sql_service, nosql_service, utils

app = FastAPI()

# Mount templates
templates = Jinja2Templates(directory="templates")

# Include the external routers
app.include_router(sql_router)
app.include_router(nosql_router)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "sql_data": sql_service.fetch_sql("company_main"),
        "nosql_data": nosql_service.fetch_nosql("company_main")
    })

@app.post("/search")
async def search(request: Request, uid: str = Form(...), mode: str = Form(...)):
    parity_db = f"{utils.get_parity(uid)}_shard"
    result = None
    if mode == "SQL":
        result = sql_service.search_sql_user(parity_db, uid)
    else:
        result = nosql_service.search_nosql_user(parity_db, uid)
        
    return templates.TemplateResponse("index.html", {
        "request": request, "search_res": result, "mode": mode, "search_id": uid,
        "sql_data": sql_service.fetch_sql("company_main"),
        "nosql_data": nosql_service.fetch_nosql("company_main")
    })

@app.get("/shard_view/{mode}/{parity}")
async def shard_view(request: Request, mode: str, parity: str):
    db_name = f"{parity}_shard"
    db_content = sql_service.fetch_sql(db_name) if mode == "SQL" else nosql_service.fetch_nosql(db_name)
    csv_content = utils.fetch_from_csv(mode, parity)
    
    return templates.TemplateResponse("shard_view.html", {
        "request": request, "data": db_content, "csv_data": csv_content, 
        "mode": mode, "parity": parity
    })

# --- THIS BLOCK RUNS THE SERVER ---
if __name__ == "__main__":
    print("Starting FastAPI Server on http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)