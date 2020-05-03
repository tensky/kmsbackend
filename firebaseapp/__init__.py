import firebase_admin
from firebase_admin import credentials

if not firebase_admin._apps:
    cred = credentials.Certificate("./key.json")
    firebase_admin.initialize_app(cred)