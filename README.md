bingpy
======

A python interface to the Bing search api


Installation
=============
    cd /tmp
    git clone git://github.com/steinitzu/bingpy.git
    cd bingpy
    python setup.py install


Usage
=============
    from bing import Bing
    b = Bing(api_key='xxxxxxxx')
    results = b['cupcakes']