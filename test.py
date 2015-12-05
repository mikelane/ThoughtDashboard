#!/usr/bin/env python

"""
Short description

Longer description
"""

__author__ = "Mike Lane"
__copyright__ = "Copyright 2015, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"

__author__ = 'Mike Lane'


from pocket import Pocket

redirect_uri = "https://boiling-mesa-6040.herokuapp.com/"
consumer_key = "48825-6118628e966a9634d51fbb9a"
request_token = Pocket.get_request_token(consumer_key=consumer_key,
                                         redirect_uri=redirect_uri)
auth_url = Pocket.get_auth_url(code=request_token, redirect_uri=redirect_uri)
user_credentials = Pocket.get_credentials(consumer_key=consumer_key, code=request_token)

access_token = user_credentials['access_token']

