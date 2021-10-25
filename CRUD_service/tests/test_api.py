from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_upload_file():
    response = client.post(
        "/upload_file/",
        files={"file": ("test_file.txt", open("tests/test_file.txt", "rb"))}
    )
    assert response.status_code == 200
    assert response.json()["file_id"] is not None


def test_upload_file_without_file():
    response = client.post("/upload_file/")
    assert response.status_code == 422


def test_create_metadata():
    response = client.post(
        "/upload_file/",
        files={"file": ("test_file.txt", open("tests/test_file.txt", "rb"))}
    )
    file_id = response.json()["file_id"]
    open(f"files_metadata/{file_id}.txt")
