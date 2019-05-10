import functools

from ._common import *

#
# Meta

meta_base = functools.partial(XmlSingle, 'meta')


def meta_charset(charset: str = 'utf-8'):
    return meta_base(charset=charset)


def meta(name: str, content: str):
    return meta_base(name=name, content=content)


#
# Link

def link(rel: str, href: str, **kwargs: str):
    return XmlSingle('link', rel=rel, href=href, **kwargs)


def stylesheet(href: str, **kwargs: str):
    return link('stylesheet', href, **kwargs)


#
# Title

title = get_xml_block_factory('title')
