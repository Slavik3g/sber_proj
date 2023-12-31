from app.exceptions.document import ProcessingException
from app.interfaces.base_services import BaseHandler


class DataHandler(BaseHandler):
    @classmethod
    async def __merge_dicts(cls, first: dict, second: dict) -> dict:
        """
        Рерурсивное объедение двух словарей.

        Parameters:
            first (dict): Первый словарь.
            second (dict): Второй словарь.
        Returns:
            dict: Объединенные словари.
        """

        merged = first.copy()
        for key, value in second.items():
            if (
                    key in merged
                    and isinstance(merged[key], dict)
                    and isinstance(value, dict)
            ):
                merged[key] = await cls.__merge_dicts(merged[key], value)
            elif (
                    key not in merged
                    and isinstance(value, list)
            ):
                merged[key] = cls.__get_flat_values(value)
            else:
                merged[key] = value
        return merged

    @classmethod
    def __get_flat_values(cls, to_merge: list) -> list:
        """
        Объединить список словарей в список строк
        """
        result = []
        for item in to_merge:
            if isinstance(item, dict):
                result.extend(cls.__get_flat_values(list(item.values())))
            else:
                result.append(item)
        return result

    @classmethod
    async def merge_trees(cls, data: dict) -> dict:
        """
        Рерурсивное объедение двух вложенных словарей.

        Returns:
            dict: Один словарь с объединенными полями.
        """
        try:
            result = {}
            if isinstance(data, dict):
                for child in data.values():
                    result = await cls.__merge_dicts(result, child)
            else:
                return data
            return result
        except Exception as exc:
            raise ProcessingException(f"Ошибка во время объединения.\nДетали: {exc}")
