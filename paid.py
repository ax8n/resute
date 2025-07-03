import csv
import requests
from datetime import datetime
from io import StringIO

def vu(ID=None):
    try:
        if ID is None or str(ID).strip() == "":
            print("✖ Invalid user ID.")
            return False

        url = "https://raw.githubusercontent.com/ax8n/resute/refs/heads/main/access.csv"
        response = requests.get(url)
        response.raise_for_status()

        csv_data = StringIO(response.text)
        reader = csv.DictReader(csv_data)

        for row in reader:
            user_id = row["user_id"].strip()
            if user_id == str(ID).strip():
                raw_date = row["expire_date"].strip()
                cleaned_date = " ".join(raw_date.split())
                try:
                    expire = datetime.strptime(cleaned_date, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    break  

                if datetime.now() <= expire:
                    return True  
                else:
                    break  

        print("✖ Access expired!")
        print("To renew or buy access, contact: @aniipy")
        return False

    except Exception as e:
        print(f"✖ Error checking access: {e}")
        return False
