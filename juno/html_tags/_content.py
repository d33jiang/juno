from functools import partial

from ._common import *


#
# Containers

def _container(name: str, *elem_class: str, elem_id: str = None):
    attributes = {}
    if elem_id:
        attributes['id'] = elem_id
    if elem_class:
        attributes['class'] = ' '.join(elem_class)

    return get_xml_block_factory(name, **attributes)


div = partial(_container, 'div')
span = partial(_container, 'span')

#
# Text

p = get_xml_block_factory('p')

h1 = get_xml_block_factory('h1')
h2 = get_xml_block_factory('h2')
h3 = get_xml_block_factory('h3')
h4 = get_xml_block_factory('h4')
h5 = get_xml_block_factory('h5')
h6 = get_xml_block_factory('h6')


#
# Images

def img(src: str):
    return XmlSingle('img', src=src)


#
# Formatting

_br = XmlSingle('br')


def br():
    return _br
