from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import ORJSONResponse

from app.exceptions.base import BaseDocumentException


def document_exception_handler(request: Request, exc: BaseDocumentException):
    return ORJSONResponse(exc.detail, status_code=exc.status_code)


def default_exception_handler(request: Request, exc: Exception):
    return ORJSONResponse(
        "Неожиданная ошибка",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def add_exception_handlers(app: FastAPI):
    app.add_exception_handler(BaseDocumentException, document_exception_handler)
    app.add_exception_handler(Exception, default_exception_handler)
