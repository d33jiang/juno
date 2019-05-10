from typing import Callable, Dict

from juno.renderables import OutputIO, Renderable, Renderer, render
from juno.renderables.containers import Wrapped
from ._text_utils import get_replacer

__all__ = [
    'XmlBlock',
    'XmlComment',
    'XmlSingle',
]

_XML_ESCAPE_SEQUENCES = {
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;',
    '\'': '&apos;',
    '"': '&quot;'
}
_escape = get_replacer(_XML_ESCAPE_SEQUENCES)  # type: Callable[[str], str]


def _quote(s: str) -> str:
    return f'"{_escape(s)}"'


def _prepare_xml_tag_contents(name: str, attributes: Dict[str, str]) -> str:
    return name + \
           ''.join(
               f' {key}={_quote(value)}'
               for key, value in attributes.items()
           )


class XmlBlock(Wrapped):
    """Instances of this class represent XML block elements."""

    def __init__(self, _tag_name: str, _tag_content: Renderable, **_tag_attributes: str):
        open_tag = f'<{_prepare_xml_tag_contents(_tag_name, _tag_attributes)}>'
        close_tag = f'</{_tag_name}>'

        super().__init__(
            inner=_tag_content,
            prefix=open_tag,
            suffix=close_tag
        )

    @staticmethod
    def get_factory_method(_tag_name: str, **_tag_attributes: str):
        def create_element(*_tag_content: Renderable) -> 'XmlBlock':
            return XmlBlock(
                _tag_name,
                _tag_content,
                **_tag_attributes
            )

        return create_element


class XmlSingle(Renderer):
    """Instances of this class represent XML empty elements."""

    def __init__(self, _tag_name: str, **_tag_attributes: str):
        self._element_tag = f'<{_prepare_xml_tag_contents(_tag_name, _tag_attributes)} />'

    def render(self, out: OutputIO):
        render(out, self._element_tag)


class XmlComment(Renderer):
    """Instances of this class represent XML comments."""

    def __init__(self, body: str):
        self._comment = f'<!-- {body} -->'

    def render(self, out: OutputIO):
        render(out, self._comment)
