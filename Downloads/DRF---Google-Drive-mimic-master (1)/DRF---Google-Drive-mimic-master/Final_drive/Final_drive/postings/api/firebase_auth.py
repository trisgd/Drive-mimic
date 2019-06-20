# import pyrebase
# var firebaseConfig = {
#     apiKey: "AIzaSyC1utyp4gUdGWCzjTLZFbPhdCa0Jw7r36c",
#     authDomain: "gd-mimic.firebaseapp.com",
#     databaseURL: "https://gd-mimic.firebaseio.com",
#     projectId: "gd-mimic",
#     storageBucket: "gd-mimic.appspot.com",
#     messagingSenderId: "1026740904881",
#     appId: "1:1026740904881:web:8bd0c95c0bd477b6"
#   }
#   // Initialize Firebase
#   firebase = pyrebase.initialize_app(config)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from django.conf import settings

base_dir = settings.BASE_DIR
cert_dir = os.path.join(BASE_DIR, 'gd-mimic-11b6d082299b.json')

cred = credentials.Certificate(cert_dir)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gd-mimic.appspot.com'
})

bucket = storage.bucket()

source_file_name = os.path.join(BASE_DIR, "media")

def upload_blob("gd-mimic", source_file_name, files):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('gd-mimic')
    blob = bucket.blob(files)

    blob.upload_from_filename(source_file_name)

    ####
    
