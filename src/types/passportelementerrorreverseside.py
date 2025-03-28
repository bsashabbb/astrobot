from __future__ import annotations
from typing import Optional, List, Union

class PassportElementErrorReverseSide:
    def __init__(
        self,
        source: 'str',
        type: 'str',
        file_hash: 'str',
        message: 'str'
    ):
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message