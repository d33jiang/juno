from juno.renderables import render_to_string
from juno.renderables.containers import Optional, Thunk, Wrapped


def test_wrapped():
    assert render_to_string(Wrapped('CONTENT', '(', ')')) == '(CONTENT)'
    assert render_to_string(Wrapped(('foo', 'bar'), '<p>', '</p>')) == '<p>foobar</p>'


def test_optional():
    assert render_to_string(
        (
            'BEFORE ',
            Optional(True, 'the_visible_stuff'),
            ' AFTER',
        )
    ) == 'BEFORE the_visible_stuff AFTER'

    assert render_to_string(
        (
            'BEFORE ',
            Optional(False, 'the_invisible_stuff'),
            ' AFTER',
        )
    ) == 'BEFORE  AFTER'


def test_thunk():
    def some_calculation():
        return '42'

    assert render_to_string(
        (
            'The answer is: ',
            Thunk(some_calculation),
        )
    ) == 'The answer is: 42'
