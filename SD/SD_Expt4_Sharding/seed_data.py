import pandas as pd
import requests

# Load the 50 rows
df = pd.read_csv("data/dummy_users.csv")

print("Seeding data to server...")
for _, row in df.iterrows():
    # This sends data to the server, which then processes triple sharding
    try:
        requests.post("http://127.0.0.1:8000/sql/add", data=row.to_dict())
        requests.post("http://127.0.0.1:8000/nosql/add", data=row.to_dict())
    except Exception as e:
        print(f"Error seeding ID {row['id']}: {e}")

print("Seeding Done. Please refresh the browser.")