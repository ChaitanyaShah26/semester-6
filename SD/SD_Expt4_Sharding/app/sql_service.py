from .config import get_sql_conn

def insert_sql(db_name, data):
    try:
        conn = get_sql_conn(db_name)
        cursor = conn.cursor()
        cols, params = ", ".join(data.keys()), ", ".join(["%s"] * len(data))
        cursor.execute(f"INSERT INTO users ({cols}) VALUES ({params})", tuple(data.values()))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Insert Error in {db_name}: {e}")

def fetch_sql(db_name):
    try:
        conn = get_sql_conn(db_name)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        res = cursor.fetchall()
        conn.close()
        return res
    except Exception as e:
        print(f"Fetch Error in {db_name}: {e}")
        return [] # Return empty list so UI doesn't crash

def search_sql_user(db_name, uid):
    try:
        conn = get_sql_conn(db_name)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (uid,))
        res = cursor.fetchone()
        conn.close()
        return res
    except:
        return None

def delete_sql(db_name, uid):
    try:
        conn = get_sql_conn(db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (uid,))
        conn.commit()
        conn.close()
    except:
        pass