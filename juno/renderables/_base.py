from typing import Iterable, TextIO, Union

__all__ = [
    'OutputIO',
    'Renderable',
    'Renderer',
]

OutputIO = TextIO

Renderable = Union[
    str,
    'Renderer',
    Iterable['Renderable']
]


class Renderer:

    def render(self, out: OutputIO):
        raise NotImplementedError

    def __call__(self, out: OutputIO):
        self.render(out)
