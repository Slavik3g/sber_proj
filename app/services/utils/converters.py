import xml
import xmltodict

from app.exceptions.document import ValidationError
from app.interfaces.base_services import BaseConverter


class XmlConverter(BaseConverter):
    """
    Конвертер из XML в dict
    """
    @classmethod
    async def convert(cls, data: str) -> dict:
        try:
            return xmltodict.parse(data)["root"]
        except xml.parsers.expat.ExpatError:
            raise ValidationError("Ошибочные данные XML")
