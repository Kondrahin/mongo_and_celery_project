import bson
import gridfs
from celery import Celery

from mongo_services import db

app = Celery('files_tasks')
app.conf.broker_url = 'redis://redis:6379/0'
app.conf.result_backend = 'redis://redis:6379/0'


@app.task
def double_file(file_id: str):
    fs = gridfs.GridFS(db, "files_database")
    file_id_json = bson.objectid.ObjectId(file_id)
    file = fs.get(file_id_json)

    contents = file.read()
    obj = fs.put(contents*2, content_type=file.content_type)
    return {"id": str(obj)}
