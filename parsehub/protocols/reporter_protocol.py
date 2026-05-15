from typing import Protocol, Any


class Reporter(Protocol):

    def generate(
        self,
        records: Any
    ) -> str:
        ...