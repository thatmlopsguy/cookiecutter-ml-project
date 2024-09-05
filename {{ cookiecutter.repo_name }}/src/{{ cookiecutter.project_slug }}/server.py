import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from config import settings

app = FastAPI(
    title=settings.project_name,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


@app.get("/")
async def root():
    return RedirectResponse("/docs")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        access_log=True,
    )
