from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from . import sharding_manager, sql_service, utils

router = APIRouter(prefix="/sql")
templates = Jinja2Templates(directory="templates")

@router.get("/manage")
async def manage_sql(request: Request):
    return templates.TemplateResponse("manage_sql.html", {
        "request": request,
        "main_data": sql_service.fetch_sql("company_main"),
        "shard_hr": sql_service.fetch_sql("shard_hr"),
        "shard_it": sql_service.fetch_sql("shard_it"),
        "shard_eng": sql_service.fetch_sql("shard_engineering"),
        # Fetching CSV data for the right-side panel
        "odd_ids": utils.fetch_from_csv("SQL", "odd"),
        "even_ids": utils.fetch_from_csv("SQL", "even")
    })

@router.post("/add")
async def add_sql(id:str=Form(...), name:str=Form(...), contact:str=Form(...), 
                  email:str=Form(...), address:str=Form(...), joining_date:str=Form(...), 
                  dob:str=Form(...), age:int=Form(...), role:str=Form(...), 
                  salary:float=Form(...), department:str=Form(...), password:str=Form(...)):
    data = {"id": id, "name": name, "contact": contact, "email": email, "address": address,
            "joining_date": joining_date, "dob": dob, "age": age, "role": role,
            "salary": salary, "department": department, "password": password}
    sharding_manager.process_sharding(data, mode="SQL")
    return RedirectResponse("/sql/manage", status_code=303)

@router.get("/delete/{uid}/{dept}")
async def del_sql(uid: str, dept: str):
    sql_service.delete_sql("company_main", uid)
    sql_service.delete_sql(f"shard_{dept.lower()}", uid)
    # Also delete from parity DB
    parity = "even" if int(uid) % 2 == 0 else "odd"
    sql_service.delete_sql(f"{parity}_shard", uid)
    return RedirectResponse("/sql/manage", status_code=303)