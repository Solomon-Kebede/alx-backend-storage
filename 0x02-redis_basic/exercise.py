#!/usr/bin/env python3
"""
1. Reading from Redis and recovering original type
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Wrapper that counts the number of calls of a certain method'''
    @wraps(method)
    def wrapper(*args, **kwargs):
        key = method.__qualname__
        self = args[0]
        self._redis.incr(key)
        output = method(*args, **kwargs)
        return output
    return wrapper


def call_history(method: Callable) -> Callable:
    '''Wrapper that saves function call history a certain method'''
    @wraps(method)
    def wrapper(*args, **kwargs):
        key_base = method.__qualname__
        input_key = f'{key_base}:inputs'
        output_key = f'{key_base}:outputs'
        self = args[0]
        self._redis.rpush(input_key, f"('{args[1]}',)")
        output = method(*args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    '''Display the history of calls of a
    particular function'''
    key_base = method.__qualname__
    r = redis.Redis()
    inputs = r.lrange(f"{key_base}:inputs", 0, -1)
    outputs = r.lrange(f"{key_base}:outputs", 0, -1)
    assert len(inputs) == len(outputs)
    print(f'{key_base} was called {len(inputs)} times:')
    for ins, outs in zip(inputs, outputs):
        print(f"{key_base}(*{ins.decode('utf-8')}) -> {outs.decode('utf-8')}")


class Cache:
    """Cache class"""
    def __init__(self):
        """Instantiate a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
