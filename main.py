import requests
import datetime

FIREBASE_URL = "https://admin-panel-d48f2-default-rtdb.firebaseio.com/keys/"

def validate_key(key):
    url = f"{FIREBASE_URL}{key}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        key_data = response.json()
        if key_data:
            expiry_date_str = key_data.get('expiry_date')
            expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
            
            if datetime.date.today() <= expiry_date:
                return True, "Key is valid."
            else:
                return False, "Key has expired."
        else:
            return False, "Invalid key."
    else:
        return False, "Error connecting to Firebase."

# Usage Example:
# user_key = "SR-GAMER-XXXX-XXXX"
# is_valid, message = validate_key(user_key)
# print(message)
