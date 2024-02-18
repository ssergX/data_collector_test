from fastapi import FastAPI
from routers import device, stats, maths

app = FastAPI()


app.include_router(device.router, prefix="/devices", tags=["devices"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])
app.include_router(maths.router, prefix="/maths", tags=["maths"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
