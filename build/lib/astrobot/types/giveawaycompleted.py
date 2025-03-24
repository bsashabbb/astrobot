from __future__ import annotations
from typing import Optional, List, Union, Any

class GiveawayCompleted:
    """GiveawayCompleted Telegram API type"""

    def __init__(
        self,
        winner_count: int,
        unclaimed_prize_count: Optional[int],
        giveaway_message: Optional['Message'],
        is_star_giveaway: Optional[bool]
    ):
        self.winner_count = winner_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.giveaway_message = giveaway_message
        self.is_star_giveaway = is_star_giveaway
