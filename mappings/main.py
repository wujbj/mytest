#!/usr/bin/env python

from wsgiref import simple_server
from urls import mappings
from selector import Selector

app = Selector(mappings)
server = simple_server.make_server('', 8000, app)
server.serve_forever()
