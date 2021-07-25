from typing import Dict, Any, Callable
import functools
from .Helper import Helper


def set_base_context(func: Callable) -> None:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        context: Dict[str, Any] = {
            'title': 'Test RPC 1',
            'apps': Helper.getAllApps()
        }

        return func(*args, context, **kwargs, )

    return wrapper
