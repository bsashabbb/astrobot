from __future__ import annotations
from typing import Optional, List, Union

class PassportElementErrorFiles:
    def __init__(
        self,
        source: 'str',
        type: 'str',
        file_hashes: 'List[str]',
        message: 'str'
    ):
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message