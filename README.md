# 🥝 async-qiwi

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple wrapper for QIWI Kassa for Invoice creating.

**Alpha release!**

## Installation

```shell
$ python3 -m pip install async-qiwi
```

## Dependencies

| Library  | Description       |
|----------|-------------------|
| aiohttp  | http client       |
| pydantic | schema validation |

## Example

```python
import asyncio
import logging
from datetime import datetime, timedelta

from qiwi import Qiwi

# noinspection PyArgumentList
logging.basicConfig(handlers=[logging.FileHandler('log.txt', 'w', 'utf-8')],
                    level=logging.WARNING,
                    format='{%(pathname)s:%(lineno)d} %(asctime)s - %(levelname)s - %(message)s')

qiwi = Qiwi(private_key='PRIVATE KEY')  # Use your PRIVATE KEY from https://qiwi.com/p2p-admin/transfers/api


async def test():
    bill = await qiwi.create_bill(1, 'RUB', datetime.utcnow() + timedelta(hours=1))
    print(bill.payUrl)
    check = await qiwi.check_bill(bill_id=bill.billId)
    print(check.status)

    await qiwi.close_session()  # Close aiohttp session on shutdown!


loop = asyncio.get_event_loop()
loop.create_task(test())
loop.run_forever()

```

