# project/app/main.py


import logging

import uvicorn
from fastapi import FastAPI

from app.api import ping, summaries


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )  # new

    return application


log = logging.getLogger(__name__)

app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
