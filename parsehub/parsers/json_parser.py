import json


class JSONParser:

    def parse(
        self,
        raw_data: str
    ):

        return json.loads(
            raw_data
        )