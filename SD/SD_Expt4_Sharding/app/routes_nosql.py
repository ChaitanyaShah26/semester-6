from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from . import sharding_manager, nosql_service, utils

router = APIRouter(prefix="/nosql")
templates = Jinja2Templates(directory="templates")

@router.get("/manage")
async def manage_nosql(request: Request):
    return templates.TemplateResponse("manage_nosql.html", {
        "request": request,
        "main_data": nosql_service.fetch_nosql("company_main"),
        "shard_hr": nosql_service.fetch_nosql("shard_hr"),
        "shard_it": nosql_service.fetch_nosql("shard_it"),
        "shard_eng": nosql_service.fetch_nosql("shard_engineering"),
        # Fetching CSV data for the right-side panel
        "odd_ids": utils.fetch_from_csv("NOSQL", "odd"),
        "even_ids": utils.fetch_from_csv("NOSQL", "even")
    })

@router.post("/add")
async def add_nosql(id:str=Form(...), name:str=Form(...), contact:str=Form(...), 
                  email:str=Form(...), address:str=Form(...), joining_date:str=Form(...), 
                  dob:str=Form(...), age:int=Form(...), role:str=Form(...), 
                  salary:float=Form(...), department:str=Form(...), password:str=Form(...)):
    
    user_data = {
        "id": id, "name": name, "contact": contact, "email": email, "address": address,
        "joining_date": joining_date, "dob": dob, "age": age, "role": role,
        "salary": salary, "department": department, "password": password
    }
    sharding_manager.process_sharding(user_data, mode="NOSQL")
    return RedirectResponse("/nosql/manage", status_code=303)

@router.get("/delete/{uid}/{dept}")
async def del_nosql(uid: str, dept: str):
    # 1. Delete from Main
    nosql_service.delete_nosql("company_main", uid)
    # 2. Delete from Dept Shard
    nosql_service.delete_nosql(f"shard_{dept.lower()}", uid)
    # 3. Delete from Parity Shard
    parity = "even" if int(uid) % 2 == 0 else "odd"
    nosql_service.delete_nosql(f"{parity}_shard", uid)
    
    return RedirectResponse("/nosql/manage", status_code=303)