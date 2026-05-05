from . import sql_service, nosql_service, utils

def process_sharding(user_data, mode="SQL"):
    # Generate common fields
    user_data['login_id'] = utils.make_login_id(user_data['name'], user_data['id'])
    user_data['password'] = utils.hash_pw(user_data['password'])
    
    parity = utils.get_parity(user_data['id'])
    dept = user_data['department'].lower()

    if mode == "SQL":
        # 1. Main DB
        sql_service.insert_sql("company_main", user_data)
        # 2. Dept Shard
        sql_service.insert_sql(f"shard_{dept}", user_data)
        # 3. Parity Shard (DB)
        sql_service.insert_sql(f"{parity}_shard", user_data)
        # 4. Parity Shard (CSV)
        utils.write_to_csv_shard("SQL", user_data)
    else:
        # 1. Main NoSQL
        nosql_service.insert_nosql("company_main", user_data)
        # 2. Dept Shard
        nosql_service.insert_nosql(f"shard_{dept}", user_data)
        # 3. Parity Shard (DB)
        nosql_service.insert_nosql(f"{parity}_shard", user_data)
        # 4. Parity Shard (CSV)
        utils.write_to_csv_shard("NOSQL", user_data)