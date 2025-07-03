import csv
import requests
from datetime import datetime
from io import StringIO

def vu(ID):
    try:
        url = "https://raw.githubusercontent.com/ax8n/resute/refs/heads/main/access.csv"
        response = requests.get(url)
        response.raise_for_status()
        csv_data = StringIO(response.text)
        reader = csv.DictReader(csv_data)

        for row in reader:
            user_id = row["user_id"].strip().replace('\r', '').replace('\n', '')
            if user_id == str(ID).strip():
                expire = datetime.strptime(row["expire_date"].strip(), "%Y-%m-%d %H:%M:%S")
                if datetime.now() <= expire:
                    return True
                else:
                    print("✖ Access expired!")
                    print("To renew or buy access, contact: @aniipy")
                    return False
        print("✖ Invalid user ID.")
        return False

    except Exception as e:
        print("✖ Error checking access")
        return False
