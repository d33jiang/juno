from juno.renderables import OutputIO, Renderer, render_to_string


def test_render_string():
    assert render_to_string(
        'Lorem ipsum.'
    ) == 'Lorem ipsum.'

    assert render_to_string(
        ''
    ) == ''


def test_render_renderer():
    class MockRenderer(Renderer):
        def render(self, out: OutputIO):
            out.write('foo')
            out.write('bar')

    assert render_to_string(MockRenderer()) == 'foobar'
