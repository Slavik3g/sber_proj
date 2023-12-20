from app.interfaces.base_services import BaseService
from app.services.utils.converters import XmlConverter
from app.services.utils.handlers import DataHandler
from app.services.utils.normalizer import DataNormalizer


# class DocumentService(BaseService):
#     def __init__(self,
#                  converter: BaseConverter,
#                  handler: BaseHandler = DataNormalizer(),
#                  normalizer: BaseNormalizer = DataHandler()):
#         self.converter = converter
#         self.handler = handler
#         self.normalizer = normalizer
#
#     async def parse_document(self, data: str | dict) -> dict:
#         result = await self.converter.convert(data)
#         # result = await self.handler.merge_trees(result)
#         # result = await self.normalizer.normalize(result)
#         return result

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
        result = await XmlConverter.convert(data)
        result = await DataHandler.merge_trees(result)
        result = DataNormalizer.normalize(result)
        return result
