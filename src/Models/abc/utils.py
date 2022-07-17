from __future__ import annotations

import asyncio
import time
from typing import TypeAlias, Generic, TypeVar, Protocol, Callable, Awaitable, Any

_seconds: TypeAlias = int
T = TypeVar("T")
V = TypeVar("V")
K = TypeVar("K")


__all__ = ("loop", "cache_for")


class CachedAwaitable(Protocol[T, V, K]):
    __cache__: _CachedFunc[T, V, K]

    async def __call__(self, *args: T, **kwargs: V) -> K:
        pass


class _CachedValue(Generic[K]):
    """
    Value for cache_for
    """
    def __init__(self, value: K, duration: _seconds):
        self.value: K = value
        self.duration = duration
        self.time_began = time.time()

    @property
    def needs_refreshed(self) -> bool:
        return time.time() - self.time_began > self.duration


class _CachedFunc(Generic[T, V, K]):
    """
    Function representation for cache_for
    """
    def __init__(self, func: Callable[[T, V], Awaitable[K]], duration: _seconds):
        self.func = func
        self.duration = duration
        self.cache: dict[Any, _CachedValue[K]] = {}

    async def call(self, *args: T, **kwargs: V) -> K:
        key = str(args) + str(kwargs)
        if key not in self.cache or self.cache[key].needs_refreshed:
            # is not present or is time to reset
            self.cache[key] = _CachedValue(await self.func(*args, **kwargs), self.duration)
        return self.cache[key].value


def cache_for(*, seconds: int = 0, minutes: int = 0, hours: int = 0):
    duration = seconds + minutes * 60 + hours * 60 * 60

    def inner(func: CachedAwaitable[T, V, K]):
        func.__cache__ = _CachedFunc(func, duration)

        async def wrapper(*args: T, **kwargs: V) -> K:
            return await func.__cache__.call(*args, **kwargs)

        return wrapper
    return inner


class Loop(Generic[T]):
    def __init__(self, func: T, duration: _seconds, count: int = -1):
        self.func = func
        self.duration = duration
        self.count = count
        self._continue = False

    async def _loop(self, *args: Any, **kwargs: Any) -> None:
        self._continue = True
        count = 0
        while self._continue and (count < self.count or self.count == -1):
            await self.func(*args, **kwargs)
            await asyncio.sleep(self.duration)
            count += 1

    def start(self, *args: Any, **kwargs: Any) -> None:
        # potentially add cancel features? meh
        asyncio.create_task(self._loop(*args, **kwargs))

    def stop(self) -> None:
        self._continue = False

    def change_duration(self, *, seconds: int = 0, minutes: int = 0, hours: int = 0) -> None:
        if seconds == minutes == hours == 0:
            return
        self.duration = seconds + minutes * 60 + hours * 60 * 60


def loop(*, seconds: int = 0, minutes: int = 0, hours: int = 0, count: int = -1) -> Callable[[T], Loop[T]]:
    """
    Loops a function every so often
    :param seconds:
    :param minutes:
    :param hours:
    :param count:
    :return:
    """

    def inner(func: T) -> Loop[T]:
        return Loop(func, seconds + minutes * 60 + hours * 60 * 60, count)

    return inner
