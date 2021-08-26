import asyncio
import collections
import typing as t


class Node:
    __slots__ = ("value", "_next", "_prev",)

    def __init__(
        self,
        value: t.Any, *,
        _next: t.Optional["Node"] = None,
        _prev: t.Optional["Node"] = None,
    ) -> None:
        self.value = value

        self._next = _next
        self._prev = _prev

    @property
    def tail(self) -> "Node":
        node = self

        while node._next:
            node = node._next

        return node

    def bound(self, value: t.Any) -> "Node":
        cls = self.__class__

        node = self.tail
        prev = self if node is self else node

        node._next = cls(value, _prev=prev)

        return node._next

    def unbound(self) -> None:
        if not self._prev:  # self is head
            if self._next:
                self._next._prev = None

            return

        if not self._next:  # self is tail
            return setattr(self._prev, "_next", None)

        self._prev._next = self._next
        self._next._prev = self._prev


class Connection:
    def __init__(self) -> None:
        self._fs = collections.defaultdict(list)

    def dispatch(self, event: str, data: t.Dict[str, t.Any]):
        fs = self._fs

        for f in fs:
            fs.done(data)

        fs.clear()

    def wait_for(self, event: str, *, timeout: int = 5):
        future = asyncio.Future()
        self._fs[event].append(future)

        return asyncio.wait_for(future, timeout=timeout)
