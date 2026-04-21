from fastapi import FastAPI
from starlette.responses import FileResponse
from prometheus_client import start_http_server

app = FastAPI()

# Start Prometheus metrics server (runs on separate port)
start_http_server(8001)

@app.get('/')
def home():
    return FileResponse('index.html')