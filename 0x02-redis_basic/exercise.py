#!/usr/bin/env python3
"""
'exercise' creates a class enabling manipulation of a Redis database
"""
from functools import wraps
import redis
from typing import Callable, Optional, Union
import uuid


def call_history(method: Callable) -> Callable:
    """
    decorates a method to record its input output history
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        meth_name = method.__qualname__
        self._redis.rpush(meth_name + ":inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(meth_name + ":outputs", output)
        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    decorates a method to count how many times it was called
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Blueprint facilitating Redis database interaction."""

    def __init__(self):
        """Constructor for all class instances."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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