class HTMLReporter:

    def generate(
        self,
        records
    ) -> str:

        output = "<ul>"

        for record in records:

            output += (
                f"<li>{record}</li>"
            )

        output += "</ul>"

        return output