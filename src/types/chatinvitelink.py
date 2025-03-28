from __future__ import annotations
from typing import Optional, List, Union

class ChatInviteLink:
    def __init__(
        self,
        invite_link: 'str',
        creator: 'User',
        creates_join_request: 'bool',
        is_primary: 'bool',
        is_revoked: 'bool',
        name: 'Optional[str]' = None,
        expire_date: 'Optional[int]' = None,
        member_limit: 'Optional[int]' = None,
        pending_join_request_count: 'Optional[int]' = None,
        subscription_period: 'Optional[int]' = None,
        subscription_price: 'Optional[int]' = None
    ):
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count
        self.subscription_period = subscription_period
        self.subscription_price = subscription_price