from pydantic import validator
from pydantic import validators

__all__ = (
    'bool_validator',
    'list_validator',
    'obj_validator'
)


def list_validator(*attr: str):
    @validator(*attr, allow_reuse=True)
    def _validator(value):
        return value if isinstance(value, list) else []
    return _validator


def bool_validator(*attr: str):
    @validator(*attr, allow_reuse=True)
    def _validator(value):
        return value if isinstance(value, bool) else bool(value)
    return _validator


def obj_validator(type: type, *attr: str):
    @validator(*attr, allow_reuse=True)
    def _validator(value):
        return value if isinstance(value, type) else type()
    return _validator
