from fastapi import FastAPI

from app.api.router import api_router
from app.exceptions.handlers import add_exception_handlers
from app.middlewares.content import DocumentTypeCheckerMiddleware

app = FastAPI()
app.add_middleware(DocumentTypeCheckerMiddleware)

app.include_router(api_router)
add_exception_handlers(app)
