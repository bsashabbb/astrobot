from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultCachedGif:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        gif_file_id: 'str',
        title: 'Optional[str]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None
    ):
        self.type = type
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content