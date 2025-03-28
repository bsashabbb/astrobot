from __future__ import annotations
from typing import Optional, List, Union

class BackgroundTypePattern:
    def __init__(
        self,
        type: 'str',
        document: 'Document',
        fill: 'BackgroundFill',
        intensity: 'int',
        is_inverted: 'Optional[bool]' = None,
        is_moving: 'Optional[bool]' = None
    ):
        self.type = type
        self.document = document
        self.fill = fill
        self.intensity = intensity
        self.is_inverted = is_inverted
        self.is_moving = is_moving