class TextReporter:

    def generate(
        self,
        records
    ) -> str:

        return "\n".join(
            str(record)
            for record in records
        )