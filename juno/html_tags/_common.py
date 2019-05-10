from juno.renderables.xml import XmlBlock, XmlComment, XmlSingle

__all__ = [
    'XmlBlock',
    'XmlComment',
    'XmlSingle',
    'get_xml_block_factory',
]

get_xml_block_factory = XmlBlock.get_factory_method
