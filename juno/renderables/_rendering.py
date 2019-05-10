import io
from typing import Iterable

from ._base import OutputIO, Renderable, Renderer

__all__ = [
    'render',
    'render_to_string',
]


def render(out: OutputIO, renderable: Renderable):
    """
    Render the provided renderable.

    Args:
        out: The target of the rendering operation.
        renderable: The item to be rendered.

    Returns:
        None.

    """
    try:
        if isinstance(renderable, str):
            out.write(renderable)
        elif isinstance(renderable, Renderer):
            renderable(out)
        elif isinstance(renderable, Iterable):
            for child in renderable:
                render(out, child)
        else:
            raise TypeError(f'Argument renderable has an unexpected type: {renderable}')
    except Exception:
        print(renderable)
        raise


def render_to_string(renderable: Renderable) -> str:
    """
    Render the provided renderable into a string.

    Args:
        renderable: The item to be rendered.

    Returns:
        The resulting string.

    """
    with io.StringIO() as s:
        render(s, renderable)
        return s.getvalue()
