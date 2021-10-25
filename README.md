## Simple application with mongodb and celery

**Deploy**

- `docker compose up -d`

###  Upload file in first service:

1. Go to `127.0.0.1:8000/docs`
2. Upload file via docs 
3. Copy `file_id`

### Double file using second service
1. Go to `127.0.0.1:8001/docs`
2. Double file via method `double_file` using a previously copied `file_id`
3. Copy `task_id`
4. Download doubled file via method `download_file` inserting a previously copied `task_id`
