import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

# Initialize Firebase
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://admin-panel-d48f2-default-rtdb.firebaseio.com/'
})

def validate_key(key):
    ref = db.reference('keys/' + key)
    key_data = ref.get()
    
    if key_data:
        expiry_date_str = key_data.get('expiry_date')
        expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
        
        if datetime.date.today() <= expiry_date:
            return True, "Key is valid."
        else:
            return False, "Key has expired."
    else:

        return False, "Invalid key."

# Usage Example:
# user_key = "ENTERED_KEY"
# is_valid, message = validate_key(user_key)
# print(message)
