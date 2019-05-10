from juno.renderables import render_to_string as render
from juno.renderables.xml import XmlBlock


def test_xml_block_with_no_attributes():
    assert render(
        XmlBlock('p', 'foo')
    ) == '<p>foo</p>'


def test_xml_block_with_one_child_and_one_attribute():
    assert render(
        XmlBlock('p', 'bar', style='color: #ff0000')
    ) == '<p style="color: #ff0000">bar</p>'


def test_xml_block_with_one_child_and_multiple_attributes():
    assert render(
        XmlBlock('p', 'baz', id='the_baz', style='color: #ff0000')
    ) == '<p id="the_baz" style="color: #ff0000">baz</p>'


def test_xml_block_factory_method_with_no_attributes():
    paragraph = XmlBlock.get_factory_method('p')

    assert render(
        paragraph()
    ) == '<p></p>'

    assert render(
        paragraph('foo')
    ) == '<p>foo</p>'

    assert render(
        paragraph('foo', 'bar')
    ) == '<p>foobar</p>'


def test_xml_block_factory_method_with_one_attribute():
    red_paragraph = XmlBlock.get_factory_method('p', style='color: #ff0000')

    assert render(
        red_paragraph()
    ) == '<p style="color: #ff0000"></p>'

    assert render(
        red_paragraph('foo')
    ) == '<p style="color: #ff0000">foo</p>'

    assert render(
        red_paragraph('foo', 'bar')
    ) == '<p style="color: #ff0000">foobar</p>'


def test_xml_block_factory_method_with_multiple_attributes():
    red_paragraph = XmlBlock.get_factory_method('p', id='the_paragraph', style='color: #ff0000')

    assert render(
        red_paragraph()
    ) == '<p id="the_paragraph" style="color: #ff0000"></p>'

    assert render(
        red_paragraph('foo')
    ) == '<p id="the_paragraph" style="color: #ff0000">foo</p>'

    assert render(
        red_paragraph('foo', 'bar')
    ) == '<p id="the_paragraph" style="color: #ff0000">foobar</p>'
