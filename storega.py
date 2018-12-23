from google.cloud import storage

def create_bucket(bucket_name):
    """Creates a new bucket."""
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print('Bucket {} created'.format(bucket.name))

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
    # export GOOGLE_APPLICATION_CREDENTIALS=MyFirstProject-c3ea55891d63.json 
    # run it before run app 

            # bucket name , link file,                                                          name in bucket
    upload_blob('testdi','/home/drstrange/Code/FlaskPython/flaskupload/Store/uphinhtotest.png','test')