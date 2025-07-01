import csv
import requests
from datetime import datetime
from io import StringIO

def check_paid_access(user_id, token):
    try:
        url = "https://raw.githubusercontent.com/ax8n/aniipy/main/access.csv"
        response = requests.get(url)
        response.raise_for_status()
        csv_data = StringIO(response.text)
        reader = csv.DictReader(csv_data)

        for row in reader:
            if row["user_id"] == str(user_id) and row["token"] == token:
                expire = datetime.strptime(row["expire_date"], "%Y-%m-%d")
                if datetime.now() <= expire:
                    return True
                else:
                    print("✖ Access expired.")
                    return False
        print("✖ Invalid token or ID.")
        return False
    except Exception as e:
        print(f"✖ Error: {e}")
        return False
