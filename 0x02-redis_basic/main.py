#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

del cache
del key

cache = Cache()

TEST_CASES = {
    b"foo": None,
    "bar": lambda d: d.decode("utf-8"),
    123: int,
    b"foofoo": lambda d: d.decode("utf-8"),
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    print(cache.get(key, fn=fn), value)
    print(type(cache.get(key, fn=fn)))
    assert cache.get(key, fn=fn) == value
