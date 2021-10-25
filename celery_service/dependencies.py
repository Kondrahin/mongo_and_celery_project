from fastapi import Depends
from gridfs import GridFS

from mongo_services import db


def get_fs():
    return GridFS(db, "files_database")


get_fs_dependency = Depends(get_fs)
