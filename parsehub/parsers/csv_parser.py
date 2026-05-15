class CSVParser:

    def parse(
        self,
        raw_data: str
    ) -> list[list[str]]:

        lines = raw_data.split("\n")

        records = [
            line.split(",")
            for line in lines
            if line
        ]

        with open(
            "output.log",
            "a"
        ) as file:

            file.write(
                str(records) + "\n"
            )

        return records