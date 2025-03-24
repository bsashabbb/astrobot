from __future__ import annotations
from typing import Optional, List, Union

class setChatAdministratorCustomTitle:
    def __init__(
        self,
        chat_id: 'Union[str]',
        user_id: 'int',
        custom_title: 'str'
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.custom_title = custom_title