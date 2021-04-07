import json
import logging
from typing import Optional, Type, Union

from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)


def prepare_amount_value(digit: Union[int, float]) -> str:
    return '{:.2f}'.format(digit)


def process_result(model: Type[BaseModel], result: dict, request: Optional[dict] = None):
    try:
        processed = model(**result)

    except ValidationError as exc:
        logger.error('Validation error in %s:\n'
                     'Request: %s'
                     '\n'
                     'Response: %s', model.__name__, json.dumps(request, indent=4), json.dumps(result, indent=4))
        raise ValidationError(exc.raw_errors, model)

    else:
        return processed
