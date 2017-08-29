# -*- coding: utf-8 -*-
import base64
# Start your middleware class
class ProxyMiddleware(object):
 # overwrite process request
 def process_request(self, request, spider):
  # Set the location of the proxy
  request.meta['proxy'] = "http://127.0.0.1:8087"
 
  # Use the following lines if your proxy requires authentication
  proxy_user_pass = " : "
  # setup basic authentication for the proxy
  encoded_user_pass = base64.encodestring(proxy_user_pass)
  request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass