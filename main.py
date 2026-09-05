from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
return {
"status": "online",
"message": "Video Downloader API is running"
}
