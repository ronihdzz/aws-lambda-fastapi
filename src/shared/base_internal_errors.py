from enum import Enum

class ErrorCodes(Enum):
    UNKNOW = 100, "Unknown Error"
    PYDANTIC_VALIDATIONS_REQUEST = 8001, "Failed pydantic validations on request"


    def __new__(cls, value: int, description: str) -> 'ErrorCodes':
        obj = object.__new__(cls)
        obj._value_ = value
        obj._description = description
        return obj

    @property
    def description(self) -> str:
        return self._description