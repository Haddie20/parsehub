from typing import Protocol, Any


class Validator(Protocol):

    def validate(
        self,
        records: Any
    ) -> Any:
        ...