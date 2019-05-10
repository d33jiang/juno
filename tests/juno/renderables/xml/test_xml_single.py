from juno.renderables import render_to_string as render
from juno.renderables.xml import XmlSingle


def test_xml_single_with_no_attributes():
    line_break = XmlSingle('br')
    assert render(
        line_break
    ) == '<br />'


def test_xml_single_with_one_attribute():
    logo = XmlSingle('img', src='/images/logo.png')
    assert render(
        logo
    ) == '<img src="/images/logo.png" />'


def test_xml_single_with_two_attributes():
    splash_image = XmlSingle('img', src='/images/splash.png', title='home page splash')
    assert render(
        splash_image
    ) == '<img src="/images/splash.png" title="home page splash" />'
