#!/usr/bin/env python3
"""
1. Reading from Redis and recovering original type
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwargs):
        key = method.__qualname__
        r = redis.Redis()
        r.incr(key)
        method(*args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """Instantiate a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store values in redis"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key, fn=None):
        """Get values in redis"""
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        elif fn is None:
            return value

    def get_str(*cache):
        """Convert to string"""
        return str(cache)

    def get_int(*cache):
        """Convert to integer"""
        return int(cache)
