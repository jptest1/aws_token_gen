import binascii
import hashlib
import logging
import xml.etree.ElementTree as etree

import sys

if sys.version_info[0] == 2:
    import urllib2 as urllib_request
else:
    from urllib import request as urllib_request

class NDATokenGenerator(object):
    __schemas = {
        'aws_access_key': 'XXXXXX',
        'aws_secret_key': 'XXXXXXX'
    }

    def __init__(self, url='https://ndar.nih.gov/DataManager/dataManager'):
        assert url is not None
        self.url = url
        logging.debug('constructed with url %s' % url)
