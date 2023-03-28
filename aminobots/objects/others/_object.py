from dataclasses import dataclass
from typing import Any
from types import GeneratorType

__all__ = ("Object", "jsonExample")


@dataclass
class Object:
    json: Any

    def __bool__(self) -> bool:
        return bool(self.json)

    def __iter__(self) -> GeneratorType:
        yield from filter(lambda attr: not attr.startswith("__"), dir(self))

    # def __str__(self) -> str:
    #     return "<" + self.__class__.__name__ + "(" + (' '.join(
    #         f'{k}={v}' for k, v in self.json.items()
    #     ) if isinstance(self.json, dict) else str(list(self.json))) + ")>"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(json={self.json})"


jsonExample = {} or []
