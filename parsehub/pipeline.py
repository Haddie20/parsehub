from parsehub.protocols.parser_protocol import Parser
from parsehub.protocols.validator_protocol import Validator
from parsehub.protocols.reporter_protocol import Reporter


class DataPipeline:

    def __init__(
        self,
        parser: Parser,
        validator: Validator | None = None,
        reporter: Reporter | None = None
    ):

        self.parser = parser
        self.validator = validator
        self.reporter = reporter

    def process(
        self,
        raw_data: str
    ):

        records = self.parser.parse(
            raw_data
        )

        if self.validator:

            records = (
                self.validator.validate(
                    records
                )
            )

        return records

    def report(
        self,
        records
    ) -> str:

        if not self.reporter:

            raise ValueError(
                "No reporter configured"
            )

        return (
            self.reporter.generate(
                records
            )
        )