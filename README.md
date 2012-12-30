bingpy
======

A simple python interface to the Bing web search api.


Installation
=============
    cd /tmp
    git clone git://github.com/steinitzu/bingpy.git
    cd bingpy
    python setup.py install
    
This program depends on httplib2


Usage
=============
    from bing import Bing
    b = Bing(api_key='xxxxxxxx')
    results = b['cupcakes']