#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""

import redis
import uuid
from typing import Any

class Cache:
	def __init__(self):
		self._redis = redis.Redis()

	def store(self, data -> Any) -> str:
		random_key = uuid.uuid4()
		# Store the data using the random key
		return str(random_key)