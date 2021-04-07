import asyncio
from asyncio.log import logger
from datetime import datetime
from typing import Optional, Union
from uuid import uuid4

from aiohttp import ClientSession

from .methods import ApiMethods
from .models import Amount, CreateBillRequest, CreateBillResponse, Customer
from .utils import prepare_amount_value, process_result


class Qiwi:

    def __init__(self, private_key: str):
        self.__private_key = private_key
        self._session = ClientSession()
        self._headers = {
            'Authorization': f'Bearer {self.__private_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    async def create_bill(self, value: Union[int, float], currency: str, expiration_date_time: datetime,
                          customer_phone: Optional[str] = None, customer_email: Optional[str] = None,
                          customer_account: Optional[str] = None, comment: Optional[str] = None,
                          custom_fields: Optional[dict] = None) -> CreateBillResponse:
        data = CreateBillRequest(
            amount=Amount(
                value=prepare_amount_value(value),
                currency=currency
            ),
            expirationDateTime=expiration_date_time.strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            comment=comment,
            customer=Customer(
                phone=customer_phone,
                email=customer_email,
                account=customer_account
            ),
            customFields=custom_fields
        )

        async with self._session.put(f"{ApiMethods.CREATE_BILL}{uuid4().hex}", json=data.dict(),
                                     headers=self._headers) as resp:
            result = process_result(CreateBillResponse, await resp.json(), data.dict())
            return result

    async def check_bill(self, bill_id):
        async with self._session.get(f"{ApiMethods.CHECK_BILL}{bill_id}", headers=self._headers) as resp:
            result = CreateBillResponse(**(await resp.json()))
            return result

    async def close_session(self):
        await self._session.close()
        await asyncio.sleep(.25)
        logger.info('QIWI session closed.')


__all__ = ['Qiwi']
