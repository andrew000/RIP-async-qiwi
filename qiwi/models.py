from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


class Amount(BaseModel):
    value: str
    currency: str


class Status(BaseModel):
    value: Literal['WAITING', 'PAID', 'REJECTED', 'EXPIRED']
    changedDateTime: str


class CustomFields(BaseModel):
    paySourcesFilter: Optional[str]
    themeCode: Optional[str]


class Customer(BaseModel):
    email: Optional[str]
    phone: Optional[str]
    account: Optional[str]


class CreateBillRequest(BaseModel):
    amount: Amount
    expirationDateTime: str
    comment: Optional[str]
    customer: Optional[Customer]
    customFields: Optional[CustomFields]


class CreateBillResponse(BaseModel):
    site_id: str = Field(..., alias='siteId')
    bill_id: str = Field(..., alias='billId')
    amount: Amount
    status: Status
    CustomFields: Optional[CustomFields]
    customer: Optional[Customer]
    comment: Optional[str]
    creation_date_time: datetime = Field(..., alias='creationDateTime')
    expiration_date_time: datetime = Field(..., alias='expirationDateTime')
    pay_url: str = Field(..., alias='payUrl')


CheckBillResponse = CreateBillResponse  # Same response data
