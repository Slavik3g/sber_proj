from fastapi import APIRouter, Request, Body, HTTPException

from app.interfaces.base_services import BaseService

v1_router = APIRouter(prefix="/v1")


@v1_router.post('/parse_document/')
async def process_tree(request: Request, data: str | dict = Body(...)) -> dict:
    try:
        service: BaseService = request.state.service
        return await service.parse_document(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
