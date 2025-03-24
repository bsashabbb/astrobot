from __future__ import annotations
from typing import Optional, List, Union

class sendVideo:
    def __init__(
        self,
        chat_id: 'Union[str]',
        video: 'Union[str]',
        business_connection_id: 'Optional[str]' = None,
        message_thread_id: 'Optional[int]' = None,
        duration: 'Optional[int]' = None,
        width: 'Optional[int]' = None,
        height: 'Optional[int]' = None,
        thumbnail: 'Optional[Union[str]]' = None,
        caption: 'Optional[str]' = None,
        parse_mode: 'Optional[str]' = None,
        caption_entities: 'Optional[List[MessageEntity]]' = None,
        show_caption_above_media: 'Optional[bool]' = None,
        has_spoiler: 'Optional[bool]' = None,
        supports_streaming: 'Optional[bool]' = None,
        disable_notification: 'Optional[bool]' = None,
        protect_content: 'Optional[bool]' = None,
        allow_paid_broadcast: 'Optional[bool]' = None,
        message_effect_id: 'Optional[str]' = None,
        reply_parameters: 'Optional[ReplyParameters]' = None,
        reply_markup: 'Optional[Union[ReplyKeyboardMarkup]]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.video = video
        self.duration = duration
        self.width = width
        self.height = height
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler
        self.supports_streaming = supports_streaming
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.allow_paid_broadcast = allow_paid_broadcast
        self.message_effect_id = message_effect_id
        self.reply_parameters = reply_parameters
        self.reply_markup = reply_markup