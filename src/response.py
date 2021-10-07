import json
from starlette.responses import Response
from typing import Dict


class JSONResponseObject(Response):
    media_type = "application/json"

    def render(self, content: Dict) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=True,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")
