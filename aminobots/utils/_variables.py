from typing import Any, Iterable

__all__ = (
    "Variables",
)


class Variables:
    __vars = {}

    @property
    def __dict__(self) -> dict:
        return self.__vars

    def __init__(self,
                 *args,
                 **kwargs) -> None:
        self.__vars.update({key: None for key in args} | kwargs)

    def __dir__(self) -> Iterable[str]:
        f"""{object.__dir__.__doc__}"""
        return self.__vars.keys()

    def __delattr__(self,
                    item: Any) -> None:
        f"""{object.__delattr__.__doc__}"""
        del self.__vars[item]

    def __getattr__(self,
                         item: Any) -> Any:
        f"""{object.__getattribute__.__doc__}"""
        return self.__vars[item]

    def __setattr__(self,
                    key: Any,
                    value: Any) -> None:
        f"""{object.__setattr__.__doc__}"""
        self.__vars[key] = value
