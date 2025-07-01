import csv
import requests
from datetime import datetime
from io import StringIO

def vu(ID, token):
    try:
        url = "https://raw.githubusercontent.com/ax8n/aniipy/main/access.csv"
        response = requests.get(url)
        response.raise_for_status()
        csv_data = StringIO(response.text)
        reader = csv.DictReader(csv_data)

        for row in reader:
            if row["user_id"] == str(ID) and row["token"] == token:
                expire = datetime.strptime(row["expire_date"], "%Y-%m-%d %H:%M:%S")
                if datetime.now() <= expire:
                    return True
                else:
                    print("✖ Access expired!")
                    print("To renew or buy access, contact: @aniipy")
                    return False
        print("✖ Invalid token or user ID.")
        return False
    except Exception as e:
        print(f"✖ Error checking access: {e}")
        return False
