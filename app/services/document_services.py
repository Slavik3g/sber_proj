from app.interfaces.base_services import BaseService
from app.services.utils.converters import XmlConverter
from app.services.utils.handlers import DataHandler
from app.services.utils.normalizer import DataNormalizer


class JsonProcessingService(BaseService):
    """
    Обработка JSON деревьев
    """

    @classmethod
    async def parse_document(cls, data: dict) -> dict:
        result = await DataHandler.merge_trees(data)
        result = DataNormalizer.normalize(result)
        return result


class XMLProcessingService(BaseService):
    """
    Обработка XML деревьев
    """

    @classmethod
    async def parse_document(cls, data: str) -> dict:
        result = XmlConverter.convert(data)
        result = await DataHandler.merge_trees(result)
        result = DataNormalizer.normalize(result)
        return result
