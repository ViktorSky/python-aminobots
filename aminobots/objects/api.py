from dataclasses import dataclass

__all__ = 'Api',


@dataclass
class Api:
    json: dict

    @property
    def duration(self) -> str:
        return self.json.get("api:duration")

    @property
    def message(self) -> str:
        return self.json.get("api:message")

    @property
    def statuscode(self) -> int:
        return self.json.get("api:statuscode")

    @property
    def timestamp(self) -> str:
        return self.json.get("api:timestamp")

    def __str__(self) -> str:
        return object.__str__(self)
