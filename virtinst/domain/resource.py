#
# Copyright 2014 Fujitsu Limited.
# Chen Hanxiao <chenhanxiao at cn.fujitsu.com>
#
# This work is licensed under the GNU GPLv2.
# See the COPYING file in the top-level directory.

from ..xmlbuilder import XMLBuilder, XMLProperty


class DomainResource(XMLBuilder):
    """
    Class for generating <resource> XML
    """

    _XML_ROOT_NAME = "resource"
    _XML_PROP_ORDER = ["partition"]

    partition = XMLProperty("./partition")