from fastapi import status

from app.exceptions.base import BaseDocumentException


class ProcessingException(BaseDocumentException):
    DEFAULT_DETAIL = "Ошибка при обработке документа"
    DEFAULT_STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR


class ValidationError(BaseDocumentException):
    DEFAULT_DETAIL = "Некорректные данные"
    DEFAULT_STATUS_CODE = status.HTTP_422_UNPROCESSABLE_ENTITY
