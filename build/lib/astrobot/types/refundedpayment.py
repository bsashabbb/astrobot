from __future__ import annotations
from typing import Optional, List, Union, Any

class RefundedPayment:
    """RefundedPayment Telegram API type"""

    def __init__(
        self,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        telegram_payment_charge_id: str,
        provider_payment_charge_id: Optional[str]
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
