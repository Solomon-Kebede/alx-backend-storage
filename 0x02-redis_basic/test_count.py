#!/usr/bin/env python3

from redis import Redis
from web import get_page

REDIS = Redis()
url = "http://google.com"
before_count = int(REDIS.get("count:{}".format(url)))
get_page(url)
after_count = int(REDIS.get("count:{}".format(url)))
if after_count - before_count == 1:
    print("OK")
else:
    print("Fail")