#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""

import redis
import uuid
from typing import Any

class Cache:
    """Cache class"""
    def __init__(self):
        """Instantiate a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Store values in redis"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
