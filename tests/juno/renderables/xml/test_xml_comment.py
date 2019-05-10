from juno.renderables import render_to_string as render
from juno.renderables.xml import XmlComment


def test_xml_comment():
    assert render(
        XmlComment('Lorem ipsum.')
    ) == '<!-- Lorem ipsum. -->'
