# coding: utf-8

# The MIT License (MIT)
#
# Copyright 2016 Alan Fachini <https://github.com/alfakini/python-mercadobitcoin>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from distutils.core import setup


INSTALL_REQUIREMENTS = ['requests']

setup(
    name = 'hftorderbook',
    description = 'A Python wrapper for HFT Orderbook API',
    version = '69.0.1',
    packages = ['lob'],
    author = 'Bruno Volpato',
    author_email = 'brunocvcunha@gmail.com',
    url = 'https://github.com/brunocvcunha/python-orderbook',
    keywords = ['orderbook'],
    install_requires=INSTALL_REQUIREMENTS,
    classifiers = [
        'Programming Language :: Python :: 3.7'
    ]
)
