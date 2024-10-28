#!/usr/bin/env python3
"""
'exercise' creates a class enabling manipulation of a Redis database
"""
import redis
from typing import Callable, Optional, Union
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

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None,
    ) -> Union[str, bytes, int, float, None]:
        """
        returns the value stored in the redis store at the key by converting it
        to its original data type by calling the function fn. if the key is not
        found, it returns None
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            value = fn(value)
        return value

    def get_int(self, key: str) -> Union[int, None]:
        """
        returns the value stored in the redis store at the key as an int
        """
        return self.get(key, int)  # type: ignore

    def get_str(self, key: str) -> Union[str, None]:
        """
        returns the value stored in the reds store at the key as str
        """
        return self.get(key, str)  # type: ignore
