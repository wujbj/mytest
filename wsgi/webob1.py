#!/usr/bin/env python

from pprint import pprint
from webob import Request, Response

req = Request.blank('http://localhost:8000/')
pprint(req.environ)

pprint('method: ' + req.method)
pprint('host: ' + req.host)
pprint('path: ' + req.path)
pprint('query_string: ' + req.query_string)
pprint('body: ' + req.body)
#pprint('cookies: ' + req.cookies)
