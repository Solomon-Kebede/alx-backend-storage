#!/usr/bin/env python3
"""
5. Implementing an expiring web cache and tracker
"""

import redis
from typing import Callable
from functools import wraps
import requests


def request_count(func: Callable) -> Callable:
    '''Request count for a requested url'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        redis_client = redis.Redis()
        url = args[0]
        key = f'count:{url}'
        redis_client.expire(key, 10)
        redis_client.incr(key)
        print(key)
        return func(*args, **kwargs)
    return wrapper


@request_count
def get_page(url: str) -> str:
    '''Uses the requests module to obtain the HTML
    content of a particular URL and returns it'''
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    print(get_page('https://httpbin.org/anything'))
