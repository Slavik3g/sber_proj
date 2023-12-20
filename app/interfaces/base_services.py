from abc import ABC, abstractmethod


class BaseService(ABC):
    """
    Интерфейс сервиса
    """
    @abstractmethod
    async def parse_document(self, data: str | dict) -> dict:
        raise NotImplementedError


class BaseConverter(ABC):
    """
    Интерфейс для конвертиртации деревьев в нужный
    """
    @abstractmethod
    async def convert(self, data: dict | str) -> dict:
        raise NotImplementedError


class BaseHandler(ABC):
    """
    Интерфейс для объединения деревьев
    """
    @abstractmethod
    async def merge_trees(self, data: dict) -> dict:
        raise NotImplementedError


class BaseNormalizer(ABC):
    """
    Интерфейс для нормализации дерева
    """
    @abstractmethod
    def normalize(self, data: dict) -> dict:
        raise NotImplementedError
