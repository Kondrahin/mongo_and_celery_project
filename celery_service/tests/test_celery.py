import pytest
from gridfs import NoFile

from celery_worker import double_file


def test_create_task():
    with pytest.raises(NoFile):
        double_file.delay("5bce2e42f6738f20cc12518d").get()
