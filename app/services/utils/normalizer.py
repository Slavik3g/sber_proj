import dateparser
from ru_word2number import w2n

from app.exceptions.document import ProcessingException
from app.interfaces.base_services import BaseNormalizer


class DataNormalizer(BaseNormalizer):
    @classmethod
    def normalize(cls, tree: dict | str) -> dict | str:
        """
        Конвертация буквенных дат и нормализация и сроков.

        Args:
        - tree (dict | str): Входные данные для обработки.

        Returns:
        - dict | str: Обработанные данные содержащие числовые даты
                    и нормализованные к формату "ДД.ММ.ГГГГ" сроки.
        """
        try:
            for key, value in tree.items():
                if isinstance(value, dict):
                    cls.normalize(value)
                if 'дата' in key.lower():
                    tree[key] = cls.__convert_string_to_date(value)
                if 'срок' in key.lower():
                    tree[key] = cls.__parse_duration(value)
        except Exception as exc:
            raise ProcessingException(f"Ошибка при обработке.\nДетали: {exc}")
        return tree

    @staticmethod
    def __convert_string_to_date(stringed_date: str) -> str:
        """
        Преобразование буквенной даты в числовой формат даты.

        Args:
        - stringed_date (str): Буквенная дата.

        Returns:
        - str: Числовая строка даты в формате "ДД.ММ.ГГГГ".
        """
        parsed_date = dateparser.parse(stringed_date, languages=["ru"])
        return parsed_date.strftime("%d.%m.%Y") if parsed_date else None

    @classmethod
    def __parse_duration(cls, duration_text: str) -> str:
        """
        Извлечение и нормализация продолжительности времени из строки.

        Parameters:
            duration_text (str): Входная строка, содержащая описания длительности времени.

        Returns:
            str: Нормализованная и приведённая к формату "Г_М_Н_Д" строка, где:
            Г - год, М - месяц, Н – неделя, Д – день.
        """
        words = duration_text.split()

        delta = {
            'years': 0,
            'months': 0,
            'weeks': 0,
            'days': 0
        }

        for index, word in enumerate(words):
            # Обработка дат "полмесяца" и "полгода"
            if 'пол' in word[:3] and word != 'полтора':
                unit = cls.__find_mapped_word(word[3:])
                if unit == 'months':
                    delta['weeks'] += 2
                elif unit == 'years':
                    delta['months'] += 6

            elif (
                    cls.__find_mapped_word(word)
                    and index > 0
                    and ('полтора' == words[index - 1]
                         or cls.__get_number_from_string(words[index - 1]))
            ):
                unit = cls.__find_mapped_word(word)
                # Обработка дат "полтора года" и "полтора месяца"
                if words[index - 1] == 'полтора':
                    if unit == 'years':
                        delta['years'] += 1
                        delta['months'] += 6
                    elif unit == 'months':
                        delta['months'] += 1
                        delta['weeks'] += 2
                # Обработка всех остальных дат
                else:
                    delta[unit] += cls.__get_number_from_string(words[index - 1])
        return cls.__format_duration(delta)

    @staticmethod
    def __get_number_from_string(word: str) -> int | None:
        """
        Преобразование буквенной даты в числовой формат.

        Parameters:
            word (str): Входное чисто состоящее из цифр.

        Returns:
            int: Дата в числовом формате. Возвращает None в случае если было
            передано не число.
        """
        try:
            return w2n.word_to_num(word)
        except ValueError:
            return None

    @staticmethod
    def __find_mapped_word(word: str) -> str | None:
        """
         Сопоставление является ли слово подстрокой с словаре duration_mapping.

        Parameters:
            word (str): Входное слово.

        Returns:
            str: Сопоставленное значение со словарем duration_mapping, иначе None.
        """
        duration_mapping = {
            "год": "years",
            "лет": "years",
            "месяц": "months",
            "недел": "weeks",
            "ден": "days",
            "дне": "days",
            "дня": "days",
        }
        for mapped_word in duration_mapping:
            if mapped_word in word:
                return duration_mapping[mapped_word]
        return None

    @staticmethod
    def __format_duration(delta: dict) -> str:
        """
        Приведение к формату "Г_М_Н_Д" словаря сдержащего поля: years, months, weeks, days.

        Parameters:
            delta (dict): Словаря сдержащий поля: years, months, weeks, days.

        Returns:
            str: Строка в формате "Г_М_Н_Д".
        """
        formatted_duration = f"{delta['years']}_{delta['months']}_{delta['weeks']}_{delta['days']}"
        return formatted_duration
