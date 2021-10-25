import json
import uuid
from datetime import datetime

from fastapi import FastAPI, File, UploadFile
from gridfs import GridFS

from dependencies import get_fs_dependency

app = FastAPI()


@app.post("/upload_file/")
async def create_upload_file(file: UploadFile = File(...), fs: GridFS = get_fs_dependency):
    contents = await file.read()
    obj = fs.put(contents, content_type=file.content_type)
    file_id = str(obj)

    # Create document with metadata
    file_metadata_dict = {
        "user_id": str(uuid.uuid4()),
        "created_datetime": str(datetime.now()),
        "file_id": file_id,
        "file_name": file.filename
    }
    with open(f"./files_metadata/{file_id}.txt", 'w') as file_metadata:
        file_metadata.write(json.dumps(file_metadata_dict))

    return {"file_id": file_id}
