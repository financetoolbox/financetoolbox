import os
import datetime as dt
from typing import Optional


class CLI:

    def __init__(self):
        self.execution_ts = dt.datetime.utcnow()

    def hello(self, name: Optional[str] = None) -> str:
        return f"Hello, {name or 'word'}!"

    def version(self) -> str:
        with open(os.path.join(os.path.dirname(__file__), "VERSION"), "r") as file:
            return file.read().strip()
