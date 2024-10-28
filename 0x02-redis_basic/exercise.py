#!/usr/bin/env python3
"""
'exercise' creates a class enabling manipulation of a Redis database
"""
import redis
from typing import Union
import uuid


class Cache:
    """Blueprint facilitating Redis database interaction."""

    def __init__(self):
        """Constructor for all class instances."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Write information in the Redis database."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return (key)
