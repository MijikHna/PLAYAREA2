from typing import Dict, Any, Callable

import functools
import json

from .Helper import Helper


def set_base_context(func: Callable) -> None:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        context: Dict[str, Any] = {
            'title': 'Test RPC 1',
            'js': {
                'apps': json.dumps(Helper.getAllApps(serialized=True)),
            },
        }

        return func(*args, context, **kwargs, )

    return wrapper
