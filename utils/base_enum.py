from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def is_valid(cls, value):
        """
        >>> class E(BaseEnum):
        ...     x = "a"
        ...     y = "b"

        >>> E.is_valid("a")
        True
        >>> E.is_valid("c")
        False
        >>> E.is_valid("x")
        False

        check is value is a valid value
        :param value:
        :return: True if valid else False
        """
        return value in cls._value2member_map_

    @classmethod
    def values(cls):
        """
        >>> class E(BaseEnum):
        ...     x = "a"
        ...     y = "b"

        >>> E.values()
        ['a', 'b']

        get all values of class
        :return: values list
        """
        return [x.value for x in cls]
