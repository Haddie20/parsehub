class XMLParser:

    def parse(
        self,
        raw_data: str
    ):

        records = []

        for chunk in raw_data.split(
            "<record>"
        ):

            if "</record>" in chunk:

                value = chunk.split(
                    "</record>"
                )[0]

                records.append(
                    value.split(
                        "<field>"
                    )
                )

        return records