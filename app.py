import os 
from flask import Flask , flash, request, redirect,url_for
from flask import send_from_directory
from werkzeug import SharedDataMiddleware
from werkzeug.utils import secure_filename
import json 

from google.cloud import storage

UPLOAD_FOLDER = './Store'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload_file():
    idToken = request.headers['tokenId']
    if request.method == 'POST':
        if 'file' not in request.files :
            flash('not file path')
            return "error not file path"
            # redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('no file select')
            return 'error no file select'
            # redirect(request.url)

        if file  and allowed_file(file.filename) :
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            status = 'success'
            resutl = {
                'file name': filename,
                'status' : status 
            }
            print (os.path.join(app.config['UPLOAD_FOLDER'],filename))
            upload_blob('testdi',os.path.join(app.config['UPLOAD_FOLDER'],filename),'test222')

            return json.dumps(resutl)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

if __name__ == "__main__" :
    app.debug = True
    app.run(host='0.0.0.0')
