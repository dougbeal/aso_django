#!/usr/bin/env python

from distutils.core import setup
import sys

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

version = '[library version:1.0.1]'[17:-1]

kwargs = {
    'name': "python-urljr",
    'version': version,
    'url': "http://www.openidenabled.com/openid/libraries/python/",
    'download_url': "http://www.openidenabled.com/resources/downloads/python-openid/python-urljr-%s.tar.gz" % (version,),
    'author': "JanRain, Inc.",
    'author_email': "openid@janrain.com",
    'description': "JanRain's URL Utilities",
    # FIXME: 'long_description': "",
    'packages': ['urljr',
                 ],
    'license': "LGPL",
    'classifiers': [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]
    }


setup(**kwargs)
