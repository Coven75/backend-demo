import logging

import uvicorn
from fastapi import FastAPI, APIRouter

from config import settings
from app.admin.router import router as admin_router
from app.public.router import router as public_router
from plugins.logger import load_logger
from plugins.translation import load_translations

app = FastAPI()
load_logger()

app.include_router(admin_router, prefix='/api')
app.include_router(public_router, prefix='/api')

# objgraph.show_refs([service], filename='sample-graph.png')


def load_plugins():
    load_translations()


if __name__ == "__main__":
    load_plugins()
    uvicorn.run(
        "main:app",
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
        log_level="info"
    )
