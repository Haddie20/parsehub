class BasicValidator:

    def validate(
        self,
        records
    ):

        cleaned = []

        for record in records:

            if record:

                valid = True

                for field in record:

                    if field == "":
                        valid = False

                if valid:
                    cleaned.append(
                        record
                    )

        return cleaned