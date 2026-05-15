from typing import Protocol, Any


class Parser(Protocol):

    def parse(
        self,
        raw_data: str
    ) -> Any:
        ...