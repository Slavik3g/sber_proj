from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.exceptions.document import ValidationError
from app.services.document_services import JsonProcessingService, XMLProcessingService
from fastapi import Request, Response


class ApplicationTypeMiddleware(BaseHTTPMiddleware):
    """
    Миддлвар для определения типа контента
    """
    service_mapping = {
        'application/json': JsonProcessingService(),
        'application/xml': XMLProcessingService()
    }

    async def dispatch(self,
                       request: Request,
                       call_next: RequestResponseEndpoint) -> Response:

        if content_type := request.headers.get('Content-Type'):
            request.state.service = self.service_mapping.get(content_type)

            if request.state.service is None:
                raise ValidationError(f"Формат '{content_type}' не поддерживается")

            response = await call_next(request)
            return response

        raise ValidationError(f"Формат '{content_type}' не поддерживается")