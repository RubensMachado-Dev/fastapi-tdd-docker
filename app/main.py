# project/app/main.py


import logging

import uvicorn
from fastapi import FastAPI
from api import ping


log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")



@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8002, reload=True)