import tempfile

import bson
import gridfs
from celery.result import AsyncResult
from fastapi import FastAPI, HTTPException
from loguru import logger
from starlette.responses import FileResponse

from celery_worker import double_file, app as celery_app
from dependencies import get_fs_dependency

app = FastAPI()


@app.post("/double_file/")
async def double_file_handler(file_id: str, fs: gridfs.GridFS = get_fs_dependency):
    try:
        fs.get(bson.objectid.ObjectId(file_id))
    except gridfs.errors.NoFile:
        raise HTTPException(status_code=404, detail=f"File with {file_id} wasn't found!")

    task = double_file.delay(file_id)
    return {"task_id": task.id}


@app.get("/download_file/{task_id}", response_class=FileResponse)
async def download_file(task_id: str, fs: gridfs.GridFS = get_fs_dependency):
    res = AsyncResult(task_id, app=celery_app)
    if res.state == "PENDING":
        raise HTTPException(status_code=404, detail=f"File associated with {task_id} wasn't found!")

    file_id = res.get()
    file_id = bson.objectid.ObjectId(file_id["id"])

    file = fs.get(file_id)
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.read())
        return FileResponse(tmp.name, media_type=file.content_type)
