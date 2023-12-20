from fastapi import status


class BaseDocumentException(Exception):
    DEFAULT_DETAIL = "Непредвиденная ошибка"
    DEFAULT_STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail: str | None = None, status_code: int | None = None):
        self.detail = detail or self.DEFAULT_DETAIL
        self.status_code = status_code or self.DEFAULT_STATUS_CODE
