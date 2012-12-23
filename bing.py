#!/usr/bin/env/python
#encoding:utf-8

"""
A simple web search interface to the bing search api.
"""

import httplib2, tempfile, os, getpass, base64
from urllib import quote
from json import JSONDecoder

def _dir_exists(path):
    return os.path.exists(path) and os.path.isdir(path)

def _get_cache_dir():
    return os.path.join(
        tempfile.gettempdir(), 'bingpy-'+getpass.getuser()
        )
    

class Bing(object):

    search_url = 'https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources=%%27web%%27&Query=%%27%(query)s%%27&$format=json'

    def __init__(self, api_key=None, caching=True, cache_dir=None, **kwargs):
        """
        Bing(api_key=None, caching=True, cache_dir=None)
        Make a new instance of the Bing api with given api_key
        if caching==True requests will be cached.
        If cache_dir is provided as well, it will be used to store the cache, 
        otherwise it will stored in the system's temp directory.
        given cache_dir must exist, otherwise an OSException will be raised.
        """
        print kwargs
        self.api_key = api_key
        self.caching = caching
        if caching and cache_dir:
            if not _dir_exists(cache_dir):
                raise IOError(
                    '%s does not exist or is not a valid directory.' % (cache_dir)
                    )
            else: 
                self.cache_dir = cache_dir
        elif caching:
            self.cache_dir = _get_cache_dir()
        else:
            self.cache_dir = None

        self.http = self.get_http()

    def get_http(self):
        h = httplib2.Http(cache=self.cache_dir)
        return h        

    def get_json(self, query):
        """
        Returns the raw JSON for given query.
        """
        url = self.search_url % {'query' : quote(query.encode('utf-8'))}
        bsixfour = base64.encodestring(
            '%s:%s' % (self.api_key, self.api_key)
            ).replace('\n', '')        
        headers = {'Authorization' : 'Basic %s' % bsixfour}
        return self.http.request(url, headers=headers)[1]

    def get_results(self, query):
        """
        Returns a list of web results as dicts.
        """
        json = self.get_json(query)
        return JSONDecoder().decode(json)['d']['results'][0]['Web']



    
            
            