import hashlib, os, pandas as pd

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

def make_login_id(name, uid):
    parts = name.strip().split()
    first = parts[0][0]
    last = parts[-1] if len(parts) > 1 else ""
    return f"{first}{last}{uid}".lower()

def get_parity(uid):
    return "even" if int(uid) % 2 == 0 else "odd"

def write_to_csv_shard(mode, data):
    parity = get_parity(data['id'])
    # Ensures naming matches: sql_odd.csv or nosql_even.csv
    filename = f"{mode.lower()}_{parity}.csv"
    path = os.path.join("data", filename)
    
    # Ensure data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")
        
    df = pd.DataFrame([data])
    # header=not os.path.exists(path) ensures headers are written only once
    df.to_csv(path, mode='a', index=False, header=not os.path.exists(path))

def fetch_from_csv(mode, parity):
    filename = f"{mode.lower()}_{parity}.csv"
    path = os.path.join("data", filename)
    if os.path.exists(path):
        try:
            return pd.read_csv(path).to_dict('records')
        except:
            return []
    return []