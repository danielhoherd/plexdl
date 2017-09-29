# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from plexdl import client


def test_hello():
    assert client.hello() == 'world'
