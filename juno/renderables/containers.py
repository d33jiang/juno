from typing import Any, Callable

from ._base import OutputIO, Renderable, Renderer
from ._rendering import render

__all__ = [
    'Optional',
    'Thunk',
    'Wrapped',
]


class Wrapped(Renderer):

    def __init__(self, inner: Renderable, prefix: str, suffix: str):
        self._inner = inner
        self._prefix = prefix
        self._suffix = suffix

    def render(self, out: OutputIO):
        render(out, self._prefix)
        render(out, self._inner)
        render(out, self._suffix)

    @staticmethod
    def get_factory_method(prefix: str, suffix: str):
        def create_container(inner: Renderable) -> 'Wrapped':
            return Wrapped(
                inner=inner,
                prefix=prefix,
                suffix=suffix
            )

        return create_container


class Optional(Renderer):

    def __init__(self, is_visible: Any, renderable: Renderable):
        self._is_visible = bool(is_visible)
        self._renderable = renderable

    def render(self, out: OutputIO):
        if self._is_visible:
            render(out, self._renderable)


class Thunk(Renderer):

    def __init__(self, thunk: Callable[[], Renderable]):
        self._thunk = thunk

    def render(self, out: OutputIO):
        render(out, self._thunk())
