# -*- coding: utf-8 -*-
"""

"""
__title__ = 'procurecarros_sdk'
__version__ = '0.0.1'
__build__ = 0x020700
__author__ = 'Equipe Procurecarros'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Procurecarros.com'

#
# try:
#     from .packages.urllib3.contrib import pyopenssl
#     pyopenssl.inject_into_urllib3()
# except ImportError:
#     pass


# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
